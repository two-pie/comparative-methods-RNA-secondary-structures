#!/usr/bin/env python3

import subprocess
from paths import *

print('\x1b[0;31;40m' + 'CORES CALCULATOR TOOL' + '\x1b[0m')
# Archaea-90-110-allType
subprocess.run(
    ['java', '-jar', 'cores_calculator_tool', '-csv', DBNFilesNH, cores_Archaea_90_110_allType_dir])
print('\x1b[1;32;40m' + f'{coreplus_Archaea_90_110_allType} created' + '\x1b[0m')
print('\x1b[1;32;40m' + f'{core_Archaea_90_110_allType} created' + '\x1b[0m')
# Molecules-pseudoknotfree
# 5S
subprocess.run(
    ['java', '-jar', 'cores_calculator_tool', '-csv', dbnh_archaea, ARCHAEA_CORES_DIR])
print('\x1b[1;32;40m' + f'{ARCHAEA_COREPLUS} created' + '\x1b[0m')
print('\x1b[1;32;40m' + f'{ARCHAEA_CORES} created' + '\x1b[0m')
subprocess.run(
    ['java', '-jar', 'cores_calculator_tool', '-csv', dbnh_bacteria, BACTERIA_CORES_DIR])
print('\x1b[1;32;40m' + f'{BACTERIA_COREPLUS} created' + '\x1b[0m')
print('\x1b[1;32;40m' + f'{BACTERIA_CORES} created' + '\x1b[0m')
subprocess.run(
    ['java', '-jar', 'cores_calculator_tool', '-csv', dbnh_eukaryota, EUKARYOTA_CORES_DIR])
print('\x1b[1;32;40m' + f'{EUKARYOTA_COREPLUS} created' + '\x1b[0m')
print('\x1b[1;32;40m' + f'{EUKARYOTA_CORES} created' + '\x1b[0m')
