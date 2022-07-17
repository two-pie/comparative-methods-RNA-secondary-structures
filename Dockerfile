FROM ubuntu:22.04
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get -y update; apt-get -y install perl python3 build-essential openjdk-11-jdk git wget unzip
WORKDIR /gp

# ASPRAlign
RUN git clone https://github.com/bdslab/aspralign.git;


# Download and install miniconda
ENV CONDA_DIR /opt/conda
RUN  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
    /bin/bash miniconda.sh -b -p /opt/conda; \
    rm miniconda.sh

# Put conda in path
ENV PATH $CONDA_DIR/bin:$PATH

# LocaRNA
RUN conda update -y conda; \
    conda install -y -c bioconda locarna; \
    conda install -c bioconda/label/cf201901 viennarna

ADD workbench ./workbench