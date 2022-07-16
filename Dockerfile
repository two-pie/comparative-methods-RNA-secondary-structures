FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -y update; apt-get -y install perl python3 build-essential openjdk-11-jdk git wget unzip
WORKDIR /gp

#ASPRAlign
RUN git clone https://github.com/bdslab/aspralign.git; \
#ViennaRNA
wget https://github.com/ViennaRNA/ViennaRNA/releases/download/v2.5.1/ViennaRNA-2.5.1.tar.gz && tar -zxvf ViennaRNA-2.5.1.tar.gz && rm  ViennaRNA-2.5.1.tar.gz;\
cd ViennaRNA-2.5.1; \
./configure \
make \
make install; \
cd ..\
#LocARNA
wget https://github.com/s-will/LocARNA/releases/download/v2.0.0RC10/locarna-2.0.0RC10.tar.gz && tar -xf locarna-2.0.0RC10.tar.gz && rm locarna-2.0.0RC10.tar.gz; \
cd locarna-2.0.0RC10; \
./configure; \
make; \
make install; \
cd ..\
ADD molecolePerTest ./molecolePerTest
CMD tail -f /dev/null