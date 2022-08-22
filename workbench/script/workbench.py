import aspralign_workbench
import nestedalign_workbench
import rnaforester_workbench
import rnadistance_workbench
import subprocess
from paths import *

if __name__ == '__main__':
    '''    # Distance calculator
    aspralign_workbench.csv([ARCHAEA_DIR, BACTERIA_DIR, EUKARYOTA_DIR],
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
                               RNADISTANCE_EUKARYOTA_OUTPUT_FILE])
    # Core calculator
    subprocess.run(['java', '-jar', CORE_JAR], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    '''

    label = os.path.join(WORKBENCH_RESULTS_ARCHAEA, 'Archaea_core1.csv')
    # Clustering
    subprocess.run(['python', 'ClusterMatrix.py', label, ASPRALIGN_ARCHAEA_OUTPUT_FILE])
