#!/usr/bin/python

import sys
import numpy
import numpy.linalg as LA
from decimal import *
from copy import deepcopy
from itertools import permutations
from ClassesFunctions import * # S.J. 06/14/2019 - adding to use its functions
graphID = []
TreeGraphs = [] # S.J. 06/14/2019

class Base:
    index = None  #nucleotide Index
    indexBP = None  #base paired to 
    nt = None #NT value
    active = None
    jActivity = None
    flag = "0"
    nodeNumber = 0
    helixNumber = 0 #what helix is this a part of?
    def initialize(self,indexv,ntv,indexBPv): 
        self.index = int(indexv)
        self.indexBP = int(indexBPv)
        self.nt = str(ntv)
        self.active = True
        self.jActivity = True

class Loop:
    start = None
    end = None
    def __init__(self):
        pass

class Helix:
    start = None
    end = None
    flag = "" #ARE YOU A LOOP?
    Loop = None
    connected = None
    edges = 0
    def __init__(self):
        self.connected = []



#here are the types of things They all go to RNA.Nodes, common things so far are helices and toString
class StartingNode:
    start5 = None
    start3 = None
    end5 = None
    end3 = None
    lowestIndex = None
    string = ""
    helices = None
    connections = None
    def toString(self):
        return self.string
    def __init__(self):
        self.helices = []
    
class InternalLoop:
    start5 = None
    start3 = None
    end5 = None
    end3 = None
    lowestIndex = None
    string = "I"
    helices = None
    connections = []
    def toString(self):
        return self.string
    def __init__(self):
        self.helices = []

class Hairpin:
    start = None
    end = None
    lowestIndex = None
    string = "HP"
    helices = None
    connections = []
    def toString(self):
        return self.string
    def __init__(self):
        self.helices = []


class Junction:
    start = None
    end = None
    lowestIndex = None
    lowestUnpaired = None
    string = "J"
    helices = None
    connections = []
    def toString(self):
        return self.string
    def __init__(self):
        self.helices = []
class RNAInfo:
    Bases = None
    Loops = None
    Nodes = None
    Helices = None
    numVert = None
    descr = None #what is it? Helix? loop? int loop? junction?, 5' and 3'?
    adjMatrix = []
    degMatrix = []
    laplacian = None
    def __init__(self):
        self.Bases = [0]
        self.Loops = [0]
        self.Helices = [0]
        self.Nodes = [0]
        self.numVert = 0
        self.adjMatrix = []
        self.degMatrix = []
        self.laplacian = None
    def makeMatrices(self):
        for i in range(1,len(self.Nodes)):
            tArray = []
            for j in range(1,len(self.Nodes)):
                tArray.append(0)
            self.adjMatrix.append(tArray)
        for i in range(1,len(self.Nodes)):
            tArray = []
            for j in range(1,len(self.Nodes)):
                tArray.append(0)
            self.degMatrix.append(tArray)

    def addBase(self,baseA):
        self.Bases.append(baseA)
    def printSeq(self, whichBase=1000):
        if whichBase == 1000:
            for i in range(1,len(self.Bases)):
                print("%d\t%d\t%s\t%d\t%s\t%d" %(self.Bases[i].index,self.Bases[i].indexBP,self.Bases[i].nt,self.Bases[i].helixNumber,self.Bases[i].flag,self.Bases[i].nodeNumber))
    def printOut(self,whichBase=1000):
        if whichBase == 1000:
            for i in range(1,len(self.Bases)):
                print ("%d\t%d\t%s\t%d\t%s" %(self.Bases[i].index,self.Bases[i].indexBP,self.Bases[i].nt,self.Bases[i].helixNumber,self.Bases[i].flag))
        for i in range(1,len(self.Helices)):
            print ("for helix %d: start=%d, end=%d, flag=%s" %(i,self.Helices[i].start,self.Helices[i].end,self.Helices[i].flag))
        for i in range(1,len(self.Loops)):
            print ("for loop %d: start=%d, end=%d" %(i,self.Loops[i].start,self.Loops[i].end))
    def printConnections(self):
        for i in range(1,len(self.Helices)):
            print ("helix %d is connected to: %s and has %d edges." %(i,str(self.Helices[i].connected),self.Helices[i].edges))
    def printAdj(self):
        print ("Adjacency Matrix:")
        for i in self.adjMatrix:
            print (i)
    def printDeg(self):
        print ("Degree Matrix:")
        for i in self.degMatrix:
            print (i)
    def printLpl(self):
        print ("Laplacian Matrix:")
        for i in self.laplacian:
            print (i)
    def printHelices(self):
        for i in range(1,len(self.Helices)):
            print ("Vertex %d: start_pos=%d, end_pos=%d, flag=%s" %(i,self.Helices[i].start,self.Helices[i].end,self.Helices[i].flag))
    def printOrder(self,nOrder):
        order = []
        prevNode = 0
        for i in range(1,len(self.Bases)):
            currNode=self.Bases[i].nodeNumber
            if currNode != 0 and currNode != prevNode:
                prevNode = currNode
                if currNode != 0:
                    order.append(nOrder[currNode-1])
        print ("5'-" + str(order) + "-3'")
    def printNodes(self):
        for i in range(1,len(self.Nodes)): #common is toString and connections
            print ("Number: " + str(i) + " Type: " + self.Nodes[i].toString() + " Helices: " + str(self.Nodes[i].helices) + " Lowest Index: " + str(self.Nodes[i].lowestIndex))
    def clear(self):
        Bases = None
        Loops = None
        Helices = None
        numVert = None
        adjMatrix = []
        degMatrix = []
        laplacian = None
            
    def sortNodes(self):
        swapped = True
        while swapped:
            swapped = False
            for i in range(1,len(self.Nodes)-1):
                if self.Nodes[i].lowestIndex > self.Nodes[i+1].lowestIndex:
                    self.Nodes[i], self.Nodes[i+1] = self.Nodes[i+1], self.Nodes[i]
                    swapped = True
    

        

