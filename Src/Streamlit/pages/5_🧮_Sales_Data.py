import pandas as pd
from config import *
import seaborn as sns
import streamlit as st
import plotly.express as px

# Initialize the page
page_init()


def graph_demographic_sales(df_trnsct_dmg, filter, disp_filter):
    """
    This function generates a bar chart of sales value by a specified demographic filter.

    Parameters:
    df_trnsct_dmg (DataFrame): The DataFrame containing the transaction and demographic data.
    filter (str): The demographic category to group the sales data by.
    disp_filter (str): The display name of the filter for use in the chart title and axis label.

    Returns:
    fig: The figure object of the bar chart.
    sales_by_filter (DataFrame): The DataFrame of sales data grouped by the filter, without the sales percentage column.
    """
    # Calculate total sales value
    total_sales = df_trnsct_dmg["SALES_VALUE"].sum()
    # Group sales data by the specified demographic filter
    sales_by_filter = df_trnsct_dmg.groupby(filter)["SALES_VALUE"].sum().reset_index()
    # Calculate the sales percentage for each group
    sales_by_filter["SALES_PERCENTAGE"] = (
        sales_by_filter["SALES_VALUE"] / total_sales
    ) * 100
    # Sort the data by sales value in descending order
    sales_by_filter = sales_by_filter.sort_values(by="SALES_VALUE", ascending=False)
    # Convert the demographic filter to string for display
    sales_by_filter[filter] = sales_by_filter[filter].astype(str)
    # Create a color palette for the bar chart using the Blues color palette from seaborn and remove the first two colors to avoid light colors
    colors = sns.color_palette("Blues", len(sales_by_filter) + 2).as_hex()[2:]
    # Create a bar chart using Plotly Express
    fig = px.bar(
        sales_by_filter,
        x=filter,
        y="SALES_VALUE",
        title=f"Sales Value by {disp_filter}",
        labels={filter: disp_filter, "SALES_VALUE": "Sales Value"},
        text="SALES_PERCENTAGE",
    )
    # Update the bar chart layout
    fig.update_xaxes(type="category")
    fig.update_traces(
        texttemplate="%{text:.1f}%",  # Set the text template for the hover text to show the sales percentage with one decimal place
        textposition="inside",
        marker=dict(color=colors),
    )
    fig.update_layout(
        yaxis=dict(showgrid=True),
        xaxis=dict(showgrid=False),  # Show the gridlines for the y-axis
    )
    # Return the figure object and the sales data grouped by the filter without the sales percentage column for the dataframe display
    return fig, sales_by_filter.drop("SALES_PERCENTAGE", axis=1)


def general_sales_graph(daily_sales):
    """
    This function generates a line chart of average daily sales value over time, separated by year.

    Parameters:
    daily_sales (DataFrame): The DataFrame containing the daily sales data. It must have a 'TRANS_DATE' column with dates in the format "%Y-%m-%d", and a 'SALES_VALUE' column with the sales values.

    Returns:
    fig: The figure object of the line chart.
    """
    # Convert the TRANS_DATE column to datetime format
    daily_sales["TRANS_DATE"] = pd.to_datetime(
        daily_sales["TRANS_DATE"], format="%Y-%m-%d"
    )
    # Create a new column for the day of the year and the year to show the lines as overlapping
    # Extract the day of the year and year from the date
    daily_sales["day_of_year"] = daily_sales["TRANS_DATE"].dt.dayofyear
    daily_sales["year"] = daily_sales["TRANS_DATE"].dt.year
    # Create a line chart using Plotly Express to show the average daily sales value over time, separated by year
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
        markers=True,  # Show markers on the lines for better visibility
    )
    fig.update_layout(
        title={"text": "Daily Sales Value Over Time by Year", "x": 0.35},
        xaxis=dict(
            showgrid=True,
            rangeslider=dict(
                visible=True
            ),  # Show the range slider for better navigation
        ),
        yaxis=dict(showgrid=True),  # Show the gridlines for the y-axis
    )
    return fig


