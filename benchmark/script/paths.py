import os
import sys

# root directory of the workbench
WORKBENCH_PATH = os.path.dirname(os.path.dirname(os.path.realpath(sys.argv[0])))

# molecule directory
ARCHAEA_DIR = os.path.join(WORKBENCH_PATH, 'Molecules-pseudoknotfree', 'db-nH', 'Archaea', '5S')
BACTERIA_DIR = os.path.join(WORKBENCH_PATH, 'Molecules-pseudoknotfree', 'db-nH', 'Bacteria', '5S')
EUKARYOTA_DIR = os.path.join(WORKBENCH_PATH, 'Molecules-pseudoknotfree', 'db-nH', 'Eukaryota', '5S')

# ASPRAlign jar
ASPRALIGN_WORKBENCH_JAR = os.path.join(WORKBENCH_PATH, 'ASPRAlign-0.92', 'ASPRAlignWorkbench.jar')
ASPRALIGN_JAR = os.path.join(WORKBENCH_PATH, 'ASPRAlign-0.92', 'ASPRAlign.jar')

# output files
ASPRALIGN_ARCHAEA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'benchmark-results', 'Archaea', '5S-aspralign.csv')
ASPRALIGN_BACTERIA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'benchmark-results', 'Bacteria', '5S-aspralign.csv')
ASPRALIGN_EUKARYOTA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'benchmark-results', 'Eukaryota', '5S-aspralign.csv')
NESTEDALIGN_ARCHAEA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'benchmark-results', 'Archaea', '5S-nestedalign.csv')
NESTEDALIGN_BACTERIA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'benchmark-results', 'Bacteria', '5S-nestedalign.csv')
NESTEDALIGN_EUKARYOTA_OUTPUT_FILE = os.path.join(WORKBENCH_PATH, 'benchmark-results', 'Eukaryota', '5S-nestedalign.csv')