### makeMatrices ####
#####################
def makeMatrices(RNA):
    for i in range(1,len(RNA.Nodes)):
        tArray = []
        for j in range(1,len(RNA.Nodes)):
            tArray.append(0)
        RNA.adjMatrix.append(tArray)
    for i in range(1,len(RNA.Nodes)):
        tArray = []
        for j in range(1,len(RNA.Nodes)):
            tArray.append(0)
        RNA.degMatrix.append(tArray)
        
        
#Translate information from the CT file into an RNA class
def getCTInfo(arg):
    f = open(arg)
    RNA = RNAInfo()
    line = f.readline()
    while(line.split()[0] != '1'):
        line = f.readline()
    while(len(line.split()) > 1):
        oneBase = Base()
        oneBase.initialize(line.split()[0],line.split()[1],line.split()[4])
        RNA.addBase(oneBase)
        line = f.readline()
    f.close()    
    return RNA
##Translate information from BPSEQ file into an RNA class
def getBPSEQInfo(arg):
    f = open(arg)
    RNA = RNAInfo()
    line = f.readline()
    while(line.split()[0] != '1'):
        line = f.readline()
    while(len(line.split()) > 1):
        oneBase = Base()
        oneBase.initialize(line.split()[0],line.split()[1],line.split()[2])
        RNA.addBase(oneBase)
        line = f.readline()
    f.close()    
    return RNA

##Translate information from a adjacency matrix into an RNA class - S.J. 07/05/2018
def getAdjMatInfo(arg):
        f = open(arg)
        RNA = RNAInfo()
        lines = f.readlines()
        for i in range(0,len(lines)):
                line = lines[i]
                tempArray = []
                degree = 0
                for x in line.split():
                        degree += float(x)
                        tempArray.append(float(x))
                RNA.adjMatrix.append(tempArray)
                tempArray = []
                for j in range (1,i+1):
                        tempArray.append(0.0000)
                tempArray.append(degree)
                for j in range (i+1,len(lines)):
                        tempArray.append(0.0000)
                RNA.degMatrix.append(tempArray)
                if i == 0:
                        node = StartingNode()
                        RNA.Nodes.append(node)
                elif degree == 1:
                        node = Hairpin()
                        RNA.Nodes.append(node)
                elif degree == 2:
                        node = InternalLoop()
                        RNA.Nodes.append(node)
                elif degree >= 3:
                        node = Junction()
                        RNA.Nodes.append(node)
        f.close()
        return RNA

