#!/usr/loca/bin/python
# Swati Jain (S.J.) - python file containig generic classes and functions used by different scripts
# changed to work with tree graphs

import sys
from copy import deepcopy
import numpy.linalg as LA
from decimal import *
import os
from numpy import *
from itertools import permutations

#class to contain information about tree graphs
class TreeGraph: # 06/08/2019
    
    def __init__(self,a,b,c,d):
        self.vertices = a
        self.adjMatrix = b
        self.graphID = c
        self.eigenvalues = d
    
    # function to see if the graphs are the same or not
    # first check eigen values, if it is the same, then check graph isomorphism - 06/11/2018
    # adding the vertexOrder, i.e, if asked the isomorphism function will update it - 07/11/2018
    def match(self,d,a,vertexOrder=None):
        if self.eigenvalues == d:
            iso = checkIsomorphism(self.adjMatrix,a,vertexOrder)
            if iso == True: # if they are isomorphic
                return self.graphID
            else:
                return "NA"
        else:
            return "NA"

    # to print eigen values of a dual graph - 05/18/2017
    def printEigen(self,filename):
        file = open(filename,'a')
        file.write(">%s"%self.graphID)
        file.write("\n")
        file.close()
        printEigenValues(self.eigenvalues,filename)

    # set functions - 05/18/2018
    def setVertices(self,v):
        self.vertices = v

    def setadjMatrix(self,a):
        self.adjMatrix = a

    def setGraphID(self,g):
        self.graphID = g

    def setEigen(self,e):
        self.eigenvalues = e


# function to print matrices - 05/17/2018
def printMat(Matrix,filename=None):
    
    if filename == None:
        file = sys.stdout
    else:
        file = open(filename,'a')

    file.write("\n")
    for i in range(0,len(Matrix)):
        for j in range(0,len(Matrix)):
            file.write("\t%d"%Matrix[i][j]),
        file.write("\n")
    file.write("\n")

    if file is not sys.stdout:
        file.close()


#function to calculate eigen values of a given adjacency matrix - 05/17/2018
def calcEigenValues(adjMatrix):

    laplacian = []
    numVertices = len(adjMatrix)
    
    for i in range(0,numVertices):
        degree=0
        tempArray = []
        for j in range(0,numVertices):
            if i != j: # ignore self loops
                tempArray.append(-adjMatrix[i][j])
                degree += adjMatrix[i][j]
            else:
                tempArray.append(0)
        tempArray[i] += degree
        laplacian.append(tempArray)

    eigen = sort(LA.eigvals(laplacian))
    decimalArray = []
    decimalPlace = Decimal("0.00000001")
    for i in eigen:
        if isinstance(i, complex): # 04/20/2018 - S.J.
            decimalArray.append(Decimal(str(i.real)).quantize(decimalPlace))
        else:
            decimalArray.append(Decimal(str(i)).quantize(decimalPlace))
    return decimalArray

#function to print eigen values in 0.8 precision that are in the form of a decimalArray - 05/17/2018
# copied and modified from calcEigenvals.py
# 07/09/2018 - changes so that it can print to stdout as well (with labels)
def printEigenValues(eigen,filename=None):
    
    if filename == None:
        file = sys.stdout
    else:
        file = open(filename,'a')

    decimalPlace = Decimal("0.00000001")
    for i in range(0,len(eigen)): # print eigen values upto .8 precision without negative signs
        if str(eigen[i])[0] == "-":
            eigen[i] = Decimal(str(eigen[i])[1:]).quantize(decimalPlace)
        if filename == None:
            file.write("Eigenvalue: %d: "%(i+1))
        file.write('{0:.8f}'.format(eigen[i]))
        file.write("\n")

    if file is not sys.stdout:
        file.close()

# function to load all tree graph IDs and eigen values from a given file and create tree graph instances
# creates the tree graph instances (with vertices, graphID, and eigenvalues set) and adds them to the Graphs list.
def loadEigenvalues(Graphs,num_vertices,file):
    
    decimalPlace = Decimal("0.00000001")
    emptyArray = []
    tArray = []
    graph_num = 0
    f = open(file,'r')
    for line in f:
        if(len(line) > 0 and line[0] == '>'): # reading in the graph id
            key = line[1:-1]
        elif(len(line) > 0 and line[0] != '>'): # reaing in the eigen values
            tArray.append(Decimal(str(line[:-1])).quantize(decimalPlace))
        if len(tArray) == num_vertices: # when enough eigen values are read
            Graphs.append(TreeGraph(num_vertices,emptyArray,key,tArray)) # creating a dual graph instance and adding it to the graph list - 06/08/2019
            graph_num+=1
            tArray = []
    f.close()
    #print "Read eigenvalues for %d dual graphs from file %s"%(graph_num,file)


# function to load all adj matrices from given files into the Graphs list - 05/18/2018
# needs the Graphs list to be already initialized with tree graph instances
# Assuming that the adjacency matrices are in the same order as eigen values file that was used to initialize the tree graphs in Graphs
def loadAdjMatrices(Graphs,num_vertices,file):

    tempAdjMatrix = []
    tempArray = []
    graph_num=0
    size=0
    f = open(file,'r')
    for line in f: # read the adjacency matrices
        if line != '\n':
            size +=  1
            tempArray = []
            for x in line.split():
                tempArray.append(float(x))
            tempAdjMatrix.append(tempArray)
            if size == num_vertices: # when enough rows are read, then add the adjacency matrix to the Graphs list
                Graphs[graph_num].setadjMatrix(tempAdjMatrix)
                graph_num += 1
                #re-initialize the variables
                tempAdjMatrix = []
                size = 0
    f.close()
    #print "Read adjacency matrices for %d dual graphs from file %s"%(graph_num,file)

