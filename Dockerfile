FROM mathworks/matlab:r2022a

WORKDIR /home/matlab/Documents/MATLAB/gp

ENV DEBIAN_FRONTEND=noninteractive

RUN sudo apt-get -y update; sudo apt-get -y install python3 git curl sudo openjdk-17-jdk openjdk-17-jre; \
    # Installing google chrome
    curl -O https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get -y install ./google-chrome-stable_current_amd64.deb  \
    && rm google-chrome-stable_current_amd64.deb; \
    # ASPRAlign
    git clone https://github.com/bdslab/aspralign.git; \
    # Download and install miniconda
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh  \
    && sudo /bin/bash miniconda.sh -b -p /opt/conda  \
    && rm miniconda.sh

# ViennaRNA
RUN sudo /opt/conda/bin/conda update -y conda; \
    sudo /opt/conda/bin/conda install -y -c bioconda/label/cf201901 viennarna; \
    # Remove unnecessary packages
    sudo apt-get -y purge --auto-remove curl git

# This section is just for caching, it will be removed later
ADD requirements.txt .
RUN sudo pip -q install -r requirements.txt  \
    && rm requirements.txt
ADD workbench ./workbench