## Translate information from a dot bracket notation into an RNA class - S.J. 07/25/2018
# first line of a dot bracket notation should contain the sequence, and the second line should contain the dot bracket notation
def getDotBracketInfo(arg):
    f = open(arg)
    lines=f.readlines()
    f.close()
    
    found_seq = False
    found_dotb = False
    
    for line in lines:
        line = line.strip().split()[0]
        if (not found_seq) and (line[0] == "A" or line[0] == "G" or line[0] == "C" or line[0] == "U"): # this is the sequence line
            sequence = [c for c in line] # stores the base identity of the residue
            found_seq = True
        elif (not found_dotb) and (line[0] == "." or line[0] == "(" or line[0] == ")"): # this is the dot bracket line
            dotb = [c for c in line]
            found_dotb = True
    
    stack_bp=[]
    base_pair=[] # to store the residue number of base pair
    RNA = RNAInfo()
    
    for i in range(0,len(dotb)):
        base_pair.append(0) # initializing base pairs with all 0's
    
    for i in range(0,len(dotb)):
        if dotb[i] == "(": # opening bracket, add the res number to stack
            stack_bp.append(i)
        elif dotb[i] == ")": # closing bracket, then pop the res number from the stack, and assign base_pairs to both residues
            i_bp = stack_bp.pop()
            base_pair[i]=i_bp+1 #as numbers start from 1
            base_pair[i_bp]=i+1

    #add bases to RNA
    for i in range(0,len(dotb)):
        oneBase = Base()
        if found_seq:
            oneBase.initialize(i+1,sequence[i],base_pair[i])
        else:
            oneBase.initialize(i+1,"N",base_pair[i])
        RNA.addBase(oneBase)

    return RNA


#Determine whether or not there are pseudoknots in the structure
def pseudoKnots(RNA):
    for i in range(1,len(RNA.Bases)-1):
        if RNA.Bases[i].indexBP > 0:
            for j in range(i+1,len(RNA.Bases)):
                if RNA.Bases[j].indexBP > 0:
                    if (j < RNA.Bases[i].indexBP and RNA.Bases[i].indexBP < RNA.Bases[j].indexBP):
                        return True
    return False    

### countHelices ####
#####################
#This method counts the number of helices and loops
def countHelices(RNA):
    nHelix = 0
    i = 1
    #Skip any unpaired bases and find the first Helix
    while (RNA.Bases[i].indexBP==0):
        i += 1
        
    # Rest of Helices
    for j in range(i,len(RNA.Bases)):
        if(RNA.Bases[j].indexBP>0 and RNA.Bases[j].active == True):
            if (RNA.Bases[j+1].indexBP > 0 and RNA.Bases[j].indexBP - 1 == RNA.Bases[j+1].indexBP):
                nHelix += 1
                RNA.Helices.append(Helix())
                RNA.Helices[nHelix].start = j
                RNA.Helices[nHelix].end = j+1
                
                RNA.Bases[j].helixNumber = nHelix
                RNA.Bases[j+1].helixNumber = nHelix
                RNA.Bases[RNA.Bases[j].indexBP].helixNumber = nHelix
                RNA.Bases[RNA.Bases[j+1].indexBP].helixNumber = nHelix
                
                RNA.Bases[j].active = False
                RNA.Bases[j+1].active = False
                RNA.Bases[RNA.Bases[j].indexBP].active = False
                RNA.Bases[RNA.Bases[j+1].indexBP].active = False
              
                j+=2
                
                while(RNA.Bases[j].indexBP != 0 and RNA.Bases[j-1].indexBP -1 == RNA.Bases[j].indexBP):
                    RNA.Bases[j].helixNumber = nHelix
                    RNA.Bases[RNA.Bases[j].indexBP].helixNumber = nHelix #The other side also belongs to nHelix
                    RNA.Bases[j].active = False
                    RNA.Bases[RNA.Bases[j].indexBP].active = False
                    RNA.Helices[nHelix].end = j;
                    j+=1
            else:
                RNA.Bases[j].index = 0
                RNA.Bases[j].helixNumber = 0
                RNA.Bases[j].indexBP=0
                #RNA.Bases[RNA.Bases[j].indexBP].active = False
                RNA.Bases[j].active=False

    for i in range(1,len(RNA.Helices)):
        helixEnd = RNA.Helices[i].end
        if clearPathNew(RNA,helixEnd,RNA.Bases[helixEnd].indexBP):
            loop = Loop()
            loop.start = RNA.Helices[i].start
            loop.end = RNA.Bases[RNA.Helices[i].start].indexBP
            RNA.Loops.append(loop)
            RNA.Helices[i].flag = 'L'
            RNA.Helices[i].Loop = loop

