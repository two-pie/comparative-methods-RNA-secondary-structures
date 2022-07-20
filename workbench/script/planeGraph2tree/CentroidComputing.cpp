#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

#include "CentroidComputing.h"

using namespace std;

/*~~~~~~~~Structures~~~~~~~~*/
struct vertices
{
    int index;

    halfEdges *incident_hE;

    vertices *oriV;
};

struct halfEdges
{
    int index;

    faces *incident_f;
    vertices *target_v;
    halfEdges *twin_hE, *prev_hE, *next_hE;
};

struct faces
{
    int index;

    halfEdges *arbitarary_hE;
};

struct nodes
{
    int index;

    nodes* parentN;

    vector<nodes*> childrenN;

    nodes* oriN;

    bool isLeaf = false;

    string label;
};


/*~~~~~~~~~~~~~DCEL~~~~~~~~~~~~~*/
Graph_DCEL::Graph_DCEL(void)
{
    cout << "Graph will be built in DCEL" << endl;
}
Graph_DCEL::~Graph_DCEL()
{
    cout << "Graph has been deleted." << endl;
}

/*--------------Build the graph------------------------*/
int Graph_DCEL::buildGraph(string ver_path, string edge_path, string face_path)
{
    // finds the index where the substring "_ver.txt" begins
    int ver_start_index = ver_path.find("_ver.txt");
    this->graphName = ver_path.substr(0, ver_start_index);
    cout << "The graph is " << graphName << endl;
    /*Graph builder*/
    readVer("./DCEL/"+ver_path);
    creatVer();

    readEdge("./DCEL/"+edge_path);
    creatEdge();

    readFace("./DCEL/"+face_path);
    creatFace();

    buildVer();
    buildFace();
    buildEdge();

    return 0;
}


/*--------------Verlist builder-----------------------*/
int Graph_DCEL::readVer(string vPath)
{
    string s;
    string d;
    ifstream read(vPath, ios::in);
    vector<string> verData;

    if (!read.is_open())
    {
        cout << "error" << endl;
    }
    else
    {
        while (!read.eof())
        {
            getline(read, s);
            s.erase(s.begin());
            s.erase(s.end() - 1);
            //cout << s << endl;

            for (int i = 0; i < s.length(); i++)
            {
                //cout << s[i] << endl;
                if (isdigit(s[i]))
                {
                    d += s[i];
                }
                else if (isalpha(s[i]))
                {
                    d += s[i];
                }
                else
                {
                    verData.push_back(d);
                    d.clear();
                }
                //cout << d << endl;

            }
            verData.push_back(d);
            d.clear();
            this->verListS.push_back(verData);
            verData.clear();
        }
    }


    for (int i = 0; i < verListS.size(); i++)
    {
        if (this->verListS[i].size() != 2)
        {
            cout << "The size of No." << i + 1 << " ver set is error" << endl;
        }
        //cout << verListS[i][0]<<" "<<stoi(verListS[i][1]) << endl;
    }
    return 0;
}
int Graph_DCEL::creatVer()
{
    vertices v;
    for (vector<vector<string>>::iterator vLit=verListS.begin();vLit!=verListS.end();++vLit)
    {
        v = { stoi((*vLit)[0]) };
        this->verList.push_back(v);
    }
    verList_ori = verList;
    verList_tree = verList;
    return 0;
}
int Graph_DCEL::buildVer()
{

    int i = 0;
    if (this->verList.size() != this->verListS.size())
    {
        cout << "Size of the verList & strList are not equal" << endl;
    }
    else
    {
        for (vector<vertices>::iterator vLit=verList.begin();vLit!=verList.end();++vLit)//int i = 0; i < this->verList.size(); i++)
        {
            for (vector<vector<string>>::iterator vLsIt=verListS.begin();vLsIt!=verListS.end();++vLsIt)
            {
                if ((*vLit).index == stoi((*vLsIt)[0]))
                {

                    (*vLit).incident_hE = &this->edgeList[searchEdge(stoi((*vLsIt)[1]))];
                    verList_ori[i].incident_hE= &this->edgeList_ori[searchEdge(stoi((*vLsIt)[1]))];
                    verList_tree[i].incident_hE = &this->edgeList_tree[searchEdge(stoi((*vLsIt)[1]))];
                    vLsIt = verListS.erase(vLsIt);
                    break;
                }
            }
            i++;
            //cout << verList[i].index<<" "<<verList[i].incident_hE->index << endl;
        }
    }



    return 0;
}
bool Graph_DCEL::checkVer()
{

    cout << "---------------Vertices Checking Start---------------" << endl;

    int count = 0;

    this->verCount = 0;

    for (vector<vertices>::iterator vLit=verList.begin();vLit!=verList.end();++vLit)//int i = 0; i < this->verList.size(); i++)
    {
        if ((*vLit).index != -604)
        {
            verCount++;
            if (this->listVis)
            {
                cout <<"vIndex: "<< (*vLit).index << " incE:" << (*vLit).incident_hE->index << endl;
            }
            if ((*vLit).incident_hE->target_v->index != (*vLit).index)
            {
                cout << "The incident half-edge for No." << (*vLit).index << " vertices is error." << endl;
                count++;
            }
        }

    }
    if (count > 0)
    {
        cout << "--------Fail to pass the vertex checking--------" << endl;
        return false;
    }
    else
    {
        cout << "--------Passed the vertex checking--------" << endl;
        return true;
    }
}


/*--------------EdgeList builder---------------------*/
int Graph_DCEL::readEdge(string ePath)
{
    string s;
    string d;
    ifstream read(ePath, ios::in);
    vector<string> edgeData;

    if (!read.is_open())
    {
        cout << "error" << endl;
    }
    else
    {
        while (!read.eof())
        {
            getline(read, s);
            s.erase(s.begin());
            s.erase(s.end() - 1);
            for (int i = 0; i < s.length(); i++)
            {
                if (isdigit(s[i]))
                {
                    d += s[i];
                }
                else if (isalpha(s[i]))
                {
                    d += s[i];
                }
                else
                {
                    edgeData.push_back(d);
                    d.clear();
                }
            }
            edgeData.push_back(d);
            d.clear();
            this->edgeListS.push_back(edgeData);
            edgeData.clear();
        }
    }


    for (int i = 0; i < this->edgeListS.size(); i++)
    {
        if (this->edgeListS[i].size() != 6)
        {
            cout << "The size of No." << i + 1 << " edge set is error" << endl;
        }
        //cout << edgeListS[i][0]<<" "<<edgeListS[i][1]<<" "<<edgeListS[i][2]<<" "<<edgeListS[i][3]<<" "<< edgeListS[i][4]<<" "<< edgeListS[i][5] << endl;
    }



    return 0;
}
int Graph_DCEL::creatEdge()
{
    halfEdges h;

    for (vector<vector<string>>::iterator eLsIt=edgeListS.begin();eLsIt!=edgeListS.end();++eLsIt)
    {
        h = { stoi((*eLsIt)[0]) };
        this->edgeList.push_back(h);
    }

    edgeList_ori = edgeList;
    edgeList_tree = edgeList;

    return 0;
}
int Graph_DCEL::buildEdge()
{


    int i = 0;

    if (this->edgeList.size() != this->edgeListS.size())
    {
        cout << "Size of the edgeList & strList are not equal" << endl;
    }
    else
    {
        for (vector<halfEdges>::iterator eLit = edgeList.begin(); eLit != edgeList.end(); ++eLit)
        {
            for (vector<vector<string>>::iterator eLsIt = edgeListS.begin(); eLsIt != edgeListS.end(); ++eLsIt)
            {
                if ((*eLit).index == stoi((*eLsIt)[0]))
                {
                    /*connect incident face*/
                    (*eLit).incident_f = &this->faceList[searchFace(stoi((*eLsIt)[1]))];
                    edgeList_ori[i].incident_f= &this->faceList_ori[searchFace(stoi((*eLsIt)[1]))];
                    edgeList_tree[i].incident_f = &this->faceList_tree[searchFace(stoi((*eLsIt)[1]))];
                    /*connect target vertices*/
                    (*eLit).target_v = &this->verList[searchVer(stoi((*eLsIt)[2]))];
                    edgeList_ori[i].target_v= &this->verList_ori[searchVer(stoi((*eLsIt)[2]))];
                    edgeList_tree[i].target_v = &this->verList_tree[searchVer(stoi((*eLsIt)[2]))];
                    /*connect twin half edge*/
                    (*eLit).twin_hE = &this->edgeList[searchEdge(stoi((*eLsIt)[3]))];
                    edgeList_ori[i].twin_hE= &this->edgeList_ori[searchEdge(stoi((*eLsIt)[3]))];
                    edgeList_tree[i].twin_hE = &this->edgeList_tree[searchEdge(stoi((*eLsIt)[3]))];
                    /*connect preview half edge*/
                    (*eLit).prev_hE = &this->edgeList[searchEdge(stoi((*eLsIt)[4]))];
                    edgeList_ori[i].prev_hE= &this->edgeList_ori[searchEdge(stoi((*eLsIt)[4]))];
                    edgeList_tree[i].prev_hE = &this->edgeList_tree[searchEdge(stoi((*eLsIt)[4]))];
                    /*connect next half edge*/
                    (*eLit).next_hE = &this->edgeList[searchEdge(stoi((*eLsIt)[5]))];
                    edgeList_ori[i].next_hE= &this->edgeList_ori[searchEdge(stoi((*eLsIt)[5]))];
                    edgeList_tree[i].next_hE = &this->edgeList_tree[searchEdge(stoi((*eLsIt)[5]))];

                    eLsIt = edgeListS.erase(eLsIt);

                    break;
                }
            }
            i++;
        }
    }



    return 0;
}
bool Graph_DCEL::checkEdge()
{
    /*--DATA CHECKING--*/

    cout << "---------------Half-edge Checking Start---------------" << endl;

    int count = 0;

    this->edgeCount = 0;

    for (vector<halfEdges>::iterator eLit=edgeList.begin();eLit!=edgeList.end();++eLit)
    {
        if ((*eLit).index!=-604)
        {
            edgeCount++;
            if (this->listVis)
            {
                cout << "eIndex: " << (*eLit).index << " incF: " << (*eLit).incident_f->index << " tarV: " << (*eLit).target_v->index << " twinE:" << (*eLit).twin_hE->index << " prevE:" << (*eLit).prev_hE->index << " nextE: " << (*eLit).next_hE->index << endl;
            }

            if ((*eLit).twin_hE->twin_hE->index != (*eLit).index)
            {
                cout << "The twin half-edge for No." << (*eLit).index << " half-edge is error." << endl;
                count++;
            }

            if ((*eLit).prev_hE->next_hE->index != (*eLit).index)
            {
                cout << "The pre half-edge for No." << (*eLit).index << " half-edge is error." << endl;
                count++;
            }
            if ((*eLit).next_hE->prev_hE->index != (*eLit).index)
            {
                cout << "The next half-edge for No." << (*eLit).index << " half-edge is error." << endl;
                count++;
            }
        }
    }
    if (count > 0)
    {
        cout << "--------Fail to pass the half-edge checking--------" << endl;
        return false;
    }
    else
    {
        cout << "--------Passed the half-edge checking----------" << endl;
        return true;
    }
}

