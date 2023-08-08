import requests
from pymongo import MongoClient
import pymongo



def get_mongo_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://meetkp1311mp:Meetp788@cluster0.znucqm6.mongodb.net/final_project?retryWrites=true&w=majority"    

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    return client["final_project"]["final_project"]

def cronJob():
    get_client_instance = get_mongo_database()
    response = requests.get(
        'https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=15'
        )
    json_data = response.json()
    if (len(json_data) >= 10):
        # Getting top most 10 data
        dumpdata = json_data[:10]
        # Creating a variable for indexing
        index = 0
        for i in dumpdata:
            # Inserting data to mongodb client
            get_client_instance.insert_one(i)
            index += 1
            print("inserting data to mongodb #{} = {}".format(index, i["title"]))
    else:
        pass



if __name__ == '__main__':
    cronJob()