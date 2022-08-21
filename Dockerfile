FROM eclipse-temurin:17-jammy
WORKDIR /gp

RUN apt-get -y update  \
    && apt-get -y upgrade; \
    apt-get -y install python3 git curl; \
    # Installing google chrome
    curl -O https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get -y install ./google-chrome-stable_current_amd64.deb  \
    && rm google-chrome-stable_current_amd64.deb; \
    # ASPRAlign
    git clone https://github.com/bdslab/aspralign.git; \
    # Download and install miniconda
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh  \
    && /bin/bash miniconda.sh -b -p /opt/conda  \
    && rm miniconda.sh

# Put conda in path
ENV PATH /opt/conda/bin:$PATH

# ViennaRNA
RUN conda update -y conda; \
    conda install -y -c bioconda/label/cf201901 viennarna; \
    # Remove unnecessary packages
    apt-get -y purge --auto-remove curl git

# This section is just for caching, it will be removed later
ADD requirements.txt .
RUN pip -q install -r requirements.txt  \
    && rm requirements.txt
ADD workbench ./workbench