def get_customer_acquisition_w_zero(df_customer_acquisition, include_zero=False):
    """
    This function processes a DataFrame of customer acquisition data, converting the 'Date_of_first_purchase' column to datetime format and optionally filling in missing dates with zero.

    Parameters:
    df_customer_acquisition (DataFrame): The DataFrame containing the customer acquisition data. It must have a 'Date_of_first_purchase' column with dates in the format "%Y-%m-%d".
    include_zero (bool): If True, the function will fill in missing dates in the 'Date_of_first_purchase' column with zero. If False, the function will return the DataFrame as is. Default is False.

    Returns:
    DataFrame: The processed DataFrame of customer acquisition data.
    """
    # Convert the 'Date_of_first_purchase' column to datetime format
    df_customer_acquisition["Date_of_first_purchase"] = pd.to_datetime(
        df_customer_acquisition["Date_of_first_purchase"], format="%Y-%m-%d"
    )
    return (
        df_customer_acquisition.set_index("Date_of_first_purchase")
        .reindex(
            pd.date_range("2012-01-01", "2013-12-31", freq="D")
        )  # Reindex the DataFrame with daily frequency filling in the missing dates
        .fillna(0)  # Fill missing values with zero
        .reset_index()
        .rename(columns={"index": "Date_of_first_purchase"})
        if include_zero
        else df_customer_acquisition  # Return the DataFrame as is if include_zero is False
    )


def fig_customer_acquisition(df_customer_acquisition):
    """
    This function generates a line chart of the number of households acquired over time.

    Parameters:
    df_customer_acquisition (DataFrame): The DataFrame containing the customer acquisition data. It must have a 'Date_of_first_purchase' column with dates and a 'Number_of_households' column with the number of households.

    Returns:
    fig (plotly.graph_objs._figure.Figure): The figure object of the line chart.
    """
    # Create a line chart using Plotly Express to show the number of households acquired over time
    fig = px.line(
        df_customer_acquisition,
        x="Date_of_first_purchase",
        y="Number_of_households",
        markers=True,  # Show markers on the data points for better visibility
        labels={
            "Date_of_first_purchase": "Date of first purchase",
            "Number_of_households": "Number of households",
        },
    )
    fig.update_layout(
        title={
            "text": "Number of households acquired over time",
            "x": 0.35,
        },  # Set the title of the line chart
        yaxis=dict(
            showgrid=True,
        ),
        xaxis=dict(showgrid=True, type="date"),
    )
    return fig


# Function to read and cache data from CSV files
@st.cache_data
def read_data():
    return (
        pd.read_csv(CLEAN_DATA_PATH + "transaction_data_cleaned.csv"),
        pd.read_csv(CLEAN_DATA_PATH + "daily_sales.csv"),
        pd.read_csv(CLEAN_DATA_PATH + "hh_demographic_cleaned.csv"),
    )


st.title("🧮 Sales Data")
# Read the cleaned transaction, daily sales, and demographic data from CSV files
df_transaction, daily_sales, df_demographic = read_data()
# Convert the TRANS_DATE column to datetime format
df_transaction["TRANS_DATE"] = pd.to_datetime(
    df_transaction["TRANS_DATE"], format="%Y-%m-%d"
)
st.write(
    f"##### The dataset contains the transaction data of {df_transaction['BASKET_ID'].nunique():,} transaction operations for the sales of {df_transaction['QUANTITY'].sum():,} items in {df_transaction['STORE_ID'].nunique()} stores from {df_transaction['TRANS_DATE'].dt.date.min()} to {df_transaction['TRANS_DATE'].dt.date.max()}"
)
st.divider()

# -- General Transaction Statistics --
st.write("- ##### General Transaction Statistics: ")
st.write("###### We explore several statistics around the transactional data")

# Calculate and display descriptive statistics of selected columns
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

# Format TRANS_DATE and TRANS_TIME columns for better display by splitting the date and time and converting to integer
df_transaction_description["TRANS_DATE"] = df_transaction_description[
    "TRANS_DATE"
].apply(
    lambda x: str(x).split(" ")[0]
)  # Split the date and time and take the date

# Format the first row of TRANS_DATE Description as it is a count
df_transaction_description["TRANS_DATE"].iloc[
    0
] = f"{int(df_transaction_description['TRANS_DATE'].iloc[0]):,}"
df_transaction_description["TRANS_DATE"].iloc[
    -1
] = "-"  # Last value of description is not applicable

# Convert Time to string, split the time and format it as HH:MM
df_transaction_description["TRANS_TIME"] = (
    df_transaction_description["TRANS_TIME"]
    .astype("str")
    .apply(
        lambda x: x.split(".")[0].zfill(4)
    )  # Split the time and fill with zeros to make it 4 digits
    .apply(lambda x: f"{x[:2]}:{x[2:]}")  # Format the time as HH:MM
)
# Format the first row of TRANS_TIME as it is a count
df_transaction_description["TRANS_TIME"].iloc[
    0
] = f"{int(df_transaction_description['TRANS_TIME'].iloc[0].replace(':','')):,}"
df_transaction_description["TRANS_TIME"].iloc[-1] = "-"
# Display the descriptive statistics of the transaction data
st.dataframe(df_transaction_description, use_container_width=True)

