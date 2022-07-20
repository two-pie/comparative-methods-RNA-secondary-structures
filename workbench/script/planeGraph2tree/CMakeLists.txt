cmake_minimum_required(VERSION 3.22)
project(planeGraph2tree)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(planeGraph2tree
        CanonicalFormComputing.cpp
        CentroidComputing.cpp
        CentroidComputing.h
        DCELformTransfer.cpp
        DCELformTransfer.h
        RootTransformation.cpp
        RootTransformation.h
        stdafx.cpp
        stdafx.h
        targetver.h)
