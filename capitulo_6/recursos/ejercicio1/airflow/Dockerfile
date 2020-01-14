FROM puckel/docker-airflow

USER root
RUN pip3 install pandas kafka-python google-cloud httplib2 google-api-python-client google-auth-httplib2 google-cloud-storage
RUN mkdir /data
RUN mkdir /credentials
USER airflow