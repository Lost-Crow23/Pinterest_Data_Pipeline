import requests 
import yaml 
from time import sleep
import random
from multiprocessing import Process
import boto3
import json
from sqlalchemy import create_engine
from sqlalchemy import text


random.seed(100)


class AWSDBConnector:

    def __init__(self):
        pass 

    def read_db_creds(self, file_path : str):
        try:
            with open(file_path) as file: 
                credentials = yaml.safe_load(file)
                return credentials
        except FileNotFoundError:
            print("credentials file not found, create it with the correct credentials. ")
            return {}

        
    def create_db_connector(self, credentials : dict):

        HOST = credentials['HOST']
        USER = credentials['USER']
        PASSWORD = credentials['PASSWORD']
        DATABASE = credentials['DATABASE']
        PORT = credentials['PORT']

        engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf8mb4")
        return engine


new_connector = AWSDBConnector()

def send_data_to_Kafka(data, topic_name, payload):
    invoke_url = "https://1w4otinw69.execute-api.us-east-1.amazonaws.com/dev"
    url = invoke_url + "/topics/" + topic_name
    print(url)

    headers = {'Content-Type': 'application/vnd.kafka.json.v2+json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.status_code)

    return

def run_infinite_post_data_loop():
    while True:
        sleep(random.randrange(0, 2))
        random_row = random.randint(0, 11000)
        db_creds = new_connector.read_db_creds('db_creds.yaml')
        engine = new_connector.create_db_connector(db_creds)

        with engine.connect() as connection:

            pin_string = text(f"SELECT * FROM pinterest_data LIMIT {random_row}, 1")
            pin_selected_row = connection.execute(pin_string)
            
            for row in pin_selected_row:
                pin_result = dict(row._mapping)
                topic_name = "124eb5889d67.pin"
                payload = json.dumps({
                    "records": [
                        {
                        "value": {"index": pin_result["index"],
                            "unique_id": pin_result["unique_id"],
                            "title": pin_result["title"],
                            "description": pin_result["description"],
                            "poster_name": pin_result["poster_name"],
                            "follower_count": pin_result["follower_count"],
                            "tag_list": pin_result["tag_list"],
                            "is_image_or_video": pin_result["is_image_or_video"],
                            "image_src": pin_result["image_src"],
                            "downloaded": pin_result["downloaded"],
                            "save_location": pin_result["save_location"],
                            "category": pin_result["category"]}
                        }
                    ]
                })
                send_data_to_Kafka(pin_result, topic_name, payload)
                print("pin result sent")

            geo_string = text(f"SELECT * FROM geolocation_data LIMIT {random_row}, 1")
            geo_selected_row = connection.execute(geo_string)
            
            for row in geo_selected_row:
                geo_result = dict(row._mapping)
                topic_name = "124eb5889d67.geo"
                payload = json.dumps({
                    "records":  [
                        {
                        "value": {"ind": geo_result["ind"],
                                "timestamp": geo_result["timestamp"].isoformat(), 
                                "latitude": geo_result["latitude"],
                                "longitude": geo_result["longitude"],
                                "country": geo_result["country"]}        
                        }
                    ]
                })
                send_data_to_Kafka(geo_result, topic_name, payload)
                print("geo result sent")

            user_string = text(f"SELECT * FROM user_data LIMIT {random_row}, 1")
            user_selected_row = connection.execute(user_string)
            
            for row in user_selected_row:
                user_result = dict(row._mapping)
                topic_name = "124eb5889d67.user"
                payload = json.dumps({
                    "records": [
                        {
                        "value": {"ind": user_result["ind"],
                                "first_name": user_result["first_name"],
                                "last_name": user_result["last_name"],
                                "age": user_result["age"],
                                "date_joined": user_result["date_joined"].isoformat()}
                        }
                    ]
                })
                send_data_to_Kafka(user_result, topic_name, payload)
                print("user result sent")
                
            # print(pin_result)
            # print(geo_result)
            # print(user_result)


if __name__ == "__main__":
    run_infinite_post_data_loop()
    print('Working')
    
    


