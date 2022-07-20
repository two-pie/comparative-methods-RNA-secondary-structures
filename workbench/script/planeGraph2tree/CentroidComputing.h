#pragma once



#include "stdafx.h"
#include <vector>
#include <string>
#include <direct.h>


using namespace std;

/*~~~~~~~~Structures~~~~~~~~*/
struct halfEdges;
struct vertices;
struct faces;

struct nodes;

/*~~~~~~~~~~~~~DCEL~~~~~~~~~~~~~*/
class Graph_DCEL
{
protected:

    string graphName;

    vector<vertices> verList;
    vector<halfEdges> edgeList;
    vector<faces> faceList;

    vector<vertices> verList_ori;
    vector<halfEdges> edgeList_ori;
    vector<faces> faceList_ori;

    vector<vertices> verList_tree;
    vector<halfEdges> edgeList_tree;
    vector<faces> faceList_tree;

    vector<vertices> endpointList;

    vector<vector<string>> verListS;
    vector<vector<string>> edgeListS;
    vector<vector<string>> faceListS;

    int verCount;
    int edgeCount;
    int faceCount;

    bool listVis = true;

public:Graph_DCEL(void);
public:~Graph_DCEL();

/*--------------Build the graph------------------------*/
public: int buildGraph(string ver_path, string edge_path, string face_path);

/*--------------Verlist builder-----------------------*/
private:int readVer(string path);
private:int creatVer();
private:int buildVer();
protected:bool checkVer();

/*--------------EdgeList builder---------------------*/
private:int readEdge(string path);
private:int creatEdge();
private:int buildEdge();
protected:bool checkEdge();

/*--------------FaceList builder---------------------*/
private:int readFace(string path);
private:int creatFace();
private:int buildFace();
protected:bool checkFace();

/*--------------Search ver edge face structure--------------*/
protected:int searchVer(int index);
protected:int searchFace(int index);
protected:int searchEdge(int index);
};

/*~~~~~~~~~~~PlaneGraph~~~~~~~~~~~~~*/
class PlaneGraph :public Graph_DCEL
{
private:

    faces* outerFace = nullptr;

    faces* topCenF = nullptr;
    halfEdges* topCenE = nullptr;
    vertices* topCenV = nullptr;

    int pTimes = 0;
    bool criticalMode = false;
    vector<vector<int>> endpointRel;


    vector<halfEdges*> outerC;



    vector<nodes> treeList;
    vector<nodes*> subRootN;


public:PlaneGraph(void);
public:~PlaneGraph();

public: bool isPlaneGraph();
public: int RUNNING();
public: int RUNNING_MutiRoot();

public: int setOuterFace(int n);
public: int setOuterFace(string path);

    /*------------PEELING-------------*/
public: int findOuterCircle();

public: int PEELING();
public: bool sinExpFace(faces* f);
public: bool sinExpEdge(halfEdges* e);
public: bool AdjSubGraphy(halfEdges *e1, halfEdges *e2);



    /*---------Canonical form computing---------*/
public: int treeTransfer();
public: int treeTransfer_MutiRoot();
public: int CanFormCom();

    /*Assistant method*/
private: vector<halfEdges*> innerEforF(faces* f);
private: vector<halfEdges*> outterEforF(faces* f);
private: vector<halfEdges*> outterEforE(vector<halfEdges*> e);
private: bool isConnected(vector<halfEdges*> edges);
private: int endEdge(vector<halfEdges*> edges);
private: vector<vertices*> nodeForF(faces* f);
private: vector<vertices*> nodeForE(halfEdges* e);
private: int searchNode(int index, vector<nodes> nList);
private: nodes* nextNodeOfP(nodes* n);
private: int subRootSearch();


    /*Add and Remove*/
public: int addEdge(halfEdges e);

private: int removeEdge(int index);
private: int removeFace(int index);
private: int disconnectE(int index);

    /*Setting*/
public: int listVisible(bool sta);


    /*-------Testing--------*/
public: bool seFaceTesting(vector<int> tList);
public: bool seEdgeTesting(vector<int> tList);

    /*Transfer forms*/
private: int labelIden();
private: int labelIden_sub(vector<nodes> tList);
private: int APTEDformTrans();
private: int APTEDformTrans_MutiRoot();
public: int APTEDformTrans_AllVerAsRoot();
};