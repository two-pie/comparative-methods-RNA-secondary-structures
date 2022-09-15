import os
import sys

# root directory of the workbench
WORKBENCH_PATH = os.path.dirname(os.path.dirname(os.path.realpath(sys.argv[0])))

# workbench results directory
WORKBENCH_RESULTS = os.path.join(WORKBENCH_PATH, 'workbench_results')

# Archaea-90-110-allType
Archaea_90_110_allType = os.path.join(WORKBENCH_PATH, 'datasets', 'Archaea-90-110-allType')
DBNFiles = os.path.join(Archaea_90_110_allType, 'DBNFiles')
DBNFilesNH = os.path.join(Archaea_90_110_allType, 'DBNFilesNH')
CTFiles = os.path.join(Archaea_90_110_allType, 'CTFiles')
CTFilesNH = os.path.join(Archaea_90_110_allType, 'CTFilesNH')

# Molecules-pseudoknotfree
# 5S
ARCHAEA_DIR = os.path.join('Archaea', '5S')
BACTERIA_DIR = os.path.join('Bacteria', '5S')
EUKARYOTA_DIR = os.path.join('Eukaryota', '5S')
Molecules_pseudoknotfree_db = os.path.join(WORKBENCH_PATH, 'datasets', 'Molecules-pseudoknotfree', 'db')
Molecules_pseudoknotfree_dbNH = os.path.join(WORKBENCH_PATH, 'datasets', 'Molecules-pseudoknotfree', 'db-nH')
Molecules_pseudoknotfree_ctNH = os.path.join(WORKBENCH_PATH, 'datasets', 'Molecules-pseudoknotfree', 'ct-nH')
db_archaea = os.path.join(Molecules_pseudoknotfree_db, ARCHAEA_DIR)
db_bacteria = os.path.join(Molecules_pseudoknotfree_db, BACTERIA_DIR)
db_eukaryota = os.path.join(Molecules_pseudoknotfree_db, EUKARYOTA_DIR)
dbnh_archaea = os.path.join(Molecules_pseudoknotfree_dbNH, ARCHAEA_DIR)
dbnh_bacteria = os.path.join(Molecules_pseudoknotfree_dbNH, BACTERIA_DIR)
dbnh_eukaryota = os.path.join(Molecules_pseudoknotfree_dbNH, EUKARYOTA_DIR)
ctnh_archaea = os.path.join(Molecules_pseudoknotfree_ctNH, ARCHAEA_DIR)
ctnh_bacteria = os.path.join(Molecules_pseudoknotfree_ctNH, BACTERIA_DIR)
ctnh_eukaryota = os.path.join(Molecules_pseudoknotfree_ctNH, EUKARYOTA_DIR)
# workbench_results
# distances
workbench_results = os.path.join(WORKBENCH_PATH, 'workbench_results')
Molecules_pseudoknotfree = os.path.join(workbench_results, 'Molecules-pseudoknotfree')
result_Archaea_90_110_allType = os.path.join(workbench_results, 'Archaea-90-110-allType')
distances_Archaea_90_110_allType = os.path.join(result_Archaea_90_110_allType, 'distances')
ARCHAEA_DISTANCES_DIR = os.path.join(ARCHAEA_DIR, 'distances')
BACTERIA_DISTANCES_DIR = os.path.join(BACTERIA_DIR, 'distances')
EUKARYOTA_DISTANCES_DIR = os.path.join(EUKARYOTA_DIR, 'distances')
# cores
core_calculator_workbench = os.path.join(WORKBENCH_PATH, 'cores_calculator_workbench.py')
# clustering
cores_Archaea_90_110_allType_dir = os.path.join(result_Archaea_90_110_allType, 'cores')
ARCHAEA_CORES_DIR = os.path.join(ARCHAEA_DIR, 'cores')
BACTERIA_CORES_DIR = os.path.join(BACTERIA_DIR, 'cores')
EUKARYOTA_CORES_DIR = os.path.join(EUKARYOTA_DIR, 'cores')
# core plus
coreplus_Archaea_90_110_allType = os.path.join(cores_Archaea_90_110_allType_dir, 'core_plus')
ARCHAEA_COREPLUS = os.path.join(Molecules_pseudoknotfree, ARCHAEA_CORES_DIR, 'core_plus')
BACTERIA_COREPLUS = os.path.join(Molecules_pseudoknotfree, BACTERIA_CORES_DIR, 'core_plus')
EUKARYOTA_COREPLUS = os.path.join(Molecules_pseudoknotfree, EUKARYOTA_CORES_DIR, 'core_plus')
# core
core_Archaea_90_110_allType = os.path.join(cores_Archaea_90_110_allType_dir, 'core')
ARCHAEA_CORE = os.path.join(Molecules_pseudoknotfree, ARCHAEA_CORES_DIR, 'core')
BACTERIA_CORE = os.path.join(Molecules_pseudoknotfree, BACTERIA_CORES_DIR, 'core')
EUKARYOTA_CORE = os.path.join(Molecules_pseudoknotfree, EUKARYOTA_CORES_DIR, 'core')
# clustering
clustering_Archaea_90_110_allType = os.path.join(result_Archaea_90_110_allType, 'clustering')
ARCHAEA_CLUSTERING_DIR = os.path.join(Molecules_pseudoknotfree, ARCHAEA_DIR, 'clustering')
BACTERIA_CLUSTERING_DIR = os.path.join(Molecules_pseudoknotfree, BACTERIA_DIR, 'clustering')
EUKARYOTA_CLUSTERING_DIR = os.path.join(Molecules_pseudoknotfree, EUKARYOTA_DIR, 'clustering')

