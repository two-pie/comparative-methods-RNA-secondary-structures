FROM eclipse-temurin:11-alpine
RUN apk add --no-cache git python3 build-base perl && \
 wget -O get-pip.py    https://github.com/pypa/get-pip/raw/38e54e5de07c66e875c11a1ebbdb938854625dd8/public/get-pip.py; \
python3 get-pip.py; \
rm -f get-pip.py
WORKDIR /gp

#ASPRAlign
RUN git clone https://github.com/bdslab/aspralign.git; \

#PSTAG
mkdir pstag && cd pstag; \
wget http://pstag.dna.bio.keio.ac.jp/download/pstag2_1_2-unix.zip && unzip pstag2_1_2-unix.zip && rm pstag2_1_2-unix.zip; \
cd pstag2_1_2-unix && chmod +x pstag && cd ../..; \

#MiGaL
mkdir migal && cd migal; \
wget http://www-igm.univ-mlv.fr/~allali/logiciels/migal_tgz/migal.tgz && tar -xf migal.tgz && rm migal.tgz; \
#cd migal-2.2 && make install; \
cd ..; \

#Gardenia
wget https://bioinfo.lifl.fr/gardenia/gardenia.zip && unzip gardenia.zip && rm gardenia.zip; \

#LocARNA
git clone https://github.com/s-will/LocARNA

ADD molecolePerTest ./molecolePerTest 
CMD tail -f /dev/null
