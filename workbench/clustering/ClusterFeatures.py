#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import sys
import pandas as pd

from sklearn.cluster import *
from sklearn import metrics

import argparse

if len(sys.argv) != 3:
    print("Usage: python3 " + sys.argv[
        0] + " <molecule-list-csv-file> <distances-csv-file> <distance_tool_result_csv_file>")
    sys.exit(1)
# Read the list of molecules
molecules = pd.read_csv(sys.argv[1], sep=";")

# Create dictionary Id -> Index
index_of = dict()
for i in range(len(molecules)):
    index_of[molecules.loc[i].loc['Id']] = i

if molecules.columns[2] == "CorePlus":
    # Create dictionary Id -> CorePlus
    label_of = dict()
    for i in range(len(molecules)):
        label_of[molecules.loc[i].loc['Id']] = molecules.loc[i].loc['CorePlus'].strip()
else:
    # Create dictionary Id -> Core
    label_of = dict()
    for i in range(len(molecules)):
        label_of[molecules.loc[i].loc['Id']] = molecules.loc[i].loc['Core'].strip()

# Read the list of distances
distances = pd.read_csv(sys.argv[2], sep=",")

distances.columns = ["Molecule", "ValueS", "ValueE"]
print(distances.columns)

# Create Distance Matrix

# Populate List of Features
ListFeatures = []
for k in range(len(distances)):
    i = index_of[distances.loc[k].loc['Molecule']]
    #    j = index_of[distances.loc[k].loc['Id2']]
    value1 = distances.loc[k].loc['ValueS']
    value2 = distances.loc[k].loc['ValueE']
    ListFeatures.append([value1, value2])

# Determine the number of clusters as distinct labels in molecules
n_clusters = len(set(label_of.values()))

labels_true = list(label_of.values())

# Parameter linkage can be varied to obtain clusters differently
# Options are: single, complete, average, ward (but ward works only if Euclian distance is used)

model = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='single').fit(ListFeatures)
labels_pred = model.fit_predict(ListFeatures)

f = open(sys.argv[2], 'w+')
f.write('Method,Rand_score,Homogeneity_score,completeness_score')

agg_csv = 'single,' + str(metrics.rand_score(labels_true, labels_pred)) + ',' + str(
    metrics.homogeneity_score(labels_true, labels_pred)) + ',' + str(
    metrics.completeness_score(labels_true, labels_pred))
f.write(agg_csv)

model = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='complete').fit(ListFeatures)
labels_pred = model.fit_predict(ListFeatures)

agg_csv = 'complete,' + str(metrics.rand_score(labels_true, labels_pred)) + ',' + str(
    metrics.homogeneity_score(labels_true, labels_pred)) + ',' + str(
    metrics.completeness_score(labels_true, labels_pred))
f.write(agg_csv)

model = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='average').fit(ListFeatures)
labels_pred = model.fit_predict(ListFeatures)

agg_csv = 'average,' + str(metrics.rand_score(labels_true, labels_pred)) + ',' + str(
    metrics.homogeneity_score(labels_true, labels_pred)) + ',' + str(
    metrics.completeness_score(labels_true, labels_pred))
f.write(agg_csv)
print('\x1b[1;32;40m' + f'{f} created' + '\x1b[0m')