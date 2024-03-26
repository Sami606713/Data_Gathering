from src.data_gathering.logging import logging
from src.data_gathering.exception import CustomException
import pymysql,os,sys
from dotenv import load_dotenv
import requests
import pandas as pd
import streamlit as st

load_dotenv()

host=os.getenv('host')
user=os.getenv('user')
password=os.getenv('password')

def connection():
    try:
        logging.info("Connecting to database")

        conn=pymysql.connect(
            host=host,
            user=user,
            password=password
        )
        logging.info("connection successfully")
        return conn
        # return create_db(conn=conn,database_name=database_name,table_name=table_name)
    except Exception as e:
        raise CustomException(e,sys)

def database_connection(database_name,table_name):
    try:
        return create_db(conn=connection(),database_name=database_name,table_name=table_name)
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
        query = f"""CREATE TABLE if not exists {database_name}.{table_name} (
                news_id INTEGER PRIMARY KEY AUTO_INCREMENT,
                author VARCHAR(50) DEFAULT NULL,
                title VARCHAR(250) DEFAULT NULL,
                description TEXT DEFAULT NULL,
                published_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                content TEXT DEFAULT NULL,
                url VARCHAR(255) DEFAULT NULL,
                url_to_image VARCHAR(255) DEFAULT NULL
            );"""

        cursor.execute(query)
            
        conn.commit()
        logging.info("database created")

def getting_data():
    api=os.getenv("api")
    # st.write(api)
    url=f'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={api}'
    response=requests.get(url)
    # print(response.json()['articles'])
    response=response.json()['articles']

    return response
    # return insert_data(conn=connection(),response=response)

from datetime import datetime

def insert_data(dic):
    try:
        conn = connection()  # Assuming connection() returns a valid connection object
        with conn.cursor() as cursor:
            # Iterate over each row in the DataFrame
            for row in dic.to_dict('records'):
                # Convert the datetime string to a valid MySQL datetime format
                published_at = datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%SZ')
                
                query = """INSERT INTO International_news.headlines 
                           (news_id, author, title, description, published_at, content, url, url_to_image) 
                           VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
                data = (None, row['author'], row['title'], row['desc'], 
                        published_at, row['content'], row['url'], row['url-to-image'])
                cursor.execute(query, data)
        conn.commit()
        st.success("Successfully Inserted Data Into The Database.")
        logging.info("Data Insert Data Successfully")
    except Exception as e:
        st.write("Error:", e)
    finally:
        conn.close()  # Make sure to close the connection after use

def clean_data(response):
    # st.write("ok")
    # response=response
    author=[]
    title=[]
    desc=[]
    content=[]
    pub_date=[]
    url=[]
    url_to_image=[]
    for i in response:
        # st.write("clean your data")
        # st.write(i["author"])
        author.append(i["author"])

        # st.write(i["title"])
        title.append(i["title"])

        # st.write(i["description"])
        desc.append(i["description"])

        # st.write(i["content"])
        content.append(i["content"])

        # st.write(i["publishedAt"])
        pub_date.append(i["publishedAt"])

        # st.write(i["url"])
        url.append(i["url"])

        # st.write(i["urlToImage"])
        url_to_image.append(i["urlToImage"])
        # st.write(i)
        # break
    dic={
        'author':author,
        'title':title,
        'desc':desc,
        'content':content,
        'date':pub_date,
        'url':url,
        'url-to-image':url_to_image
    }

    return pd.DataFrame(dic)