/*--------------FaceList builder---------------------*/
int Graph_DCEL::readFace(string fPath)
{
    string s;
    string d;
    ifstream read(fPath, ios::in);
    vector<string> faceData;

    if (!read.is_open())
    {
        cout << "error" << endl;
    }
    else
    {
        while (!read.eof())
        {
            getline(read, s);
            s.erase(s.begin());
            s.erase(s.end() - 1);
            //cout << s << endl;

            for (int i = 0; i < s.length(); i++)
            {
                //cout << s[i] << endl;
                if (isdigit(s[i]))
                {
                    d += s[i];
                }
                else if (isalpha(s[i]))
                {
                    d += s[i];
                }
                else
                {
                    faceData.push_back(d);
                    d.clear();
                }
                //cout << d << endl;

            }
            faceData.push_back(d);
            d.clear();
            this->faceListS.push_back(faceData);
            faceData.clear();
        }
    }

    /*-----Data check-----*/
    for (int i = 0; i < this->faceListS.size(); i++)
    {
        if (this->faceListS[i].size() != 2)
        {
            cout << "The size of No." << i + 1 << " face set is error" << endl;
        }
        //cout << this->faceListS[i][0]<<" "<<stoi(this->faceListS[i][1]) << endl;
    }
    return 0;
}
int Graph_DCEL::creatFace()
{
    faces f;
    for (vector<vector<string>>::iterator fLsIt = faceListS.begin(); fLsIt != faceListS.end(); ++fLsIt)
    {
        f = { stoi((*fLsIt)[0]) };
        this->faceList.push_back(f);
    }

    faceList_ori = faceList;
    faceList_tree = faceList;

    return 0;
}
int Graph_DCEL::buildFace()
{

    int i = 0;

    if (this->faceList.size() != this->faceListS.size())
    {
        cout << "Size of the faceList & strList are not equal" << endl;
    }
    else
    {
        for (vector<faces>::iterator fLit = faceList.begin(); fLit != faceList.end(); ++fLit)
        {
            for (vector<vector<string>>::iterator fLsIt = faceListS.begin(); fLsIt != faceListS.end(); ++fLsIt)
            {
                if (((*fLit).index == stoi((*fLsIt)[0])))
                {
                    (*fLit).arbitarary_hE = &this->edgeList[searchEdge(stoi((*fLsIt)[1]))];
                    faceList_ori[i].arbitarary_hE= &this->edgeList_ori[searchEdge(stoi((*fLsIt)[1]))];
                    faceList_tree[i].arbitarary_hE = &this->edgeList_tree[searchEdge(stoi((*fLsIt)[1]))];

                    fLsIt = faceListS.erase(fLsIt);

                    //cout << this->faceList[i].arbitarary_hE->index << endl;
                    break;
                }
            }
            i++;
        }
    }

    faceList_ori = faceList;

    return 0;
}
bool Graph_DCEL::checkFace()
{

    cout << "---------------Face Checking Start---------------" << endl;

    /*--DATA CHECKING--*/
    int count = 0;

    this->faceCount = 0;

    for (vector<faces>::iterator fLit=faceList.begin();fLit!=faceList.end();++fLit)
    {
        if ((*fLit).index != -604)
        {
            faceCount++;
            if (this->listVis)
            {
                cout <<"fIndex: " <<(*fLit).index << " arbE: " << (*fLit).arbitarary_hE->index << endl;
            }
            if ((*fLit).arbitarary_hE->incident_f->index != (*fLit).index)
            {
                cout << "The arbitarary half-edge for No." << (*fLit).index << " face is error." << endl;
                count++;
            }
        }

    }
    if (count > 0)
    {
        cout << "--------Fail to pass the face checking--------" << endl;
        return false;
    }
    else
    {
        cout << "--------Passed the face checking--------" << endl;
        return true;
    }
}

/*--------------Search ver edge face structure--------------*/
int Graph_DCEL::searchVer(int index)
{
    if (index != -604)
    {
        for (unsigned int i = 0; i < this->verList.size(); i++)
        {
            if (this->verList[i].index == index)
            {
                return i;
            }
        }
    }

    cout << "Cannot find the Vertex whose index is " << index << "." << endl;
    return -427;
}

int Graph_DCEL::searchEdge(int index)
{
    if (index != -604)
    {
        for (unsigned int i = 0; i < this->edgeList.size(); i++)
        {
            if (this->edgeList[i].index == index)
            {
                return i;
            }
        }
    }

    cout << "Cannot find the HalfEdge whose index is " << index << "." << endl;
    return -427;
}

int Graph_DCEL::searchFace(int index)
{
    if (index != -604)
    {
        for (unsigned int i = 0; i < this->faceList.size(); i++)
        {
            if (this->faceList[i].index == index)
            {
                return i;
            }
        }
    }

    cout << "Cannot find the Face whose index is " << index << "." << endl;
    return -427;
}


/*~~~~~~~~~~~PlaneGraph~~~~~~~~~~~~~*/
PlaneGraph::PlaneGraph(void)
{
    cout << "PlaneGraph has been built." << endl;
}

PlaneGraph::~PlaneGraph()
{
    cout << "planeGraph has been deleted." << endl;
}

bool PlaneGraph::isPlaneGraph()
{
    if (verCount + faceCount - edgeCount / 2 == 2)//Euler's fomula
    {
        cout << "This is a plane graph." << endl;
        return true;
    }
    else
    {
        cout << this->graphName<<" is not a plane graph." << endl;
        return false;
    }
}

int PlaneGraph::RUNNING()
{
    while (true)
    {
        if (criticalMode == true)
        {
            cout << "-.-.-.-.-.-.-.-.-.-PEELING complected-.-.-.-.-.-.-.-.-.-" << endl;
            break;
        }

        if (!checkVer() || !checkEdge() || !checkFace() || !isPlaneGraph())
        {
            cout << "------------ERROR Cause -> PEELING Stop---------------" << endl;
            break;
        }

        this->PEELING();
    }

    //Endpoint relationship dealing


    cout << "******************************************The transfered tree in DCEL list******************************************" << endl;
    for (vector<halfEdges>::iterator eLit=edgeList_tree.begin();eLit!=edgeList_tree.end();++eLit)
    {
        if ((*eLit).target_v == nullptr)
        {
            for (vector<vector<int>>::iterator epRit = endpointRel.begin(); epRit != endpointRel.end(); ++epRit)
            {
                if ((*eLit).index == (*epRit)[0])
                {
                    for (vector<vertices>::iterator epIt = endpointList.begin(); epIt != endpointList.end(); ++epIt)
                    {
                        if ((*epIt).index == (*epRit)[1])
                        {
                            (*eLit).target_v = &(*epIt);
                        }
                    }
                }
            }
        }
        if ((*eLit).target_v->oriV == nullptr)
        {
            cout << "eIndex: " << (*eLit).index << " incF: " << (*eLit).incident_f->index << " tarV: " << (*eLit).target_v->index << " twinE:" << (*eLit).twin_hE->index << " prevE:" << (*eLit).prev_hE->index << " nextE: " << (*eLit).next_hE->index << endl;
        }
        else
        {
            cout << "eIndex: " << (*eLit).index << " incF: " << (*eLit).incident_f->index << " newTarV: " << (*eLit).target_v->index <<" oriV:"<<(*eLit).target_v->oriV->index<< " twinE:" << (*eLit).twin_hE->index << " prevE:" << (*eLit).prev_hE->index << " nextE: " << (*eLit).next_hE->index << endl;
        }

    }
    cout << "*******************************************"<<this->graphName<<"*************************************************************************" << endl;

    treeTransfer();

    APTEDformTrans();

    //CanFormCom();


    return 0;
}

int PlaneGraph::RUNNING_MutiRoot()
{
    while (true)
    {
        if (criticalMode == true)
        {
            cout << "-.-.-.-.-.-.-.-.-.-PEELING complected-.-.-.-.-.-.-.-.-.-" << endl;
            break;
        }

        if (!checkVer() || !checkEdge() || !checkFace() || !isPlaneGraph())
        {
            cout << "------------ERROR Cause -> PEELING Stop---------------" << endl;
            break;
        }

        this->PEELING();
    }

    //Endpoint relationship dealing


    cout << "******************************************The transfered tree in DCEL list******************************************" << endl;
    for (vector<halfEdges>::iterator eLit = edgeList_tree.begin(); eLit != edgeList_tree.end(); ++eLit)
    {
        if ((*eLit).target_v == nullptr)
        {
            for (vector<vector<int>>::iterator epRit = endpointRel.begin(); epRit != endpointRel.end(); ++epRit)
            {
                if ((*eLit).index == (*epRit)[0])
                {
                    for (vector<vertices>::iterator epIt = endpointList.begin(); epIt != endpointList.end(); ++epIt)
                    {
                        if ((*epIt).index == (*epRit)[1])
                        {
                            (*eLit).target_v = &(*epIt);
                        }
                    }
                }
            }
        }
        if ((*eLit).target_v->oriV == nullptr)
        {
            cout << "eIndex: " << (*eLit).index << " incF: " << (*eLit).incident_f->index << " tarV: " << (*eLit).target_v->index << " twinE:" << (*eLit).twin_hE->index << " prevE:" << (*eLit).prev_hE->index << " nextE: " << (*eLit).next_hE->index << endl;
        }
        else
        {
            cout << "eIndex: " << (*eLit).index << " incF: " << (*eLit).incident_f->index << " newTarV: " << (*eLit).target_v->index << " oriV:" << (*eLit).target_v->oriV->index << " twinE:" << (*eLit).twin_hE->index << " prevE:" << (*eLit).prev_hE->index << " nextE: " << (*eLit).next_hE->index << endl;
        }

    }
    cout << "*******************************************" << this->graphName << "*************************************************************************" << endl;
    /*
    if (topCenV != nullptr)
    {
        treeTransfer();

        APTEDformTrans();
    }
    else
    {
        treeTransfer_MutiRoot();
    }

    */

    treeTransfer();

    APTEDformTrans_MutiRoot();

    return 0;
}

int PlaneGraph::setOuterFace(int n)
{
    outerFace = &faceList[searchFace(n)];

    //cout << "The index of outer face for this graph is "<<outerFace->index <<"."<< endl;

    return 0;
}

int PlaneGraph::setOuterFace(string path)
{
    string s;
    ifstream outerF("./DCEL/"+path, ios::in);
    if (outerF.is_open())
    {
        getline(outerF, s);
    }
    else
    {
        cout << path << "'s outerFace file is error." << endl;
    }
    setOuterFace(stoi(s));
    return 0;
}

/*------------PEELING-------------*/

