#!/usr/bin/env python3

import subprocess
import os
import sys
import argparse
import pandas as pd

CORE_JAR_PATH = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), 'coresCalculator.jar')


def calculate_core1(molecules_dir, organism_file, output_file):
    # create a dataframe for the csv file
    df = pd.DataFrame(columns=['Id', 'Organism', 'Core1'])

    # open organism csv
    organism_df = pd.read_csv(organism_file)

    molecules = sorted(os.listdir(molecules_dir))

    for molecule in molecules:
        core1 = subprocess.run(['java', '-jar', CORE_JAR_PATH, '-core1', os.path.join(molecules_dir, molecule)],
                               capture_output=True)
        print(core1)
        # search the organism of a molecule
        organism_name = organism_df.loc[organism_df['Id'] == molecule.split('.')[0]]['Organism'].values[0]
        df.loc[len(df)] = [molecule.split('.')[0], organism_name, core1]
    df.to_csv(output_file, index=False)


def calculate_core2(molecules_dir, organism_file, output_file):
    # create a dataframe for the csv file
    df = pd.DataFrame(columns=['Id', 'Organism', 'Core2'])

    # open organism csv
    organism_df = pd.read_csv(organism_file)

    molecules = sorted(os.listdir(molecules_dir))

    for molecule in molecules:
        core2 = subprocess.run(['java', '-jar', CORE_JAR_PATH, '-core2', os.path.join(molecules_dir, molecule)],
                               capture_output=True)
        organism_name = organism_df.loc[organism_df['Id'] == molecule.split('.')[0]]['Organism'].values[0]
        df.loc[len(df)] = [molecule.split('.')[0], organism_name, core2]
    df.to_csv(output_file, index=False)


parser = argparse.ArgumentParser(description='cores calculator tool', formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('molecules_dir', help='directory containing all molecules in db format')
parser.add_argument('organism_csv', help="csv file (use comma ',' as separator) in which each molecule is specified "
                                         "\nunder the Id column(just the name of the molecule file without extension)"
                                         "\nand its organism is specified on the Organism "
                                         "column. \nFor example, if you want to calculate the cores of two molecules"
                                         "\nsaved in the files bpRNA_SPR_54.db and bpRNA_SPR_184.db then the csv "
                                         "\nwill have to look like:"
                                         "\nId,Organism"
                                         "\nbpRNA_SPR_54,Bacillus_subtilis"
                                         "\nbpRNA_SPR_184,Escherichia_coli")
parser.add_argument('output_folder',
                    help='Destination folder on which two files called core1.csv and core2.csv are saved. '
                         'If the files do not exist they are created , otherwise they are overwritten.')
args = parser.parse_args()
calculate_core1(args.molecules_dir, args.organism_csv, os.path.join(args.output_folder, 'core1.csv'))
calculate_core2(args.molecules_dir, args.organism_csv, os.path.join(args.output_folder, 'core2.csv'))
