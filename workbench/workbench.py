from aspralign_workbench import aspralign_workbench
from nestedalign_workbench import nestedalign_workbench
from rnaforester_workbench import rnaforester_workbench
from rnadistance_workbench import rnadistance_workbench
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


    # Clustering
    '''molecule_files = os.listdir(WORKBENCH_RESULTS)
    for f in molecule_files:
        read_files(os.path.join(WORKBENCH_RESULTS, f, 'cores'), os.path.join(WORKBENCH_RESULTS, f, 'distances'))'''
