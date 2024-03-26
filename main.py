from src.data_gathering.logging import logging
from src.data_gathering.exception import CustomException
from src.data_gathering.utils import database_connection,getting_data,insert_data,clean_data
import sys,time
import streamlit as st

def page_cnfig():
    st.set_page_config(
    page_title="Gather New Data",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://docs.streamlit.io',
        # 'Report a Bug': 'https://github.com/streamlit/streamlit/issues',
        'About': '# This app contain the data from news api and store in my data base.'
    }
    )
def main():
    try:
        page_cnfig()
        st.title("News Data Gathering 📰🚀")
        st.success("Conneting to database")
        time.sleep(2)
        conn=database_connection("International_news",'headlines')
        st.success("Connection Successfull")

        time.sleep(2)
        st.success("Creating Database")
        logging.info("creating the database")

        time.sleep(2)
        st.success("Database Created")
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
            with st.status("Exporting data..."):
                dic=clean_data(session_state.data)
                # st.write(dic)
                insert_data(dic=dic)
                st.write("Searching for data...")
                time.sleep(2)
    except Exception as e:
        st.error("Error In your DataBase")
        raise CustomException(e,sys)

if __name__=="__main__":
    main()
    logging.info("start..")

