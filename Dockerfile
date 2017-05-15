FROM python:2.7
RUN pip install paho-mqtt
RUN pip install pymongo
RUN mkdir /rpi-cpu
COPY database.py /rpi-cpu
WORKDIR	/rpi-cpu

CMD ["python", "database.py"]
