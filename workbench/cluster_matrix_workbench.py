import subprocess

from workbench.paths import *

# clustering for Archaea-90-110-allType
# core plus
subprocess.run(
    [cluster_matrix_workbench, coreplus_Archaea_90_110_allType, result_AT_aspralign,
     os.path.join(clustering_Archaea_90_110_allType, 'aspralign_clustering_matrix.csv')])
subprocess.run(
    [cluster_matrix_workbench, coreplus_Archaea_90_110_allType, result_AT_dualgraph,
     os.path.join(clustering_Archaea_90_110_allType, 'dualgraph_clustering_matrix.csv')])
subprocess.run(
    [cluster_matrix_workbench, coreplus_Archaea_90_110_allType, result_AT_nestedalign,
     os.path.join(clustering_Archaea_90_110_allType, 'nestedalign_clustering_matrix.csv')])
subprocess.run(
    [cluster_matrix_workbench, coreplus_Archaea_90_110_allType, result_AT_rnadistance,
     os.path.join(clustering_Archaea_90_110_allType, 'rnadistance_clustering_matrix.csv')])
subprocess.run(
    [cluster_matrix_workbench, coreplus_Archaea_90_110_allType, result_AT_rnaforester,
     os.path.join(clustering_Archaea_90_110_allType, 'rnaforester_clustering_matrix.csv')])
subprocess.run(
    [cluster_matrix_workbench, coreplus_Archaea_90_110_allType, result_AT_treegraph,
     os.path.join(clustering_Archaea_90_110_allType, 'treegraph_clustering_matrix.csv')])
# core
subprocess.run(
    [cluster_matrix_workbench, core_Archaea_90_110_allType, result_AT_aspralign,
     os.path.join(clustering_Archaea_90_110_allType, 'aspralign_clustering_matrix.csv')])
subprocess.run(
    [cluster_matrix_workbench, core_Archaea_90_110_allType, result_AT_dualgraph,
     os.path.join(clustering_Archaea_90_110_allType, 'dualgraph_clustering_matrix.csv')])
subprocess.run(
    [cluster_matrix_workbench, core_Archaea_90_110_allType, result_AT_nestedalign,
     os.path.join(clustering_Archaea_90_110_allType, 'nestedalign_clustering_matrix.csv')])
subprocess.run(
    [cluster_matrix_workbench, core_Archaea_90_110_allType, result_AT_rnadistance,
     os.path.join(clustering_Archaea_90_110_allType, 'rnadistance_clustering_matrix.csv')])
subprocess.run(
    [cluster_matrix_workbench, core_Archaea_90_110_allType, result_AT_rnaforester,
     os.path.join(clustering_Archaea_90_110_allType, 'rnaforester_clustering_matrix.csv')])
subprocess.run(
    [cluster_matrix_workbench, core_Archaea_90_110_allType, result_AT_treegraph,
     os.path.join(clustering_Archaea_90_110_allType, 'treegraph_clustering_matrix.csv')])

# clustering for Molecules-pseudoknotfree
# Archaea
# core plus
subprocess.run([cluster_matrix_workbench, ARCHAEA_COREPLUS, result_MP_aspralign_Archaea,
                os.path.join(ARCHAEA_CLUSTERING_DIR, 'aspralign_clustering_matrix.csv')])
subprocess.run([cluster_matrix_workbench, ARCHAEA_COREPLUS, result_MP_dualgraph_Archaea,
                os.path.join(ARCHAEA_CLUSTERING_DIR, 'dualgraph_clustering_matrix.csv')])
subprocess.run([cluster_matrix_workbench, ARCHAEA_COREPLUS, result_MP_nestedalign_Archaea,
                os.path.join(ARCHAEA_CLUSTERING_DIR, 'nestedalign_clustering_matrix.csv')])
subprocess.run([cluster_matrix_workbench, ARCHAEA_COREPLUS, result_MP_rnadistance_Archaea,
                os.path.join(ARCHAEA_CLUSTERING_DIR, 'rnadistance_clustering_matrix.csv')])
