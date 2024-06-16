import pandas as pd
from config import *
import streamlit as st

# Initialize the Streamlit page settings
page_init()

st.title("🔍 Data Exploration")

# Introduction text explaining the focus of the study
st.write(
    "##### Due to the complexity of the data, we decided to focus on studying the customer demographics and how they affect the revenue and financials of the retailer.",
    "\n",
    "##### So we will be using the following datasets: [HH_DEMOGRAPHIC, TRANSACTION_DATA, PRODUCT]",
)
st.divider()

# --Missing Values section--
st.subheader("Missing Values")
# Information about missing values in the datasets
st.info(
    "Several datasets have missing values, those missing values however are not present as NaN... They are present as empty strings or strings with the values 'U' or 'UNKNOWN'",
)

# --Transaction Dataset section--
st.markdown("- ##### The Transaction Data has no missing values but has missing days.")

# --Product Dataset section--
# Load the Product dataset and calculate missing values
df_product_missing = (
    pd.read_csv(DATASET_PATH + "product.csv")
    .replace(
        [" ", "NO COMMODITY DESCRIPTION", "NO SUBCOMMODITY DESCRIPTION"], pd.NA
    )  # Replace empty strings and equivalent missing values with NA
    .isna()
    .sum()  # Count the missing values
    .sort_values(ascending=False)
    .rename("Nb Missing Values")
)
# Display information about missing values in the Product Data
st.markdown(
    f"- ##### The Product Data has several missing values in the following columns:"
)
st.code(
    f"[{', '.join(df_product_missing[df_product_missing>0].index.to_list())}]"
)  # Display the column list in a code block for visibility
st.dataframe(df_product_missing)  # Display the missing values in a dataframe

# --Household Demographic Dataset section--
# Load the Household Demographic dataset and calculate missing values
df_hh_demographic_missing = (
    pd.read_csv(DATASET_PATH + "hh_demographic.csv")
    .replace(
        [r"\bUnknown\b|\bUnknown\w*|\w*Unknown\b", "U"], pd.NA, regex=True
    )  # Replace 'U' and all strings having 'Unknwown' values with NA using regex
    .isna()
    .sum()
    .sort_values(ascending=False)
    .rename("Nb Missing Values")
)
# Display information about missing values in the Household Demographic Data
st.markdown(
    f"- ##### The Household Demographic Data has several missing values in the following columns:"
)
st.code(
    f"[{', '.join(df_hh_demographic_missing[df_hh_demographic_missing>0].index.tolist())}]"
)
st.dataframe(df_hh_demographic_missing)

# Additional information about other missing data found in daily sales data and other metrics
st.write(
    "- ##### Other missing data was also found when generating the daily sales data and other metrics, we will explore how we handled this in the notebook."
)

# Add a download button to download the notebook where missing data was handled
st.info("Check the notebook to see how the missing data was handled")
st.download_button(
    "Download Notebook",
    data=open(NOTEBOOK_PATH, "rb").read(),
    file_name="Data_Exploration-Preprocessing.ipynb",
    mime="application/zip",
    type="primary",
)