# function to calculate permutations - in case we ever need it
def calcPermutations(index,prevPermut):

        global PermList

        if index == numVertices:
                PermList.append(prevPermut)
                return

        allowed_vertices = []
        for j in range(0,numVertices):
                found = False
                for k in range(0,index):
                        if j == prevPermut[k]:
                                found = True
                if not found:
                        allowed_vertices.append(j)

        for i in range(0,len(allowed_vertices)):

                curPermut=deepcopy(prevPermut)
                curPermut[index]=allowed_vertices[i]
                calcPermutations(index+1,curPermut)

# 06/11/2019 to combine permutations
def combinePermuts(PermList,i_perm,prevPermut,PermList2):

    if i_perm == len(PermList):
        PermList2.append(prevPermut)
        return

    for perm_list in PermList[i_perm]: # for each permutation generated for this particular degree
        curPermut=deepcopy(prevPermut)
        for perm in perm_list:
            curPermut.append(perm)
        combinePermuts(PermList,i_perm+1,curPermut,PermList2)

# function to check isomorphism for two adjacency matrices - 06/11/2018
# Removes self-loops before checking for isomorphism
# 07/11/2018 - will return the vertex order if that argument is passed
# 06/11/2019 - changes to have a better check for isomorphism
def checkIsomorphism(adj_source,adj_toComp,vertexOrder = None):

    deg_source=sum(adj_source,axis=1)
    deg_toComp=sum(adj_toComp,axis=1)
    
    numVertices = len(adj_source)
    vert_source = range(numVertices)
    vert_toComp = range(numVertices)
    
    deg_source, vert_source = (list(t) for t in zip(*sorted(zip(deg_source, vert_source))))
    deg_toComp, vert_toComp = (list(t) for t in zip(*sorted(zip(deg_toComp, vert_toComp))))
    
    if deg_source != deg_toComp: # if degree sequences are not same, the graphs are not isomorphic
        return False
    else:
        
        #arrange the toComp matrix according to sorted degree sequence - use this to compare
        toComp = deepcopy(adj_toComp)
        for j in range(0,numVertices):
            jI = vert_toComp[j]
            for k in range(0,numVertices):
                kI= vert_toComp[k]
                toComp[j][k] = adj_toComp[jI][kI]

        #generate permutations of the source, but only between the sorted list of source vertices that have the same degree
        PermList = []
        uni_deg=sorted(set(deg_source)) # unique degrees
        uni_deg_numV=[] # number of vertices with that degree
        for i in uni_deg:
            num = []
            for j in range(0,numVertices):
                if deg_source[j] == i: # this vertex has the degree we are looking at
                    num.append(vert_source[j])
            uni_deg_numV.append(len(num))
            PermList.append(list(permutations(num)))

        #take the individual permutations and combine them in a recursive function to create the PermList2
        PermList2=[]
        curPermut=[]
        combinePermuts(PermList,0,curPermut,PermList2)

        #for for each of those permutations, arrange the source matrix and compare it to the toComp matrix
        permutMatrix = deepcopy(adj_source)
        for i in PermList2: # for every permutation of the vertices of the source matrix
            listI = list(i)
            for j in range(0,numVertices):
                jI = listI[j]
                for k in range(0,numVertices):
                    kI= listI[k]
                    permutMatrix[j][k] = adj_source[jI][kI] # create the permutation matrix
                if permutMatrix==toComp: # compare the permutation with the toComp matrix, if same then they are isomorphic
                    if vertexOrder != None: # if vertex order is passed
                        for i in range(0,len(listI)):
                            listI[i]+=1
                            vertexOrder[i]=listI[i]
                        #print str(vertexOrder)
                    #break
                    return True

        return False

# function to assign a graph ID for the given eigenvalue spectrum and adjacency matrix
# this will do a binary search which will be log(n) time as the read tree graphs are alresdy sorted in the new files
# 08/24/2018
def searchtoAssignID(Graphs,start,end,eigen,matrix):
    
    # not found termination condition
    if start > end:
        return "NA"

    index = (start+end)/2 # the mid point graph to check
    id = Graphs[index].match(eigen,matrix)
    
    # found termination condition - assigned graph ID
    if id != "NA":
        return id
    
    if eigen == Graphs[index].eigenvalues: # same eigen values but non-isomorphic graphs
        
        # search in the left side of equal
        i = index-1
        while eigen == Graphs[i].eigenvalues:
            id = Graphs[i].match(eigen,matrix)
            if id != "NA":
                return id
            i=i-1

        # search in the right side of equals
        i = index+1
        while eigen == Graphs[i].eigenvalues:
            id = Graphs[i].match(eigen,matrix)
            if id != "NA":
                return id
            i = i+1

        # same eigenvalues but graph not found
        return "NA"

    elif eigen < Graphs[index].eigenvalues: # search on the left part of the array
        return searchtoAssignID(Graphs,start,index-1,eigen,matrix)
    elif eigen > Graphs[index].eigenvalues: # search in the right part of the array
        return searchtoAssignID(Graphs,index+1,end,eigen,matrix)

