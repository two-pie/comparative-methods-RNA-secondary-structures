#!/usr/bin/env python3

import os
import subprocess
import argparse
import pandas as pd


def __rnadistance(directory, df):
    molecules = sorted(os.listdir(directory))
    molecule_pairs = [(molecule_1, molecule_2) for i, molecule_1 in enumerate(molecules, start=1) for molecule_2 in
                      molecules[i:]]
    for molecule_1, molecule_2 in molecule_pairs:
        with open(os.path.join(directory, molecule_1), 'r') as file_1:
            # get the content of the first molecule
            content_molecule_1 = file_1.read()
            with open(os.path.join(directory, molecule_2), 'r') as file_2:
                content_molecule_2 = file_2.read()
                sp = subprocess.Popen(['RNAdistance'], stdout=subprocess.PIPE,
                                      stdin=subprocess.PIPE)
                distance = sp.communicate(input=f'{content_molecule_1}\n{content_molecule_2}'.encode('utf-8'))[
                               0].decode('utf-8').strip()[3:]
                df.loc[len(df)] = [molecule_1.split('.')[0], molecule_2.split('.')[0], distance]


def csv(molecules_dir, output_file):
    # create a dataframe for the csv file
    df = pd.DataFrame(columns=['Molecule 1', 'Molecule 2', 'Distance'])

    # fill the dataframe with the data from the nestedalign website
    __rnadistance(molecules_dir, df)

    # save the dataframe as a csv file
    df.to_csv(output_file, index=False)
    print(f'{output_file} created')


parser = argparse.ArgumentParser(description='rnadistance tool')
parser.add_argument('molecules_dir', help='directory containing all molecules in db format (without header)')
parser.add_argument('output_file_csv',
                    help='file used to store the calculation as csv file. if the file does not exist it is created, '
                         'otherwise it is overwritten')
args = parser.parse_args()
csv(args.molecules_dir, args.output_file_csv)
