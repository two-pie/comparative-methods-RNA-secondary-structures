#!/usr/bin/env python3
import aspralign_workbench
import nestedalign_workbench
import os
import sys

GROUP_PROJECT = os.path.dirname(os.path.dirname(os.path.realpath(sys.argv[0])))
ARCHAEA = os.path.join(GROUP_PROJECT, 'Molecules-pseudoknotfree', 'db-nH', 'Archaea', '5S')
BACTERIA = os.path.join(GROUP_PROJECT, 'Molecules-pseudoknotfree', 'db-nH', 'Bacteria', '5S')
EUKARYOTA = os.path.join(GROUP_PROJECT, 'Molecules-pseudoknotfree', 'db-nH', 'Eukaryota', '5S')
ARCHAEA_OUTPUT = os.path.join(GROUP_PROJECT, 'benchmark-results', 'Archaea')
BACTERIA_OUTPUT = os.path.join(GROUP_PROJECT, 'benchmark-results', 'Bacteria')
EUKARYOTA_OUTPUT = os.path.join(GROUP_PROJECT, 'benchmark-results', 'Eukaryota')
ASPRALIGN_WORKBENCH_JAR = os.path.join(GROUP_PROJECT, 'ASPRAlign-0.92')

if __name__ == '__main__':
    aspralign_workbench.csv([ARCHAEA, BACTERIA, EUKARYOTA], [os.path.join(ARCHAEA_OUTPUT, '5S-aspralign.csv'),
                                                             os.path.join(BACTERIA_OUTPUT, '5S-aspralign.csv'),
                                                             os.path.join(EUKARYOTA_OUTPUT, '5S-aspralign.csv')],
                            ASPRALIGN_WORKBENCH_JAR)
    nestedalign_workbench.csv([ARCHAEA, BACTERIA, EUKARYOTA], [ARCHAEA_OUTPUT, BACTERIA_OUTPUT, EUKARYOTA_OUTPUT])
