from src.data_gathering.logging import logging
from src.data_gathering.exception import CustomException
from src.data_gathering.utils import database_connection,getting_data,insert_data,clean_data
import sys,time
import streamlit as st

def main():
    try:
        st.title("data gathering")
        st.write("conneting to db")
        conn=database_connection("International_news",'headlines')
        st.write("conneting successfull")

        logging.info("creating the database")

        st.write("database created")
        logging.info("database created")
        session_state = st.session_state
        if "data" not in session_state:
            session_state.data = None

        # dic = None
        if st.button("View Data"):
            # st.write("ok sir")
            session_state.data=data=getting_data()
            dic=clean_data(session_state.data)
            st.dataframe(dic)
            # st.write(dic['title'])
        if session_state.data is not None and st.button("Export Data"):
            st.write("exporting")
            with st.status("Exporting data..."):
                dic=clean_data(session_state.data)
                # st.write(dic)
                insert_data(dic=dic)
                st.write("Searching for data...")
                time.sleep(2)
                # st.write(f"done {dic}")
                # time.sleep(1)
                # st.write("Downloading data...")
                # # insert_data()
                # time.sleep(1)
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