int PlaneGraph::PEELING()
{
    cout << "-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.PEELING Start-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-." << endl;
    pTimes++;
    cout << "========================================="<<pTimes<<"===========================================" << endl;
    this->findOuterCircle();

    vector<vector<halfEdges*>> cla;
    vector<vector<halfEdges*>>::iterator claIt;
    vector<halfEdges*> set;
    int remEnum = 0;

    //Classify the outter circle half-edge by inner face of its twin edge.
    for (vector<halfEdges*>::iterator outerCit=outerC.begin();outerCit!=outerC.end();outerCit++)
    {
        if (!cla.empty())
        {
            for (claIt=cla.begin();claIt!=cla.end(); ++claIt)
            {
                if ((*outerCit)->twin_hE->incident_f->index == (*claIt)[0]->twin_hE->incident_f->index)
                {
                    (*claIt).push_back(*outerCit);
                    break;
                }
            }
            if (claIt == cla.end())
            {
                set.push_back(*outerCit);
                cla.push_back(set);
                set.clear();
            }
        }
        else
        {
            set.push_back(*outerCit);
            cla.push_back(set);
            set.clear();
        }
    }

    //Classification checking

    cout << "----Classification----" << endl;
    for (int i = 0; i < cla.size(); i++)
    {
        cout << "Set" << i + 1 << endl;
        for (int j = 0; j < cla[i].size(); j++)
        {
            cout <<"F: " <<cla[i][j]->twin_hE->incident_f->index << " eIndex: " << cla[i][j]->index << endl;;
        }
        cout << endl;
    }

    /*
    if (cla.size() == 1)
    {
        topCenF = (cla[0][0]->twin_hE->incident_f);

        vector<vector<halfEdges*>> adjSubGraphSets;
        vector<vector<halfEdges*>> adjOutterEset;
        vector<halfEdges*> adjEset;
        halfEdges* ajuE;
        for (claIt = cla.begin(); claIt != cla.end(); ++claIt)
        {
            for (vector<halfEdges*>::iterator eSet1 = (*claIt).begin(); eSet1 != (*claIt).end(); ++eSet1)
            {
                for (vector<halfEdges*>::iterator eSet2 = (*claIt).begin(); eSet2 != (*claIt).end(); ++eSet2)
                {
                    if ((*eSet1)->index != (*eSet2)->index && AdjSubGraphy((*eSet1), (*eSet2)))
                    {

                        //cout << (*eSet1)->index << " " << (*eSet2)->index << endl;
                        ajuE = (*eSet2)->twin_hE;
                        while (true)
                        {
                            ajuE = ajuE->next_hE;
                            if (ajuE->index == (*eSet1)->twin_hE->index)
                            {
                                break;
                            }
                            adjEset.push_back(ajuE);
                        }
                        adjOutterEset.push_back(adjEset);
                        adjEset.clear();

                    }
                }
            }
        }

        for (vector<vector<halfEdges*>>::iterator aSsetIt = adjSubGraphSets.begin(); aSsetIt != adjSubGraphSets.end(); ++aSsetIt)
        {
            (*aSsetIt).erase((*aSsetIt).begin());
        }

        //Adjunct subgraph outter edges checking
        cout << "----Adjunct subgraph outter edges checking----" << endl;
        for (int i = 0; i < adjOutterEset.size(); i++)
        {
            cout << "Set" << i + 1 << endl;
            for (int j = 0; j < adjOutterEset[i].size(); j++)
            {
                cout << adjOutterEset[i][j]->index << " ";
            }
            cout << endl << endl;
        }


        for (vector<vector<halfEdges*>>::iterator adjIt = adjOutterEset.begin(); adjIt != adjOutterEset.end(); ++adjIt)
        {
            adjEset = outterEforE(*adjIt);
            adjSubGraphSets.push_back(adjEset);
            adjEset.clear();
        }

        //Adjunct subgraph checking
        cout << "----Adjunct subgraph edges checking----" << endl;
        for (int i = 0; i < adjSubGraphSets.size(); i++)
        {
            cout << "Set" << i + 1 << endl;
            for (int j = 0; j < adjSubGraphSets[i].size(); j++)
            {
                cout << adjSubGraphSets[i][j]->index << " ";
            }
            cout << endl << endl;
        }

        cout << "-------Remove the adjunct subgraph-------" << endl;
        for (vector<vector<halfEdges*>>::iterator aSsetIt = adjSubGraphSets.begin(); aSsetIt != adjSubGraphSets.end(); ++aSsetIt)
        {
            for (vector<halfEdges*>::iterator aSit = (*aSsetIt).begin(); aSit != (*aSsetIt).end(); ++aSit)
            {
                removeEdge((*aSit)->index);
            }
        }

        this->outerC.clear();
        cla.clear();

        return 0;

    }
    */
    vector<int> sinExpEdgeIndex;
    vector<int> sinExpFaceIndex;

    //Identify the single exposed edge and single exposed face.
    for (claIt = cla.begin(); claIt != cla.end(); )//Find the half-edge which is exposed;
    {
        /*single exposed edge part*/
        if ((*claIt)[0]->twin_hE->incident_f->index == this->outerFace->index)//If the inner face of the twin half-edge of a outter half-edge is outter face of thie graph, this edge is the exposed edge(may not single exposed).
        {
            for (vector<halfEdges*>::iterator expEdge = (*claIt).begin(); expEdge != (*claIt).end(); ++expEdge)
            {
                if (sinExpEdge((*expEdge)))
                {
                    remEnum++;
                    sinExpEdgeIndex.push_back((*expEdge)->index);
                }
            }
            claIt = cla.erase(claIt);
        }
            /*single exposed face part*/
        else if (sinExpFace((*claIt)[0]->twin_hE->incident_f))
        {
            remEnum += (*claIt).size()*2;
            sinExpFaceIndex.push_back((*claIt)[0]->twin_hE->incident_f->index);
            claIt = cla.erase(claIt);
        }
            /*least part is the detachable edges part and this part can be used to find adjunct subgraphs*/
        else if (isConnected(*claIt))
        {
            ++claIt;
        }
        else
        {
            claIt = cla.erase(claIt);
        }

    }
    /*Checking*/

    cout << "----Detachable edges-----" << endl;
    for (int i = 0; i < cla.size(); i++)
    {
        remEnum += cla[i].size()*2;
        cout <<"Set"<<i+1<< endl;
        for (int j = 0; j < cla[i].size(); j++)
        {
            cout <<"F: " <<cla[i][j]->twin_hE->incident_f->index << "  eIndex: " << cla[i][j]->index << endl;
        }
        cout << endl;
    }
    cout << "----Single exposed edges-----" << endl;
    for (int i = 0; i < sinExpEdgeIndex.size(); i++)
    {
        cout << "eIndex: "<<sinExpEdgeIndex[i] << endl;
    }
    cout << "----Single exposed faces-----" << endl;
    for (int i = 0; i < sinExpFaceIndex.size(); i++)
    {
        cout<<"fIndex: " << sinExpFaceIndex[i] << endl;
    }


    //Find the adjunct subgraph
    vector<vector<halfEdges*>> adjSubGraphSets;
    vector<vector<halfEdges*>> adjOutterEset;
    vector<halfEdges*> adjEset;
    halfEdges* ajuE;
    for (claIt = cla.begin(); claIt != cla.end();++claIt)
    {
        for (vector<halfEdges*>::iterator eSet1 = (*claIt).begin(); eSet1 != (*claIt).end(); ++eSet1)
        {
            for (vector<halfEdges*>::iterator eSet2 = (*claIt).begin(); eSet2 != (*claIt).end(); ++eSet2)
            {
                if ((*eSet1)->index != (*eSet2)->index && AdjSubGraphy((*eSet1), (*eSet2)))
                {

                    //cout << (*eSet1)->index << " " << (*eSet2)->index << endl;
                    ajuE = (*eSet2)->twin_hE;
                    while (true)
                    {
                        ajuE = ajuE->next_hE;
                        if (ajuE->index == (*eSet1)->twin_hE->index)
                        {
                            break;
                        }
                        adjEset.push_back(ajuE);
                    }
                    adjOutterEset.push_back(adjEset);
                    adjEset.clear();

                }
            }
        }
    }

    for (vector<vector<halfEdges*>>::iterator aSsetIt = adjSubGraphSets.begin(); aSsetIt != adjSubGraphSets.end(); ++aSsetIt)
    {
        (*aSsetIt).erase((*aSsetIt).begin());
    }

    //Adjunct subgraph outter edges checking
    cout << "----Adjunct subgraph outter edges checking----" << endl;
    for (int i = 0; i < adjOutterEset.size(); i++)
    {
        cout << "Set" << i + 1 << endl;
        for (int j = 0; j < adjOutterEset[i].size(); j++)
        {
            cout << adjOutterEset[i][j]->index << " ";
        }
        cout << endl << endl;
    }


    for (vector<vector<halfEdges*>>::iterator adjIt = adjOutterEset.begin(); adjIt != adjOutterEset.end(); ++adjIt)
    {
        adjEset = outterEforE(*adjIt);
        adjSubGraphSets.push_back(adjEset);
        adjEset.clear();
    }

    //Adjunct subgraph checking and make a tree duplicate
    vector<vector<halfEdges*>> adjSubGraphSets_tree;
    vector<halfEdges*> adjSubGraph_tree;
    cout << "----Adjunct subgraph edges checking----" << endl;
    for (int i = 0; i < adjSubGraphSets.size(); i++)
    {
        cout << "Set" << i + 1 << endl;
        remEnum += adjSubGraphSets[i].size();
        for (int j = 0; j < adjSubGraphSets[i].size(); j++)
        {
            adjSubGraph_tree.push_back(&edgeList_tree[searchEdge(adjSubGraphSets[i][j]->index)]);
            cout << adjSubGraphSets[i][j]->index << " ";
        }
        adjSubGraphSets_tree.push_back(adjSubGraph_tree);
        adjSubGraph_tree.clear();
        cout << endl<<endl;
    }

    //Critical Mode
    if (remEnum == edgeCount)
    {
        criticalMode = true;
    }

    if (criticalMode == true)
    {
        cout << "==================The Critical Mode ON====================" << endl;
        if (!cla.empty())
        {
            this->topCenF = (cla[0][0]->twin_hE->incident_f);
            cout << "=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=The No." << topCenF->index << " Face is the Topological Centroid of this Plane Graph.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=" << endl;
            cla.erase(cla.begin());
        }
        else if (!sinExpFaceIndex.empty())
        {
            if (sinExpEdgeIndex.size() == 0 && sinExpFaceIndex.size() == 1)//Only a face lefts.
            {
                this->topCenF = &(this->faceList_tree[searchFace(sinExpFaceIndex[0])]);
                cout << "=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=The No." << topCenF->index << " Face is the Topological Centroid of this Plane Graph.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=" << endl;
                sinExpFaceIndex.erase(sinExpFaceIndex.begin());
            }
            else if (sinExpEdgeIndex.size() == 0 && sinExpFaceIndex.size() > 1)//Only faces left.
            {
                vector<vertices*> nodes = nodeForF(&faceList[searchFace(sinExpFaceIndex[0])]);
                if (nodes.size() == 1)
                {
                    topCenV = &verList_tree[searchVer(nodes[0]->index)];
                    cout << "=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=The No." << topCenV->index << " vertices is the Topological Centroid of this Plane Graph.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=" << endl;
                }
                else
                {
                    cout << "Error" << nodes.size() << endl;
                }
            }
            else if (sinExpEdgeIndex.size() > 0 && sinExpFaceIndex.size() >= 1)//faces and single edges left.
            {
                vector<vertices*> nodes = nodeForF(&faceList[searchFace(sinExpFaceIndex[0])]);
                if (nodes.size() == 1)
                {
                    topCenV = &verList_tree[searchVer(nodes[0]->index)];
                    cout << "=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=The No." << topCenV->index << " vertices is the Topological Centroid of this Plane Graph.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=" << endl;
                }
                else
                {
                    cout << "Error" << nodes.size() << endl;
                }
            }

        }
        else if (!sinExpEdgeIndex.empty())
        {
            if (sinExpEdgeIndex.size() == 2)//Only a edge lefts.
            {
                this->topCenE = &(this->edgeList_tree[searchEdge(sinExpEdgeIndex[0])]);
                cout << "=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=The No." << topCenE->index << " Edge is the Topological Centroid of this Plane Graph.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=" << endl;
                sinExpEdgeIndex.erase(sinExpEdgeIndex.begin());
            }
            else//edges left.
            {
                vector<vertices*> nodes = nodeForE(&edgeList[searchEdge(sinExpEdgeIndex[0])]);
                if (nodes.size() == 1)
                {
                    topCenV = &verList_tree[searchVer(nodes[0]->index)];
                    cout << "=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=The No." << topCenV->index << " vertices is the Topological Centroid of this Plane Graph.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=" << endl;
                }
            }

        }
        else
        {
            cout << "PEELING is error, please check the process." << endl;
        }
    }


    //EndPoint dealing
    for (vector<vector<halfEdges*>>::iterator dEsIt = cla.begin(); dEsIt != cla.end(); ++dEsIt)//detachable edge
    {
        disconnectE(endEdge(*dEsIt));
    }
    for (vector<int>::iterator sEfIit = sinExpFaceIndex.begin(); sEfIit != sinExpFaceIndex.end(); ++sEfIit)//singleExposedFace
    {
        disconnectE(endEdge(outterEforF(&faceList[searchFace(*sEfIit)])));
    }
    for (vector<vector<halfEdges*>>::iterator aSgSit = adjSubGraphSets_tree.begin(); aSgSit != adjSubGraphSets_tree.end(); ++aSgSit)//adjunctSubgraph
    {
        while (true)
        {
            vector<halfEdges*>::iterator aSgIt;
            for (aSgIt = (*aSgSit).begin(); aSgIt != (*aSgSit).end(); ++aSgIt)
            {
                if ((*aSgIt)->incident_f->index != this->outerFace->index)
                {
                    disconnectE(endEdge(outterEforF((*aSgIt)->incident_f)));
                    break;
                }
            }

            if (aSgIt == (*aSgSit).end())
            {
                break;
            }
        }
    }



    /*Remove the single exposed half-edges*/
    cout << "-------Remove single exposed half-edges-------" << endl;
    for (vector<int>::iterator sEeIit = sinExpEdgeIndex.begin(); sEeIit != sinExpEdgeIndex.end(); ++sEeIit)
    {
        removeEdge((*sEeIit));

    }

    /*Remove the single exposed faces*/
    cout << "-------Remove single exposed faces-------" << endl;
    for (vector<int>::iterator sEfIit = sinExpFaceIndex.begin(); sEfIit != sinExpFaceIndex.end(); ++sEfIit)
    {
        cout << "fIndex: " << (*sEfIit) << endl;
        removeFace(*sEfIit);
    }

    /*Remove the adjunct subgraph*/
    cout << "-------Remove adjunct subgraph-------" << endl;
    for (vector<vector<halfEdges*>>::iterator aSsetIt = adjSubGraphSets.begin(); aSsetIt != adjSubGraphSets.end(); ++aSsetIt)
    {
        for (vector<halfEdges*>::iterator aSit = (*aSsetIt).begin(); aSit != (*aSsetIt).end(); ++aSit)
        {
            removeEdge((*aSit)->index);
        }
    }

    /*Remove the detachable edges*/
    cout << "-------Remove dismantled edges-------" << endl;
    for (vector<vector<halfEdges*>>::iterator dEsetIt = cla.begin(); dEsetIt != cla.end(); ++dEsetIt)
    {
        for (vector<halfEdges*>::iterator dEit = (*dEsetIt).begin(); dEit != (*dEsetIt).end(); ++dEit)
        {
            removeEdge((*dEit)->index);
        }
    }


    if (this->outerFace->arbitarary_hE->index == -604)
    {
        for (vector<halfEdges>::iterator eLit = edgeList.begin(); eLit != edgeList.end(); ++eLit)
        {
            if ((*eLit).index!=-604 && (*eLit).incident_f->index == outerFace->index)
            {
                outerFace->arbitarary_hE = &(*eLit);
                break;
            }
        }
    }

    this->outerC.clear();
    cla.clear();

    return 0;
}

