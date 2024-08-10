
from pymongo import MongoClient
from datetime import datetime

class MongoConnector:
    
    def __init__(self):
        self.mongo_uri = 'mongodb://localhost:27017/'
        self.db_name = 'randomMessages'
        self.collection_name = 'messages'

    def connect(self):
        mongo_client = MongoClient(self.mongo_uri)
        db = mongo_client[self.db_name]
        self.collection = db[self.collection_name]
        
    def get_data(self, start_time, end_time):
        filter = { "timestring": {
                    "$gte": start_time,
                    "$lte": end_time
                    }
                }
        # #####if arguments are in list form ex . [2024, 8, 10, 15, 0, 0]
        # start_time = datetime(*eval(start_time))
        # end_time = datetime(*eval(end_time))
        # filter = { "timestamp": {
        #             "$gte": start_time,
        #             "$lte": end_time
        #             }
        #         }
        
        pipeline= [
            {
                "$match":  filter
                
            },
            {
                "$group": {
                    "_id": "$status", 
                    "count": {"$sum": 1}
                }
            },
            {
            "$project": {
                "_id": 0,              
                "status": "$_id" ,  
                "count": 1 ,
            }
            }
        ]
        cursor = self.collection.aggregate(pipeline)
        return list(cursor)
    
    def insert_data(self, msg_body):
        self.collection.insert_one(msg_body)