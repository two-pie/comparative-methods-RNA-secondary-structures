import os
import sys

# root directory of the workbench
WORKBENCH_PATH = os.path.dirname(os.path.dirname(os.path.realpath(sys.argv[0])))

# molecule directory
ARCHAEA_DIR = os.path.join(WORKBENCH_PATH, 'Molecules-pseudoknotfree', 'db-nH', 'Archaea', '5S')
BACTERIA_DIR = os.path.join(WORKBENCH_PATH, 'Molecules-pseudoknotfree', 'db-nH', 'Bacteria', '5S')
EUKARYOTA_DIR = os.path.join(WORKBENCH_PATH, 'Molecules-pseudoknotfree', 'db-nH', 'Eukaryota', '5S')

# ASPRAlign
ASPRALIGN_WORKBENCH_JAR = os.path.join(WORKBENCH_PATH, 'script', 'aspralign', 'ASPRAlignWorkbench.jar')
ASPRALIGN_CONFIG_FILE = os.path.join(WORKBENCH_PATH, 'script', 'aspralign', 'ASPRAlign-config.txt')

# output files
ASPRALIGN_ARCHAEA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'workbench-results', 'Archaea', '5S-aspralign.csv')
ASPRALIGN_BACTERIA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'workbench-results', 'Bacteria', '5S-aspralign.csv')
ASPRALIGN_EUKARYOTA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'workbench-results', 'Eukaryota', '5S-aspralign.csv')
NESTEDALIGN_ARCHAEA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'workbench-results', 'Archaea', '5S-nestedalign.csv')
NESTEDALIGN_BACTERIA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'workbench-results', 'Bacteria', '5S-nestedalign.csv')
NESTEDALIGN_EUKARYOTA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'workbench-results', 'Eukaryota', '5S-nestedalign.csv')
RNAFORESTER_ARCHAEA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'workbench-results', 'Archaea', '5S-rnaforester.csv')
RNAFORESTER_BACTERIA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'workbench-results', 'Bacteria', '5S-rnaforester.csv')
RNAFORESTER_EUKARYOTA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'workbench-results', 'Eukaryota', '5S-rnaforester.csv')