int PlaneGraph::findOuterCircle()
{
    outerC.clear();
    for (vector<halfEdges>::iterator elIt=edgeList.begin();elIt!=edgeList.end();++elIt)
    {
        if ((*elIt).index != -604 && outerFace->index == (*elIt).incident_f->index)//Check the edge compose a inner face or not.
        {
            outerC.push_back(&(*elIt));
        }
    }

    //OuterCircle testing
    /*
    for (int i = 0; i < outerC.size(); i++)
    {
    cout << outerC[i]->index << endl;
    }
    */
    return 0;
}

bool PlaneGraph::sinExpFace(faces* f)
{
    vector<halfEdges*> innerE = innerEforF(f);
    vector<halfEdges*> outterE;
    for (vector<halfEdges*>::iterator ieIt=innerE.begin();ieIt!=innerE.end();++ieIt)//unsigned int i = 0; i < innerE.size(); i++)
    {
        outterE.push_back((*ieIt)->twin_hE);

        if (this->outerFace->index != (*ieIt)->twin_hE->incident_f->index)
        {
            return false;
        }
    }

    return isConnected(outterE);


    /*
    vector<faces> outterF;
    for (int i = 0; i < outterE.size(); i++)
    {
    for (int j = 0; j < outterF.size(); j++)
    {
    if (outterF[j].index == outterE[i].incident_f->index)
    {
    break;
    }
    outterF.push_back(*outterE[i].incident_f);
    }
    }

    if (outterF.size() <= 1)
    {
    return true;
    }
    else
    {
    return false;
    }
    */
}

bool PlaneGraph::sinExpEdge(halfEdges* e)
{
    if ((outerFace->index == e->incident_f->index) && (outerFace->index == e->twin_hE->incident_f->index) && (e->twin_hE->index == e->prev_hE->index || e->twin_hE->index == e->next_hE->index))
        //If the twin edge do not compose a face either and this twin edge also is the pre or next edge for testing edge, it would be a Single Exposed Edge.
    {
        //cout << e.twin_hE->index << endl;
        return true;
    }
    else
    {
        return false;
    }
}

