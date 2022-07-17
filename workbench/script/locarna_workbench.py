import os
import pandas as pd
import time
import subprocess


def csv(molecules_dirs, output_files):
    for directory, output in zip(molecules_dirs, output_files):
        # create a dataframe for the csv file
        df = pd.DataFrame(columns=['Molecule 1', 'Molecule 2', 'Distance', 'Execution time [ns]'])

        # list of molecules in the directory
        molecules = sorted(os.listdir(directory))

        # use list comprehension to get all pairs of molecules
        molecules_pairs = [(molecule_1, molecule_2) for i, molecule_1 in enumerate(molecules, start=1) for molecule_2 in
                           molecules[i:]]

        # iterate over all pairs of molecules
        for molecule_1, molecule_2 in molecules_pairs:
            # save initial time
            initial_time = time.time_ns()

            # align the two molecules with locarna and retrieve the distance
            distance = subprocess.run(
                ['locarna', os.path.join(directory, molecule_1), os.path.join(directory, molecule_2)],
                capture_output=True).stdout.decode('utf-8').split('\n')[0][7:]

            # save final time
            end_time = time.time_ns() - initial_time

            # save the data in the dataframe
            df.loc[len(df)] = [os.path.splitext(molecule_1)[0], os.path.splitext(molecule_2)[0], distance,
                               end_time]

        # save the dataframe as a csv file
        df.to_csv(output, index=False)
        print(f'{output} generated')