### changeHelices ####
#####################
#Combines helices if they are only separated by one unpaired NT
def changeHelices(RNA):    
    changes = []
    for i in range(1,len(RNA.Helices)-1):  
        #never do this to loops
        if RNA.Helices[i].flag == 'L' and RNA.Helices[i+1].flag == 'L':
            pass
        else:
            helix2fiveStart = RNA.Helices[i+1].start
            helix2fiveEnd = RNA.Helices[i+1].end
            helix2threeEnd = RNA.Bases[RNA.Helices[i+1].start].indexBP
            helix2threeStart = RNA.Bases[RNA.Helices[i+1].end].indexBP
            helix1fiveEnd = RNA.Helices[i].end
            helix1fiveStart = RNA.Helices[i].start
            helix1threeStart = RNA.Bases[RNA.Helices[i].end].indexBP
            helix1threeEnd = RNA.Bases[RNA.Helices[i].start].indexBP
            Total5P = abs(helix2fiveStart - helix1fiveEnd)-1
            Total3P = abs(helix1threeStart - helix2threeEnd)-1
            if ((abs(Total5P + Total3P) < 2) or (abs(Total5P) == 1 and abs(Total3P) == 1)):
                changes.append(i)
    for i in changes: #change bases
        j = 1
        ##Base Change
        while(RNA.Bases[j].helixNumber <=i):
            j += 1
        for k in range(j,len(RNA.Bases)):
            if RNA.Bases[k].helixNumber != 0 and RNA.Bases[k].helixNumber>i:
                RNA.Bases[k].helixNumber -= 1
        
        RNA.Helices[i].end = RNA.Helices[i+1].end
        if RNA.Helices[i+1].flag == 'L':
            RNA.Helices[i].flag = 'L'
            RNA.Helices[i].Loop = RNA.Helices[i+1].Loop 
            RNA.Helices[i].Loop.start = RNA.Helices[i].start 
            RNA.Helices[i].Loop.end = RNA.Helices[i].end 
        del RNA.Helices[i+1]
        for m in range(0,len(changes)):
            if changes[m] > i:
                changes[m] -= 1

    singleHelices = []
    for i in range(1,len(RNA.Helices)):
        if RNA.Helices[i].start == RNA.Helices[i].end:
            singleHelices.append(i)
            fivePrime = RNA.Helices[i].start
            threePrime  = RNA.Bases[fivePrime].indexBP
            #print "Helix %d is a single base-pair helix with 5' = %d and 3' = %d!" %(i,fivePrime,threePrime)
    for i in singleHelices:
        fivePrime = RNA.Helices[i].start
        threePrime  = RNA.Bases[fivePrime].indexBP
        RNA.Bases[fivePrime].indexBP = 0
        RNA.Bases[fivePrime].helixNumber = 0
        RNA.Bases[threePrime].indexBP = 0
        RNA.Bases[threePrime].helixNumber = 0
        
        j = 1
        while(j<len(RNA.Bases) and RNA.Bases[j].helixNumber <=i):
            j+=1
            for k in range(j,len(RNA.Bases)):
                if RNA.Bases[k].helixNumber != 0 and RNA.Bases[k].helixNumber>i:
                    RNA.Bases[k].helixNumber -= 1
        del RNA.Helices[i]
        for m in range(0,len(singleHelices)):
            if singleHelices[m] > i:
                singleHelices[m] -= 1

