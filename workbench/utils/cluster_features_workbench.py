import subprocess

from paths import *

print('\x1b[0;31;40m' + 'CLUSTER FEATURES TOOL' + '\x1b[0m')
# clustering for Archaea-90-110-allType
# core plus
subprocess.run(
    ['cluster_features', os.path.join(coreplus_Archaea_90_110_allType, 'corePlus.csv'), result_AT_dualgraph,
     os.path.join(clustering_Archaea_90_110_allType, 'dualgraph_clustering_features_corePlus.csv')])
# subprocess.run( todo: da errore, aspettando lo script fixato
# [cluster_features_workbench, coreplus_Archaea_90_110_allType, result_AT_treegraph,
# os.path.join(clustering_Archaea_90_110_allType, 'treegraph_clustering_features.csv')])
# core
subprocess.run(
    ['cluster_features', os.path.join(core_Archaea_90_110_allType, 'core.csv'), result_AT_dualgraph,
     os.path.join(clustering_Archaea_90_110_allType, 'dualgraph_clustering_features_core.csv')])
# subprocess.run(
# ['cluster_features', core_Archaea_90_110_allType, result_AT_treegraph,
# os.path.join(clustering_Archaea_90_110_allType, 'treegraph_clustering_features_core.csv')])

# clustering for Molecules-pseudoknotfree
# Archaea
# core plus
subprocess.run(['cluster_features', os.path.join(ARCHAEA_COREPLUS, 'corePlus.csv'), result_MP_dualgraph_Archaea,
                os.path.join(ARCHAEA_CLUSTERING_DIR, 'dualgraph_clustering_features_corePlus.csv')])
subprocess.run(['cluster_features', os.path.join(ARCHAEA_COREPLUS, 'corePlus.csv'), result_MP_treegraph_Archaea,
                os.path.join(ARCHAEA_CLUSTERING_DIR, 'treegraph_clustering_features_corePlus.csv')])
# core
subprocess.run(['cluster_features', os.path.join(ARCHAEA_CORE, 'core.csv'), result_MP_dualgraph_Archaea,
                os.path.join(ARCHAEA_CLUSTERING_DIR, 'dualgraph_clustering_features_core.csv')])
subprocess.run(['cluster_features', os.path.join(ARCHAEA_CORE, 'core.csv'), result_MP_treegraph_Archaea,
                os.path.join(ARCHAEA_CLUSTERING_DIR, 'treegraph_clustering_features_core.csv')])

# Bacteria
# core plus
subprocess.run(['cluster_features', os.path.join(BACTERIA_COREPLUS, 'corePlus.csv'), result_MP_dualgraph_Bacteria,
                os.path.join(BACTERIA_CLUSTERING_DIR, 'dualgraph_clustering_features_corePlus.csv')])
subprocess.run(['cluster_features', os.path.join(BACTERIA_COREPLUS, 'corePlus.csv'), result_MP_treegraph_Bacteria,
                os.path.join(BACTERIA_CLUSTERING_DIR, 'treegraph_clustering_features_corePlus.csv')])
# core
subprocess.run(['cluster_features', os.path.join(BACTERIA_CORE, 'core.csv'), result_MP_dualgraph_Bacteria,
                os.path.join(BACTERIA_CLUSTERING_DIR, 'dualgraph_clustering_features_core.csv')])
subprocess.run(['cluster_features', os.path.join(BACTERIA_CORE, 'core.csv'), result_MP_treegraph_Bacteria,
                os.path.join(BACTERIA_CLUSTERING_DIR, 'treegraph_clustering_features_core.csv')])
# Eukaryota
# core plus
subprocess.run(['cluster_features', os.path.join(EUKARYOTA_COREPLUS, 'corePlus.csv'), result_MP_dualgraph_Eukaryota,
                os.path.join(EUKARYOTA_CLUSTERING_DIR, 'dualgraph_clustering_features_corePlus.csv')])
subprocess.run(['cluster_features', os.path.join(EUKARYOTA_COREPLUS, 'corePlus.csv'), result_MP_treegraph_Eukaryota,
                os.path.join(EUKARYOTA_CLUSTERING_DIR, 'treegraph_clustering_features_corePlus.csv')])
# core
subprocess.run(['cluster_features', os.path.join(EUKARYOTA_CORE, 'core.csv'), result_MP_dualgraph_Eukaryota,
                os.path.join(EUKARYOTA_CLUSTERING_DIR, 'dualgraph_clustering_features_core.csv')])
subprocess.run(['cluster_features', os.path.join(EUKARYOTA_CORE, 'core.csv'), result_MP_treegraph_Eukaryota,
                os.path.join(EUKARYOTA_CLUSTERING_DIR, 'treegraph_clustering_features_core.csv')])
