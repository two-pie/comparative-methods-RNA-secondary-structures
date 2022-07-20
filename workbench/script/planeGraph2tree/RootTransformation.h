#pragma once

#include "stdafx.h"
#include <vector>
#include <string>
#include <direct.h>
using namespace std;

class rootTrans
{
public:rootTrans(void);
public:~rootTrans();

public:

    int running(string index);

private:

    string readFile(string path);
    int transfer(string index);
    int saveFile(string index, int no, string result);

};