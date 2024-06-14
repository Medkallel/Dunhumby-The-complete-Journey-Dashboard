import pandas as pd
from config import *
import streamlit as st

page_init()

st.title("🧮 Transaction Data")
df_transaction = pd.read_csv(CLEAN_DATA_PATH + "transaction_data_cleaned.csv")
df_transaction["TRANS_DATE"] = pd.to_datetime(df_transaction["TRANS_DATE"], format="%Y-%m-%d")
st.write(
    f"##### The dataset contains the transaction data of {df_transaction['BASKET_ID'].nunique():,} transaction operations for the sales of {df_transaction['QUANTITY'].sum():,} items in {df_transaction['STORE_ID'].nunique()} stores from {df_transaction['TRANS_DATE'].dt.date.min()} to {df_transaction['TRANS_DATE'].dt.date.max()}"
)
st.divider()
st.write("- ##### Transactions Descriptive Statistics: ")
df_transaction_description = pd.DataFrame(
    df_transaction[
        [
            "QUANTITY",
            "SALES_VALUE",
            "RETAIL_DISC",
            "COUPON_DISC",
            "COUPON_MATCH_DISC",
            "TRANS_DATE",
            "TRANS_TIME",
        ]
    ].describe()
)
df_transaction_description["TRANS_DATE"]=df_transaction_description["TRANS_DATE"].apply(lambda x: str(x).split(" ")[0])
df_transaction_description["TRANS_DATE"].iloc[0] = f"{int(df_transaction_description['TRANS_DATE'].iloc[0]):,}"
df_transaction_description["TRANS_DATE"].iloc[-1] = "-"
df_transaction_description["TRANS_TIME"]=df_transaction_description["TRANS_TIME"].astype("str").apply(lambda x:x.split(".")[0].zfill(4)).apply(lambda x: f"{x[:2]}:{x[2:]}")
df_transaction_description["TRANS_TIME"].iloc[0]=f"{int(df_transaction_description['TRANS_TIME'].iloc[0].replace(':','')):,}"
df_transaction_description["TRANS_TIME"].iloc[-1] = "-"
st.write(df_transaction_description)