bool PlaneGraph::AdjSubGraphy(halfEdges *e1, halfEdges *e2)
{
    if (e2->twin_hE->incident_f->index == e1->twin_hE->incident_f->index)
    {
        if (e1->next_hE->index == e2->index && e2->twin_hE->next_hE->index != e1->twin_hE->index)
        {
            return true;
        }
            /* Another way to find the adjunct subgraph but one way is enough.
            else if (e1->prev_hE->index == e2->index&&e2->twin_hE->prev_hE->index != e1->twin_hE->index)
            {
                return true;
            }
            */
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

}


/*---------Canonical form computing---------*/

int PlaneGraph::treeTransfer()
{
    //Build basic tree struct
    for (vector<vertices>::iterator vLit = verList_tree.begin(); vLit != verList_tree.end(); ++vLit)
    {
        nodes n = { (*vLit).index };
        treeList.push_back(n);
    }
    for (vector<vertices>::iterator ePit = endpointList.begin(); ePit != endpointList.end(); ++ePit)
    {
        nodes n;
        n.index = (*ePit).index;
        treeList.push_back(n);
    }
    for (vector<vertices>::iterator ePit = endpointList.begin(); ePit != endpointList.end(); ++ePit)
    {
        treeList[searchNode((*ePit).index,treeList)].oriN = &treeList[searchNode((*ePit).oriV->index, treeList)];
    }
    /*
    for (int i = 0; i < treeList.size(); i++)
    {
        if (treeList[i].oriN == nullptr)
        {
            cout << "nINDEX: " << treeList[i].index << endl;
        }
        else
        {
            cout << "nINDEX: " << treeList[i].index <<" oriN: "<<treeList[i].oriN->index<< endl;
        }

    }
    */

    //Define sub-root nodes
    if (topCenE != nullptr)
    {
        subRootN.push_back(&treeList[searchNode(topCenE->target_v->index, treeList)]);
        subRootN.push_back(&treeList[searchNode(topCenE->twin_hE->target_v->index, treeList)]);
    }
    else if (topCenF != nullptr)
    {
        vector<halfEdges*> innerEtcf = innerEforF(topCenF);
        for (vector<halfEdges*>::iterator iEit = innerEtcf.begin(); iEit != innerEtcf.end(); ++iEit)
        {
            subRootN.push_back(&treeList[searchNode((*iEit)->target_v->index, treeList)]);
        }
    }
    else if (topCenV != nullptr)
    {
        subRootN.push_back(&treeList[searchNode((topCenV)->index, treeList)]);
    }
    else
    {
        cout << "============================Topological Centroid is error============================" << endl;
    }

    for (vector<nodes*>::iterator sRit = subRootN.begin(); sRit != subRootN.end(); ++sRit)
    {
        //Parents node for subtree searching
        vertices* v = nullptr;
        for (vector<vertices>::iterator vLtIt = verList_tree.begin(); vLtIt != verList_tree.end(); ++vLtIt)
        {
            if ((*vLtIt).index == (*sRit)->index)
            {
                v = &(*vLtIt);
                break;
            }
        }
        halfEdges* e=v->incident_hE;
        halfEdges* e_ori = v->incident_hE;
        while (true)
        {
            e = e->next_hE;
            vector<nodes*>::iterator cNit;
            for (cNit = (*sRit)->childrenN.begin(); cNit != (*sRit)->childrenN.end(); ++cNit)
            {
                if (e->target_v->index == (*cNit)->index)
                {
                    break;
                }
            }
            if (cNit != (*sRit)->childrenN.end())
            {
                break;
            }


            vector<nodes*>::iterator sRitv1;
            for (sRitv1 = subRootN.begin(); sRitv1 != subRootN.end(); ++sRitv1)
            {
                if ((*sRitv1)->index == e->target_v->index)
                {
                    break;
                }
            }
            if (sRitv1 == subRootN.end())
            {
                (*sRit)->childrenN.push_back(&treeList[searchNode(e->target_v->index, treeList)]);
                treeList[searchNode(e->target_v->index, treeList)].parentN = &treeList[searchNode((*sRit)->index,treeList)];
            }
            e = e->twin_hE;
            if (e->index == e_ori->index)
            {
                break;
            }

        }
        //Parents node for subtree searching is end

        if ((*sRit)->childrenN.empty())
        {
            (*sRit)->isLeaf = 1;
        }

        for (vector<nodes*>::iterator cNit = (*sRit)->childrenN.begin(); cNit != (*sRit)->childrenN.end(); ++cNit)
        {
            vector<nodes*> subTlist;
            subTlist.push_back(*cNit);
            vector<nodes*> subTlist_p;
            for (vector<nodes*>::iterator cNcNit = (*cNit)->childrenN.begin(); cNcNit != (*cNit)->childrenN.end(); ++cNcNit)
            {
                vector<nodes*>::iterator sRitv1;
                for (sRitv1 = subRootN.begin(); sRitv1 != subRootN.end(); ++sRitv1)
                {
                    if ((*sRitv1)->index == (*cNcNit)->index)
                    {
                        break;
                    }
                }
                if (sRitv1 == subRootN.end())
                {
                    subTlist.push_back((*cNcNit));
                }
            }
            while (true)
            {
                bool expandFin = true;
                vector<nodes*>::iterator sTlIt;
                for (sTlIt = subTlist.begin(); sTlIt != subTlist.end(); ++sTlIt)
                {
                    if ((*sTlIt)->childrenN.empty() && !(*sTlIt)->isLeaf&&(*sTlIt)->parentN!=nullptr)
                    {
                        expandFin = false;

                        vertices* v_node=nullptr;
                        for (vector<vertices>::iterator vLtIt = verList_tree.begin(); vLtIt != verList_tree.end(); ++vLtIt)
                        {
                            if ((*vLtIt).index == (*sTlIt)->index)
                            {
                                v_node = &(*vLtIt);
                                break;
                            }
                        }
                        if (v_node == nullptr)
                        {
                            for (vector<vertices>::iterator ePit = endpointList.begin(); ePit != endpointList.end(); ++ePit)
                            {
                                if ((*ePit).index == (*sTlIt)->index)
                                {
                                    v_node = &(*ePit);
                                    break;
                                }
                            }
                        }

                        halfEdges* e_node = v_node->incident_hE;

                        while (true)
                        {
                            e_node=e_node->next_hE;
                            if (e_node->target_v->index == (*sTlIt)->parentN->index)
                            {
                                e_node=e_node->twin_hE;
                                e_node=e_node->next_hE;
                                break;
                            }
                            e_node=e_node->twin_hE;
                        }

                        while (true)
                        {
                            if (e_node->target_v->index == (*sTlIt)->parentN->index)
                            {
                                break;
                            }
                            treeList[searchNode(e_node->target_v->index, treeList)].parentN = &treeList[searchNode((*sTlIt)->index,treeList)];
                            (*sTlIt)->childrenN.push_back(&treeList[searchNode(e_node->target_v->index, treeList)]);

                            e_node=e_node->twin_hE;
                            e_node=e_node->next_hE;
                        }

                        if ((*sTlIt)->childrenN.empty())
                        {
                            (*sTlIt)->isLeaf = true;
                        }
                        else
                        {
                            subTlist_p.insert(subTlist_p.end(), (*sTlIt)->childrenN.begin(), (*sTlIt)->childrenN.end());
                        }



                    }
                }
                subTlist.insert(subTlist.end(), subTlist_p.begin(), subTlist_p.end());
                subTlist_p.clear();
                if (expandFin == true)
                {
                    subTlist.clear();
                    break;
                }
            }
        }



    }

    labelIden();
    for (vector<nodes>::iterator tLit = treeList.begin(); tLit != treeList.end(); ++tLit)
    {
        cout << "NodeIndex: " << (*tLit).index << endl;
        if ((*tLit).parentN == nullptr)
        {
            cout << " isLeaf: " << (*tLit).isLeaf << endl;
        }
        else
        {
            cout << "ParentNode: " << (*tLit).parentN->index<<" isLeaf: "<<(*tLit).isLeaf << endl;


        }
        if (!(*tLit).isLeaf)
        {
            cout << "ChindNodes: ";
            for (vector<nodes*>::iterator cTit = (*tLit).childrenN.begin(); cTit != (*tLit).childrenN.end(); ++cTit)
            {
                cout << (*cTit)->index << " ";
            }
            cout << endl;
        }
        cout << "Label: " << (*tLit).label << endl;
        cout << "-----------------------------------------" << endl;

    }
    /*
    for (vector<nodes*>::iterator sRit = subRootN.begin(); sRit != subRootN.end(); ++sRit)
    {
        cout << (*sRit)->index << endl;
        for (vector<nodes*>::iterator i=(*sRit)->childrenN.begin();i!= (*sRit)->childrenN.end();++i)
        {
            cout << (*i)->index << " " << endl;
        }
        cout <<"==================="<< endl;
    }
    */


    return 0;


}

int PlaneGraph::treeTransfer_MutiRoot()
{
    //Build basic tree struct
    for (vector<vertices>::iterator vLit = verList_tree.begin(); vLit != verList_tree.end(); ++vLit)
    {
        nodes n = { (*vLit).index };
        treeList.push_back(n);
    }
    for (vector<vertices>::iterator ePit = endpointList.begin(); ePit != endpointList.end(); ++ePit)
    {
        nodes n;
        n.index = (*ePit).index;
        treeList.push_back(n);
    }
    for (vector<vertices>::iterator ePit = endpointList.begin(); ePit != endpointList.end(); ++ePit)
    {
        treeList[searchNode((*ePit).index, treeList)].oriN = &treeList[searchNode((*ePit).oriV->index, treeList)];
    }

    //Dealing topological centroid




    /*
    if (topCenE != nullptr)
    {
        cout << "=========================Result of " << topCenE->target_v->index << " as ROOT=========================" << endl;
        subRootN.push_back(&treeList[searchNode(topCenE->target_v->index, treeList)]);
        subRootSearch();
        APTEDformTrans_MutiRoot();

        //Clear and start over for the other root.
        subRootN.clear();
        treeList.clear();

        //Rebuild basic tree struct.
        for (vector<vertices>::iterator vLit = verList_tree.begin(); vLit != verList_tree.end(); ++vLit)
        {
            nodes n = { (*vLit).index };
            treeList.push_back(n);
        }
        for (vector<vertices>::iterator ePit = endpointList.begin(); ePit != endpointList.end(); ++ePit)
        {
            nodes n;
            n.index = (*ePit).index;
            treeList.push_back(n);
        }
        for (vector<vertices>::iterator ePit = endpointList.begin(); ePit != endpointList.end(); ++ePit)
        {
            treeList[searchNode((*ePit).index, treeList)].oriN = &treeList[searchNode((*ePit).oriV->index, treeList)];
        }


        cout << "=========================Result of " << topCenE->twin_hE->target_v->index << " as ROOT=========================" << endl;
        subRootN.push_back(&treeList[searchNode(topCenE->twin_hE->target_v->index, treeList)]);
        subRootSearch();

        APTEDformTrans_MutiRoot();
    }
    else if (topCenF != nullptr)
    {

    }
    else
    {
        cout << "============================Topological Centroid is error============================" << endl;
    }
    */




    return 0;

}

int PlaneGraph::CanFormCom()
{
    if (topCenE != nullptr)
    {

    }

    else if (topCenF != nullptr)
    {

    }

    else if (topCenV != nullptr)
    {
        for (vector<halfEdges>::iterator iEit = edgeList_ori.begin(); iEit != edgeList_ori.end(); ++iEit)
        {
            if ((*iEit).target_v->index == topCenV->index)
            {

            }
        }
    }


    return 0;
}


/*Assistant method*/
vector<halfEdges*> PlaneGraph::innerEforF(faces* f)//Find all inner edges for a face.
{
    vector<halfEdges*> innerE;
    halfEdges *e = f->arbitarary_hE;
    while (true)
    {
        innerE.push_back(e);
        e = e->next_hE;
        for (vector<halfEdges*>::iterator iEit=innerE.begin();iEit!=innerE.end();++iEit)
        {
            if (e->index == (*iEit)->index)
            {
                return innerE;
            }
        }
    }
}
vector<halfEdges*> PlaneGraph::outterEforF(faces* f)
{
    vector<halfEdges*> innerE;
    vector<halfEdges*> outterE;
    halfEdges *e = f->arbitarary_hE;
    while (true)
    {
        innerE.push_back(e);
        if (e->twin_hE->incident_f->index != f->index)
        {
            outterE.push_back(e->twin_hE);
        }
        e = e->next_hE;
        for (vector<halfEdges*>::iterator iEit = innerE.begin(); iEit != innerE.end(); ++iEit)
        {
            if (e->index == (*iEit)->index)
            {
                return outterE;
            }
        }
    }
}
vector<halfEdges*> PlaneGraph::outterEforE(vector<halfEdges*> e)
{
    vector<halfEdges*> eTem;
    int count = 0;
    while (true)
    {
        for (vector<halfEdges*>::iterator eIt = e.begin(); eIt != e.end(); ++eIt)
        {
            //cout << (*eIt)->index << " ";
            vector<halfEdges*>::iterator twinIt;
            for (twinIt = e.begin(); twinIt != e.end(); ++twinIt)
            {
                if ((*twinIt)->index == (*eIt)->twin_hE->index)
                {
                    break;
                }
            }

            if (twinIt == e.end())
            {
                eTem.push_back((*eIt)->twin_hE);
                count++;
            }

            vector<halfEdges*>::iterator prevIt;
            for (prevIt = e.begin(); prevIt != e.end(); ++prevIt)
            {
                if (eIt==e.begin() || (*prevIt)->index == (*eIt)->prev_hE->index)
                {
                    break;
                }
            }
            if (prevIt == e.end())
            {
                eTem.push_back((*eIt)->prev_hE);
                count++;
            }

        }
        //cout << endl;
        //break condision
        if (count == 0)
        {
            break;
        }
        //count reset
        count = 0;

        //Merge the vectors.
        e.insert(e.end(),eTem.begin(), eTem.end());
        eTem.clear();
    }

    return e;

}
bool PlaneGraph::isConnected(vector<halfEdges*> edges)
{
    int count = edges.size();
    for (vector<halfEdges*>::iterator eIt1=edges.begin();eIt1!=edges.end();++eIt1)
    {
        for (vector<halfEdges*>::iterator eIt2 = edges.begin(); eIt2 != edges.end(); ++eIt2)
        {
            if ((*eIt1)->next_hE->index == (*eIt2)->index)
            {
                count--;
                break;
            }
        }
    }

    if (count <= 1)
    {
        return true;
    }
    else
    {
        return false;
    }
}
int PlaneGraph::endEdge(vector<halfEdges*> edges)
{
    for (vector<halfEdges*>::iterator eIt1 = edges.begin(); eIt1 != edges.end(); ++eIt1)
    {
        vector<halfEdges*>::iterator eIt2;
        for (eIt2 = edges.begin(); eIt2 != edges.end(); ++eIt2)
        {
            if ((*eIt1)->next_hE->index == (*eIt2)->index)
            {
                break;
            }
        }
        if (eIt2 == edges.end())
        {
            return (*eIt1)->index;
        }
    }
}
vector<vertices*> PlaneGraph::nodeForF(faces* f)
{
    vector<vertices*> nodes;
    vector<halfEdges*> innerE = innerEforF(f);
    for (vector<halfEdges*>::iterator iEit = innerE.begin(); iEit != innerE.end(); ++iEit)
    {
        if ((*iEit)->next_hE->twin_hE->index != (*iEit)->twin_hE->prev_hE->index)
        {
            nodes.push_back((*iEit)->target_v);
            //cout << (*iEit)->index << " " << (*iEit)->next_hE->twin_hE->index << " " << (*iEit)->twin_hE->prev_hE->index << " " << (*iEit)->target_v->index << endl;
        }
    }
    return nodes;
}
vector<vertices*> PlaneGraph::nodeForE(halfEdges* e)
{
    vector<vertices*> nodes;
    /*
    if (e->next_hE->twin_hE->index == e->twin_hE->prev_hE->index)
    {
        nodes.push_back(e->target_v);
    }
    if (e->prev_hE->twin_hE->index == e->twin_hE->next_hE->index)
    {
        nodes.push_back(e->twin_hE->target_v);
    }
    */
    if (e->next_hE->index != e->twin_hE->index)
    {
        nodes.push_back(e->target_v);
    }
    else
    {
        nodes.push_back(e->twin_hE->target_v);
    }
    return nodes;
}
int PlaneGraph::searchNode(int index, vector<nodes> nList)
{
    for (int i=0;i<nList.size();i++)
    {
        if (nList[i].index == index)
        {
            return i;
        }
    }
}
nodes* PlaneGraph::nextNodeOfP(nodes* n)
{
    for (vector<nodes*>::iterator nPit = (n->parentN->childrenN.begin()); nPit != n->parentN->childrenN.end(); ++nPit)
    {
        if ((*nPit)->index == n->index)
        {
            ++nPit;
            if ((nPit) != n->parentN->childrenN.end())
            {
                return (*nPit);
            }
            else
            {
                return nullptr;
            }
        }
    }
}
int PlaneGraph::subRootSearch()
{
    for (vector<nodes*>::iterator sRit = subRootN.begin(); sRit != subRootN.end(); ++sRit)
    {
        //Parents node for subtree searching
        vertices* v = nullptr;
        for (vector<vertices>::iterator vLtIt = verList_tree.begin(); vLtIt != verList_tree.end(); ++vLtIt)
        {
            if ((*vLtIt).index == (*sRit)->index)
            {
                v = &(*vLtIt);
                break;
            }
        }
        halfEdges* e = v->incident_hE;
        halfEdges* e_ori = v->incident_hE;
        while (true)
        {
            e = e->next_hE;
            vector<nodes*>::iterator cNit;
            for (cNit = (*sRit)->childrenN.begin(); cNit != (*sRit)->childrenN.end(); ++cNit)
            {
                if (e->target_v->index == (*cNit)->index)
                {
                    break;
                }
            }
            if (cNit != (*sRit)->childrenN.end())
            {
                break;
            }


            vector<nodes*>::iterator sRitv1;
            for (sRitv1 = subRootN.begin(); sRitv1 != subRootN.end(); ++sRitv1)
            {
                if ((*sRitv1)->index == e->target_v->index)
                {
                    break;
                }
            }
            if (sRitv1 == subRootN.end())
            {
                (*sRit)->childrenN.push_back(&treeList[searchNode(e->target_v->index, treeList)]);
                treeList[searchNode(e->target_v->index, treeList)].parentN = &treeList[searchNode((*sRit)->index, treeList)];
            }
            e = e->twin_hE;
            if (e->index == e_ori->index)
            {
                break;
            }

        }
        //Parents node for subtree searching is end

        if ((*sRit)->childrenN.empty())
        {
            (*sRit)->isLeaf = 1;
        }

        for (vector<nodes*>::iterator cNit = (*sRit)->childrenN.begin(); cNit != (*sRit)->childrenN.end(); ++cNit)
        {
            vector<nodes*> subTlist;
            subTlist.push_back(*cNit);
            vector<nodes*> subTlist_p;
            for (vector<nodes*>::iterator cNcNit = (*cNit)->childrenN.begin(); cNcNit != (*cNit)->childrenN.end(); ++cNcNit)
            {
                vector<nodes*>::iterator sRitv1;
                for (sRitv1 = subRootN.begin(); sRitv1 != subRootN.end(); ++sRitv1)
                {
                    if ((*sRitv1)->index == (*cNcNit)->index)
                    {
                        break;
                    }
                }
                if (sRitv1 == subRootN.end())
                {
                    subTlist.push_back((*cNcNit));
                }
            }
            while (true)
            {
                bool expandFin = true;
                vector<nodes*>::iterator sTlIt;
                for (sTlIt = subTlist.begin(); sTlIt != subTlist.end(); ++sTlIt)
                {
                    if ((*sTlIt)->childrenN.empty() && !(*sTlIt)->isLeaf && (*sTlIt)->parentN != nullptr)
                    {
                        expandFin = false;

                        vertices* v_node = nullptr;
                        for (vector<vertices>::iterator vLtIt = verList_tree.begin(); vLtIt != verList_tree.end(); ++vLtIt)
                        {
                            if ((*vLtIt).index == (*sTlIt)->index)
                            {
                                v_node = &(*vLtIt);
                                break;
                            }
                        }
                        if (v_node == nullptr)
                        {
                            for (vector<vertices>::iterator ePit = endpointList.begin(); ePit != endpointList.end(); ++ePit)
                            {
                                if ((*ePit).index == (*sTlIt)->index)
                                {
                                    v_node = &(*ePit);
                                    break;
                                }
                            }
                        }

                        halfEdges* e_node = v_node->incident_hE;

                        while (true)
                        {
                            e_node = e_node->next_hE;
                            if (e_node->target_v->index == (*sTlIt)->parentN->index)
                            {
                                e_node = e_node->twin_hE;
                                e_node = e_node->next_hE;
                                break;
                            }
                            e_node = e_node->twin_hE;
                        }

                        while (true)
                        {
                            if (e_node->target_v->index == (*sTlIt)->parentN->index)
                            {
                                break;
                            }
                            treeList[searchNode(e_node->target_v->index, treeList)].parentN = &treeList[searchNode((*sTlIt)->index, treeList)];
                            (*sTlIt)->childrenN.push_back(&treeList[searchNode(e_node->target_v->index, treeList)]);

                            e_node = e_node->twin_hE;
                            e_node = e_node->next_hE;
                        }

                        if ((*sTlIt)->childrenN.empty())
                        {
                            (*sTlIt)->isLeaf = true;
                        }
                        else
                        {
                            subTlist_p.insert(subTlist_p.end(), (*sTlIt)->childrenN.begin(), (*sTlIt)->childrenN.end());
                        }



                    }
                }
                subTlist.insert(subTlist.end(), subTlist_p.begin(), subTlist_p.end());
                subTlist_p.clear();
                if (expandFin == true)
                {
                    subTlist.clear();
                    break;
                }
            }
        }
    }

    labelIden();
    for (vector<nodes>::iterator tLit = treeList.begin(); tLit != treeList.end(); ++tLit)
    {
        cout << "NodeIndex: " << (*tLit).index << endl;
        if ((*tLit).parentN == nullptr)
        {
            cout << " isLeaf: " << (*tLit).isLeaf << endl;
        }
        else
        {
            cout << "ParentNode: " << (*tLit).parentN->index << " isLeaf: " << (*tLit).isLeaf << endl;


        }
        if (!(*tLit).isLeaf)
        {
            cout << "ChindNodes: ";
            for (vector<nodes*>::iterator cTit = (*tLit).childrenN.begin(); cTit != (*tLit).childrenN.end(); ++cTit)
            {
                cout << (*cTit)->index << " ";
            }
            cout << endl;
        }
        cout << "Label: " << (*tLit).label << endl;
        cout << "-----------------------------------------" << endl;

    }

    return 0;
}

/*Add and Remove*/
int PlaneGraph::removeEdge(int index) //Remove the relationship for a half-edge and its twin half-edge.
{
    if (index == -604)
    {
        return 0;
    }

    int n = searchEdge(index);

    if (n == -427)
    {
        return 0;
    }

    int tIndex = edgeList[n].twin_hE->index;

    //face relationship
    faces &f = *this->edgeList[n].incident_f;
    faces &twinf = *this->edgeList[n].twin_hE->incident_f;
    if (f.index != twinf.index)
    {
        if (twinf.index != outerFace->index)
        {
            vector<halfEdges*> inEforF = innerEforF(&twinf);
            for (vector<halfEdges*>::iterator iEit=inEforF.begin();iEit!=inEforF.end();++iEit)
            {
                (*iEit)->incident_f = &f;
            }

            //delete the face from list.
            for (vector<faces>::iterator fLit = faceList.begin(); fLit != faceList.end(); ++fLit)
            {
                if ((*fLit).index == twinf.index)
                {
                    *fLit = { -604 };
                    break;
                }
            }

        }
        else
        {
            vector<halfEdges*> inEforF = innerEforF(&f);
            for (vector<halfEdges*>::iterator iEit = inEforF.begin(); iEit != inEforF.end(); ++iEit)
            {

                (*iEit)->incident_f = &twinf;
            }
            //delete the face from list.
            for (vector<faces>::iterator fLit = faceList.begin(); fLit != faceList.end(); ++fLit)
            {
                if ((*fLit).index == f.index)
                {
                    //fLit = faceList.erase(fLit);
                    *fLit = { -604 };
                    break;
                }
            }
        }

    }

    //half-edge relationship

    this->edgeList[n].prev_hE->next_hE = this->edgeList[n].twin_hE->next_hE;
    this->edgeList[n].twin_hE->next_hE->prev_hE = this->edgeList[n].prev_hE;

    this->edgeList[n].next_hE->prev_hE = this->edgeList[n].twin_hE->prev_hE;
    this->edgeList[n].twin_hE->prev_hE->next_hE = this->edgeList[n].next_hE;







    //veticle relationship
    if (edgeList[n].target_v->incident_hE->index == edgeList[n].index)
    {
        if (edgeList[n].index == edgeList[n].twin_hE->prev_hE->index)//If the half-edge's twin half-edge's pre-half-edge is itself, the vertices between them is the single vertices which can be remove with edges.
        {
            for (vector<vertices>::iterator vLit = verList.begin(); vLit != verList.end(); ++vLit)
            {
                if ((*vLit).index == edgeList[n].target_v->index)
                {
                    *vLit = { -604 };
                    break;
                }
            }
        }
        else
        {
            edgeList[n].target_v->incident_hE = edgeList[n].twin_hE->prev_hE;
        }

    }

    if (edgeList[n].twin_hE->target_v->incident_hE->index == edgeList[n].twin_hE->index)
    {
        if (edgeList[n].twin_hE->index == edgeList[n].prev_hE->index)//If the half-edge's twin half-edge's pre-half-edge is itself, the vertices between them is the single vertices which can be remove with edges.
        {
            for (vector<vertices>::iterator vLit = verList.begin(); vLit != verList.end(); ++vLit)
            {
                if ((*vLit).index == edgeList[n].twin_hE->target_v->index)
                {
                    //vLit = verList.erase(vLit);
                    *vLit = { -604 };
                    break;
                }
            }
        }
        else
        {
            edgeList[n].twin_hE->target_v->incident_hE = edgeList[n].prev_hE;
        }
    }


    //delete the half-edge and its twin edge from list.
    for (vector<halfEdges>::iterator eLit = edgeList.begin(); eLit != edgeList.end(); ++eLit)
    {
        if ((*eLit).index == index|| (*eLit).index == tIndex)
        {
            cout << "Remove the No." << (*eLit).index << " from the edgelist." <<endl;
            //eLit = edgeList.erase(eLit);
            *eLit = {-604};
        }
    }


    return 0;
}
int PlaneGraph::removeFace(int index)
{
    if (index == -604)
    {
        return 0;
    }

    int n = searchFace(index);

    if (n == -427)
    {
        return 0;
    }
    vector<halfEdges*> innerE = innerEforF(&faceList[n]);
    for (vector<halfEdges*>::iterator iEit = innerE.begin(); iEit != innerE.end(); ++iEit)
    {
        //cout << (*iEit)->index << endl;
        removeEdge((*iEit)->index);
    }

    return 0;
}
int PlaneGraph::disconnectE(int index)
{
    int n = searchEdge(index);
    vertices dupV = { endpointList.size()+1000001,&edgeList_tree[n] ,edgeList_tree[n].target_v };

    this->endpointList.push_back(dupV);



    //Face relationship
    faces* f = this->edgeList_tree[n].incident_f;
    faces* twinf = this->edgeList_tree[n].twin_hE->incident_f;
    if (f->index != twinf->index)
    {
        if (twinf->index != outerFace->index)
        {
            vector<halfEdges*> inEforF = innerEforF(twinf);
            for (vector<halfEdges*>::iterator iEit = inEforF.begin(); iEit != inEforF.end(); ++iEit)
            {
                (*iEit)->incident_f = f;
            }

            //delete the face from list.
            for (vector<faces>::iterator fLit = faceList_tree.begin(); fLit != faceList_tree.end(); ++fLit)
            {
                if ((*fLit).index == twinf->index)
                {
                    *fLit = { -604 };
                    break;
                }
            }

        }
        else
        {
            vector<halfEdges*> inEforF = innerEforF(f);
            for (vector<halfEdges*>::iterator iEit = inEforF.begin(); iEit != inEforF.end(); ++iEit)
            {

                (*iEit)->incident_f = twinf;
            }
            //delete the face from list.
            for (vector<faces>::iterator fLit = faceList_tree.begin(); fLit != faceList_tree.end(); ++fLit)
            {
                if ((*fLit).index == f->index)
                {
                    //fLit = faceList.erase(fLit);
                    *fLit = { -604 };
                    break;
                }
            }
        }

    }
    else
    {
        cout << "!=!=!=!=!=!=!=!=! disconnectedEdge Face merge Error !=!=!=!=!=!=!=!=!" << endl;
    }

    //vertices relationship
    if (edgeList_tree[n].target_v->incident_hE->index == edgeList_tree[n].index)
    {
        edgeList_tree[n].target_v->incident_hE = edgeList_tree[n].twin_hE->prev_hE;
    }
    //this->edgeList_tree[n].target_v = &(*(endpointList.back()));
    this->edgeList_tree[n].target_v = nullptr;
    vector<int> rel = { edgeList_tree[n].index,endpointList.back().index };
    endpointRel.push_back(rel);

    //half-edge relationship
    edgeList_tree[n].next_hE->prev_hE = edgeList_tree[n].twin_hE->prev_hE;
    edgeList_tree[n].twin_hE->prev_hE->next_hE = edgeList_tree[n].next_hE;

    edgeList_tree[n].next_hE = edgeList_tree[n].twin_hE;
    edgeList_tree[n].twin_hE->prev_hE = &edgeList_tree[n];
    return 0;
}

/*Setting*/
int PlaneGraph::listVisible(bool sta)
{
    if (sta == true)
    {
        cout << "list is visible when checking lists." << endl;
    }
    else
    {
        cout << "list is invisible when checking lists" << endl;
    }

    this->listVis == sta;

    return 0;
}

/*-------Testing--------*/
bool PlaneGraph::seFaceTesting(vector<int> tList)
{
    return true;
}

bool PlaneGraph::seEdgeTesting(vector<int> tList)
{

    return true;
}


/*Transfer forms*/
int PlaneGraph::labelIden()
{
    for (vector<nodes>::iterator tLit = treeList.begin(); tLit != treeList.end(); ++tLit)
    {
        if ((*tLit).oriN == nullptr)
        {
            switch ((*tLit).index/100000)
            {
                case 1:
                    (*tLit).label = 'A';
                    break;
                case 2:
                    (*tLit).label = 'U';
                    break;
                case 3:
                    (*tLit).label = 'G';
                    break;
                case 4:
                    (*tLit).label = 'C';
                    break;
                case 5:
                    (*tLit).label = 'T';
                    break;
                case 6:
                    (*tLit).label = 'X';
                    break;
                case 7:
                    (*tLit).label = 'Y';
                    break;
                default:
                    break;
            }
        }
        else
        {
            switch ((*tLit).oriN->index / 100000)
            {
                case 1:
                    (*tLit).label = 'A';
                    break;
                case 2:
                    (*tLit).label = 'U';
                    break;
                case 3:
                    (*tLit).label = 'G';
                    break;
                case 4:
                    (*tLit).label = 'C';
                    break;
                case 5:
                    (*tLit).label = 'T';
                    break;
                case 6:
                    (*tLit).label = 'X';
                    break;
                case 7:
                    (*tLit).label = 'Y';
                default:
                    break;
            }
        }
        //cout << (*tLit).index << " " << (*tLit).index /10000<< (*tLit).label << endl;
    }
    return 0;
}

int PlaneGraph::labelIden_sub(vector<nodes> tList)
{
    for (vector<nodes>::iterator tLit = tList.begin(); tLit != tList.end(); ++tLit)
    {
        if ((*tLit).oriN == nullptr)
        {
            switch ((*tLit).index / 100000)
            {
                case 1:
                    (*tLit).label = 'A';
                    break;
                case 2:
                    (*tLit).label = 'U';
                    break;
                case 3:
                    (*tLit).label = 'G';
                    break;
                case 4:
                    (*tLit).label = 'C';
                    break;
                case 5:
                    (*tLit).label = 'T';
                    break;
                case 6:
                    (*tLit).label = 'X';
                    break;
                case 7:
                    (*tLit).label = 'Y';
                    break;
                default:
                    break;
            }
        }
        else
        {
            switch ((*tLit).oriN->index / 100000)
            {
                case 1:
                    (*tLit).label = 'A';
                    break;
                case 2:
                    (*tLit).label = 'U';
                    break;
                case 3:
                    (*tLit).label = 'G';
                    break;
                case 4:
                    (*tLit).label = 'C';
                    break;
                case 5:
                    (*tLit).label = 'T';
                    break;
                case 6:
                    (*tLit).label = 'X';
                    break;
                case 7:
                    (*tLit).label = 'Y';
                default:
                    break;
            }
        }
    }
    return 0;
}

int PlaneGraph::APTEDformTrans()
{
    _mkdir("tree_result_inPsudoVer");
    ofstream treeString("./tree_result_inPsudoVer/" + this->graphName+".txt");// + "_treeString.txt");
    cout << "Tree transfer to string form:" << endl;


    if (topCenE != nullptr)
    {
        treeString << "{E";
        cout << "{E";
    }
    else if (topCenF != nullptr)
    {
        treeString << "{F";
        cout << "{F";
    }
    else if (topCenV != nullptr)
    {
        treeString << "{V";
        cout << "{V";
    }
    else
    {
        cout << "============================Topological Centroid is error============================" << endl;
    }


    nodes* n;
    nodes* n_p;
    for (vector<nodes*>::iterator tLit = subRootN.begin(); tLit != subRootN.end(); ++tLit)
    {
        n = (*tLit);
        bool loopStop = false;
        while (true)
        {
            treeString << "{" + n->label;
            cout << "{" + n->label;
            if (n->isLeaf)
            {
                treeString << "}";
                cout << "}";
                if (n->index == (*tLit)->index)
                {
                    break;
                }
                while (true)
                {
                    n_p = nextNodeOfP(n);
                    if (n_p != nullptr)
                    {
                        n = n_p;
                        break;
                    }
                    else
                    {
                        treeString << "}";
                        cout << "}";
                        n = n->parentN;
                        if (n->index == (*tLit)->index)
                        {
                            loopStop = true;
                            break;
                        }
                    }

                }
            }
            else
            {
                n = n->childrenN[0];
            }
            if (loopStop)
            {
                break;
            }
        }
    }
    treeString << "}";
    cout << "}" << endl;
    treeString.close();
    return 0;
}

int PlaneGraph::APTEDformTrans_MutiRoot()
{
    //Creat folder
    string folderPath = "tree_result_MutiRoot";
    _mkdir((folderPath).c_str());
    _mkdir(("./" + folderPath + "/" + this->graphName).c_str());

    for (int i = 0; i < subRootN.size(); i++)
    {
        ofstream treeString(folderPath + this->graphName + "/" + to_string(i+1)  + ".txt");// + "_treeString.txt");
        cout << "Tree transfer to string form: No" + to_string(i+1)<<" of "<<this->graphName << endl;

        //Let one of nodes be a root.

        bool isLeaf = false;

        if (subRootN[i]->isLeaf == true)
        {
            //Save the original type.
            isLeaf = true;
        }

        for (int j = 0; j < subRootN.size(); j++)
        {
            if (i == j)
            {
                for (int k = 0; k < subRootN.size(); k++)
                {
                    if (i != k)
                    {
                        subRootN[i]->childrenN.push_back(subRootN[k]);
                        if (subRootN[i]->isLeaf = true)
                        {
                            subRootN[i]->isLeaf = false;
                        }
                    }
                }
            }
            else
            {
                subRootN[j]->parentN = subRootN[i];
            }
        }

        nodes* n;
        nodes* n_p;
        n = subRootN[i];
        bool loopStop = false;
        int outputCount = 0;
        while (true)
        {
            treeString << "{" + n->label;
            outputCount++;
            cout << "{" + n->label;
            if (n->isLeaf)
            {
                treeString << "}";
                cout << "}";
                if (n->index == subRootN[i]->index)
                {
                    break;
                }
                while (true)
                {
                    n_p = nextNodeOfP(n);
                    if (n_p != nullptr)
                    {
                        n = n_p;
                        break;
                    }
                    else
                    {
                        treeString << "}";
                        cout << "}";
                        n = n->parentN;
                        if (n->index == subRootN[i]->index)
                        {
                            loopStop = true;
                            break;
                        }
                    }

                }
            }
            else
            {
                n = n->childrenN[0];
            }
            if (loopStop)
            {
                break;
            }
        }



        treeString.close();

        if (outputCount != (verList.size()+endpointList.size()))
        {
            cout << "----------------------Output result error----------------------" << endl;
            cout << "Output amount is " << outputCount << endl;
            cout << "The Base amout is " << verList.size()+endpointList.size();
            cout << endl;
        }

        //recover list

        for (vector<nodes*>::iterator tLit = subRootN.begin(); tLit != subRootN.end(); ++tLit)
        {
            (*tLit)->parentN = nullptr;
        }

        if (isLeaf)
        {
            subRootN[i]->childrenN.clear();
        }
        else
        {
            for (vector<nodes*>::iterator cLit = subRootN[i]->childrenN.begin(); cLit != subRootN[i]->childrenN.end();)
            {
                vector<nodes*>::iterator tLit2;
                for (tLit2 = subRootN.begin(); tLit2 != subRootN.end(); ++tLit2)
                {
                    if ((*cLit)->index == (*tLit2)->index)
                    {
                        break;
                    }
                }

                if (tLit2 == subRootN.end())
                {
                    cLit++;
                }
                else
                {
                    if (cLit + 1 == subRootN[i]->childrenN.end())
                    {
                        subRootN[i]->childrenN.erase(cLit);
                        break;
                    }
                    else
                    {
                        subRootN[i]->childrenN.erase(cLit);
                    }

                }
            }
        }

        if (subRootN[i]->childrenN.size() == 0)
        {
            subRootN[i]->isLeaf = true;
        }

    }





    return 0;

}

int PlaneGraph::APTEDformTrans_AllVerAsRoot()
{
    _mkdir("tree_result_allVerAsRoot");
    string folderPath = "./tree_result_allVerAsRoot/" + this->graphName;
    _mkdir(folderPath.c_str());
    string patternFile;

    if (topCenF != nullptr)
    {
        int n = searchEdge(topCenF->arbitarary_hE->index);
        vertices dupV = { endpointList.size() + 1000001,&edgeList_tree[n] ,edgeList_tree[n].target_v };
        this->endpointList.push_back(dupV);

        edgeList_tree[n].target_v->incident_hE = edgeList_tree[n].next_hE->twin_hE;
        edgeList_tree[n].target_v = &endpointList.back();

        edgeList_tree[n].next_hE->prev_hE = edgeList_tree[n].twin_hE->prev_hE;
        edgeList_tree[n].twin_hE->prev_hE->next_hE = edgeList_tree[n].next_hE;
        edgeList_tree[n].next_hE = edgeList_tree[n].twin_hE;
        edgeList_tree[n].twin_hE->prev_hE = &edgeList_tree[n];

        //show result.
        if (false)
        {
            checkEdge();

            for (vector<halfEdges>::iterator eLit = edgeList_tree.begin(); eLit != edgeList_tree.end(); ++eLit)
            {
                if ((*eLit).target_v == nullptr)
                {
                    for (vector<vector<int>>::iterator epRit = endpointRel.begin(); epRit != endpointRel.end(); ++epRit)
                    {
                        if ((*eLit).index == (*epRit)[0])
                        {
                            for (vector<vertices>::iterator epIt = endpointList.begin(); epIt != endpointList.end(); ++epIt)
                            {
                                if ((*epIt).index == (*epRit)[1])
                                {
                                    (*eLit).target_v = &(*epIt);
                                }
                            }
                        }
                    }
                }
                if ((*eLit).target_v->oriV == nullptr)
                {
                    cout << "eIndex: " << (*eLit).index << " incF: " << (*eLit).incident_f->index << " tarV: " << (*eLit).target_v->index << " twinE:" << (*eLit).twin_hE->index << " prevE:" << (*eLit).prev_hE->index << " nextE: " << (*eLit).next_hE->index << endl;
                }
                else
                {
                    cout << "eIndex: " << (*eLit).index << " incF: " << (*eLit).incident_f->index << " newTarV: " << (*eLit).target_v->index << " oriV:" << (*eLit).target_v->oriV->index << " twinE:" << (*eLit).twin_hE->index << " prevE:" << (*eLit).prev_hE->index << " nextE: " << (*eLit).next_hE->index << endl;
                }

            }
        }



    }

    //Build basic tree structure
    vector<nodes> subTreeList;
    for (vector<vertices>::iterator vLit = verList_tree.begin(); vLit != verList_tree.end(); ++vLit)
    {
        nodes n = { (*vLit).index };
        subTreeList.push_back(n);
    }
    for (vector<vertices>::iterator ePit = endpointList.begin(); ePit != endpointList.end(); ++ePit)
    {
        nodes n;
        n.index = (*ePit).index;
        subTreeList.push_back(n);
    }
    for (vector<vertices>::iterator ePit = endpointList.begin(); ePit != endpointList.end(); ++ePit)
    {
        subTreeList[searchNode((*ePit).index, subTreeList)].oriN = &subTreeList[searchNode((*ePit).oriV->index, subTreeList)];
    }


    for (vector<vertices>::iterator vLitR = verList_tree.begin(); vLitR != verList_tree.end(); ++vLitR)
    {
        //rebuilt tree nodes relationship letting this vertex as root.
        //Parents node for subtree searching
        nodes* sRit = &subTreeList[searchNode((*vLitR).index, subTreeList)];
        vertices* v = &(*vLitR);

        halfEdges* e = v->incident_hE;
        halfEdges* e_ori = v->incident_hE;
        while (true)
        {
            e = e->next_hE;
            vector<nodes*>::iterator cNit;
            for (cNit = (sRit)->childrenN.begin(); cNit != (sRit)->childrenN.end(); ++cNit)
            {
                if (e->target_v->index == (*cNit)->index)
                {
                    break;
                }
            }
            if (cNit != (sRit)->childrenN.end())
            {
                break;
            }

            /*
            vector<nodes*>::iterator sRitv1;
            for (sRitv1 = subRootN.begin(); sRitv1 != subRootN.end(); ++sRitv1)
            {
                if ((*sRitv1)->index == e->target_v->index)
                {
                    break;
                }
            }
            */
            if (e->target_v->index != (*vLitR).index)
            {
                (sRit)->childrenN.push_back(&subTreeList[searchNode(e->target_v->index, subTreeList)]);
                subTreeList[searchNode(e->target_v->index, subTreeList)].parentN = &subTreeList[searchNode((sRit)->index, subTreeList)];
            }
            e = e->twin_hE;
            if (e->index == e_ori->index)
            {
                break;
            }

        }
        //Parents node for subtree searching is end


        for (vector<nodes*>::iterator cNit = (sRit)->childrenN.begin(); cNit != (sRit)->childrenN.end(); ++cNit)
        {
            vector<nodes*> subTlist;
            subTlist.push_back(*cNit);
            vector<nodes*> subTlist_p;
            for (vector<nodes*>::iterator cNcNit = (*cNit)->childrenN.begin(); cNcNit != (*cNit)->childrenN.end(); ++cNcNit)
            {
                vector<nodes*>::iterator sRitv1;
                for (sRitv1 = subRootN.begin(); sRitv1 != subRootN.end(); ++sRitv1)
                {
                    if ((*sRitv1)->index == (*cNcNit)->index)
                    {
                        break;
                    }
                }
                if (sRitv1 == subRootN.end())
                {
                    subTlist.push_back((*cNcNit));
                }
            }
            while (true)
            {
                bool expandFin = true;
                vector<nodes*>::iterator sTlIt;
                for (sTlIt = subTlist.begin(); sTlIt != subTlist.end(); ++sTlIt)
                {
                    if ((*sTlIt)->childrenN.empty() && !(*sTlIt)->isLeaf && (*sTlIt)->parentN != nullptr)
                    {
                        expandFin = false;

                        vertices* v_node = nullptr;
                        for (vector<vertices>::iterator vLtIt = verList_tree.begin(); vLtIt != verList_tree.end(); ++vLtIt)
                        {
                            if ((*vLtIt).index == (*sTlIt)->index)
                            {
                                v_node = &(*vLtIt);
                                break;
                            }
                        }
                        if (v_node == nullptr)
                        {
                            for (vector<vertices>::iterator ePit = endpointList.begin(); ePit != endpointList.end(); ++ePit)
                            {
                                if ((*ePit).index == (*sTlIt)->index)
                                {
                                    v_node = &(*ePit);
                                    break;
                                }
                            }
                        }

                        halfEdges* e_node = v_node->incident_hE;

                        while (true)
                        {
                            e_node = e_node->next_hE;
                            if (e_node->target_v->index == (*sTlIt)->parentN->index)
                            {
                                e_node = e_node->twin_hE;
                                e_node = e_node->next_hE;
                                break;
                            }
                            e_node = e_node->twin_hE;
                        }

                        while (true)
                        {
                            if (e_node->target_v->index == (*sTlIt)->parentN->index)
                            {
                                break;
                            }
                            //cout << e->index << endl;
                            subTreeList[searchNode(e_node->target_v->index, subTreeList)].parentN = &subTreeList[searchNode((*sTlIt)->index, subTreeList)];
                            (*sTlIt)->childrenN.push_back(&subTreeList[searchNode(e_node->target_v->index, subTreeList)]);

                            e_node = e_node->twin_hE;
                            e_node = e_node->next_hE;
                        }

                        if ((*sTlIt)->childrenN.empty())
                        {
                            (*sTlIt)->isLeaf = true;
                        }
                        else
                        {
                            subTlist_p.insert(subTlist_p.end(), (*sTlIt)->childrenN.begin(), (*sTlIt)->childrenN.end());
                        }



                    }
                }
                subTlist.insert(subTlist.end(), subTlist_p.begin(), subTlist_p.end());
                subTlist_p.clear();
                if (expandFin == true)
                {
                    subTlist.clear();
                    break;
                }
            }
        }

        //Label identification
        for (vector<nodes>::iterator tLitL = subTreeList.begin(); tLitL != subTreeList.end(); ++tLitL)
        {
            if ((*tLitL).oriN == nullptr)
            {
                switch ((*tLitL).index / 100000)
                {
                    case 1:
                        (*tLitL).label = 'A';
                        break;
                    case 2:
                        (*tLitL).label = 'U';
                        break;
                    case 3:
                        (*tLitL).label = 'G';
                        break;
                    case 4:
                        (*tLitL).label = 'C';
                        break;
                    case 5:
                        (*tLitL).label = 'T';
                        break;
                    case 6:
                        (*tLitL).label = 'X';
                        break;
                    case 7:
                        (*tLitL).label = 'Y';
                        break;
                    default:
                        break;
                }
            }
            else
            {
                switch ((*tLitL).oriN->index / 100000)
                {
                    case 1:
                        (*tLitL).label = 'A';
                        break;
                    case 2:
                        (*tLitL).label = 'U';
                        break;
                    case 3:
                        (*tLitL).label = 'G';
                        break;
                    case 4:
                        (*tLitL).label = 'C';
                        break;
                    case 5:
                        (*tLitL).label = 'T';
                        break;
                    case 6:
                        (*tLitL).label = 'X';
                        break;
                    case 7:
                        (*tLitL).label = 'Y';
                    default:
                        break;
                }
            }
        }

        //print tree result in node form.
        if (false)
        {
            for (vector<nodes>::iterator tLitP = subTreeList.begin(); tLitP != subTreeList.end(); ++tLitP)
            {
                cout << "NodeIndex: " << (*tLitP).index << endl;
                if ((*tLitP).parentN == nullptr)
                {
                    cout << " isLeaf: " << (*tLitP).isLeaf << endl;
                }
                else
                {
                    cout << "ParentNode: " << (*tLitP).parentN->index << " isLeaf: " << (*tLitP).isLeaf << endl;


                }
                if (!(*tLitP).isLeaf)
                {
                    cout << "ChindNodes: ";
                    for (vector<nodes*>::iterator cTit = (*tLitP).childrenN.begin(); cTit != (*tLitP).childrenN.end(); ++cTit)
                    {
                        cout << (*cTit)->index << " ";
                    }
                    cout << endl;
                }
                cout << "Label: " << (*tLitP).label << endl;
                cout << "-----------------------------------------" << endl;

            }
        }



        patternFile = folderPath + "/"+to_string((*vLitR).index) + ".txt";
        ofstream verAsRootString(patternFile);
        cout << "No." + to_string((*vLitR).index) + " vertex as root RESULT:" << endl;





        nodes* n;
        nodes* n_p;

        nodes* n_ori = &subTreeList[searchNode((*vLitR).index, subTreeList)];
        n = &subTreeList[searchNode((*vLitR).index, subTreeList)];
        bool loopStop = false;

        int countNode = 0;

        while (true)
        {
            verAsRootString << "{" + n->label;
            cout << "{" + n->label;
            countNode++;
            if (n->isLeaf)
            {
                verAsRootString << "}";
                cout << "}";
                if (n->index == (n_ori)->index)
                {
                    break;
                }
                while (true)
                {
                    n_p = nextNodeOfP(n);
                    if (n_p != nullptr)
                    {
                        n = n_p;
                        break;
                    }
                    else
                    {
                        verAsRootString << "}";
                        cout << "}";
                        n = n->parentN;
                        if (n->index == (n_ori)->index)
                        {
                            loopStop = true;
                            break;
                        }
                    }

                }
            }
            else
            {
                n = n->childrenN[0];
            }
            if (loopStop)
            {
                break;
            }
        }

        cout << endl;
        if (countNode != subTreeList.size())
        {
            cout << "!!!!!!!!!!!!!!!!Output Size error for result " << (*vLitR).index << " as ROOT!!!!!!!!!!!!!!!!!!!!!!" << endl;
        }

        //reset subTreeList.
        for (vector<nodes>::iterator sTit = subTreeList.begin(); sTit != subTreeList.end(); ++sTit)
        {
            (*sTit).childrenN.clear();
            (*sTit).isLeaf = 0;
            (*sTit).parentN = nullptr;
        }


    }
    return 0;

}