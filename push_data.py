import os
import sys
import json
import certifi 
import pandas as pd
import numpy
import pymongo
from networkSecurity.exception_handling.exception import NetworkSecurityException
from networkSecurity.logging.logging_config import logging

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
# print(MONGO_DB_URL)

ca = certifi.where()
# It is python package which provide set of root certificate. To make secure HHTP connection

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def csv_to_jso_convertor(self, file_path):
        try:
            data =pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            # converting dataframe to Json. To do this transpose and convert it
            records= list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def insert_data_to_mongodb(self, records, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))

        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__=="__main__":
    FILE_PATH = "Network_Data\phisingData.csv"
    DATABASE = "Yogesh"
    Collection = "NetworkData"

    network_object = NetworkDataExtract()
    records = network_object.csv_to_jso_convertor(file_path=FILE_PATH)
    print(records)

    no_of_records = network_object.insert_data_to_mongodb(records, DATABASE, Collection)
    print(no_of_records)