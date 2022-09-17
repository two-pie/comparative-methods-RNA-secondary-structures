#!/usr/bin/env python3

import subprocess
from paths import *


print('\x1b[0;31;40m' + 'CORES CALCULATOR TOOL' + '\x1b[0m')
# Archaea-90-110-allType
subprocess.run(
    ['cores_calculator_tool', '-csv', DBNFilesNH, coreplus_Archaea_90_110_allType, core_Archaea_90_110_allType])
print('\x1b[1;32;40m' + f'{coreplus_Archaea_90_110_allType} created' + '\x1b[0m')
print('\x1b[1;32;40m' + f'{core_Archaea_90_110_allType} created' + '\x1b[0m')
# Molecules-pseudoknotfree
# 5S
subprocess.run(
    ['cores_calculator_tool', '-csv', dbnh_archaea, ARCHAEA_COREPLUS, ARCHAEA_CORE])
print('\x1b[1;32;40m' + f'{ARCHAEA_COREPLUS} created' + '\x1b[0m')
print('\x1b[1;32;40m' + f'{ARCHAEA_CORE} created' + '\x1b[0m')
subprocess.run(
    ['cores_calculator_tool', '-csv', dbnh_bacteria, BACTERIA_COREPLUS, BACTERIA_CORE])
print('\x1b[1;32;40m' + f'{BACTERIA_COREPLUS} created' + '\x1b[0m')
print('\x1b[1;32;40m' + f'{BACTERIA_CORE} created' + '\x1b[0m')
subprocess.run(
    ['cores_calculator_tool', '-csv', dbnh_eukaryota, EUKARYOTA_COREPLUS, EUKARYOTA_CORE])
print('\x1b[1;32;40m' + f'{EUKARYOTA_COREPLUS} created' + '\x1b[0m')
print('\x1b[1;32;40m' + f'{EUKARYOTA_CORE} created' + '\x1b[0m')
