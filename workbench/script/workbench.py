import os

import aspralign_workbench
import nestedalign_workbench
import rnaforester_workbench
import rnadistance_workbench
import subprocess
from paths import *


def read_files(cores_folder, distances_folder):
    cores = os.listdir(cores_folder)
    distances = os.listdir(distances_folder)
    for c in cores:
        for d in distances:
            subprocess.run(
                ['python3', 'ClusterMatrix.py', os.path.join(cores_folder, c), os.path.join(distances_folder, d)])


if __name__ == '__main__':
    # Distance calculator
    '''aspralign_workbench.csv([ARCHAEA_DIR, BACTERIA_DIR, EUKARYOTA_DIR],
                            [ASPRALIGN_ARCHAEA_OUTPUT_FILE, ASPRALIGN_BACTERIA_OUTPUT_FILE,
                             ASPRALIGN_EUKARYOTA_OUTPUT_FILE], ASPRALIGN_WORKBENCH_JAR, ASPRALIGN_CONFIG_FILE)

    nestedalign_workbench.csv([ARCHAEA_DIR, BACTERIA_DIR, EUKARYOTA_DIR],
                              [NESTEDALIGN_ARCHAEA_OUTPUT_FILE, NESTEDALIGN_BACTERIA_OUTPUT_FILE,
                               NESTEDALIGN_EUKARYOTA_OUTPUT_FILE])

    rnaforester_workbench.csv([ARCHAEA_DIR, BACTERIA_DIR, EUKARYOTA_DIR],
                              [RNAFORESTER_ARCHAEA_OUTPUT_FILE, RNAFORESTER_BACTERIA_OUTPUT_FILE,
                               RNAFORESTER_EUKARYOTA_OUTPUT_FILE])

    rnadistance_workbench.csv([ARCHAEA_DIR, BACTERIA_DIR, EUKARYOTA_DIR],
                              [RNADISTANCE_ARCHAEA_OUTPUT_FILE, RNADISTANCE_BACTERIA_OUTPUT_FILE,
                               RNADISTANCE_EUKARYOTA_OUTPUT_FILE])'''
    # Core calculator
    subprocess.run(['java', '-jar', CORE_JAR, ARCHAEA_DIR, WORKBENCH_RESULTS_ARCHAEA_CORES, 'archaea'],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(['java', '-jar', CORE_JAR, BACTERIA_DIR, WORKBENCH_RESULTS_BACTERIA_CORES, 'bacteria'],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(['java', '-jar', CORE_JAR, EUKARYOTA_DIR, WORKBENCH_RESULTS_EUKARYOTA_CORES, 'eukaryota'],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Clustering
    '''molecule_files = os.listdir(WORKBENCH_RESULTS)
    for f in molecule_files:
        read_files(os.path.join(WORKBENCH_RESULTS, f, 'cores'), os.path.join(WORKBENCH_RESULTS, f, 'distances'))
'''