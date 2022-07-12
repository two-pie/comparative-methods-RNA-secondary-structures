#!/usr/bin/env python3
import os
# import argparse  for future use
import subprocess
import sys
import pandas as pd


def aspralign_workbench(molecules_dir, output_dir):
    # run aspralign workbench
    subprocess.run(['java', '-jar', 'ASPRAlignWorkbench.jar', '-f', molecules_dir])

    # read csv file with pandas
    csv = pd.read_csv(os.path.join(molecules_dir, 'ASPRAlignComparisonResults.csv'))

    # drop unnecessary columns
    csv.drop(csv.columns[1:5], axis=1, inplace=True)
    csv.drop(csv.columns[2:7], axis=1, inplace=True)

    # change column names
    csv.columns = ['Molecule 1', 'Molecule 2', 'Distance', 'Execution time [ns]']

    # remove extension from molecule names
    csv['Molecule 1'] = csv['Molecule 1'].map(lambda x: os.path.splitext(x)[0])
    csv['Molecule 2'] = csv['Molecule 2'].map(lambda x: os.path.splitext(x)[0])

    # save pandas dataframe to csv file
    csv.to_csv(output_dir, index=False)

    # remove csv file generated by aspralign workbench
    os.remove(os.path.join(molecules_dir, 'ASPRAlignComparisonResults.csv'))
    os.remove(os.path.join(molecules_dir, 'ASPRAlignProcessedStructures.csv'))


if __name__ == '__main__':
    # PATHS
    GROUP_PROJECT = os.path.dirname(os.path.dirname(os.path.realpath(sys.argv[0])))
    ARCHAEA = os.path.join(GROUP_PROJECT, 'Molecules-pseudoknotfree', 'db-nH', 'Archaea', '5S')
    BACTERIA = os.path.join(GROUP_PROJECT, 'Molecules-pseudoknotfree', 'db-nH', 'Bacteria', '5S')
    EUKARYOTA = os.path.join(GROUP_PROJECT, 'Molecules-pseudoknotfree', 'db-nH', 'Eukaryota', '5S')
    ARCHAEA_OUTPUT = os.path.join(GROUP_PROJECT, 'benchmark-results', 'Archaea', '5S-aspralign.csv')
    BACTERIA_OUTPUT = os.path.join(GROUP_PROJECT, 'benchmark-results', 'Bacteria', '5S-aspralign.csv')
    EUKARYOTA_OUTPUT = os.path.join(GROUP_PROJECT, 'benchmark-results', 'Eukaryota', '5S-aspralign.csv')
    ASPRALIGN_WORKBENCH_JAR = os.path.join(GROUP_PROJECT, 'ASPRAlign-0.92')

    # change directory to use default aspralign config file
    os.chdir(ASPRALIGN_WORKBENCH_JAR)

    # generate csv files with aspralign workbench
    aspralign_workbench(ARCHAEA, ARCHAEA_OUTPUT)
    aspralign_workbench(BACTERIA, BACTERIA_OUTPUT)
    aspralign_workbench(EUKARYOTA, EUKARYOTA_OUTPUT)