# -- General Sales Graph --
st.write("- ##### General Sales Graph: ")
st.write("###### We explore the average daily sales value over time")
st.plotly_chart(general_sales_graph(daily_sales))  # Display average daily sales graph
st.divider()  # Insert a divider for visual separation

# -- Sales Demographic Distribution --
st.write("- ##### Sales Demographic Distribution: ")
st.write("###### We explore the distribution of sales across different demographics")
# Merge transaction and demographic data on 'household_key' to get demographic information for each transaction
df_trnsct_dmg = df_transaction.merge(df_demographic, on="household_key", how="right")
# Replace "3" with "3+" in KID_CATEGORY_DESC
df_trnsct_dmg["KID_CATEGORY_DESC"] = (
    df_trnsct_dmg["KID_CATEGORY_DESC"].astype(str).replace("3", "3+")
)
# Replace "5" with "5+" in HOUSEHOLD_SIZE_DESC
df_trnsct_dmg["HOUSEHOLD_SIZE_DESC"] = (
    df_trnsct_dmg["HOUSEHOLD_SIZE_DESC"].astype(str).replace("5", "5+")
)
# Create columns for filter selection and graph display
col_filter, col_graph = st.columns([1, 3])
# Filter selection dropdown for demographic exploration
with col_filter:
    filter_select = st.selectbox(
        "Select the demographic to explore",
        [
            "Income",
            "Age",
            "Accomodation Status",
            "Marital Status",
            "Family Size",
            "Family Composition",
            "Number of Kids",
        ],
        index=0, # Default selection index
    )
    # Dictionary to map filter selections to corresponding columns in the dataset
    columns = {
        "Income": "INCOME_DESC",
        "Age": "AGE_DESC",
        "Marital Status": "MARITAL_STATUS_CODE",
        "Family Composition": "HH_COMP_DESC",
        "Family Size": "HOUSEHOLD_SIZE_DESC",
        "Accomodation Status": "HOMEOWNER_DESC",
        "Number of Kids": "KID_CATEGORY_DESC",
    }
    filter = columns[filter_select]
    # Generate the demographic sales graph based on selected filter
    sales_fig, sales_stat = graph_demographic_sales(
        df_trnsct_dmg, filter, filter_select
    )
    # Display statistical summary of sales data in a dataframe
    st.dataframe(sales_stat, use_container_width=True, hide_index=True)
# Display the demographic sales graph in the specified column
with col_graph:
    st.plotly_chart(sales_fig)

st.divider()

# -- Customer Acquisition --
st.write("- ##### Customer Acquisition: ")
st.write("###### We explore the number of customers acquired over time:")

# Read customer acquisition data from CSV file
df_customer_acquisition = pd.read_csv(CLEAN_DATA_PATH + "customer_acquisition.csv")
# Convert Date_of_first_purchase column to datetime format
df_customer_acquisition["Date_of_first_purchase"] = pd.to_datetime(
    df_customer_acquisition["Date_of_first_purchase"], format="%Y-%m-%d"
)
# Slider widget to select the time range for display
df_range = st.slider(
    "Select the time range to display",
    df_customer_acquisition["Date_of_first_purchase"].dt.date.min(),
    df_customer_acquisition["Date_of_first_purchase"].dt.date.max(),
    (
        df_customer_acquisition["Date_of_first_purchase"].dt.date.min(),
        df_customer_acquisition["Date_of_first_purchase"].dt.date.max(),
    ),
)
# Checkbox to include days with zero customers in the data
include_zero = st.checkbox("Include Days with Zero Customers", value=False)
# Process customer acquisition data with or without zero days
df_customer_acquisition = get_customer_acquisition_w_zero(
    df_customer_acquisition=pd.read_csv(CLEAN_DATA_PATH + "customer_acquisition.csv"),
    include_zero=include_zero,
)
# Filter data within the selected date range
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

df_customer_acquisition_description["Date_of_first_purchase"].iloc[-1] = "-" # Last value is inapplicable
# Create columns for figure and statistical summary display
col_fig, col_stat = st.columns([2, 1])

with col_stat:
    st.dataframe(df_customer_acquisition_description, use_container_width=True)
# Generate and display customer acquisition graph over time
fig = fig_customer_acquisition(df_customer_acquisition)

with col_fig:
    st.plotly_chart(fig.update_layout(xaxis=dict(range=[df_range[0], df_range[1]])))

st.divider()
