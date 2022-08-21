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
    print("Usage: python3 prove.py <molecule-list-csv-file> <distances-csv-file>")
    sys.exit(1)
# Read the list of molecules
# print("Reading", sys.argv[1], "...")
molecules = pd.read_csv(sys.argv[1], sep=";")
# print(molecules)
# molecules.columns = ["Id", "Organism", "Taxon", "Label"]
# print(molecules.columns)

# print(len(molecules))
# print(molecules['Id'][0])

# Create dictionary Id -> Index
index_of = dict()
for i in range(len(molecules)):
    index_of[molecules.loc[i].loc['Id']] = i
# print(index_of["CRW_16S_A_E_9_noHeader-2D-dotbracket.txt"])

# Create dictionary Id -> Organism 
organism_of = dict()
for i in range(len(molecules)):
    organism_of[molecules.loc[i].loc['Id']] = molecules.loc[i].loc['Organism'].strip()
# print(organism_of)
# print(organism_of["CRW_16S_A_E_9_noHeader-2D-dotbracket.txt"])

# Create dictionary Id -> Taxon 
taxon_of = dict()
for i in range(len(molecules)):
    taxon_of[molecules.loc[i].loc['Id']] = molecules.loc[i].loc['Core1'].strip()
# print(taxon_of["CRW_16S_A_E_9_noHeader-2D-dotbracket.txt"])

# Create dictionary Id -> Label 
label_of = dict()
for i in range(len(molecules)):
    label_of[molecules.loc[i].loc['Id']] = molecules.loc[i].loc['Core1'].strip()
# print(label_of)
# print(label_of["CRW_16S_A_E_9_noHeader-2D-dotbracket.txt"])

# Read the list of distances
print("Reading", sys.argv[2], "...")
distances = pd.read_csv(sys.argv[2], sep=",")
# print(distances)
# distances.columns = ["Id1", "Id2", "Distance"]
# print(distances.columns)

# Create Distance Matrix
s = (len(molecules), len(molecules))
distance_matrix = np.zeros(s)

# Populate Distance Matrix
for k in range(len(distances)):
    i = index_of[distances.loc[k].loc['Molecule 1']]
    j = index_of[distances.loc[k].loc['Molecule 2']]
    value = distances.loc[k].loc['Distance']
    distance_matrix[i][j] = value
    distance_matrix[j][i] = value

# print(distance_matrix)

# Determine the number of clusters as distinct labels in molecules

# print(label_of.values())
# print(type(label_of.values()))
n_clusters = len(set(label_of.values()))
# print(n_clusters)

labels_true = list(label_of.values())
# print("Labels True",labels_true)

# Parameter linkage can be varied to obtain clusters differently
# Options are: single, complete, average, ward (but ward works only if Euclian distance is used)

model = AgglomerativeClustering(n_clusters=n_clusters, affinity='precomputed', linkage='single').fit(distance_matrix)
labels_pred = model.fit_predict(distance_matrix)
# print("Labels Pred", list(labels_pred))

print("Method: single")
print("Rand_score", metrics.rand_score(labels_true, labels_pred))
print("Homogeneity_score", metrics.homogeneity_score(labels_true, labels_pred))
print("completeness_score", metrics.completeness_score(labels_true, labels_pred))

print("Method: complete")
model = AgglomerativeClustering(n_clusters=n_clusters, affinity='precomputed', linkage='complete').fit(distance_matrix)
labels_pred = model.fit_predict(distance_matrix)
# print("Labels Pred", list(labels_pred))

print("Rand_score", metrics.rand_score(labels_true, labels_pred))
print("Homogeneity_score", metrics.homogeneity_score(labels_true, labels_pred))
print("completeness_score", metrics.completeness_score(labels_true, labels_pred))

print("Method: average")
model = AgglomerativeClustering(n_clusters=n_clusters, affinity='precomputed', linkage='average').fit(distance_matrix)
labels_pred = model.fit_predict(distance_matrix)
# print("Labels Pred", list(labels_pred))

print("Rand_score", metrics.rand_score(labels_true, labels_pred))
print("Homogeneity_score", metrics.homogeneity_score(labels_true, labels_pred))
print("completeness_score", metrics.completeness_score(labels_true, labels_pred), end="\n\n")
# print("Labels Pred", list(labels_pred))


print("############################")
print("AffinityPropagation")
model = AffinityPropagation(affinity='precomputed').fit(distance_matrix)
labels_pred = model.fit_predict(distance_matrix)
print("Rand_score", metrics.rand_score(labels_true, labels_pred))
print("Homogeneity_score", metrics.homogeneity_score(labels_true, labels_pred))
print("completeness_score", metrics.completeness_score(labels_true, labels_pred), end="\n\n")

print("############################")
print("Birch")
model = Birch(n_clusters=n_clusters).fit(distance_matrix)
labels_pred = model.fit_predict(distance_matrix)
print("Rand_score", metrics.rand_score(labels_true, labels_pred))
print("Homogeneity_score", metrics.homogeneity_score(labels_true, labels_pred))
print("completeness_score", metrics.completeness_score(labels_true, labels_pred), end="\n\n")

print("############################")
print("DBSCAN")
model = DBSCAN(metric='precomputed').fit(distance_matrix)
labels_pred = model.fit_predict(distance_matrix)
print("Rand_score", metrics.rand_score(labels_true, labels_pred))
print("Homogeneity_score", metrics.homogeneity_score(labels_true, labels_pred))
print("completeness_score", metrics.completeness_score(labels_true, labels_pred), end="\n\n")

print("############################")
print("KMeans")
model = KMeans(n_clusters=n_clusters).fit(distance_matrix)
labels_pred = model.fit_predict(distance_matrix)
print("Rand_score", metrics.rand_score(labels_true, labels_pred))
print("Homogeneity_score", metrics.homogeneity_score(labels_true, labels_pred))
print("completeness_score", metrics.completeness_score(labels_true, labels_pred), end="\n\n")

print("############################")
print("BisectingKMeans")
model = BisectingKMeans(n_clusters=n_clusters).fit(distance_matrix)
labels_pred = model.fit_predict(distance_matrix)
print("Rand_score", metrics.rand_score(labels_true, labels_pred))
print("Homogeneity_score", metrics.homogeneity_score(labels_true, labels_pred))
print("completeness_score", metrics.completeness_score(labels_true, labels_pred), end="\n\n")

print("############################")
print("MiniBatchKMeans")
model = MiniBatchKMeans(n_clusters=n_clusters).fit(distance_matrix)
labels_pred = model.fit_predict(distance_matrix)
print("Rand_score", metrics.rand_score(labels_true, labels_pred))
print("Homogeneity_score", metrics.homogeneity_score(labels_true, labels_pred))
print("completeness_score", metrics.completeness_score(labels_true, labels_pred), end="\n\n")

print("############################")
print("MeanShift")
model = MeanShift().fit(distance_matrix)
labels_pred = model.fit_predict(distance_matrix)
print("Rand_score", metrics.rand_score(labels_true, labels_pred))
print("Homogeneity_score", metrics.homogeneity_score(labels_true, labels_pred))
print("completeness_score", metrics.completeness_score(labels_true, labels_pred), end="\n\n")

print("############################")
print("SpectralClustering")
model = SpectralClustering(n_clusters=n_clusters, affinity='precomputed').fit(distance_matrix)
labels_pred = model.fit_predict(distance_matrix)
print("Rand_score", metrics.rand_score(labels_true, labels_pred))
print("Homogeneity_score", metrics.homogeneity_score(labels_true, labels_pred))
print("completeness_score", metrics.completeness_score(labels_true, labels_pred), end="\n\n")
