#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EvalTax: executes the evaluation of 
@author: Michela Quadrini and Luca Tesei
"""
import math
import sys
import pandas as pd
import numpy as np
from sklearn.metrics import *

from sklearn.cluster import *
from sklearn import metrics

import argparse

if len(sys.argv) != 3:
    print("Usage: python3 " + sys.argv[0] + " <molecule-list-csv-file> <eigenvalues-csv-file>")
    sys.exit(1)
# Read the list of molecules
molecules = pd.read_csv(sys.argv[1], sep=";")

# Create dictionary Id -> Index
index_of = dict()
for i in range(len(molecules)):
    index_of[molecules.loc[i].loc['Id']] = i

# Create dictionary Id -> Organism 
organism_of = dict()
for i in range(len(molecules)):
    organism_of[molecules.loc[i].loc['Id']] = molecules.loc[i].loc['Organism'].strip()

if molecules.columns[2] == "Core1":
    # Create dictionary Id -> Core1
    taxon_of = dict()
    for i in range(len(molecules)):
        taxon_of[molecules.loc[i].loc['Id']] = molecules.loc[i].loc['Core1'].strip()

    # Create dictionary Id -> Core1
    label_of = dict()
    for i in range(len(molecules)):
        label_of[molecules.loc[i].loc['Id']] = molecules.loc[i].loc['Core1'].strip()
else:
    # Create dictionary Id -> Core2
    taxon_of = dict()
    for i in range(len(molecules)):
        taxon_of[molecules.loc[i].loc['Id']] = molecules.loc[i].loc['Core2'].strip()

    # Create dictionary Id -> Core2
    label_of = dict()
    for i in range(len(molecules)):
        label_of[molecules.loc[i].loc['Id']] = molecules.loc[i].loc['Core2'].strip()

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

print("Method: single")
print("Rand_score", metrics.rand_score(labels_true, labels_pred))
print("Homogeneity_score", metrics.homogeneity_score(labels_true, labels_pred))
print("completeness_score", metrics.completeness_score(labels_true, labels_pred))

model = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='complete').fit(ListFeatures)
labels_pred = model.fit_predict(ListFeatures)
# print("Labels Pred", list(labels_pred))

print("Method: complete")
print("Rand_score", metrics.rand_score(labels_true, labels_pred))
print("Homogeneity_score", metrics.homogeneity_score(labels_true, labels_pred))
print("completeness_score", metrics.completeness_score(labels_true, labels_pred))

model = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='average').fit(ListFeatures)
labels_pred = model.fit_predict(ListFeatures)
# print("Labels Pred", list(labels_pred))

print("Method: average")
print("Rand_score", metrics.rand_score(labels_true, labels_pred))
print("Homogeneity_score", metrics.homogeneity_score(labels_true, labels_pred))
print("completeness_score", metrics.completeness_score(labels_true, labels_pred))

print("############################")
print("AffinityPropagation")
model = AffinityPropagation(affinity='euclidean').fit(ListFeatures)
labels_pred = model.fit_predict(ListFeatures)
print("Rand_score", metrics.rand_score(labels_true, labels_pred))
print("Homogeneity_score", metrics.homogeneity_score(labels_true, labels_pred))
print("completeness_score", metrics.completeness_score(labels_true, labels_pred), end="\n\n")

print("############################")
print("Birch")
model = Birch(n_clusters=n_clusters).fit(ListFeatures)
labels_pred = model.fit_predict(ListFeatures)
print("Rand_score", metrics.rand_score(labels_true, labels_pred))
print("Homogeneity_score", metrics.homogeneity_score(labels_true, labels_pred))
print("completeness_score", metrics.completeness_score(labels_true, labels_pred), end="\n\n")

print("############################")
print("DBSCAN")
model = DBSCAN(metric='euclidean').fit(ListFeatures)
labels_pred = model.fit_predict(ListFeatures)
print("Rand_score", metrics.rand_score(labels_true, labels_pred))
print("Homogeneity_score", metrics.homogeneity_score(labels_true, labels_pred))
print("completeness_score", metrics.completeness_score(labels_true, labels_pred), end="\n\n")

print("############################")
print("KMeans")
model = KMeans(n_clusters=n_clusters, algorithm='full').fit(ListFeatures)
labels_pred = model.fit_predict(ListFeatures)
print("Rand_score", metrics.rand_score(labels_true, labels_pred))
print("Homogeneity_score", metrics.homogeneity_score(labels_true, labels_pred))
print("completeness_score", metrics.completeness_score(labels_true, labels_pred), end="\n\n")

print("############################")
print("BisectingKMeans")
model = BisectingKMeans(n_clusters=n_clusters).fit(ListFeatures)
labels_pred = model.fit_predict(ListFeatures)
print("Rand_score", metrics.rand_score(labels_true, labels_pred))
print("Homogeneity_score", metrics.homogeneity_score(labels_true, labels_pred))
print("completeness_score", metrics.completeness_score(labels_true, labels_pred), end="\n\n")
