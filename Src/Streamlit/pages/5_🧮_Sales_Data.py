import pandas as pd
from config import *
import seaborn as sns
import streamlit as st
import plotly.express as px

page_init()


def graph_demographic_sales(df_trnsct_dmg, filter, disp_filter):
    total_sales = df_trnsct_dmg["SALES_VALUE"].sum()
    sales_by_filter = df_trnsct_dmg.groupby(filter)["SALES_VALUE"].sum().reset_index()
    sales_by_filter["SALES_PERCENTAGE"] = (
        sales_by_filter["SALES_VALUE"] / total_sales
    ) * 100
    sales_by_filter = sales_by_filter.sort_values(by="SALES_VALUE", ascending=False)
    sales_by_filter[filter] = sales_by_filter[filter].astype(str)
    colors = sns.color_palette("Blues", len(sales_by_filter) + 2).as_hex()[2:]
    fig = px.bar(
        sales_by_filter,
        x=filter,
        y="SALES_VALUE",
        title=f"Sales Value by {disp_filter}",
        labels={filter: disp_filter, "SALES_VALUE": "Sales Value"},
        text="SALES_PERCENTAGE",
    )

    fig.update_xaxes(type="category")
    fig.update_traces(
        texttemplate="%{text:.1f}%", textposition="inside", marker=dict(color=colors)
    )
    fig.update_layout(yaxis=dict(showgrid=True), xaxis=dict(showgrid=False))
    return fig, sales_by_filter.drop("SALES_PERCENTAGE", axis=1)


def general_sales_graph(daily_sales):
    daily_sales["TRANS_DATE"] = pd.to_datetime(
        daily_sales["TRANS_DATE"], format="%Y-%m-%d"
    )
    daily_sales["day_of_year"] = daily_sales["TRANS_DATE"].dt.dayofyear
    daily_sales["year"] = daily_sales["TRANS_DATE"].dt.year
    fig = px.line(
        daily_sales,
        x="day_of_year",
        y="SALES_VALUE",
        color="year",
        labels={
            "day_of_year": "Day of Year",
            "SALES_VALUE": "Average Daily Sales Value",
            "year": "Year",
        },
        markers=True,
    )
    fig.update_layout(
        title={"text": "Daily Sales Value Over Time by Year", "x": 0.35},
        xaxis=dict(
            showgrid=True,
            rangeslider=dict(visible=True),
        ),
        yaxis=dict(showgrid=True),
    )
    return fig


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
        yaxis=dict(
            showgrid=True,
        ),
        xaxis=dict(showgrid=True, type="date"),
    )
    return fig


@st.cache_data
def read_data():
    return (
        pd.read_csv(CLEAN_DATA_PATH + "transaction_data_cleaned.csv"),
        pd.read_csv(CLEAN_DATA_PATH + "daily_sales.csv"),
        pd.read_csv(CLEAN_DATA_PATH + "hh_demographic_cleaned.csv"),
    )


st.title("🧮 Sales Data")
df_transaction, daily_sales, df_demographic = read_data()
df_transaction["TRANS_DATE"] = pd.to_datetime(
    df_transaction["TRANS_DATE"], format="%Y-%m-%d"
)
st.write(
    f"##### The dataset contains the transaction data of {df_transaction['BASKET_ID'].nunique():,} transaction operations for the sales of {df_transaction['QUANTITY'].sum():,} items in {df_transaction['STORE_ID'].nunique()} stores from {df_transaction['TRANS_DATE'].dt.date.min()} to {df_transaction['TRANS_DATE'].dt.date.max()}"
)
st.divider()
st.write("- ##### General Transaction Statistics: ")
st.write("###### We explore several statistics around the transactional data")
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
st.dataframe(df_transaction_description, use_container_width=True)
st.write("- ##### General Sales Graph: ")
st.write("###### We explore the average daily sales value over time")
st.plotly_chart(general_sales_graph(daily_sales))
st.divider()
st.write("- ##### Sales Demographic Distribution: ")
st.write("###### We explore the distribution of sales across different demographics")
df_trnsct_dmg = df_transaction.merge(df_demographic, on="household_key", how="right")
df_trnsct_dmg["KID_CATEGORY_DESC"] = (
    df_trnsct_dmg["KID_CATEGORY_DESC"].astype(str).replace("3", "3+")
)
col_filter, col_graph = st.columns([1, 3])
with col_filter:
    filter_select = st.selectbox(
        "Select the demographic to explore",
        [
            "Income",
            "Age",
            "Accomodation Status",
            "Marital Status",
            "Family Composition",
            "Number of Kids",
        ],
        index=0,
    )
    columns = {
        "Income": "INCOME_DESC",
        "Age": "AGE_DESC",
        "Marital Status": "MARITAL_STATUS_CODE",
        "Family Composition": "HH_COMP_DESC",
        "Accomodation Status": "HOMEOWNER_DESC",
        "Number of Kids": "KID_CATEGORY_DESC",
    }
    filter = columns[filter_select]
    sales_fig, sales_stat = graph_demographic_sales(
        df_trnsct_dmg, filter, filter_select
    )
    st.dataframe(sales_stat, use_container_width=True, hide_index=True)
with col_graph:
    st.plotly_chart(sales_fig)

st.divider()
st.write("- ##### Customer Acquisition: ")
st.write("###### We explore the number of customers acquired over time:")
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
col_fig, col_stat = st.columns([2, 1])

with col_stat:
    st.dataframe(df_customer_acquisition_description, use_container_width=True)

fig = fig_customer_acquisition(df_customer_acquisition)

with col_fig:
    st.plotly_chart(fig.update_layout(xaxis=dict(range=[df_range[0], df_range[1]])))

st.divider()

