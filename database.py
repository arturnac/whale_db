
import paho.mqtt.client as paho
from pymongo import MongoClient

broker = "34.210.186.4"
port = 1883

client = MongoClient()
dbClient = MongoClient('localhost', 27017)
db = client.whaleDB

collection = db.whaleCPU

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("rpi/cpu")

def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))

	rpi_cpu = {"CPU": (msg.payload)}
	post_id = collection.insert_one(rpi_cpu).inserted_id

client = paho.Client("testclient", clean_session=False, protocol=paho.MQTTv31)
client.on_message = on_message
client.connect("localhost", 1883)
client.subscribe("rpi/cpu", qos=1)

client.loop_forever() 
