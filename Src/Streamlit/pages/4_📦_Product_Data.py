import pandas as pd
from config import *
import streamlit as st
page_init()
st.title("📦 Product Data")

# Load the product data
df_products = pd.read_csv(CLEAN_DATA_PATH + "product_cleaned.csv")
st.write(
    f"##### The dataset contains the product data of {df_products['PRODUCT_ID'].nunique():,} unique products sold by the retailer"
)
st.divider()

st.write("- ##### General Product Statistics: ")
st.write("###### We explore several statistics around the product data")
st.write(df_products.describe(include="all"))
st.dataframe(df_products.head())