from src.data_gathering.logging import logging
from src.data_gathering.exception import CustomException
from src.data_gathering.utils import database_connection,getting_data
import sys
import streamlit as st


def main():
    try:
        st.title("data gathering")
        st.write("conneting to db")
        # conn=database_connection("International_news",'Headlines')
        st.write("conneting successfull")

        logging.info("creating the database")

        st.write("database created")
        logging.info("database created")
        if st.button("Start gathering"):
            st.write("ok sir")
            data=getting_data()
            st.dataframe(data)

            if(st.button("Export Data")):
                st.write("exporting")
    except Exception as e:
        raise CustomException(e,sys)

if __name__=="__main__":
    main()
    logging.info("start..")
    # try:
    #     # database_connection()
    #     # getting_data()
    # except Exception as e:
    #     raise CustomException(e,sys)