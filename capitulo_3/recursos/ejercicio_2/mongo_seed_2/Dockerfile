from ubuntu:16.04
MAINTAINER Moisés <moises@fictizia.com>

RUN apt update
RUN apt install wget -y
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
RUN echo "deb [ arch=amd64 ] http://repo.mongodb.org/apt/ubuntu/ xenial/mongodb-org/3.4 multiverse" |  tee /etc/apt/sources.list.d/mongodb-3.4.list
RUN apt-get update
RUN apt-get install -y mongodb-org
RUN mkdir /outdata
COPY ./data/output.json /outdata/output.json
WORKDIR /outdata
CMD ["mongoimport", "--host", "172.18.10.4", "--port", "27017", "--db", "FICTIZIA", "--collection", "cancer", "--drop", "--file", "output.json", "--jsonArray"]
