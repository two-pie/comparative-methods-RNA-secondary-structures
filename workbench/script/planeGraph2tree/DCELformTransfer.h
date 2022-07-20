#pragma once
#include "stdafx.h"
#include <vector>
#include <string>
#include <direct.h>

using namespace std;

struct halfEdges;
struct vertices;
struct faces;


class DCELformTransfer
{
public:DCELformTransfer(void);
public:~DCELformTransfer();

public:int splitTXT(string path);
public:int formTransfer(string path);
};