##even if a certain thing is 0, it still should be part of a helix if it is not big enough to be a node
def correctHNumbers(RNA):
    for i in range(1,len(RNA.Helices)):
        for j in range(RNA.Helices[i].start,RNA.Helices[i].end+1):
            #if RNA.Bases[j].helixNumber == 0:
                RNA.Bases[j].helixNumber = i
        for l in range(RNA.Bases[RNA.Helices[i].end].indexBP,RNA.Bases[RNA.Helices[i].start].indexBP+1):        
            #if RNA.Bases[l].helixNumber == 0:
                RNA.Bases[l].helixNumber = i
### flag bases ###
#Just get a general idea for the layout of the thing
def flagBases(RNA):
    for i in range(1,len(RNA.Helices)):
        #Label all bases belonging to a helix as something 
        for j in range(RNA.Helices[i].start,RNA.Helices[i].end+1):
            RNA.Bases[j].flag = "H"
        for l in range(RNA.Bases[RNA.Helices[i].end].indexBP,RNA.Bases[RNA.Helices[i].start].indexBP+1):        
            RNA.Bases[l].flag = "H"

def firstNode(RNA):
    #here you need to account for when the first node is a junction, because it's a special node
    start = 1
    end = RNA.Bases[len(RNA.Bases)-1].index
    for i in range(1,len(RNA.Bases)):
        if RNA.Bases[i].indexBP != 0:
            break
        RNA.Bases[i].flag = "S"
    for j in range(len(RNA.Bases)-1,0,-1):
        if RNA.Bases[j].indexBP != 0:
            break
        RNA.Bases[j].flag = "E"
    #print "s: " + str(i) + " e: "  + str(j)
    sNode = StartingNode()
    sNode.start5 = start
    sNode.start3 = j
    sNode.end5 = i
    sNode.end3 = end
    sNode.lowestIndex = i
    #find out what it's connected to 
    if RNA.Bases[i].helixNumber == RNA.Bases[j].helixNumber:
        sNode.string = "S"
        sNode.helices.append(RNA.Bases[j].helixNumber)
    else:
        sNode.string = "SJ"
        iHelix = RNA.Bases[i].helixNumber
        jHelix = RNA.Bases[j].helixNumber
        sNode.helices.append(iHelix)
        sNode.helices.append(jHelix)
        #walk around the junction
        index = sNode.end5
        while(index < len(RNA.Bases)):
            RNA.Bases[index].flag = "SJ"
            if RNA.Bases[index].helixNumber!=0:        
                RNA.Bases[index].flag = "H"
                if RNA.Bases[index].helixNumber not in sNode.helices:
                    sNode.helices.append(RNA.Bases[index].helixNumber)
            
                index = RNA.Bases[index].indexBP
            index +=1
        
        '''
        while iHelix<jHelix:
            print RNA.Helices[iHelix].end
            RNA.Helices[iHelix+1].start
            if clearPathNew(RNA,RNA.Bases[RNA.Helices[iHelix].start].indexBP,RNA.Helices[iHelix+1].start): #3' start to 3'end
                print "There is a connection for " + str(iHelix)
                if iHelix+1 not in sNode.helices:
                    sNode.helices.append(iHelix+1)
            iHelix+=1
        
        while jHelix>1:
            print RNA.Bases[RNA.Helices[jHelix-1].start].indexBP
            RNA.Helices[iHelix+1].start
            if clearPathNew(RNA,RNA.Bases[RNA.Helices[jHelix-1].start].indexBP,RNA.Helices[jHelix].start):
                print "There is a connection for " + str(jHelix)
                if iHelix+1 not in sNode.helices:
                    sNode.helices.append(jHelix-1)
            jHelix-=1
        '''
    #now you have to see how many so something like while i < j
    sNode.helices.sort()
    RNA.Nodes.append(sNode)
    

    #you could add a provision for 
    

