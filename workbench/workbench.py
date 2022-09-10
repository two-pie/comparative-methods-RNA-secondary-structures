import subprocess
from paths import *

if __name__ == '__main__':
    # Distance calculator
    # Archaea-90-110-allType
    subprocess.run(['aspralign_distance_tool', DBNFilesNH, result_AT_aspralign])
    subprocess.run(['dualgraph_distance_tool', CTFilesNH, result_AT_dualgraph])
    subprocess.run(['nestedalign_distance_tool', DBNFilesNH, result_AT_nestedalign])
    subprocess.run(['rnadistance_distance_tool', DBNFilesNH, result_AT_rnadistance])
    subprocess.run(['rnaforester_distance_tool', DBNFilesNH, result_AT_rnaforester])
    # subprocess.run(['treegraph_distance_tool', CTFilesNH, result_AT_treegraph]) # TODO: da errore, aspettando lo script fixato

    # Molecules-pseudoknotfree
    # Archaea
    subprocess.run(['aspralign_distance_tool', DBNFilesNH, result_MP_aspralign_Archaea])
    subprocess.run(['dualgraph_distance_tool', ctnh_archaea, result_MP_dualgraph_Archaea])
    subprocess.run(['nestedalign_distance_tool', dbnh_archaea, result_MP_nestedalign_Archaea])
    subprocess.run(['rnadistance_distance_tool', dbnh_archaea, result_MP_rnadistance_Archaea])
    subprocess.run(['rnaforester_distance_tool', DBNFilesNH, result_MP_rnaforester_Archaea])
    subprocess.run(['treegraph_distance_tool', ctnh_archaea, result_MP_treegraph_Archaea])
    # Bacteria
    subprocess.run(['aspralign_distance_tool', DBNFilesNH, result_MP_aspralign_Bacteria])
    subprocess.run(['dualgraph_distance_tool', ctnh_bacteria, result_MP_dualgraph_Bacteria])
    subprocess.run(['nestedalign_distance_tool', dbnh_bacteria, result_MP_nestedalign_Bacteria])
    subprocess.run(['rnadistance_distance_tool', dbnh_bacteria, result_MP_rnadistance_Bacteria])
    subprocess.run(['rnaforester_distance_tool', DBNFilesNH, result_MP_rnaforester_Bacteria])
    subprocess.run(['treegraph_distance_tool', ctnh_bacteria, result_MP_treegraph_Bacteria])

    # Eukaryota
    subprocess.run(['aspralign_distance_tool', DBNFilesNH, result_MP_aspralign_Eukaryota])
    subprocess.run(['dualgraph_distance_tool', ctnh_eukaryota, result_MP_dualgraph_Eukaryota])
    subprocess.run(['nestedalign_distance_tool', dbnh_eukaryota, result_MP_nestedalign_Eukaryota])
    subprocess.run(['rnadistance_distance_tool', dbnh_eukaryota, result_MP_rnadistance_Eukaryota])
    subprocess.run(['rnaforester_distance_tool', DBNFilesNH, result_MP_rnaforester_Eukaryota])
    subprocess.run(['treegraph_distance_tool', ctnh_eukaryota, result_MP_treegraph_Eukaryota])

    # Core calculator
    subprocess.run(['python3', 'cores_calculator_workbench.py'])

    # Clustering calculator
    subprocess.run(['python3', 'cluster_matrix_workbench.py'])
    subprocess.run(['python3', 'cluster_features_workbench.py'])
