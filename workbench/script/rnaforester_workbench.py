import os
import subprocess

import pandas as pd


def __rnaforester(directory):
    # list of molecules in the directory
    molecules = sorted(os.listdir(directory))

    # use list comprehension to get all pairs of molecules
    molecule_pairs = [(molecule_1, molecule_2) for i, molecule_1 in enumerate(molecules, start=1) for molecule_2 in
                      molecules[i:]]
    # iterate over all pairs of molecules
    for molecule_1, molecule_2 in molecule_pairs:
        with open(os.path.join(directory, molecule_1), 'r') as file_1:
            with open(os.path.join(directory, molecule_2), 'r') as file_2:
                # run RNAforester workbench and suppress output
                subprocess.run(['RNAforester', '-d', '-f', file_1, file_2], stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL)


def csv(molecules_dirs, output_files):
    # create csv for each molecule
    for directory, output in zip(molecules_dirs, output_files):
        # create a dataframe for the csv file
        df = pd.DataFrame(columns=['Molecule 1', 'Molecule 2', 'Distance', 'Execution time [ns]'])

        # fill the dataframe with the data from the nestedalign website
        __rnaforester(directory)

        # save the dataframe as a csv file
        df.to_csv(output, index=False)
        print(f'{output} created')
