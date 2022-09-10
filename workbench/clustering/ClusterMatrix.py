#!/usr/bin/env python3
import sys
import pandas as pd
import numpy as np
from sklearn.cluster import *
from sklearn import metrics

if len(sys.argv) != 4:
    print("Usage: python3 " + sys.argv[
        0] + " <molecule-list-csv-file> <distances-csv-file> <distance_tool_result_csv_file>")
    sys.exit(1)
# Read the list of molecules
molecules = pd.read_csv(sys.argv[1], sep=";")

# Create dictionary Id -> Index
index_of = dict()
for i in range(len(molecules)):
    index_of[molecules.loc[i].loc['Id']] = i
label_of = dict()
if molecules.columns[2] == "CorePlus":
    # Create dictionary Id -> CorePlus
    for i in range(len(molecules)):
        label_of[molecules.loc[i].loc['Id']] = molecules.loc[i].loc['CorePlus'].strip()
else:
    # Create dictionary Id -> Core
    for i in range(len(molecules)):
        label_of[molecules.loc[i].loc['Id']] = molecules.loc[i].loc['Core'].strip()

# Read the list of distances
print("Reading", sys.argv[2], "...")
distances = pd.read_csv(sys.argv[2], sep=",")

# Create Distance Matrix
s = (len(molecules), len(molecules))
distance_matrix = np.zeros(s)

# Populate Distance Matrix
for k in range(len(distances)):
    i = index_of[distances.loc[k].loc['Molecule1']]
    j = index_of[distances.loc[k].loc['Molecule2']]
    value = distances.loc[k].loc['Distance']
    distance_matrix[i][j] = value
    distance_matrix[j][i] = value

# Determine the number of clusters as distinct labels in molecules
n_clusters = len(set(label_of.values()))
labels_true = list(label_of.values())

model = AgglomerativeClustering(n_clusters=n_clusters, affinity='precomputed', linkage='single').fit(distance_matrix)
labels_pred = model.fit_predict(distance_matrix)

f = open(sys.argv[2], 'w+')
f.write('Method,Rand_score,Homogeneity_score,completeness_score')
agg_csv = 'single,' + str(metrics.rand_score(labels_true, labels_pred)) + ',' + str(
    metrics.homogeneity_score(labels_true, labels_pred)) + ',' + str(
    metrics.completeness_score(labels_true, labels_pred))
f.write(agg_csv)
model = AgglomerativeClustering(n_clusters=n_clusters, affinity='precomputed', linkage='complete').fit(distance_matrix)
labels_pred = model.fit_predict(distance_matrix)

f.write('Method,Rand_score,Homogeneity_score,completeness_score')
agg_csv = 'complete,' + str(metrics.rand_score(labels_true, labels_pred)) + ',' + str(
    metrics.homogeneity_score(labels_true, labels_pred)) + ',' + str(
    metrics.completeness_score(labels_true, labels_pred))
f.write(agg_csv)
model = AgglomerativeClustering(n_clusters=n_clusters, affinity='precomputed', linkage='average').fit(distance_matrix)
labels_pred = model.fit_predict(distance_matrix)

f.write('Method,Rand_score,Homogeneity_score,completeness_score')
agg_csv = 'average,' + str(metrics.rand_score(labels_true, labels_pred)) + ',' + str(
    metrics.homogeneity_score(labels_true, labels_pred)) + ',' + str(
    metrics.completeness_score(labels_true, labels_pred))
f.write(agg_csv)

print('\x1b[1;32;40m' + f'{f} created' + '\x1b[0m')
