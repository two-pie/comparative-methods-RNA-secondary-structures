// CanonicalFormComputing.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

#include "CentroidComputing.h"
#include "DCELformTransfer.h"
#include "RootTransformation.h"

using namespace std;



int main(int argc, char **argv)
{

    /*Example code*/

    string fileName = argv[1];
    cout << fileName;

    DCELformTransfer DT;
    DT.formTransfer(fileName);

    PlaneGraph PG;
    PG.buildGraph(fileName + "_ver.txt", fileName + "_edge.txt", fileName + "_face.txt");
    PG.setOuterFace(fileName + "_outerF.txt");
    PG.RUNNING();

    rootTrans RT;
    RT.running(fileName);
    PG.APTEDformTrans_AllVerAsRoot();
    return 0;
}