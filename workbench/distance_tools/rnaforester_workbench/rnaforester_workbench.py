#!/usr/bin/env python3

import os
import subprocess
import argparse
import sys
import pandas as pd


def __rnaforester(directory, df):
    local_dir_path = os.path.dirname(os.path.realpath(sys.argv[0]))
    # list of molecules in the directory
    molecules = sorted(os.listdir(directory))

    # use list comprehension to get all pairs of molecules
    molecule_pairs = [(molecule_1, molecule_2) for i, molecule_1 in enumerate(molecules, start=1) for molecule_2 in
                      molecules[i:]]
    i = 1
    # iterate over all pairs of molecules
    for molecule_1, molecule_2 in molecule_pairs:
        print(f'{i}/{len(molecule_pairs)}')
        i += 1
        with open(os.path.join(directory, molecule_1), 'r') as file_1:
            with open(os.path.join(directory, molecule_2), 'r') as file_2:
                with open(local_dir_path + '/tmp.txt', 'w') as tmp:
                    tmp.write(file_1.read())
                    tmp.write('\n' + file_2.read())
                # run RNAforester workbench and suppress output
                output = subprocess.run(['RNAforester', '-d', '-f', local_dir_path + '/tmp.txt'], capture_output=True)
                # convert from CompletedProcess to string
                output = output.stdout.decode('utf-8').strip()
                # recover distance in substring
                distance = output[
                           output.find('global optimal score:') + len('global optimal score: '):].split('\n')[0]
                # remove spaces from string: example s ***
                if distance.find(' ') != -1:
                    distance = distance[:distance.find(' ')]
                df.loc[len(df)] = [molecule_1.split('.')[0], molecule_2.split('.')[0], distance]
    # delete tmp.txt
    os.remove(local_dir_path + '/tmp.txt')


def csv(molecules_dir, output_file):
    # create a dataframe for the csv file
    df = pd.DataFrame(columns=['Molecule 1', 'Molecule 2', 'Distance'])

    # fill the dataframe with the data from the nestedalign website
    __rnaforester(molecules_dir, df)

    # save the dataframe as a csv file
    df.to_csv(output_file, index=False)
    print('\x1b[6;30;42m' + f'{output_file} created' + '\x1b[0m')


parser = argparse.ArgumentParser(description='rnaforester tool')
parser.add_argument('molecules_dir', help='directory containing all molecules in db format (without header)')
parser.add_argument('output_file_csv',
                    help='file used to store the calculation as csv file. if the file does not exist it is created, '
                         'otherwise it is overwritten')
args = parser.parse_args()
csv(args.molecules_dir, args.output_file_csv)
