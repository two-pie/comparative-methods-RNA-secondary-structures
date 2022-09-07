#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys
import shutil
from pathlib import Path

import pandas as pd


def create_matrices(molecules_dir, output_file_csv):
    # request matlab credentials
    subprocess.run(['matlab', '-batch', 'exit;'])
    current_dir = os.getcwd()
    molecules = sorted(os.listdir(molecules_dir))
    # paths
    local_directory_path = os.path.dirname(os.path.realpath(sys.argv[0]))
    jar_path = os.path.join(local_directory_path, 'dualgraph', 'MatrixConverter.jar')
    tmp_path = os.path.join(local_directory_path, 'tmp')
    no_extracted_matrix_path = os.path.join(tmp_path, 'no_extracted_matrices')
    extracted_matrices_path = os.path.join(tmp_path, 'extracted_matrices')
    dualgraph_script_path = os.path.join(local_directory_path, 'dualgraph', 'dualGraphs.py')
    matlab_input_path = os.path.join(local_directory_path, 'features_computation', 'benchmark-processes.txt')
    matlab_script = os.path.join(local_directory_path, 'features_computation', 'FeaturesComputationDoBenchmark.m')
    if not (os.path.isabs(output_file_csv)):
        output_file_csv = os.path.join(Path.cwd(), output_file_csv)
    # change dir
    os.chdir(local_directory_path)
    # make tmp dirs
    os.makedirs(no_extracted_matrix_path)
    os.makedirs(extracted_matrices_path)
    # create no extracted matrices
    no_extracted_matrices(molecules_dir, no_extracted_matrix_path, dualgraph_script_path)
    # extract matrices
    extract_matrices(no_extracted_matrix_path, extracted_matrices_path, jar_path)
    # run matlab script
    with open(matlab_input_path, 'w+') as f:
        f.write(extracted_matrices_path + '\n')
        f.write(output_file_csv)
    matlab_command = f'matlab -batch \"run(\'{matlab_script}\');\"'
    subprocess.run(matlab_command, shell=True)
    # remove unnecessary files and directories
    os.remove(matlab_input_path)
    shutil.rmtree(tmp_path)
    # rename molecules in the csv with an appropiate name
    molecules_df = pd.DataFrame({'Molecule': molecules})
    molecules_df['Molecule'] = molecules_df['Molecule'].map(lambda x: x.split('.')[0])
    result_df = pd.read_csv(output_file_csv)
    result_df['Molecule'] = molecules_df['Molecule']
    result_df.to_csv(output_file_csv, index=False)
    os.chdir(current_dir)
    print('\x1b[6;30;42m' + f'{output_file_csv} created' + '\x1b[0m')


def extract_matrices(no_extracted_matrices_path, output_dir, jar_path):
    for f in sorted(os.listdir(no_extracted_matrices_path)):
        f_path = os.path.join(no_extracted_matrices_path, f)
        subprocess.run(['java', '-jar', jar_path, f_path, os.path.join(output_dir, f) + '_AdjMat.txt'],
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)


def no_extracted_matrices(molecules_dir, output_dir, dualgraph_script_path):
    subprocess.run(['python', dualgraph_script_path, molecules_dir, output_dir])


parser = argparse.ArgumentParser(description='dualgraph tool')
parser.add_argument('molecules_dir', help='directory containing all molecules in ct format')
parser.add_argument('output_file_csv',
                    help='file used to store the calculation as csv file. if the file does not exist it is created, '
                         'otherwise it is overwritten')
args = parser.parse_args()
create_matrices(args.molecules_dir, args.output_file_csv)
