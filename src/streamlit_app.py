import pandas as pd
import streamlit as st
from pymongo import MongoClient

# Define mongodb details
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DB_NAME = 'Test'
COLLECTION_NAME = 'Test'

# Connect to the mongo client and db/collection
connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
collection = connection[DB_NAME][COLLECTION_NAME]

# Set the page title and icon and set layout to "wide" to minimise margains
st.set_page_config(page_title="Blog & Portfolio", page_icon=":flower:")

with st.container():
    # Add a sub header (approx <h3/>)
    st.subheader("I'm to lazy to water my plants...")
    # Add a title (approx <h1/>)
    st.title("AI Plant Watering!")
    # Add a line divider
    st.write("---")

with st.container():
    # Read data from mongoDB
    data = collection.find()
    # Load the data into a dataframe
    df = pd.DataFrame(list(data))

    st.line_chart(df["Reading"])

    if st.button("Refresh"):
        "Chart refreshed"