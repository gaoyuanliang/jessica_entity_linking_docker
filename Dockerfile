###########Dockerfile############
FROM ubuntu:xenial

RUN apt-get update
RUN apt-get install -y openjdk-8-jdk
RUN apt-get install -y wget
RUN apt-get install -y git 
RUN apt-get install -y curl

RUN apt-get install -y python3-pip
RUN apt-get install -y python3-dev

RUN wget http://dexter.isti.cnr.it/dexter.tar.gz

RUN apt-get install -y tar
RUN tar xvzf dexter.tar.gz

RUN mv /dexter2/* ./

RUN pip3 install requests==2.24.0
RUN pip3 install rdflib==5.0.0
RUN pip3 install pyspark==3.0.1

ENV PYSPARK_PYTHON /usr/bin/python3.5
ENV PYSPARK_DRIVER_PYTHON /usr/bin/python3.5

RUN pip3 install gdown
RUN gdown https://drive.google.com/uc?id=19A9dmnwz3w09hrgL4aDzgaDiNvLHHnk-
RUN gdown https://drive.google.com/uc?id=1K2_4J4z28BxoFrfGE94d2LTtAWFwNJA_

EXPOSE 8080

RUN echo "dgsgd"

RUN git clone https://github.com/gaoyuanliang/jessica_entity_linking_docker.git
RUN mv jessica_entity_linking_docker/* ./

CMD bash
###########Dockerfile############