### find internal loops ###
# FOR ALL OF THESE YOU MUST INCLUDE THE FACT THAT THE HELICES COULD BE NEXT TO EACH OTHER
def InternalLoops(RNA):
    for i in range(1,len(RNA.Helices)-1):
        helix2five = RNA.Helices[i+1].start
        helix2three = RNA.Bases[RNA.Helices[i+1].start].indexBP
        helix1five = RNA.Helices[i].end
        helix1three = RNA.Bases[RNA.Helices[i].end].indexBP
        if clearPathNew(RNA,helix1five,helix2five) and clearPath(RNA,helix2three,helix1three): #ASSYMETRIC BULGE
            iLoop = InternalLoop()
            iLoop.start5=helix1five            
            iLoop.end5=helix2five
            iLoop.start3=helix2three
            iLoop.end3=helix1three
            iLoop.helices.append(i)
            iLoop.helices.append(i+1)
            iLoop.lowestIndex = helix1five
            RNA.Nodes.append(iLoop)
            for j in range(helix1five+1,helix2five):
                RNA.Bases[j].flag="I"
            for k in range(helix2three+1,helix1three):
                RNA.Bases[k].flag="I"
        
def hairpins(RNA):
    for i in range(1,len(RNA.Helices)):
        if clearPathNew(RNA,RNA.Helices[i].end,RNA.Bases[RNA.Helices[i].end].indexBP):
            HP = Hairpin()
            HP.start = RNA.Helices[i].end
            HP.lowestIndex = RNA.Helices[i].end
            HP.end = RNA.Bases[RNA.Helices[i].end].indexBP
            HP.helices.append(i)
            RNA.Nodes.append(HP)
            for j in range(RNA.Helices[i].end+1,RNA.Bases[RNA.Helices[i].end].indexBP):
                RNA.Bases[j].flag="HP"

def junctions(RNA):
    for i in range(1,len(RNA.Bases)):
        #print i
        if RNA.Bases[i].flag == "0" and RNA.Bases[i].jActivity==True:
            circle = []
            newJ = Junction()
            #print "Here, for " + str(i)
            RNA.Bases[i].flag = "J"
            index = i
            while(index < len(RNA.Bases) and RNA.Bases[index].jActivity==True):
                #print "inside, " + str(index) + " stat: " + str(RNA.Bases[index].jActivity)
                circle.append(index)
                RNA.Bases[index].jActivity = False
                RNA.Bases[index].flag = "J"
                if RNA.Bases[index].helixNumber!=0:        
                    index = RNA.Bases[index].indexBP
                    RNA.Bases[index].flag = "J"
                    RNA.Bases[index].jActivity = False
                    if RNA.Bases[index].helixNumber not in newJ.helices:
                        newJ.helices.append(RNA.Bases[index].helixNumber)
                    circle.append(index)
                index +=1
            circle.sort()
            newJ.lowestIndex = circle[0]
            for nt in circle:
                if RNA.Bases[nt].indexBP == 0:
                    break
            newJ.lowestUnpaired = nt
            newJ.helices.sort()
            RNA.Nodes.append(newJ)
            #print circle


def connectNodes(RNA):    
    for i in range(1,len(RNA.Nodes)-1):
        for j in range(i+1,len(RNA.Nodes)):
            for l in RNA.Nodes[i].helices:
                if l in RNA.Nodes[j].helices:
                    #print "Node " + str(i) + " is connected to Node " + str(j)
                    RNA.adjMatrix[i-1][j-1] = 1
                    RNA.adjMatrix[j-1][i-1] = 1
                    RNA.degMatrix[i-1][i-1] +=1
                    RNA.degMatrix[j-1][j-1] +=1

