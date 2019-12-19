FROM ubuntu:18.04
MAINTAINER Moisés <moises@fictizia.com>

RUN apt-get update && apt-get install -y python3 python3-pip && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN mkdir /app
RUN mkdir /app/src
COPY src /app/src
COPY requirements.txt /app
WORKDIR /app
RUN pip3 install -r requirements.txt
WORKDIR /app/src
EXPOSE 5005
CMD ["python3", "server.py"]