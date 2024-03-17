from src.data_gathering.logging import logging
from src.data_gathering.exception import CustomException
import pymysql,os,sys
from dotenv import load_dotenv
import requests

load_dotenv()

host=os.getenv('host')
user=os.getenv('user')
password=os.getenv('password')

def database_connection(database_name,table_name):
    try:
        logging.info("Connecting to database")

        conn=pymysql.connect(
            host=host,
            user=user,
            password=password
        )
        logging.info("connection successfull")
        return create_db(conn=conn,database_name=database_name,table_name=table_name)
    except Exception as e:
        raise CustomException(e,sys)

def create_db(conn,database_name,table_name):
    try:
        logging.info("creating the database")
        with conn.cursor() as cursor:
            query=f"""create database if not exists {database_name}"""

            cursor.execute(query)
            
            conn.commit()
            create_table(conn=conn,database_name=database_name,table_name=table_name)
            logging.info("database created")
    except Exception as e:
        raise CustomException(e,sys)


def create_table(conn,database_name,table_name):
    with conn.cursor() as cursor:
        query = f"""CREATE TABLE {database_name}.{table_name} (
            author VARCHAR(50) DEFAULT NULL,
            title VARCHAR(250) DEFAULT NULL,
            description TEXT DEFAULT NULL,
            published_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            content TEXT DEFAULT NULL,
            url varchar(255) default null,
            url_to_image varchar(255) default null
        )"""

        cursor.execute(query)
            
        conn.commit()
        logging.info("database created")

def getting_data():
    url='https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=be805478ab5840a3b820a974b56fe770'
    response=requests.get(url)
    print(response.json()['articles'])
    return response.json()['articles']

def insert_data(conn,response):
    pass