from pymongo.mongo_client import MongoClient
import pandas as pd
import json
#from src.constant import *

# Uniform Resource identifier
uri = "mongodb+srv://srivastavapratham52:Pratham01@cluster0.qj0ivgu.mongodb.net/?retryWrites=true&w=majority"

import os
os.environ['REQUESTS_CA_BUNDLE'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'venv/Lib/site-packages/certifi/cacert.pem')

import certifi
client =MongoClient(f"mongodb+srv://srivastavapratham52:Pratham01@cluster0.qj0ivgu.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=certifi.where())
# Create a new client and connect to the server
#client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    

# create database name and collection name
MONGO_DATABASE_NAME = "pwskills"
MONGO_COLLECTION_NAME = "Cement"

# read the data as a dataframe
df=pd.read_csv("C:\\Users\\Pratham srivastava\\OneDrive - Sikkim Manipal University\\Desktop\\Cement_Strength_Prediction-main\\notebook\\cement_data.csv")

# Convert the data into json
json_record=list(json.loads(df.T.to_json()).values())

#now dump the data into the database
client[MONGO_DATABASE_NAME][MONGO_COLLECTION_NAME].insert_many(json_record)