result_AT_aspralign = os.path.join(distances_Archaea_90_110_allType, 'aspralign.csv')
result_AT_dualgraph = os.path.join(distances_Archaea_90_110_allType, 'dualgraph.csv')
result_AT_nestedalign = os.path.join(distances_Archaea_90_110_allType, 'nestedalign.csv')
result_AT_rnadistance = os.path.join(distances_Archaea_90_110_allType, 'rnadistance.csv')
result_AT_rnaforester = os.path.join(distances_Archaea_90_110_allType, 'rnaforester.csv')
result_AT_treegraph = os.path.join(distances_Archaea_90_110_allType, 'treegraph.csv')

result_MP_aspralign_Archaea = os.path.join(Molecules_pseudoknotfree, ARCHAEA_DISTANCES_DIR, 'aspralign.csv')
result_MP_dualgraph_Archaea = os.path.join(Molecules_pseudoknotfree, ARCHAEA_DISTANCES_DIR, 'dualgraph.csv')
result_MP_nestedalign_Archaea = os.path.join(Molecules_pseudoknotfree, ARCHAEA_DISTANCES_DIR, 'nestedalign.csv')
result_MP_rnadistance_Archaea = os.path.join(Molecules_pseudoknotfree, ARCHAEA_DISTANCES_DIR, 'rnadistance.csv')
result_MP_rnaforester_Archaea = os.path.join(Molecules_pseudoknotfree, ARCHAEA_DISTANCES_DIR, 'rnaforester.csv')
result_MP_treegraph_Archaea = os.path.join(Molecules_pseudoknotfree, ARCHAEA_DISTANCES_DIR, 'treegraph.csv')

result_MP_aspralign_Bacteria = os.path.join(Molecules_pseudoknotfree, BACTERIA_DISTANCES_DIR, 'aspralign.csv')
result_MP_dualgraph_Bacteria = os.path.join(Molecules_pseudoknotfree, BACTERIA_DISTANCES_DIR, 'dualgraph.csv')
result_MP_nestedalign_Bacteria = os.path.join(Molecules_pseudoknotfree, BACTERIA_DISTANCES_DIR, 'nestedalign.csv')
result_MP_rnadistance_Bacteria = os.path.join(Molecules_pseudoknotfree, BACTERIA_DISTANCES_DIR, 'rnadistance.csv')
result_MP_rnaforester_Bacteria = os.path.join(Molecules_pseudoknotfree, BACTERIA_DISTANCES_DIR, 'rnaforester.csv')
result_MP_treegraph_Bacteria = os.path.join(Molecules_pseudoknotfree, BACTERIA_DISTANCES_DIR, 'treegraph.csv')

result_MP_aspralign_Eukaryota = os.path.join(Molecules_pseudoknotfree, EUKARYOTA_DISTANCES_DIR, 'aspralign.csv')
result_MP_dualgraph_Eukaryota = os.path.join(Molecules_pseudoknotfree, EUKARYOTA_DISTANCES_DIR, 'dualgraph.csv')
result_MP_nestedalign_Eukaryota = os.path.join(Molecules_pseudoknotfree, EUKARYOTA_DISTANCES_DIR, 'nestedalign.csv')
result_MP_rnadistance_Eukaryota = os.path.join(Molecules_pseudoknotfree, EUKARYOTA_DISTANCES_DIR, 'rnadistance.csv')
result_MP_rnaforester_Eukaryota = os.path.join(Molecules_pseudoknotfree, EUKARYOTA_DISTANCES_DIR, 'rnaforester.csv')
result_MP_treegraph_Eukaryota = os.path.join(Molecules_pseudoknotfree, EUKARYOTA_DISTANCES_DIR, 'treegraph.csv')
