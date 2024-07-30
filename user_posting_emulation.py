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

        # self.HOST = "pinterestdbreadonly.cq2e8zno855e.eu-west-1.rds.amazonaws.com"
        # self.USER = 'project_user'
        # self.PASSWORD = ':t%;yCY3Yjg'
        # self.DATABASE = 'pinterest_data'
        # self.PORT = 3306
        pass 

    def read_db_creds(self, file_path : str):
        with open(file_path) as file: 
            credentials = yaml.safe_load(file)
            return credentials 
        
    def create_db_connector(self, credentials : dict):

        HOST = credentials['HOST']
        USER = credentials['USER']
        PASSWORD = credentials['PASSWORD']
        DATABASE = credentials['DATABASE']
        PORT = credentials['PORT']

        engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf8mb4")
        return engine


new_connector = AWSDBConnector()


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

            geo_string = text(f"SELECT * FROM geolocation_data LIMIT {random_row}, 1")
            geo_selected_row = connection.execute(geo_string)
            
            for row in geo_selected_row:
                geo_result = dict(row._mapping)

            user_string = text(f"SELECT * FROM user_data LIMIT {random_row}, 1")
            user_selected_row = connection.execute(user_string)
            
            for row in user_selected_row:
                user_result = dict(row._mapping)
            
            print(pin_result)
            print(geo_result)
            print(user_result)


if __name__ == "__main__":
    run_infinite_post_data_loop()
    print('Working')
    
    


