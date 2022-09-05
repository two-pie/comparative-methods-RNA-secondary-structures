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

    # Archaea-90-110-allType
    subprocess.run(['aspralign_distance_tool', DBNFilesNH, result_AT_aspralign])
    subprocess.run(['dualgraph_distance_tool', CTFilesNH, result_AT_dualgraph])
    subprocess.run(['nestedalign_distance_tool', DBNFilesNH, result_AT_nestedalign])
    subprocess.run(['rnadistance_distance_tool', DBNFilesNH, result_AT_rnadistance])
    subprocess.run(['rnaforester_distance_tool', DBNFilesNH, result_AT_rnaforester])

    # Molecules-pseudoknotfree
    # Archaea
    subprocess.run(['aspralign_distance_tool', DBNFilesNH, result_MP_aspralign_Archaea])
    subprocess.run(['dualgraph_distance_tool', CTFilesNH, result_MP_dualgraph_Archaea])
    subprocess.run(['nestedalign_distance_tool', DBNFilesNH, result_MP_nestedalign_Archaea])
    subprocess.run(['rnadistance_distance_tool', DBNFilesNH, result_MP_rnadistance_Archaea])
    subprocess.run(['rnaforester_distance_tool', DBNFilesNH, result_MP_rnaforester_Archaea])

    # Bacteria
    subprocess.run(['aspralign_distance_tool', DBNFilesNH, result_MP_aspralign_Bacteria])
    subprocess.run(['dualgraph_distance_tool', CTFilesNH, result_MP_dualgraph_Bacteria])
    subprocess.run(['nestedalign_distance_tool', DBNFilesNH, result_MP_nestedalign_Bacteria])
    subprocess.run(['rnadistance_distance_tool', DBNFilesNH, result_MP_rnadistance_Bacteria])
    subprocess.run(['rnaforester_distance_tool', DBNFilesNH, result_MP_rnaforester_Bacteria])

    # Eukaryota
    subprocess.run(['aspralign_distance_tool', DBNFilesNH, result_MP_aspralign_Eukaryota])
    subprocess.run(['dualgraph_distance_tool', CTFilesNH, result_MP_dualgraph_Eukaryota])
    subprocess.run(['nestedalign_distance_tool', DBNFilesNH, result_MP_nestedalign_Eukaryota])
    subprocess.run(['rnadistance_distance_tool', DBNFilesNH, result_MP_rnadistance_Eukaryota])
    subprocess.run(['rnaforester_distance_tool', DBNFilesNH, result_MP_rnaforester_Eukaryota])

    # Clustering
    '''molecule_files = os.listdir(WORKBENCH_RESULTS)
    for f in molecule_files:
        read_files(os.path.join(WORKBENCH_RESULTS, f, 'cores'), os.path.join(WORKBENCH_RESULTS, f, 'distances'))'''
