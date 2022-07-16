#!/usr/bin/env python3
import aspralign_workbench
import nestedalign_workbench
import rnaforester_workbench
import rnadistance_workbench
from paths import *

if __name__ == '__main__':
    aspralign_workbench.csv([ARCHAEA_DIR, BACTERIA_DIR, EUKARYOTA_DIR],
                            [ASPRALIGN_ARCHAEA_OUTPUT_FILE, ASPRALIGN_BACTERIA_OUTPUT_FILE,
                             ASPRALIGN_EUKARYOTA_OUTPUT_FILE], ASPRALIGN_WORKBENCH_JAR, ASPRALIGN_CONFIG_FILE)

    nestedalign_workbench.csv([ARCHAEA_DIR, BACTERIA_DIR, EUKARYOTA_DIR],
                              [NESTEDALIGN_ARCHAEA_OUTPUT_FILE, NESTEDALIGN_BACTERIA_OUTPUT_FILE,
                               NESTEDALIGN_EUKARYOTA_OUTPUT_FILE])

    rnaforester_workbench.csv([ARCHAEA_DIR, BACTERIA_DIR, EUKARYOTA_DIR],
                              [NESTEDALIGN_ARCHAEA_OUTPUT_FILE, NESTEDALIGN_BACTERIA_OUTPUT_FILE,
                               NESTEDALIGN_EUKARYOTA_OUTPUT_FILE])

    rnadistance_workbench.csv([ARCHAEA_DIR, BACTERIA_DIR, EUKARYOTA_DIR],
                              [NESTEDALIGN_ARCHAEA_OUTPUT_FILE, NESTEDALIGN_BACTERIA_OUTPUT_FILE,
                               NESTEDALIGN_EUKARYOTA_OUTPUT_FILE])