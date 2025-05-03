import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
import json

st.set_page_config(page_icon="📌", layout="wide")
st.title("Proyecto integrador - API")
st.title("https://miguela173.github.io/Planifyy/")
df= pd.read_csv("dataset/planiffy_users.csv")
st.dataframe(df)
