import pandas as pd
from config import *
import streamlit as st

page_init()

st.title("🔍 Data Exploration")
st.write(
    "##### Due to the complexity of the data, we decided to focus on studying the customer demographics and how they affect the revenue and financials of the retailer.",
    "\n",
    "##### So we will be using the following datasets: [HH_DEMOGRAPHIC, TRANSACTION_DATA, PRODUCT]",
)
st.divider()
st.subheader("Missing Values")
st.info(
    "Several datasets have missing values, those missing values however are not present as NaN... They are present as empty strings or strings with the values 'U' or 'UNKNOWN'"
)
st.markdown("- ##### The Transaction Data has no missing values")
df_product_missing = (
    pd.read_csv(DATASET_PATH + "product.csv")
    .replace([" ", "NO COMMODITY DESCRIPTION", "NO SUBCOMMODITY DESCRIPTION"], pd.NA)
    .isna()
    .sum()
    .sort_values(ascending=False)
    .rename("Nb Missing Values")
)
st.markdown(
    f"- ##### The Product Data has several missing values in the following columns:"
)
st.code(f"[{', '.join(df_product_missing[df_product_missing>0].index.to_list())}]")
st.dataframe(df_product_missing)
df_hh_demographic_missing = (
    pd.read_csv(DATASET_PATH + "hh_demographic.csv")
    .replace([r"\bUnknown\b|\bUnknown\w*|\w*Unknown\b", "U"], pd.NA, regex=True)
    .isna()
    .sum()
    .sort_values(ascending=False)
    .rename("Nb Missing Values")
)
st.markdown(
    f"- ##### The Household Demographic Data has several missing values in the following columns:"
)
st.code(
    f"[{', '.join(df_hh_demographic_missing[df_hh_demographic_missing>0].index.tolist())}]"
)
st.dataframe(df_hh_demographic_missing)
st.info("Check the notebook to see how the missing data was handled")
st.download_button(
    "Download Notebook",
    data=open(NOTEBOOK_PATH, "rb").read(),
    file_name="Data_Exploration-Preprocessing.ipynb",
    mime="application/zip",
    type="primary",
)
