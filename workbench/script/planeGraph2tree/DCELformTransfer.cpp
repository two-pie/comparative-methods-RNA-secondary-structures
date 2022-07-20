#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

#include "DCELformTransfer.h"

using namespace std;

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


DCELformTransfer::DCELformTransfer(void)
{
    cout << "DCEL form transfer start." << endl;
}

DCELformTransfer::~DCELformTransfer()
{
    cout << "DCEL form transfer end." << endl;
}

/*This is only for expriment in paper to split the continus BPSEQ format*/
int DCELformTransfer::splitTXT(string path)
{
    string s;
    int index = 1;
    ifstream sLread("BPSEQ_result.txt", ios::in);
    if (!sLread.is_open())
    {
        cout << "Error! Cannot open the split file. "<<path << endl;
    }
    else
    {
        ofstream out;
        out.open("./DCEL_result/PKB" + to_string(index) + ".txt");
        while (!sLread.eof())
        {
            getline(sLread, s);
            //cout << s<<endl;
            if (s == "")
            {
                out.close();
                index++;
                out.open("./BPSEQ_result/PKB" + to_string(index) + ".txt");
                getline(sLread, s);
            }
            out << s << endl;

        }
        out.close();
    }
    return 0;
}

int DCELformTransfer::formTransfer(string path)
{
    cout << "Start to transfer the BPSEQ form file " << path << " to DCEL form" << endl;
    string s;

    vector<vector<int>> BPSEQform;
    vector<int> iSset;
    string iS;
    ifstream fTread("./BPSEQ_data/"+path , ios::in);
    if (!fTread.is_open())
    {
        cout << "Error! Cannot open the transfer file. " << path << endl;
    }
    else
    {
        while (!fTread.eof())
        {
            getline(fTread, s);
            if (s == "")
            {
                break;
            }
            else
            {
                for (int i=0;i<s.length();i++)
                {
                    //cout << (*sI) << endl;
                    if (isdigit(s[i]))
                    {
                        iS += s[i];
                    }
                    else if (isalpha(s[i]))
                    {
                        if ((s[i]) == 'A')
                        {
                            iS = '1';
                        }
                        else if ((s[i]) == 'U')
                        {
                            iS = '2';
                        }
                        else if ((s[i]) == 'G')
                        {
                            iS = '3';
                        }
                        else if ((s[i]) == 'C')
                        {
                            iS = '4';
                        }
                        else if ((s[i]) == 'T')
                        {
                            iS = '5';
                        }
                        else if ((s[i]) == 'X')
                        {
                            iS = '6';
                        }
                        else if ((s[i]) == 'Y')
                        {
                            iS = '7';
                        }
                    }
                    else
                    {
                        iSset.push_back(stoi(iS));
                        iS.clear();
                    }
                }
                iSset.push_back(stoi(iS));
                iS.clear();
                BPSEQform.push_back(iSset);
                iSset.clear();
            }
        }
    }

    /*Transfer result*/
    cout << "-----------Basic Transfer result-----------" << endl;
    for (vector<vector<int>>::iterator BPSEQit = BPSEQform.begin(); BPSEQit != BPSEQform.end(); ++BPSEQit)
    {
        for (vector<int>::iterator BitIt = (*BPSEQit).begin(); BitIt != (*BPSEQit).end(); ++BitIt)
        {
            cout << (*BitIt) << " ";
        }
        cout << endl;
    }

    //Basic transfer result testing
    for (vector<vector<int>>::iterator BPSEQit = BPSEQform.begin(); BPSEQit != BPSEQform.end(); ++BPSEQit)
    {
        if ((*BPSEQit)[2] != 0)
        {
            for (vector<vector<int>>::iterator Bit = BPSEQform.begin(); Bit != BPSEQform.end(); )
            {
                if ((*Bit)[0] == (*BPSEQit)[2])
                {
                    if ((*Bit)[2] != (*BPSEQit)[0])
                    {
                        cout <<"The note"<< (*BPSEQit)[0]<< " of File " << path << " is error" << endl;
                        return 0;
                    }
                    else
                    {
                        break;
                    }

                }
                ++Bit;
                if (Bit == BPSEQform.end())
                {
                    cout << "File " << path << " is error" << endl;
                    return 0;
                }
            }
        }
    }


    /*This index need be changed to AUGC form at last!!!!*/
    vector<vertices> verList;
    vertices v;
    for (vector<vector<int>>::iterator BPSEQit = BPSEQform.begin(); BPSEQit != BPSEQform.end(); ++BPSEQit)
    {
        v.index = (*BPSEQit)[0];
        verList.push_back(v);
    }

    /*Set halfedge index begin from 1*/
    int count = 1;
    vector<halfEdges> heList;
    halfEdges h;
    for (vector<vertices>::iterator vLit = verList.begin(); vLit != verList.end()-1; ++vLit)
    {
        h.index = count++;
        h.incident_f = nullptr;
        heList.push_back(h);
        h.index = count++;
        h.incident_f = nullptr;
        heList.push_back(h);

    }
    int heCount = 0;
    for (vector<vertices>::iterator vLit = verList.begin(); vLit != verList.end()-1; ++vLit)
    {
        (*vLit).incident_hE = &heList[heCount];
        if (vLit == verList.begin())
        {
            heList[heCount].next_hE = &heList[heCount + 1];
            heList[heCount].prev_hE = &heList[heCount + 2];
            heList[heCount].twin_hE = &heList[heCount + 1];
            heList[heCount].target_v = &(*vLit);
            heCount++;
            heList[heCount].next_hE = &heList[heCount + 2];
            heList[heCount].prev_hE = &heList[heCount - 1];
            heList[heCount].twin_hE = &heList[heCount - 1];
            heList[heCount].target_v = &(*(vLit + 1));
            heCount++;
        }
        else if (vLit == verList.end() - 2)
        {
            heList[heCount].next_hE = &heList[heCount - 2];
            heList[heCount].prev_hE = &heList[heCount + 1];
            heList[heCount].twin_hE = &heList[heCount+1];
            heList[heCount].target_v = &(*vLit);
            heCount++;
            heList[heCount].next_hE = &heList[heCount - 1];
            heList[heCount].prev_hE = &heList[heCount - 2];
            heList[heCount].twin_hE = &heList[heCount - 1];
            heList[heCount].target_v = &(*(vLit + 1));
            (*(vLit + 1)).incident_hE = &heList[heCount];
        }
        else
        {
            heList[heCount].next_hE = &heList[heCount - 2];
            heList[heCount].prev_hE = &heList[heCount + 2];
            heList[heCount].twin_hE = &heList[heCount + 1];
            heList[heCount].target_v = &(*vLit);
            heCount++;
            heList[heCount].next_hE = &heList[heCount + 2];
            heList[heCount].prev_hE = &heList[heCount - 2];
            heList[heCount].twin_hE = &heList[heCount - 1];
            heList[heCount].target_v = &(*(vLit + 1));
            heCount++;
        }
    }

    if (heCount != heList.size() - 1 || heList.size()!=2*(verList.size()-1))
    {
        cout << "Edge amount is error" << endl;
    }

    int mode = 0;
    halfEdges* e = &*(heList.begin());
    halfEdges* tarHE;
    vertices* tarVer=nullptr;
    vertices* tarVerM = nullptr;

    vector<halfEdges> connectedHeList;

    //Connect nucleobases

    for (vector<vector<int>>::iterator BPSEQit = BPSEQform.begin(); BPSEQit != BPSEQform.end(); ++BPSEQit)
    {
        if ((*BPSEQit)[2] != 0 && (*BPSEQit)[0]>(*BPSEQit)[2])
        {
            count++;
            halfEdges cE1;
            cE1.index = count;
            cE1.incident_f = nullptr;
            count++;
            halfEdges cE2;
            cE2.index = count;
            cE2.incident_f = nullptr;
            connectedHeList.push_back(cE1);
            connectedHeList.push_back(cE2);
        }
    }

    vector<halfEdges>::iterator cHlIt = connectedHeList.begin();
    while (true)
    {
        for (vector<vector<int>>::iterator BPSEQit = BPSEQform.begin(); BPSEQit != BPSEQform.end(); ++BPSEQit)
        {
            //There are 2 vertices need to be connected
            if (e->target_v->index==(*BPSEQit)[0] && (*BPSEQit)[2] > e->target_v->index)
            {
                //Change mode
                if (tarVer != nullptr && (*BPSEQit)[2] > tarVer->index && e->target_v->index < tarVerM->index)///////////
                {
                    switch (mode)
                    {
                        case 0:
                            mode = 1;
                            e = e->next_hE->twin_hE;
                            break;
                        case 1:
                            e = e->next_hE->twin_hE;
                            mode = 0;
                            break;
                        default:
                            break;
                    }
                }


                //Search the target vertices.

                for (vector<vertices>::iterator vLit = verList.begin(); vLit != verList.end(); ++vLit)
                {
                    if ((*vLit).index == (*BPSEQit)[2])
                    {
                        tarVer = &(*vLit);
                        if (tarVerM == nullptr || tarVerM->index < tarVer->index)///////////////////////////
                        {
                            tarVerM = &(*vLit);
                        }
                        break;
                    }
                }



                //Search the target halfedge
                tarHE = e;
                while (true)
                {
                    switch (mode)
                    {
                        case 0:
                            tarHE = tarHE->next_hE;
                            break;
                        case 1:
                            tarHE = tarHE->prev_hE;
                            break;
                        default:
                            cout << "mode error" << endl;
                            break;
                    }

                    if (tarHE->target_v->index == tarVer->index)
                    {
                        break;
                    }

                }

                //Add 2 new half edge to connect nucleobase.
                //New connect half-edge 1

                (*cHlIt).next_hE = e->twin_hE;
                //e->twin_hE->prev_hE = &(*cHlIt);
                (*cHlIt).prev_hE = tarHE->next_hE->twin_hE;
                //tarHE->next_hE->twin_hE->next_hE = &(*cHlIt);
                (*cHlIt).target_v = e->target_v;
                (*cHlIt).twin_hE = &(*(cHlIt + 1));
                ++cHlIt;

                //New connect half-edge 2
                (*cHlIt).next_hE = tarHE->twin_hE;
                //tarHE->twin_hE->prev_hE = &(*cHlIt);
                (*cHlIt).prev_hE = e->next_hE->twin_hE;
                //e->next_hE->twin_hE->next_hE = &(*cHlIt);
                (*cHlIt).target_v = tarHE->target_v;
                (*cHlIt).twin_hE = &(*(cHlIt - 1));
                ++cHlIt;

                break;
            }
        }



        switch (mode)
        {
            case 0:
                e = e->next_hE;
                break;
            case 1:
                e = e->prev_hE;
                break;

            default:
                cout << "mode error" << endl;
                break;
        }

        if (e->target_v->index == (*(BPSEQform.end() - 1))[0])
        {
            break;
        }
    }

    for (vector<halfEdges>::iterator cElIt = connectedHeList.begin(); cElIt != connectedHeList.end(); ++cElIt)
    {
        (*cElIt).next_hE->prev_hE = &(*cElIt);
        (*cElIt).prev_hE->next_hE = &(*cElIt);
    }



    //Set faces.
    vector<faces> faceList;
    int fCount = 1;
    int fEdgesC = 0;
    vector<vector<int>> fCsum;
    vector<int> fC;
    for (vector<halfEdges>::iterator heLit = heList.begin(); heLit != heList.end(); ++heLit)
    {
        if ((*heLit).incident_f == nullptr)
        {
            faces f;
            f.index = fCount;
            fCount++;
            f.arbitarary_hE = &(*heLit);
            faceList.push_back(f);
            halfEdges* e = &(*heLit);
            while (true)
            {
                e = e->next_hE;
                if (e->incident_f != nullptr)
                {
                    break;
                }
                e->incident_f = &(*(faceList.end() - 1));
                fEdgesC++;
            }
        }
    }
    for (vector<halfEdges>::iterator cElIt = connectedHeList.begin(); cElIt != connectedHeList.end(); ++cElIt)
    {
        if ((*cElIt).incident_f == nullptr)
        {
            faces f;
            f.index = fCount;
            fCount++;
            f.arbitarary_hE = &(*cElIt);
            faceList.push_back(f);
            (*cElIt).incident_f = &(*(faceList.end() - 1));
            halfEdges* e = &(*cElIt);
            while (true)
            {
                e = e->next_hE;
                if (e->incident_f != nullptr)
                {
                    break;
                }
                e->incident_f = &(*(faceList.end() - 1));
                fEdgesC++;
            }
        }
    }
    //Because the vector type, there need to be reset.
    for (vector<halfEdges>::iterator heLit = heList.begin(); heLit != heList.end(); ++heLit)
    {
        (*heLit).incident_f = nullptr;
    }
    for (vector<halfEdges>::iterator cElIt = connectedHeList.begin(); cElIt != connectedHeList.end(); ++cElIt)
    {
        (*cElIt).incident_f = nullptr;
    }

    for (vector<faces>::iterator fLit = faceList.begin(); fLit != faceList.end(); ++fLit)
    {
        fEdgesC = 0;
        halfEdges* e = (*fLit).arbitarary_hE;
        e->incident_f = &(*fLit);
        while (true)
        {
            fEdgesC++;
            e = e->next_hE;
            if (e->incident_f != nullptr)
            {
                break;
            }
            e->incident_f = &(*fLit);
        }
        fC = { (*fLit).index,fEdgesC };
        fCsum.push_back(fC);
        fCount++;

    }

    //Test & Repair

    if (verList.size() - (heList.size() + connectedHeList.size()) / 2 + faceList.size() != 2)//Eular's formal
    {
        cout << "VerCount: " << verList.size() << " heCount: " << (heList.size() + connectedHeList.size()) / 2 << " FaceCount: " << faceList.size() << endl;
        cout << "----------------This is not a plane graph, repair program start-----------------" << endl;

        while (true)
        {
            //Find abnormal data
            //for (vector<halfEdges>::iterator cElIt = connectedHeList.begin(); cElIt != connectedHeList.end(); ++cElIt)
            for (vector<halfEdges>::iterator heLit = heList.begin(); heLit != heList.end(); ++heLit)
            {
                //A pair of twin half edge cannot have a same face
                if ((*heLit).incident_f->index == (*heLit).twin_hE->incident_f->index)
                {
                    halfEdges* e = &(*heLit);
                    halfEdges* eR = nullptr;
                    while (true)
                    {
                        //The cause must be some connected half edges.
                        if (e->index > (*(heList.end() - 1)).index && e->incident_f != nullptr)
                        {
                            eR = e;
                            e = e->next_hE;
                            eR->prev_hE->next_hE = eR->prev_hE->twin_hE->prev_hE->twin_hE;
                            eR->next_hE->prev_hE = eR->next_hE->twin_hE->next_hE->twin_hE;

                            eR->twin_hE->prev_hE->next_hE = eR->twin_hE->prev_hE->twin_hE->prev_hE->twin_hE;
                            eR->twin_hE->next_hE->prev_hE = eR->twin_hE->next_hE->twin_hE->next_hE->twin_hE;

                            eR->prev_hE = eR->prev_hE->twin_hE->prev_hE;
                            eR->next_hE = eR->next_hE->twin_hE->next_hE;
                            eR->twin_hE->prev_hE = eR->twin_hE->prev_hE->twin_hE->prev_hE;
                            eR->twin_hE->next_hE = eR->twin_hE->next_hE->twin_hE->next_hE;

                            eR->prev_hE->next_hE = eR->twin_hE->twin_hE;
                            eR->next_hE->prev_hE = eR->twin_hE->twin_hE;
                            eR->twin_hE->prev_hE->next_hE = eR->twin_hE;
                            eR->twin_hE->next_hE->prev_hE = eR->twin_hE;



                            e->incident_f = nullptr;
                            e->twin_hE->incident_f = nullptr;
                        }
                        else
                        {
                            e = e->next_hE;
                        }


                        if (e->index == (*heLit).index)
                        {
                            break;
                        }
                    }
                    break;
                }
            }

            //------------------------------------------Reset faces------------------------------------------//
            for (vector<halfEdges>::iterator heLit = heList.begin(); heLit != heList.end(); ++heLit)
            {
                (*heLit).incident_f = nullptr;
            }
            for (vector<halfEdges>::iterator cElIt = connectedHeList.begin(); cElIt != connectedHeList.end(); ++cElIt)
            {
                (*cElIt).incident_f = nullptr;
            }
            faceList.clear();
            fCsum.clear();
            fC.clear();
            fCount = 1;
            fEdgesC = 0;

            for (vector<halfEdges>::iterator heLit = heList.begin(); heLit != heList.end(); ++heLit)
            {
                if ((*heLit).incident_f == nullptr)
                {
                    faces f;
                    f.index = fCount;
                    fCount++;
                    f.arbitarary_hE = &(*heLit);
                    faceList.push_back(f);
                    halfEdges* e = &(*heLit);
                    while (true)
                    {
                        e = e->next_hE;
                        if (e->incident_f != nullptr)
                        {
                            break;
                        }
                        e->incident_f = &(*(faceList.end() - 1));
                        fEdgesC++;
                    }
                }
            }
            for (vector<halfEdges>::iterator cElIt = connectedHeList.begin(); cElIt != connectedHeList.end(); ++cElIt)
            {
                if ((*cElIt).incident_f == nullptr)
                {
                    faces f;
                    f.index = fCount;
                    fCount++;
                    f.arbitarary_hE = &(*cElIt);
                    faceList.push_back(f);
                    (*cElIt).incident_f = &(*(faceList.end() - 1));
                    halfEdges* e = &(*cElIt);
                    while (true)
                    {
                        e = e->next_hE;
                        if (e->incident_f != nullptr)
                        {
                            break;
                        }
                        e->incident_f = &(*(faceList.end() - 1));
                        fEdgesC++;
                    }
                }
            }
            //Because the vector type, there need to be reset.
            for (vector<halfEdges>::iterator heLit = heList.begin(); heLit != heList.end(); ++heLit)
            {
                (*heLit).incident_f = nullptr;
            }
            for (vector<halfEdges>::iterator cElIt = connectedHeList.begin(); cElIt != connectedHeList.end(); ++cElIt)
            {
                (*cElIt).incident_f = nullptr;
            }

            for (vector<faces>::iterator fLit = faceList.begin(); fLit != faceList.end(); ++fLit)
            {
                fEdgesC = 0;
                halfEdges* e = (*fLit).arbitarary_hE;
                e->incident_f = &(*fLit);
                while (true)
                {
                    fEdgesC++;
                    e = e->next_hE;
                    if (e->incident_f != nullptr)
                    {
                        break;
                    }
                    e->incident_f = &(*fLit);
                }
                fC = { (*fLit).index,fEdgesC };
                fCsum.push_back(fC);
                fCount++;

            }

            //------------------------------------------Reset Faces Finished------------------------------------------//
            //Loop until it could be a plane graph
            if (verList.size() - (heList.size() + connectedHeList.size()) / 2 + faceList.size() == 2)
            {
                cout << "Repair succeeded!" << endl;
                break;
            }
            else
            {
                cout << "VerCount: " << verList.size() << " heCount: " << (heList.size() + connectedHeList.size()) / 2 << " FaceCount: " << faceList.size() << endl;
            }
        }
    }
    else
    {
        cout << "-----------------This is a plane graph.---------------------" << endl;
    }



    //Deside the outer face.*******************************************************Not perfect algorithm
    int OuterIndex = 0;
    if (heList[0].incident_f->index == heList[1].incident_f->index)
    {
        OuterIndex = heList[0].incident_f->index;
    }
    else
    {
        if (fCsum[0][1] > fCsum[1][1])
        {
            OuterIndex = fCsum[0][0];
        }
        else
        {
            OuterIndex = fCsum[1][0];
        }
    }

    /*
    int OuterIndex=0;
    int mFheCount=0;
    for (vector<vector<int>>::iterator fcIt = fCsum.begin(); fcIt != fCsum.end(); ++fcIt)
    {
        cout << (*fcIt)[0] << " " << (*fcIt)[1] << endl;
        if ((*fcIt)[1] > mFheCount)
        {
            OuterIndex = (*fcIt)[0];
            mFheCount = (*fcIt)[1];
        }
    }
    */


    //Change the Index for vertices.
    int Aindex = 100001;
    int Uindex = 200001;
    int Gindex = 300001;
    int Cindex = 400001;
    int Tindex = 500001;
    int Xindex = 600001;
    int Yindex = 700001;

    for (vector<vertices>::iterator vLit = verList.begin(); vLit != verList.end(); ++vLit)
    {
        for (vector<vector<int>>::iterator BPSEQit = BPSEQform.begin(); BPSEQit != BPSEQform.end(); ++BPSEQit)
        {
            if ((*BPSEQit)[0] == (*vLit).index)
            {
                switch ((*BPSEQit)[1])
                {
                    case 1:
                        (*vLit).index = Aindex++;
                        break;
                    case 2:
                        (*vLit).index = Uindex++;
                        break;
                    case 3:
                        (*vLit).index = Gindex++;
                        break;
                    case 4:
                        (*vLit).index = Cindex++;
                        break;
                    default:
                        break;
                }
                break;
            }
        }
    }

    //Output
    _mkdir("DCEL");
    //vertices
    ofstream VerOutput("./DCEL/" + path + "_ver" + ".txt");
    cout << "-------vertices design-------" << endl;
    for (vector<vertices>::iterator vLit = verList.begin(); vLit != verList.end(); ++vLit)
    {
        if (vLit == verList.end() - 1)
        {
            VerOutput << "{" <<(*vLit).index << "," << (*vLit).incident_hE->index<<"}";
        }
        else
        {
            VerOutput << "{" << (*vLit).index << "," << (*vLit).incident_hE->index << "}" << endl;
        }

        cout << "vIndex: " << (*vLit).index << " incidentHe: " << (*vLit).incident_hE->index << endl;
    }
    VerOutput.close();

    //output
    //half-edges
    ofstream EdgeOutput("./DCEL/" + path + "_edge" + ".txt");
    cout << "-------halfEdge design-------" << endl;
    for (vector<halfEdges>::iterator heLit = heList.begin(); heLit != heList.end(); ++heLit)
    {

        EdgeOutput << "{" << (*heLit).index << "," << (*heLit).incident_f->index << "," << (*heLit).target_v->index << "," << (*heLit).twin_hE->index << "," << (*heLit).prev_hE->index << "," << (*heLit).next_hE->index << "}" << endl;
        cout << "heIndex: " << (*heLit).index << "IncF: " << (*heLit).incident_f->index << " tVer:" << (*heLit).target_v->index << " prevE: " << (*heLit).prev_hE->index << " nextE: " << (*heLit).next_hE->index << " twinE: " << (*heLit).twin_hE->index << endl;
    }
    cout << "-------connected halfEdge design-------" << endl;
    for (vector<halfEdges>::iterator cElIt = connectedHeList.begin(); cElIt != connectedHeList.end(); ++cElIt)
    {
        if (cElIt != connectedHeList.end() - 1)
        {
            EdgeOutput << "{" << (*cElIt).index << "," << (*cElIt).incident_f->index << "," << (*cElIt).target_v->index << "," << (*cElIt).twin_hE->index << "," << (*cElIt).prev_hE->index << "," << (*cElIt).next_hE->index << "}" << endl;
        }
        else
        {
            EdgeOutput << "{" << (*cElIt).index << "," << (*cElIt).incident_f->index << "," << (*cElIt).target_v->index << "," << (*cElIt).twin_hE->index << "," << (*cElIt).prev_hE->index << "," << (*cElIt).next_hE->index << "}";
        }
        cout << "cnctHeIndex: " << (*cElIt).index << "IncF: " << (*cElIt).incident_f->index << " tVer:" << (*cElIt).target_v->index << " prevE: " << (*cElIt).prev_hE->index << " nextE: " << (*cElIt).next_hE->index << " twinE: " << (*cElIt).twin_hE->index << endl;
    }
    EdgeOutput.close();
    //output
    //faces
    ofstream faceOutput("./DCEL/" + path + "_face" + ".txt");
    for (vector<faces>::iterator fLit = faceList.begin(); fLit != faceList.end(); ++fLit)
    {
        if (fLit != faceList.end() - 1)
        {
            faceOutput << "{" << (*fLit).index << "," << (*fLit).arbitarary_hE->index << "}" << endl;
        }
        else
        {
            faceOutput << "{" << (*fLit).index << "," << (*fLit).arbitarary_hE->index << "}";
        }

        cout << "fIndex: " << (*fLit).index << " incHalfEdge: " << (*fLit).arbitarary_hE->index << endl;
    }
    faceOutput.close();

    //output
    //outerface
    ofstream outerFoutput("./DCEL/" + path + "_outerF" + ".txt");
    outerFoutput << OuterIndex;

    cout << "DCEL form transfer is finished. ^ ^" << endl;

    return 0;

}