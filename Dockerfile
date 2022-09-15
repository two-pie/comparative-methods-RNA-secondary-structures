# syntax=docker/dockerfile:1
FROM mathworks/matlab:r2022a

WORKDIR /home/matlab/Documents/MATLAB/gp

ENV DEBIAN_FRONTEND=noninteractive

RUN sudo apt-get -y update; sudo apt-get -y install python3 git curl sudo openjdk-17-jdk openjdk-17-jre; \
    # Installing google chrome
    sudo curl -O https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && sudo apt-get -y install ./google-chrome-stable_current_amd64.deb  \
    && sudo rm google-chrome-stable_current_amd64.deb; \
    # Download and install miniconda
    sudo wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh  \
    && sudo /bin/bash miniconda.sh -b -p /opt/conda  \
    && sudo rm miniconda.sh

# ViennaRNA
RUN sudo /opt/conda/bin/conda update -y conda; \
    sudo /opt/conda/bin/conda install -y -c bioconda/label/cf201901 viennarna; \
    # Remove unnecessary packages
    sudo apt-get -y purge --auto-remove curl git

# This section is just for caching, it will be removed later
ADD requirements.txt .
RUN sudo pip -q install -r requirements.txt  \
    && sudo rm requirements.txt \
    && sudo pip install --upgrade urllib3 \
    && sudo pip install --upgrade requests
ADD workbench ./workbench
RUN sudo chmod -R 777 /home/matlab/Documents/MATLAB/gp
RUN mkdir -p workbench/workbench_results/Archaea-90-110-allType/distances  \
    workbench/workbench_results/Molecules-pseudoknotfree/Archaea/5S/distances  \
    workbench/workbench_results/Molecules-pseudoknotfree/Bacteria/5S/distances  \
    workbench/workbench_results/Molecules-pseudoknotfree/Eukaryota/5S/distances \
    workbench/workbench_results/Archaea-90-110-allType/cores/core \
    workbench/workbench_results/Archaea-90-110-allType/cores/core_plus \
    workbench/workbench_results/Archaea-90-110-allType/clustering \
    workbench/workbench_results/Molecules-pseudoknotfree/Archaea/5S/cores/core \
    workbench/workbench_results/Molecules-pseudoknotfree/Archaea/5S/cores/core_plus \
    workbench/workbench_results/Molecules-pseudoknotfree/Archaea/5S/clustering \
    workbench/workbench_results/Molecules-pseudoknotfree/Bacteria/5S/cores/core \
    workbench/workbench_results/Molecules-pseudoknotfree/Bacteria/5S/cores/core_plus \
    workbench/workbench_results/Molecules-pseudoknotfree/Bacteria/5S/clustering \
    workbench/workbench_results/Molecules-pseudoknotfree/Eukaryota/5S/cores/core \
    workbench/workbench_results/Molecules-pseudoknotfree/Eukaryota/5S/cores/core_plus \
    workbench/workbench_results/Molecules-pseudoknotfree/Eukaryota/5S/clustering \
    symlinks; \
    # Symbolic link tools
    cd symlinks  \
    && ln -s /home/matlab/Documents/MATLAB/gp/workbench/distance_tools/aspralign_workbench/aspralign_workbench.py aspralign_distance_tool; \
    ln -s /home/matlab/Documents/MATLAB/gp/workbench/distance_tools/dualgraph_workbench/dualgraph_workbench.py dualgraph_distance_tool; \
    ln -s /home/matlab/Documents/MATLAB/gp/workbench/distance_tools/nestedalign_workbench/nestedalign_workbench.py nestedalign_distance_tool; \
    ln -s /home/matlab/Documents/MATLAB/gp/workbench/distance_tools/rnadistance_workbench/rnadistance_workbench.py rnadistance_distance_tool; \
    ln -s /home/matlab/Documents/MATLAB/gp/workbench/distance_tools/rnaforester_workbench/rnaforester_workbench.py rnaforester_distance_tool; \
    ln -s /home/matlab/Documents/MATLAB/gp/workbench/distance_tools/treegraph_workbench/treegraph_workbench.py treegraph_distance_tool; \
    ln -s /home/matlab/Documents/MATLAB/gp/workbench/core/coresCalculator.sh cores_calculator_tool; \
    ln -s /home/matlab/Documents/MATLAB/gp/workbench/clustering/ClusterMatrix.py cluster_matrix; \
    ln -s /home/matlab/Documents/MATLAB/gp/workbench/clustering/ClusterFeatures.py cluster_features; \
    ln -s /opt/conda/bin/RNAforester RNAforester; \
    ln -s /opt/conda/bin/RNAdistance RNAdistance; \
    echo "export PATH='$(pwd):$PATH'" | sudo tee -a /etc/bash.bashrc
