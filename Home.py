import streamlit as st
import pandas as pd
from query import view_all_data 
import plotly.express as px
from numerize.numerize import numerize
from query import *  
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Interruption Data analysis Dashboard", page_icon="🌍", layout="wide")
st.subheader("Interruption Data analysis Dashboard")
st.markdown("##")

#Here I'm fetching data from database(SQL)
result = view_all_data()
df = pd.DataFrame(result, columns=["CIRCLE", "DISTRICT", "ZONE_ID", "GRID_NAME", "FEEDER_NAME", "SUBSTATION_NAME", "OPEN_DATE", "CLOSE_DATE", "FAULT_TYPE","FAULT_REASON","id"])
st.dataframe(df)

#Sidebar
st.sidebar.subheader("Visualization Settings")

#Switch for visualization
st.sidebar.header("Please select the Options")
CIRCLE = st.sidebar.multiselect(
    "Select the Circle",
    options=df["CIRCLE"].unique(),
    default=df["CIRCLE"].unique(),
)

DISTRICT = st.sidebar.multiselect(
    "Select the District",
    options=df["DISTRICT"].unique(),
    default=df["DISTRICT"].unique(),
)

ZONE = st.sidebar.multiselect(
    "Select the ZONE",
    options=df["ZONE_ID"].unique(),
    
)

Feeder = st.sidebar.multiselect(
    "Select the Feeder",
    options=df["FEEDER_NAME"].unique(),
    default=df["FEEDER_NAME"].unique(),
)

df_selection = df.query(
    "CIRCLE == @CIRCLE & DISTRICT == @DISTRICT & ZONE_ID == @ZONE & FEEDER_NAME == @Feeder"
)

def Home():
    with st.expander("Tabular"):
        showData = st.multiselect('Filter:', df_selection.columns, default=[])
        st.write(df_selection[showData])
    #compute top analystics
        total_