subprocess.run([cluster_matrix_workbench, ARCHAEA_COREPLUS, result_AT_rnaforester,
                os.path.join(ARCHAEA_CLUSTERING_DIR, 'rnaforester_clustering_matrix.csv')])
subprocess.run([cluster_matrix_workbench, ARCHAEA_COREPLUS, result_MP_treegraph_Archaea,
                os.path.join(ARCHAEA_CLUSTERING_DIR, 'treegraph_clustering_matrix.csv')])
# core
subprocess.run([cluster_matrix_workbench, ARCHAEA_CORES, result_MP_aspralign_Archaea,
                os.path.join(ARCHAEA_CLUSTERING_DIR, 'aspralign_clustering_matrix.csv')])
subprocess.run([cluster_matrix_workbench, ARCHAEA_CORES, result_MP_dualgraph_Archaea,
                os.path.join(ARCHAEA_CLUSTERING_DIR, 'dualgraph_clustering_matrix.csv')])
subprocess.run([cluster_matrix_workbench, ARCHAEA_CORES, result_MP_nestedalign_Archaea,
                os.path.join(ARCHAEA_CLUSTERING_DIR, 'nestedalign_clustering_matrix.csv')])
subprocess.run([cluster_matrix_workbench, ARCHAEA_CORES, result_MP_rnadistance_Archaea,
                os.path.join(ARCHAEA_CLUSTERING_DIR, 'rnadistance_clustering_matrix.csv')])
subprocess.run([cluster_matrix_workbench, ARCHAEA_CORES, result_AT_rnaforester,
                os.path.join(ARCHAEA_CLUSTERING_DIR, 'rnaforester_clustering_matrix.csv')])
subprocess.run([cluster_matrix_workbench, ARCHAEA_CORES, result_MP_treegraph_Archaea,
                os.path.join(ARCHAEA_CLUSTERING_DIR, 'treegraph_clustering_matrix.csv')])

# Bacteria
# core plus
subprocess.run([cluster_matrix_workbench, BACTERIA_COREPLUS, result_MP_aspralign_Bacteria,
                os.path.join(BACTERIA_CLUSTERING_DIR, 'aspralign_clustering_matrix.csv')])
subprocess.run([cluster_matrix_workbench, BACTERIA_COREPLUS, result_MP_dualgraph_Bacteria,
                os.path.join(BACTERIA_CLUSTERING_DIR, 'dualgraph_clustering_matrix.csv')])
subprocess.run([cluster_matrix_workbench, BACTERIA_COREPLUS, result_MP_nestedalign_Bacteria,
                os.path.join(BACTERIA_CLUSTERING_DIR, 'nestedalign_clustering_matrix.csv')])
subprocess.run([cluster_matrix_workbench, BACTERIA_COREPLUS, result_MP_rnadistance_Bacteria,
                os.path.join(BACTERIA_CLUSTERING_DIR, 'rnadistance_clustering_matrix.csv')])
subprocess.run([cluster_matrix_workbench, BACTERIA_COREPLUS, result_MP_rnaforester_Bacteria,
                os.path.join(BACTERIA_CLUSTERING_DIR, 'rnaforester_clustering_matrix.csv')])
subprocess.run([cluster_matrix_workbench, BACTERIA_COREPLUS, result_MP_treegraph_Bacteria,
                os.path.join(BACTERIA_CLUSTERING_DIR, 'treegraph_clustering_matrix.csv')])
# core
subprocess.run([cluster_matrix_workbench, BACTERIA_CORES, result_MP_aspralign_Bacteria,
                os.path.join(BACTERIA_CLUSTERING_DIR, 'aspralign_clustering_matrix.csv')])
subprocess.run([cluster_matrix_workbench, BACTERIA_CORES, result_MP_dualgraph_Bacteria,
                os.path.join(BACTERIA_CLUSTERING_DIR, 'dualgraph_clustering_matrix.csv')])