#def calcEigen(RNA,arg):
# S.J. 06/14/2019 - changes to use functions in ClassesFunctions file
def calcEigen(RNA): # S.J. 07/05/2018 - removing the last argument as that is not needed
    
    if len(RNA.Nodes)-1==1:
        print ("1_1" )
    #elif len(RNA.Nodes)>11:
    elif len(RNA.Nodes)>14: # S.J. 05/12/2017 - to take into account graph with vertices 11-13
        print ("TMV,%d" %(len(RNA.Nodes)-1))
    else: # S.J. 06/14/2019 - changes to use functions in ClassesFunctions file
        eigFile = "TreeEig/%dEigen"%(len(RNA.Nodes)-1)
        adjMatFile = "TreeAdj/V%dAdjDG"%(len(RNA.Nodes)-1)
        
        TreeGraphs = []
        loadEigenvalues(TreeGraphs,len(RNA.Nodes)-1,eigFile)
        loadAdjMatrices(TreeGraphs,len(RNA.Nodes)-1,adjMatFile)
        
        RNA.laplacian = numpy.array(RNA.degMatrix) - numpy.array(RNA.adjMatrix)
        RNA.printLpl()
        
        eigen = calcEigenValues(RNA.adjMatrix)
        printEigenValues(eigen)
        
        loc = "NA"
        for g in TreeGraphs: # looking for a match in the DualGraphs read 
            loc = g.match(eigen,RNA.adjMatrix)
            if loc != "NA": # match found, print ID
                print ("Graph ID: %s"%(loc))
                graphID.append(loc)
                break
                
        if loc == "NA":
            print ("ERROR: 100!")
            exit()


def labelBases(RNA):
    #this labels the bases NodeNumber. Each node, inner junctions aside, is overlabelled, so that (...) is really #####, rather than 0###0
    #reset activities to true
    for i in range(1,len(RNA.Bases)):
        RNA.Bases[i].jActivity = True
    if RNA.Nodes[1].toString() == "S":
        start = RNA.Nodes[1].end5
        end = RNA.Nodes[1].start3
        RNA.Bases[start].nodeNumber = 1
        RNA.Bases[end].nodeNumber = 1
    elif RNA.Nodes[1].toString() == "SJ":
        index = 1
        while(index < len(RNA.Bases) and RNA.Bases[index].jActivity==True):
            RNA.Bases[index].jActivity = False
            RNA.Bases[index].nodeNumber = 1
            if RNA.Bases[index].helixNumber!=0:        
                index = RNA.Bases[index].indexBP
                RNA.Bases[index].nodeNumber = 1
                RNA.Bases[index].jActivity = False
            index +=1
    for i in range(2,len(RNA.Nodes)):    
        if RNA.Nodes[i].toString() == "I":
            for nt in range(RNA.Nodes[i].start5,RNA.Nodes[i].end5+1):
                RNA.Bases[nt].nodeNumber = i
            for nt in range(RNA.Nodes[i].start3,RNA.Nodes[i].end3+1):
                RNA.Bases[nt].nodeNumber = i 
        if RNA.Nodes[i].toString() == "HP":
            for nt in range(RNA.Nodes[i].start,RNA.Nodes[i].end+1):
                RNA.Bases[nt].nodeNumber = i 
        if RNA.Nodes[i].toString() == "J":
            index = RNA.Nodes[i].lowestUnpaired
            while(index < len(RNA.Bases) and RNA.Bases[index].jActivity==True):
                RNA.Bases[index].jActivity = False
                RNA.Bases[index].nodeNumber = i
                if RNA.Bases[index].helixNumber!=0:        
                    index = RNA.Bases[index].indexBP
                    RNA.Bases[index].nodeNumber = i
                    RNA.Bases[index].jActivity = False
                index +=1


def label(RNA):
        #Code to LABEL, please address any PROBLEMS!###ALSO FIX GRAPHID
        #for tree graphs, you first have to add node labels...
        nodeOrder = None
        ID = graphID[0]
        vNum = int(ID.split('_')[0])
        ID = int(ID.split('_')[1])
        g = open("V%dAdjTG" %(vNum),'r')
        a = []
        #print ((ID-1)*(vNum+2)+2)
        for j in range(0,((ID-1)*(vNum+2)+2)-1):
            g.readline()
        for k in range(0,vNum):
            tempA = []
            for l in g.readline().split():
                tempA.append(int(float(l)))
            a.append(tempA)
        g.close()
        b = RNA.adjMatrix
        c = deepcopy(a)
        num = []
        for i in range(0,len(a)):
            num.append(i)
        for i in list(permutations(num)):
            listI = list(i) 
            for j in range(0,len(c)):
                jI = listI[j]
                for k in range(0,len(c)):
                    kI= listI[k]
                    c[j][k] = a[jI][kI]
            if c==b:
                for i in range(0,len(listI)):
                    listI[i]+=1
                nodeOrder = listI
                #experimental!
                break
        #print str(nodeOrder)    
        if nodeOrder != None:            
            RNA.printOrder(nodeOrder)
        else:
            print ("No matching adjacency found.")

