import subprocess

from paths import *

print('\x1b[0;31;40m' + 'CLUSTER MATRIX TOOL' + '\x1b[0m')
# clustering for Archaea-90-110-allType
# core plus
subprocess.run(
    ['cluster_matrix', os.path.join(coreplus_Archaea_90_110_allType, 'corePlus.csv'), result_AT_aspralign,
     os.path.join(clustering_Archaea_90_110_allType, 'aspralign_clustering_matrix_corePlus.csv')])
subprocess.run(
    ['cluster_matrix', os.path.join(coreplus_Archaea_90_110_allType, 'corePlus.csv'), result_AT_nestedalign,
     os.path.join(clustering_Archaea_90_110_allType, 'nestedalign_clustering_matrix_corePlus.csv')])
subprocess.run(
    ['cluster_matrix', os.path.join(coreplus_Archaea_90_110_allType, 'corePlus.csv'), result_AT_rnadistance,
     os.path.join(clustering_Archaea_90_110_allType, 'rnadistance_clustering_matrix_corePlus.csv')])
subprocess.run(
    ['cluster_matrix', os.path.join(coreplus_Archaea_90_110_allType, 'corePlus.csv'), result_AT_rnaforester,
     os.path.join(clustering_Archaea_90_110_allType, 'rnaforester_clustering_matrix_corePlus.csv')])

# core
subprocess.run(
    ['cluster_matrix', os.path.join(core_Archaea_90_110_allType, 'core.csv'), result_AT_aspralign,
     os.path.join(clustering_Archaea_90_110_allType, 'aspralign_clustering_matrix_core.csv')])
subprocess.run(
    ['cluster_matrix', os.path.join(core_Archaea_90_110_allType, 'core.csv'), result_AT_nestedalign,
     os.path.join(clustering_Archaea_90_110_allType, 'nestedalign_clustering_matrix_core.csv')])
subprocess.run(
    ['cluster_matrix', os.path.join(core_Archaea_90_110_allType, 'core.csv'), result_AT_rnadistance,
     os.path.join(clustering_Archaea_90_110_allType, 'rnadistance_clustering_matrix_core.csv')])
subprocess.run(
    ['cluster_matrix', os.path.join(core_Archaea_90_110_allType, 'core.csv'), result_AT_rnaforester,
     os.path.join(clustering_Archaea_90_110_allType, 'rnaforester_clustering_matrix_core.csv')])

# clustering for Molecules-pseudoknotfree
# Archaea
# core plus
subprocess.run(['cluster_matrix', os.path.join(ARCHAEA_COREPLUS, 'corePlus.csv'), result_MP_aspralign_Archaea,
                os.path.join(ARCHAEA_CLUSTERING_DIR, 'aspralign_clustering_matrix_corePlus.csv')])
subprocess.run(['cluster_matrix', os.path.join(ARCHAEA_COREPLUS, 'corePlus.csv'), result_MP_nestedalign_Archaea,
                os.path.join(ARCHAEA_CLUSTERING_DIR, 'nestedalign_clustering_matrix_corePlus.csv')])
subprocess.run(
    ['cluster_matrix', os.path.join(ARCHAEA_COREPLUS, 'corePlus.csv'), result_MP_rnadistance_Archaea,
     os.path.join(ARCHAEA_CLUSTERING_DIR, 'rnadistance_clustering_matrix_corePlus.csv')])
subprocess.run(
    ['cluster_matrix', os.path.join(ARCHAEA_COREPLUS, 'corePlus.csv'), result_MP_rnaforester_Archaea,
     os.path.join(ARCHAEA_CLUSTERING_DIR, 'rnaforester_clustering_matrix_corePlus.csv')])
# core
subprocess.run(['cluster_matrix', os.path.join(ARCHAEA_CORE, 'core.csv'), result_MP_aspralign_Archaea,
                os.path.join(ARCHAEA_CLUSTERING_DIR, 'aspralign_clustering_matrix_core.csv')])
subprocess.run(['cluster_matrix', os.path.join(ARCHAEA_CORE, 'core.csv'), result_MP_nestedalign_Archaea,
                os.path.join(ARCHAEA_CLUSTERING_DIR, 'nestedalign_clustering_matrix_core.csv')])
subprocess.run(['cluster_matrix', os.path.join(ARCHAEA_CORE, 'core.csv'), result_MP_rnadistance_Archaea,
                os.path.join(ARCHAEA_CLUSTERING_DIR, 'rnadistance_clustering_matrix_core.csv')])
subprocess.run(['cluster_matrix', os.path.join(ARCHAEA_CORE, 'core.csv'), result_MP_rnaforester_Archaea,
                os.path.join(ARCHAEA_CLUSTERING_DIR, 'rnaforester_clustering_matrix_core.csv')])

