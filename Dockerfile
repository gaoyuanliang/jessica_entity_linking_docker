###########Dockerfile############
FROM ubuntu:xenial
#FROM ubuntu:18.10

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

EXPOSE 8080

CMD java -Xmx3000m -jar dexter-2.1.0.jar &
###########Dockerfile############
