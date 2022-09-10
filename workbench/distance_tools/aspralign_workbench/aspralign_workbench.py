#!/usr/bin/env python3

import os
import subprocess
import argparse
import sys
import pandas as pd


def csv(molecules_dir, output_file, aspralign_workbench_jar, aspralign_config):
    # run aspralign workbench and suppress output
    subprocess.run(['java', '-jar', aspralign_workbench_jar, '-f', molecules_dir, '-n', aspralign_config],
                   stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)
    # read csv file with pandas
    dataframe = pd.read_csv(os.path.join(molecules_dir, 'ASPRAlignComparisonResults.csv'))

    # drop unnecessary columns
    dataframe.drop(dataframe.columns[1:5], axis=1, inplace=True)
    dataframe.drop(dataframe.columns[2:7], axis=1, inplace=True)
    dataframe = dataframe.iloc[:, :-1]

    # change column names
    dataframe.columns = ['Molecule 1', 'Molecule 2', 'Distance']

    # set the name of the molecules
    dataframe['Molecule 1'] = dataframe['Molecule 1'].map(lambda x: x.split('.')[0])
    dataframe['Molecule 2'] = dataframe['Molecule 2'].map(lambda x: x.split('.')[0])

    # save pandas dataframe to csv file
    dataframe.to_csv(output_file, index=False)

    # remove csv file generated by aspralign workbench
    os.remove(os.path.join(molecules_dir, 'ASPRAlignComparisonResults.csv'))
    os.remove(os.path.join(molecules_dir, 'ASPRAlignProcessedStructures.csv'))

    print('\x1b[1;32;40m' + f'{output_file} created' + '\x1b[0m')


aspralign_jar_path = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), 'ASPRAlignWorkbench.jar')
aspralign_config_path = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), 'ASPRAlign-config.txt')
parser = argparse.ArgumentParser(description='aspralign tool')
parser.add_argument('molecules_dir', help='directory containing all molecules in db, aas, bpseq or ct format')
parser.add_argument('output_file_csv',
                    help='file used to store the calculation as csv file. if the file does not exist it is created, '
                         'otherwise it is overwritten')
args = parser.parse_args()
print('\x1b[0;31;40m' + 'ASPRALIGN DISTANCE TOOL' + '\x1b[0m')
csv(args.molecules_dir, args.output_file_csv, aspralign_jar_path, aspralign_config_path)
