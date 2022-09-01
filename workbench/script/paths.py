import os
import sys

# root directory of the workbench
WORKBENCH_PATH = os.path.dirname(os.path.dirname(os.path.realpath(sys.argv[0])))

# workbench results directory
WORKBENCH_RESULTS = os.path.join(WORKBENCH_PATH, 'workbench-results')
# cores
WORKBENCH_RESULTS_ARCHAEA_CORES = os.path.join(WORKBENCH_RESULTS, 'Archaea', 'cores')
WORKBENCH_RESULTS_BACTERIA_CORES = os.path.join(WORKBENCH_RESULTS, 'Bacteria', 'cores')
WORKBENCH_RESULTS_EUKARYOTA_CORES = os.path.join(WORKBENCH_RESULTS, 'Eukaryota', 'cores')
# distances
WORKBENCH_RESULTS_ARCHAEA_DISTANCES = os.path.join(WORKBENCH_RESULTS, 'Archaea', 'distances')
WORKBENCH_RESULTS_BACTERIA_DISTANCES = os.path.join(WORKBENCH_RESULTS, 'Bacteria', 'distances')
WORKBENCH_RESULTS_EUKARYOTA_DISTANCES = os.path.join(WORKBENCH_RESULTS, 'Eukaryota', 'distances')

# molecules directory
ARCHAEA_DIR = os.path.join(WORKBENCH_PATH, 'Molecules-pseudoknotfree', 'db', 'Archaea', '5S')
BACTERIA_DIR = os.path.join(WORKBENCH_PATH, 'Molecules-pseudoknotfree', 'db', 'Bacteria', '5S')
EUKARYOTA_DIR = os.path.join(WORKBENCH_PATH, 'Molecules-pseudoknotfree', 'db', 'Eukaryota', '5S')

# ASPRAlign
ASPRALIGN_WORKBENCH_JAR = os.path.join(os.sep, 'gp', 'aspralign', 'executable-jar', 'ASPRAlignWorkbench.jar')
ASPRALIGN_CONFIG_FILE = os.path.join(os.sep, 'gp', 'aspralign', 'ASPRAlign-config.txt')
# core aspralign jar for clustering
CORE_JAR = os.path.join(WORKBENCH_PATH, 'core', 'coresCalculator.jar')

# distances output files
ASPRALIGN_ARCHAEA_OUTPUT_FILE = os.path.join(WORKBENCH_RESULTS_ARCHAEA_DISTANCES, '5S-aspralign.csv')
ASPRALIGN_BACTERIA_OUTPUT_FILE = os.path.join(WORKBENCH_RESULTS_BACTERIA_DISTANCES, '5S-aspralign.csv')
ASPRALIGN_EUKARYOTA_OUTPUT_FILE = os.path.join(WORKBENCH_RESULTS_EUKARYOTA_DISTANCES, '5S-aspralign.csv')

NESTEDALIGN_ARCHAEA_OUTPUT_FILE = os.path.join(WORKBENCH_RESULTS_ARCHAEA_DISTANCES, '5S-nestedalign.csv')
NESTEDALIGN_BACTERIA_OUTPUT_FILE = os.path.join(WORKBENCH_RESULTS_BACTERIA_DISTANCES, '5S-nestedalign.csv')
NESTEDALIGN_EUKARYOTA_OUTPUT_FILE = os.path.join(WORKBENCH_RESULTS_EUKARYOTA_DISTANCES, '5S-nestedalign.csv')

RNAFORESTER_ARCHAEA_OUTPUT_FILE = os.path.join(WORKBENCH_RESULTS_ARCHAEA_DISTANCES, '5S-rnaforester.csv')
RNAFORESTER_BACTERIA_OUTPUT_FILE = os.path.join(WORKBENCH_RESULTS_BACTERIA_DISTANCES, '5S-rnaforester.csv')
RNAFORESTER_EUKARYOTA_OUTPUT_FILE = os.path.join(WORKBENCH_RESULTS_EUKARYOTA_DISTANCES, '5S-rnaforester.csv')

RNADISTANCE_ARCHAEA_OUTPUT_FILE = os.path.join(WORKBENCH_RESULTS_ARCHAEA_DISTANCES, '5S-rnadistance.csv')
RNADISTANCE_BACTERIA_OUTPUT_FILE = os.path.join(WORKBENCH_RESULTS_BACTERIA_DISTANCES, '5S-rnadistance.csv')
RNADISTANCE_EUKARYOTA_OUTPUT_FILE = os.path.join(WORKBENCH_RESULTS_EUKARYOTA_DISTANCES, '5S-rnadistance.csv')
