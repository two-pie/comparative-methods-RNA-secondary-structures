import subprocess

from workbench.paths import *

# clustering for Archaea-90-110-allType
subprocess.run(['cluster_matrix_workbench', DBNFilesNH, result_AT_aspralign,
                os.path.join(result_Archaea_90_110_allType, 'aspralign_clustering.csv')])
subprocess.run(['cluster_matrix_workbench', CTFilesNH, result_AT_dualgraph,
                os.path.join(result_Archaea_90_110_allType, 'dualgraph_clustering.csv')])
subprocess.run(['cluster_matrix_workbench', DBNFilesNH, result_AT_nestedalign,
                os.path.join(result_Archaea_90_110_allType, 'nestedalign_clustering.csv')])
subprocess.run(['cluster_matrix_workbench', DBNFilesNH, result_AT_rnadistance,
                os.path.join(result_Archaea_90_110_allType, 'rnadistance_clustering.csv')])
subprocess.run(['cluster_matrix_workbench', DBNFilesNH, result_AT_rnaforester,
                os.path.join(result_Archaea_90_110_allType, 'rnaforester_clustering.csv')])
subprocess.run(['cluster_matrix_workbench', CTFilesNH, result_AT_treegraph,
                os.path.join(result_Archaea_90_110_allType, 'treegraph_clustering.csv')])

# clustering for Molecules-pseudoknotfree
# Archaea
subprocess.run(['cluster_matrix_workbench', DBNFilesNH, result_MP_aspralign_Archaea,
                os.path.join(result_Archaea_90_110_allType, 'aspralign_clustering.csv')])
subprocess.run(['cluster_matrix_workbench', CTFilesNH, result_MP_dualgraph_Archaea,
                os.path.join(result_Archaea_90_110_allType, 'dualgraph_clustering.csv')])
subprocess.run(['cluster_matrix_workbench', DBNFilesNH, result_MP_nestedalign_Archaea,
                os.path.join(result_Archaea_90_110_allType, 'nestedalign_clustering.csv')])
subprocess.run(['cluster_matrix_workbench', DBNFilesNH, result_MP_rnadistance_Archaea,
                os.path.join(result_Archaea_90_110_allType, 'rnadistance_clustering.csv')])
subprocess.run(['cluster_matrix_workbench', DBNFilesNH, result_AT_rnaforester,
                os.path.join(result_Archaea_90_110_allType, 'rnaforester_clustering.csv')])
subprocess.run(['cluster_matrix_workbench', CTFilesNH, result_MP_treegraph_Archaea,
                os.path.join(result_Archaea_90_110_allType, 'treegraph_clustering.csv')])

# Bacteria
subprocess.run(['cluster_matrix_workbench', DBNFilesNH, result_MP_aspralign_Bacteria,
                os.path.join(result_Archaea_90_110_allType, 'aspralign_clustering.csv')])
subprocess.run(['cluster_matrix_workbench', CTFilesNH, result_MP_dualgraph_Bacteria,
                os.path.join(result_Archaea_90_110_allType, 'dualgraph_clustering.csv')])
subprocess.run(['cluster_matrix_workbench', DBNFilesNH, result_MP_nestedalign_Bacteria,
                os.path.join(result_Archaea_90_110_allType, 'nestedalign_clustering.csv')])
subprocess.run(['cluster_matrix_workbench', DBNFilesNH, result_MP_rnadistance_Bacteria,
                os.path.join(result_Archaea_90_110_allType, 'rnadistance_clustering.csv')])
subprocess.run(['cluster_matrix_workbench', DBNFilesNH, result_MP_rnaforester_Bacteria,
                os.path.join(result_Archaea_90_110_allType, 'rnaforester_clustering.csv')])
subprocess.run(['cluster_matrix_workbench', CTFilesNH, result_MP_treegraph_Bacteria,
                os.path.join(result_Archaea_90_110_allType, 'treegraph_clustering.csv')])

# Eukaryota
subprocess.run(['cluster_matrix_workbench', DBNFilesNH, result_MP_aspralign_Eukaryota,
                os.path.join(result_Archaea_90_110_allType, 'aspralign_clustering.csv')])
subprocess.run(['cluster_matrix_workbench', CTFilesNH, result_MP_dualgraph_Eukaryota,
                os.path.join(result_Archaea_90_110_allType, 'dualgraph_clustering.csv')])
subprocess.run(['cluster_matrix_workbench', DBNFilesNH, result_MP_nestedalign_Eukaryota,
                os.path.join(result_Archaea_90_110_allType, 'nestedalign_clustering.csv')])
subprocess.run(['cluster_matrix_workbench', DBNFilesNH, result_MP_rnadistance_Eukaryota,
                os.path.join(result_Archaea_90_110_allType, 'rnadistance_clustering.csv')])
subprocess.run(['cluster_matrix_workbench', DBNFilesNH, result_MP_rnaforester_Eukaryota,
                os.path.join(result_Archaea_90_110_allType, 'rnaforester_clustering.csv')])
subprocess.run(['cluster_matrix_workbench', CTFilesNH, result_MP_treegraph_Eukaryota,
                os.path.join(result_Archaea_90_110_allType, 'treegraph_clustering.csv')])