# Bacteria
# core plus
subprocess.run(['cluster_matrix', os.path.join(BACTERIA_COREPLUS, 'corePlus.csv'), result_MP_aspralign_Bacteria,
                os.path.join(BACTERIA_CLUSTERING_DIR, 'aspralign_clustering_matrix_corePlus.csv')])
subprocess.run(
    ['cluster_matrix', os.path.join(BACTERIA_COREPLUS, 'corePlus.csv'), result_MP_nestedalign_Bacteria,
     os.path.join(BACTERIA_CLUSTERING_DIR, 'nestedalign_clustering_matrix_corePlus.csv')])
subprocess.run(
    ['cluster_matrix', os.path.join(BACTERIA_COREPLUS, 'corePlus.csv'), result_MP_rnadistance_Bacteria,
     os.path.join(BACTERIA_CLUSTERING_DIR, 'rnadistance_clustering_matrix_corePlus.csv')])
subprocess.run(
    ['cluster_matrix', os.path.join(BACTERIA_COREPLUS, 'corePlus.csv'), result_MP_rnaforester_Bacteria,
     os.path.join(BACTERIA_CLUSTERING_DIR, 'rnaforester_clustering_matrix_corePlus.csv')])
# core
subprocess.run(['cluster_matrix', os.path.join(BACTERIA_CORE, 'core.csv'), result_MP_aspralign_Bacteria,
                os.path.join(BACTERIA_CLUSTERING_DIR, 'aspralign_clustering_matrix_core.csv')])
subprocess.run(['cluster_matrix', os.path.join(BACTERIA_CORE, 'core.csv'), result_MP_nestedalign_Bacteria,
                os.path.join(BACTERIA_CLUSTERING_DIR, 'nestedalign_clustering_matrix_core.csv')])
subprocess.run(['cluster_matrix', os.path.join(BACTERIA_CORE, 'core.csv'), result_MP_rnadistance_Bacteria,
                os.path.join(BACTERIA_CLUSTERING_DIR, 'rnadistance_clustering_matrix_core.csv')])
subprocess.run(['cluster_matrix', os.path.join(BACTERIA_CORE, 'core.csv'), result_MP_rnaforester_Bacteria,
                os.path.join(BACTERIA_CLUSTERING_DIR, 'rnaforester_clustering_matrix_core.csv')])
# Eukaryota
# core plus
subprocess.run(
    ['cluster_matrix', os.path.join(EUKARYOTA_COREPLUS, 'corePlus.csv'), result_MP_aspralign_Eukaryota,
     os.path.join(EUKARYOTA_CLUSTERING_DIR, 'aspralign_clustering_matrix_corePlus.csv')])
subprocess.run(
    ['cluster_matrix', os.path.join(EUKARYOTA_COREPLUS, 'corePlus.csv'), result_MP_nestedalign_Eukaryota,
     os.path.join(EUKARYOTA_CLUSTERING_DIR, 'nestedalign_clustering_matrix_corePlus.csv')])
subprocess.run(
    ['cluster_matrix', os.path.join(EUKARYOTA_COREPLUS, 'corePlus.csv'), result_MP_rnadistance_Eukaryota,
     os.path.join(EUKARYOTA_CLUSTERING_DIR, 'rnadistance_clustering_matrix_corePlus.csv')])
subprocess.run(
    ['cluster_matrix', os.path.join(EUKARYOTA_COREPLUS, 'corePlus.csv'), result_MP_rnaforester_Eukaryota,
     os.path.join(EUKARYOTA_CLUSTERING_DIR, 'rnaforester_clustering_matrix_corePlus.csv')])
# core
subprocess.run(['cluster_matrix', os.path.join(EUKARYOTA_CORE, 'core.csv'), result_MP_aspralign_Eukaryota,
                os.path.join(EUKARYOTA_CLUSTERING_DIR, 'aspralign_clustering_matrix_core.csv')])
subprocess.run(['cluster_matrix', os.path.join(EUKARYOTA_CORE, 'core.csv'), result_MP_nestedalign_Eukaryota,
                os.path.join(EUKARYOTA_CLUSTERING_DIR, 'nestedalign_clustering_matrix_core..csv')])
subprocess.run(['cluster_matrix', os.path.join(EUKARYOTA_CORE, 'core.csv'), result_MP_rnadistance_Eukaryota,
                os.path.join(EUKARYOTA_CLUSTERING_DIR, 'rnadistance_clustering_matrix_core..csv')])
subprocess.run(['cluster_matrix', os.path.join(EUKARYOTA_CORE, 'core.csv'), result_MP_rnaforester_Eukaryota,
                os.path.join(EUKARYOTA_CLUSTERING_DIR, 'rnaforester_clustering_matrix_core..csv')])