subprocess.run([cluster_matrix_workbench, BACTERIA_CORES, result_MP_nestedalign_Bacteria,
                os.path.join(BACTERIA_CLUSTERING_DIR, 'nestedalign_clustering_matrix.csv')])
subprocess.run([cluster_matrix_workbench, BACTERIA_CORES, result_MP_rnadistance_Bacteria,
                os.path.join(BACTERIA_CLUSTERING_DIR, 'rnadistance_clustering_matrix.csv')])
subprocess.run([cluster_matrix_workbench, BACTERIA_CORES, result_MP_rnaforester_Bacteria,
                os.path.join(BACTERIA_CLUSTERING_DIR, 'rnaforester_clustering_matrix.csv')])
subprocess.run([cluster_matrix_workbench, BACTERIA_CORES, result_MP_treegraph_Bacteria,
                os.path.join(BACTERIA_CLUSTERING_DIR, 'treegraph_clustering_matrix.csv')])
# Eukaryota
# core plus
subprocess.run([cluster_matrix_workbench, EUKARYOTA_COREPLUS, result_MP_aspralign_Eukaryota,
                os.path.join(EUKARYOTA_CLUSTERING_DIR, 'aspralign_clustering_matrix.csv')])
subprocess.run([cluster_matrix_workbench, EUKARYOTA_COREPLUS, result_MP_dualgraph_Eukaryota,
                os.path.join(EUKARYOTA_CLUSTERING_DIR, 'dualgraph_clustering_matrix.csv')])
subprocess.run([cluster_matrix_workbench, EUKARYOTA_COREPLUS, result_MP_nestedalign_Eukaryota,
                os.path.join(EUKARYOTA_CLUSTERING_DIR, 'nestedalign_clustering_matrix.csv')])
subprocess.run([cluster_matrix_workbench, EUKARYOTA_COREPLUS, result_MP_rnadistance_Eukaryota,
                os.path.join(EUKARYOTA_CLUSTERING_DIR, 'rnadistance_clustering_matrix.csv')])
subprocess.run([cluster_matrix_workbench, EUKARYOTA_COREPLUS, result_MP_rnaforester_Eukaryota,
                os.path.join(EUKARYOTA_CLUSTERING_DIR, 'rnaforester_clustering_matrix.csv')])
subprocess.run([cluster_matrix_workbench, EUKARYOTA_COREPLUS, result_MP_treegraph_Eukaryota,
                os.path.join(EUKARYOTA_CLUSTERING_DIR, 'treegraph_clustering_matrix.csv')])
# core
subprocess.run([cluster_matrix_workbench, EUKARYOTA_CORES, result_MP_aspralign_Eukaryota,
                os.path.join(EUKARYOTA_CLUSTERING_DIR, 'aspralign_clustering_matrix.csv')])
subprocess.run([cluster_matrix_workbench, EUKARYOTA_CORES, result_MP_dualgraph_Eukaryota,
                os.path.join(EUKARYOTA_CLUSTERING_DIR, 'dualgraph_clustering_matrix.csv')])
subprocess.run([cluster_matrix_workbench, EUKARYOTA_CORES, result_MP_nestedalign_Eukaryota,
                os.path.join(EUKARYOTA_CLUSTERING_DIR, 'nestedalign_clustering_matrix.csv')])
subprocess.run([cluster_matrix_workbench, EUKARYOTA_CORES, result_MP_rnadistance_Eukaryota,
                os.path.join(EUKARYOTA_CLUSTERING_DIR, 'rnadistance_clustering_matrix.csv')])
subprocess.run([cluster_matrix_workbench, EUKARYOTA_CORES, result_MP_rnaforester_Eukaryota,
                os.path.join(EUKARYOTA_CLUSTERING_DIR, 'rnaforester_clustering_matrix.csv')])
subprocess.run([cluster_matrix_workbench, EUKARYOTA_CORES, result_MP_treegraph_Eukaryota,
                os.path.join(EUKARYOTA_CLUSTERING_DIR, 'treegraph_clustering_matrix.csv')])
