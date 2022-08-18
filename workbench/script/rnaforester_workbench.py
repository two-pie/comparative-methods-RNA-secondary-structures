import os
import subprocess

import pandas as pd

from paths import WORKBENCH_PATH


def __rnaforester(directory, df):
    # list of molecules in the directory
    molecules = sorted(os.listdir(directory))

    # use list comprehension to get all pairs of molecules
    molecule_pairs = [(molecule_1, molecule_2) for i, molecule_1 in enumerate(molecules, start=1) for molecule_2 in
                      molecules[i:]]
    # iterate over all pairs of molecules
    for molecule_1, molecule_2 in molecule_pairs:
        with open(os.path.join(directory, molecule_1), 'r') as file_1:
            with open(os.path.join(directory, molecule_2), 'r') as file_2:
                with open(WORKBENCH_PATH + '/tmp.txt', 'w') as tmp:
                    tmp.write(file_1.read())
                    tmp.write('\n' + file_2.read())
                # run RNAforester workbench and suppress output
                output = subprocess.run(['RNAforester', '-d', '-f', WORKBENCH_PATH + '/tmp.txt'], capture_output=True)
                # convert from CompletedProcess to string
                output = output.stdout.decode('utf-8').strip()
                # recover distance in substring
                distance = output[
                           output.find('global optimal score:') + len('global optimal score: '):].split('\n')[0]
                # remove spaces from string: example s ***
                if distance.find(' ') != -1:
                    distance = distance[:distance.find(' ')]
                df.loc[len(df)] = [molecule_1, molecule_2, distance]
    # delete tmp.txt
    os.remove(WORKBENCH_PATH + '/tmp.txt')


def csv(molecules_dirs, output_files):
    # create csv for each molecule
    for directory, output in zip(molecules_dirs, output_files):
        # create a dataframe for the csv file
        df = pd.DataFrame(columns=['Molecule 1', 'Molecule 2', 'Distance'])

        # fill the dataframe with the data from the nestedalign website
        __rnaforester(directory, df)

        # save the dataframe as a csv file
        df.to_csv(output, index=False)
        print(f'{output} created')
