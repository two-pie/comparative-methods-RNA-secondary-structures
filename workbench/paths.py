import os
import sys

# root directory of the workbench
WORKBENCH_PATH = os.path.dirname(os.path.realpath(sys.argv[0]))

# workbench results directory
WORKBENCH_RESULTS = os.path.join(WORKBENCH_PATH, 'workbench_results')

# Archaea-90-110-allType
DB_Archaea_90_110_allType = os.path.join(WORKBENCH_PATH, 'datasets', 'Archaea-90-110-allType')
DBNFiles = os.path.join(DB_Archaea_90_110_allType, 'DBNFiles')
DBNFilesNH = os.path.join(DB_Archaea_90_110_allType, 'DBNFilesNH')
CTFiles = os.path.join(DB_Archaea_90_110_allType, 'CTFiles')
CTFilesNH = os.path.join(DB_Archaea_90_110_allType, 'CTFilesNH')

# Molecules-pseudoknotfree
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
workbench_results = os.path.join(WORKBENCH_PATH, 'workbench_results')
result_Archaea_90_110_allType = os.path.join(workbench_results, 'Archaea-90-110-allType')
result_AT_aspralign = os.path.join(result_Archaea_90_110_allType, 'aspralign.csv')
result_AT_dualgraph = os.path.join(result_Archaea_90_110_allType, 'dualgraph.csv')
result_AT_nestedalign = os.path.join(result_Archaea_90_110_allType, 'nestedalign.csv')
result_AT_rnadistance = os.path.join(result_Archaea_90_110_allType, 'rnadistance.csv')
result_AT_rnaforester = os.path.join(result_Archaea_90_110_allType, 'rnaforester.csv')
result_AT_treegraph = os.path.join(result_Archaea_90_110_allType, 'treegraph.csv')

Molecules_pseudoknotfree = os.path.join(workbench_results, 'Molecules-pseudoknotfree')
result_MP_aspralign_Archaea = os.path.join(Molecules_pseudoknotfree, ARCHAEA_DIR, 'aspralign.csv')
result_MP_dualgraph_Archaea = os.path.join(Molecules_pseudoknotfree, ARCHAEA_DIR, 'dualgraph.csv')
result_MP_nestedalign_Archaea = os.path.join(Molecules_pseudoknotfree, ARCHAEA_DIR, 'nestedalign.csv')
result_MP_rnadistance_Archaea = os.path.join(Molecules_pseudoknotfree, ARCHAEA_DIR, 'rnadistance.csv')
result_MP_rnaforester_Archaea = os.path.join(Molecules_pseudoknotfree, ARCHAEA_DIR, 'rnaforester.csv')
result_MP_treegraph_Archaea = os.path.join(Molecules_pseudoknotfree, ARCHAEA_DIR, 'treegraph.csv')

result_MP_aspralign_Bacteria = os.path.join(Molecules_pseudoknotfree, BACTERIA_DIR, 'aspralign.csv')
result_MP_dualgraph_Bacteria = os.path.join(Molecules_pseudoknotfree, BACTERIA_DIR, 'dualgraph.csv')
result_MP_nestedalign_Bacteria = os.path.join(Molecules_pseudoknotfree, BACTERIA_DIR, 'nestedalign.csv')
result_MP_rnadistance_Bacteria = os.path.join(Molecules_pseudoknotfree, BACTERIA_DIR, 'rnadistance.csv')
result_MP_rnaforester_Bacteria = os.path.join(Molecules_pseudoknotfree, BACTERIA_DIR, 'rnaforester.csv')
result_MP_treegraph_Bacteria = os.path.join(Molecules_pseudoknotfree, BACTERIA_DIR, 'treegraph.csv')

result_MP_aspralign_Eukaryota = os.path.join(Molecules_pseudoknotfree, EUKARYOTA_DIR, 'aspralign.csv')
result_MP_dualgraph_Eukaryota = os.path.join(Molecules_pseudoknotfree, EUKARYOTA_DIR, 'dualgraph.csv')
result_MP_nestedalign_Eukaryota = os.path.join(Molecules_pseudoknotfree, EUKARYOTA_DIR, 'nestedalign.csv')
result_MP_rnadistance_Eukaryota = os.path.join(Molecules_pseudoknotfree, EUKARYOTA_DIR, 'rnadistance.csv')
result_MP_rnaforester_Eukaryota = os.path.join(Molecules_pseudoknotfree, EUKARYOTA_DIR, 'rnaforester.csv')
result_MP_treegraph_Eukaryota = os.path.join(Molecules_pseudoknotfree, EUKARYOTA_DIR, 'treegraph.csv')
