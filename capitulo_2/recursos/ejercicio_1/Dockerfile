FROM ubuntu:18.04
MAINTAINER Moisés <moises@fictizia.com>

RUN apt-get update && apt-get install -y python3 python3-pip && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN mkdir /api
COPY requirementes.txt /api
COPY src /api
WORKDIR /api
RUN pip3 install -r requirements.txt
EXPOSE 5005
WORKDIR /api/src
CMD ["python3", "server.py"]
