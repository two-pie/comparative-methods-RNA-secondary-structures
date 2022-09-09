#!/usr/bin/env python3

import subprocess
from workbench.paths import *

# Archaea-90-110-allType
subprocess.run(
    ['java', '-jar', 'cores_calculator_tool', '-csv', DBNFilesNH, cores_Archaea_90_110_allType_dir])
# Molecules-pseudoknotfree
# 5S
subprocess.run(
    ['java', '-jar', 'cores_calculator_tool', '-csv', dbnh_archaea, ARCHAEA_CORES_DIR])
subprocess.run(
    ['java', '-jar', 'cores_calculator_tool', '-csv', dbnh_bacteria, BACTERIA_CORES_DIR])
subprocess.run(
    ['java', '-jar', 'cores_calculator_tool', '-csv', dbnh_eukaryota, EUKARYOTA_CORES_DIR])
