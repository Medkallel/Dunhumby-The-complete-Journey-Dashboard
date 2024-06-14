import pandas as pd
from config import *
import streamlit as st
import plotly.express as px

page_init()


def get_customer_acquisition_w_zero(df_customer_acquisition, include_zero=False):
    df_customer_acquisition["Date_of_first_purchase"] = pd.to_datetime(
        df_customer_acquisition["Date_of_first_purchase"], format="%Y-%m-%d"
    )
    return (
        df_customer_acquisition.set_index("Date_of_first_purchase")
        .reindex(pd.date_range("2012-01-01", "2013-12-31", freq="D"))
        .fillna(0)
        .reset_index()
        .rename(columns={"index": "Date_of_first_purchase"})
        if include_zero
        else df_customer_acquisition
    )

def fig_customer_acquisition(df_customer_acquisition):
    fig = px.line(
        df_customer_acquisition,
        x="Date_of_first_purchase",
        y="Number_of_households",
        markers=True,
        labels={
            "Date_of_first_purchase": "Date of first purchase",
            "Number_of_households": "Number of households",
        },
    )
    fig.update_layout(
        title={"text": "Number of households acquired over time", "x": 0.35},
        yaxis=dict(showgrid=True),
        xaxis=dict(
            showgrid=True,
        type="date"
    )
    )
    return fig


st.title("🧮 Transaction Data")
df_transaction = pd.read_csv(CLEAN_DATA_PATH + "transaction_data_cleaned.csv")
df_transaction["TRANS_DATE"] = pd.to_datetime(
    df_transaction["TRANS_DATE"], format="%Y-%m-%d"
)
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
df_transaction_description["TRANS_DATE"] = df_transaction_description[
    "TRANS_DATE"
].apply(lambda x: str(x).split(" ")[0])
df_transaction_description["TRANS_DATE"].iloc[
    0
] = f"{int(df_transaction_description['TRANS_DATE'].iloc[0]):,}"
df_transaction_description["TRANS_DATE"].iloc[-1] = "-"
df_transaction_description["TRANS_TIME"] = (
    df_transaction_description["TRANS_TIME"]
    .astype("str")
    .apply(lambda x: x.split(".")[0].zfill(4))
    .apply(lambda x: f"{x[:2]}:{x[2:]}")
)
df_transaction_description["TRANS_TIME"].iloc[
    0
] = f"{int(df_transaction_description['TRANS_TIME'].iloc[0].replace(':','')):,}"
df_transaction_description["TRANS_TIME"].iloc[-1] = "-"
st.write(df_transaction_description)

st.divider()

st.write("- ##### Customer Acquisition: ")

df_customer_acquisition = pd.read_csv(CLEAN_DATA_PATH + "customer_acquisition.csv")
df_customer_acquisition["Date_of_first_purchase"] = pd.to_datetime(
    df_customer_acquisition["Date_of_first_purchase"], format="%Y-%m-%d"
)
df_range = st.slider(
    "Select the time range to display",
    df_customer_acquisition["Date_of_first_purchase"].dt.date.min(),
    df_customer_acquisition["Date_of_first_purchase"].dt.date.max(),
    (
        df_customer_acquisition["Date_of_first_purchase"].dt.date.min(),
        df_customer_acquisition["Date_of_first_purchase"].dt.date.max(),
    ),
)
include_zero = st.checkbox("Include Days with Zero Customers", value=False)
df_customer_acquisition = get_customer_acquisition_w_zero(
    df_customer_acquisition=pd.read_csv(CLEAN_DATA_PATH + "customer_acquisition.csv"),
    include_zero=include_zero,
)
df_customer_acquisition = df_customer_acquisition[
    (df_customer_acquisition["Date_of_first_purchase"] >= pd.to_datetime(df_range[0]))
    & (df_customer_acquisition["Date_of_first_purchase"] <= pd.to_datetime(df_range[1]))
]
df_customer_acquisition_description = df_customer_acquisition.describe()
df_customer_acquisition_description["Date_of_first_purchase"] = (
    df_customer_acquisition_description["Date_of_first_purchase"].apply(
        lambda x: str(x).split(" ")[0]
    )
)
df_customer_acquisition_description["Date_of_first_purchase"].iloc[-1] = "-"
col_fig,col_stat = st.columns([2,1])

with col_stat:
    st.dataframe(df_customer_acquisition_description)

fig = fig_customer_acquisition(df_customer_acquisition)

with col_fig:
    st.plotly_chart(fig.update_layout(xaxis=dict(range=[df_range[0], df_range[1]])))