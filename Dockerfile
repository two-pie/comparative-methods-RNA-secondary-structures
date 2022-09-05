FROM mathworks/matlab:r2022a

WORKDIR /home/matlab/Documents/MATLAB/gp

ENV DEBIAN_FRONTEND=noninteractive

RUN sudo apt-get -y update; sudo apt-get -y install python3 git curl sudo openjdk-17-jdk openjdk-17-jre; \
    # Installing google chrome
    curl -O https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get -y install ./google-chrome-stable_current_amd64.deb  \
    && rm google-chrome-stable_current_amd64.deb; \
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
RUN sudo chmod -R 777 /home/matlab/Documents/MATLAB/gp
RUN mkdir symlinks  \
    && cd symlinks
RUN ln -s /home/matlab/Documents/MATLAB/gp/workbench/aspralign_workbench/aspralign_workbench.py aspralign_distance_tool; \
    ln -s /home/matlab/Documents/MATLAB/gp/workbench/dualgraph_workbench/dualgraph_workbench.py dualgraph_distance_tool; \
    ln -s /home/matlab/Documents/MATLAB/gp/workbench/nestedalign_workbench/nestedalign_workbench.py nestedalign_distance_tool; \
    ln -s /home/matlab/Documents/MATLAB/gp/workbench/rnadistance_workbench/rnadistance_workbench.py rnadistance_distance_tool; \
    ln -s /home/matlab/Documents/MATLAB/gp/workbench/rnaforester_workbench/rnaforester_workbench.py rnaforester_distance_tool
RUN echo "export PATH='$(pwd):$PATH'" | sudo tee -a /etc/bash.bashrc
