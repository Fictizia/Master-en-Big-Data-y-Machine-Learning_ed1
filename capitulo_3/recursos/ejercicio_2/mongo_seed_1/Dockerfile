FROM ubuntu:18.04
RUN apt update
RUN apt install python3 python3-pip -y
RUN mkdir /app
RUN mkdir /data
RUN mkdir /app/src
COPY ./data /app/data
COPY ./requirements.txt /app
COPY ./src /app/src
WORKDIR /app
RUN pip3 install -r requirements.txt
WORKDIR /app/src
CMD ["python3", "seed.py"]