def main():            
    #for arg in sys.argv[1:]: # S.J. 07/05/2018 - eliminating the for loop, so this will run on one file at a time
        # S.J. 07/04/2018 - adding to read in adjacency matrices
    adjMatTrue = False
    if sys.argv[1] == "-adj_mat":
        adjMatTrue = True
        RNA = getAdjMatInfo(sys.argv[2])
    elif sys.argv[1] == "-dotb": # S.J. 07/25/2018 - flag to read RNA info in dotbracket notation
        RNA = getDotBracketInfo(sys.argv[2]) 
    elif sys.argv[1][-2:] == "ct":
        RNA = getCTInfo(sys.argv[1])
    else:
        RNA = getBPSEQInfo(sys.argv[1])
    if pseudoKnots(RNA):
        print ("pseudoknot!")
    else:
        if not adjMatTrue:
            countHelices(RNA) 
            changeHelices(RNA)
            #Tree graph methods
            correctHNumbers(RNA)
            flagBases(RNA)
            firstNode(RNA)
            InternalLoops(RNA)
            hairpins(RNA)
            junctions(RNA)
            #Tree graph methods
            RNA.sortNodes()
            RNA.makeMatrices()
            connectNodes(RNA)

        RNA.printAdj()
        RNA.printDeg()
        calcEigen(RNA) # S.J. removing the last argument as that is not need 07/05/2018
        
        if not adjMatTrue:
            labelBases(RNA) #must come after sort!1
        #if len(RNA.Nodes)-1==1 or len(RNA.Nodes)>11:
        if len(RNA.Nodes)-1==1 or len(RNA.Nodes)>14: # S.J. 05/12/2017 - to take into account graphs with 11-13 vertices as well
            print ("No matching graph exists because vertex number is either 1 or greater than 13.") # S.J. 07/05/2018
            pass
        #else:
            #label(RNA)
    

#check if there are only zeroes between nt (start) and nt (end)
def clearPath(RNA,start,end):
    if end<start:
        return False
    for i in range(start+1,end):
        "false for %d and %d" %(start,end)
        if RNA.Bases[i].indexBP !=  0:
            return False
    return True
def clearPathNew(RNA,start,end): #should also account for another helix ahead
    if end<start:
        return False
    if start==end-1: #like if it's helix 22 and 23 THIS IS THE NEW PART, they are obviously connected...
        return True
    for i in range(start+1,end):
        "false for %d and %d" %(start,end)
        if RNA.Bases[i].indexBP !=  0:
            return False
    return True


if __name__ == "__main__":
    
    inpath = sys.argv[1]
    outpath = sys.argv[2]
    files = os.listdir(inpath)   
    
    
    for f in files:

        sys.stdout = open(outpath+'/'+f, 'w')
        
        RNA = getCTInfo(inpath+'/'+f)
        
        if pseudoKnots(RNA):
            print ("pseudoknot!")
        else:
            countHelices(RNA) 
            changeHelices(RNA)
            correctHNumbers(RNA)
            flagBases(RNA)
            firstNode(RNA)
            InternalLoops(RNA)
            hairpins(RNA)
            junctions(RNA)
            RNA.sortNodes()
            RNA.makeMatrices()
            connectNodes(RNA)

            RNA.printAdj()
            RNA.printDeg()
            calcEigen(RNA) # S.J. removing the last argument as that is not need 07/05/2018
            
            labelBases(RNA) #must come after sort!
            if len(RNA.Nodes)-1==1 or len(RNA.Nodes)>14: # S.J. 05/12/2017 - to take into account graphs with 11-13 vertices as well
                print ("No matching graph exists because vertex number is either 1 or greater than 13.") # S.J. 07/05/2018
        
        sys.stdout.close()
