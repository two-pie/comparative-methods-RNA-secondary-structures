import os
import subprocess
import time
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
                stri = f'{content_molecule_1}\n{content_molecule_2}'
                sp = subprocess.Popen(['RNAdistance'], stdout=subprocess.PIPE,
                                      stdin=subprocess.PIPE)
                initial_time = time.time_ns()
                distance = sp.communicate(input=stri.encode('utf-8'))[0].decode('utf-8').strip()[3:]
                final_time = time.time_ns() - initial_time
                df.loc[len(df)] = [os.path.splitext(molecule_1)[0], os.path.splitext(molecule_2)[0], distance,
                                   final_time]


def csv(molecules_dirs, output_files):
    # create csv for each molecule
    for directory, output in zip(molecules_dirs, output_files):
        # create a dataframe for the csv file
        df = pd.DataFrame(columns=['Molecule 1', 'Molecule 2', 'Distance', 'Execution time [ns]'])

        # fill the dataframe with the data from the nestedalign website
        __rnadistance(directory, df)

        # save the dataframe as a csv file
        df.to_csv(output, index=False)
        print(f'{output} created')
