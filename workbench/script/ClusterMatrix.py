#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EvalTax: executes the evaluation of 
@author: Michela Quadrini and Luca Tesei
"""
import sys
import pandas as pd
import numpy as np
from sklearn.cluster import *
from sklearn import metrics

if len(sys.argv) != 3:
    print("Usage: python3 "+sys.argv[0]+" <molecule-list-csv-file> <distances-csv-file>")
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

# Create dictionary Id -> Taxon
taxon_of = dict()
for i in range(len(molecules)):
    taxon_of[molecules.loc[i].loc['Id']] = molecules.loc[i].loc['Core1'].strip()

# Create dictionary Id -> Label
label_of = dict()
for i in range(len(molecules)):
    label_of[molecules.loc[i].loc['Id']] = molecules.loc[i].loc['Core1'].strip()

# Read the list of distances
print("Reading", sys.argv[2], "...")
distances = pd.read_csv(sys.argv[2], sep=",")

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

# Determine the number of clusters as distinct labels in molecules
n_clusters = len(set(label_of.values()))

labels_true = list(label_of.values())

model = AgglomerativeClustering(n_clusters=n_clusters, affinity='precomputed', linkage='single').fit(distance_matrix)
labels_pred = model.fit_predict(distance_matrix)

print("Method: single")
print("Rand_score", metrics.rand_score(labels_true, labels_pred))
print("Homogeneity_score", metrics.homogeneity_score(labels_true, labels_pred))
print("completeness_score", metrics.completeness_score(labels_true, labels_pred))

print("Method: complete")
model = AgglomerativeClustering(n_clusters=n_clusters, affinity='precomputed', linkage='complete').fit(distance_matrix)
labels_pred = model.fit_predict(distance_matrix)

print("Rand_score", metrics.rand_score(labels_true, labels_pred))
print("Homogeneity_score", metrics.homogeneity_score(labels_true, labels_pred))
print("completeness_score", metrics.completeness_score(labels_true, labels_pred))

print("Method: average")
model = AgglomerativeClustering(n_clusters=n_clusters, affinity='precomputed', linkage='average').fit(distance_matrix)
labels_pred = model.fit_predict(distance_matrix)

print("Rand_score", metrics.rand_score(labels_true, labels_pred))
print("Homogeneity_score", metrics.homogeneity_score(labels_true, labels_pred))
print("completeness_score", metrics.completeness_score(labels_true, labels_pred), end="\n\n")

'''print("############################")
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
model = KMeans(n_clusters=n_clusters,algorithm='full').fit(distance_matrix)
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
'''