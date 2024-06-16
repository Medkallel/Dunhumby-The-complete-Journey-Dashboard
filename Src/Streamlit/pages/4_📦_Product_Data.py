import numpy as np
import pandas as pd
from config import *
from PIL import Image
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def graph_product_sales_price(sales_by_product, sales_range, product_range):
    """
    This function generates a scatter plot of product sales value versus product shelf price.

    Parameters:
    sales_by_product (DataFrame): The DataFrame containing the sales data by product.
    sales_range (list): The range of sales values to display on the y-axis.
    product_range (list): The range of product prices to display on the x-axis.

    Returns:
    fig (plotly.graph_objs._figure.Figure): The figure object of the scatter plot.
    """
    # Add a log-transformed column for sales value to use it as color for visibility
    sales_by_product["SALES_VALUE_LOG"] = np.log10(sales_by_product["SALES_VALUE"])

    # Create a scatter plot using Plotly Express
    fig = px.scatter(
        sales_by_product,
        x="PRODUCT_SHELF_PRICE",
        y=sales_by_product["SALES_VALUE"],
        title="Product Sales Value vs Product Shelf Price",
        log_y=True,  # Use logarithmic scale for y-axis for better visibility
        # Set the labels for the x and y axes
        labels={
            "PRODUCT_SHELF_PRICE": "Product Shelf Price",
            "SALES_VALUE": "Sales Value",
        },
        # Set the hover data to display the product ID and sales value when hovering over a data point
        hover_data={
            "PRODUCT_ID": True,
            "SALES_VALUE": ":,.2f",
            "SALES_VALUE_LOG": False,
        },
        color="SALES_VALUE_LOG",  # Use the log-transformed sales value as color for visibility
    )

    fig.update_layout(
        coloraxis_colorbar=dict(
            title="Sales Value",
            ticksuffix="00 K $",  # Set the colorbar title and tick suffix for the color axis for correct labeling even with the log transformation
        ),
        yaxis=dict(
            tickprefix="$", range=sales_range  # Set the y-axis range and tick prefix
        ),
        xaxis=dict(
            tickprefix="$", range=product_range  # Set the x-axis range and tick prefix
        ),
    )
    fig.update_traces(marker=dict(size=3))  # Set the marker size for better visibility
    # Return the figure object
    return fig


def graph_word_cloud(df_trnsct_prod):
    """
    This function generates a word cloud based on the frequency of product departments in the transactions.

    Parameters:
    df_trnsct_prod (DataFrame): The DataFrame containing the transaction data merged with the product data.

    Returns:
    fig (matplotlib.figure.Figure): The figure object of the word cloud.
    """
    # Concatenate all department names into a single string
    frequence_produits = df_trnsct_prod["DEPARTMENT"]
    frequence_produits = " ".join(v for v in frequence_produits)

    # Calculate the frequency of each department using log transformation for better visualization
    frequence_produits = np.log(df_trnsct_prod["DEPARTMENT"].value_counts())

    # Load the mask image for the word cloud and crop it to the desired shape
    mask = np.invert(np.array(Image.open("./Assets/WordCloudMask.png")))[::, 150:850]
    # Generate the word cloud
    wordcloud = WordCloud(
        background_color="white",
        mask=mask,
        contour_color="#263238",
        contour_width=10,
    ).generate_from_frequencies(
        frequence_produits  # Create the word cloud based on the frequency of departments
    )

    fig = plt.figure()  # Create a figure for the word cloud
    plt.imshow(
        wordcloud, interpolation="bilinear"
    )  # Load the word cloud with bilinear interpolation
    plt.axis("off")
    return fig


# Page configuration
page_init()
st.title("📦 Product Data")

# Load the product data
df_products = pd.read_csv(CLEAN_DATA_PATH + "product_cleaned.csv")
df_trnsct = pd.read_csv(CLEAN_DATA_PATH + "transaction_data_cleaned.csv")
df_trnsct_prod = df_trnsct.merge(df_products, on="PRODUCT_ID", how="left")

st.write(
    f"##### The dataset contains the product data of {df_products['PRODUCT_ID'].nunique():,} unique products sold by the retailer"  # Display the number of unique products
)
st.divider()

# -- General Product Statistics --
st.write("- ##### General Product Statistics: ")
st.write("###### We explore several statistics around the product data")
st.dataframe(
    df_products.describe(include="all")[:4],
    use_container_width=True,  # Display the product statistics in the product dataframe. We use the the first 4 and include all because of the string data
)

# -- Product Presence --
st.write("- ##### Product Presence: ")
st.write(
    "##### We explore the presence of each deprtment of products in the catalogue of sold products"
)
# Create columns for word cloud and product presence statistics
col_wordcloud, col_stat_presence_products = st.columns(2)
with col_wordcloud:
    # Display the word cloud of how much products are sold in each department
    st.pyplot(graph_word_cloud(df_trnsct_prod, df_products))
with col_stat_presence_products:
    # Display the value counts of product departments and how much products are sold in each department
    st.dataframe(
        df_trnsct_prod["DEPARTMENT"]
        .replace(
            df_trnsct_prod["DEPARTMENT"].value_counts().index[11], pd.NA  # Exclude the 11th department as it is empty
        ) 
        .value_counts(),
        height=700,
        use_container_width=True,
    )
st.divider()

# -- Product Categories and Sales --
st.write("- ##### Product Categories and Sales: ")
# Create columns for department, commodity, and sub-commodity sales and display the top 10 elements in each
col_department, col_commodity, col_subcommodity = st.columns(3)

# -- By Department --
with col_department:
    st.write("###### By Department:")
    st.caption("High Level")
    sales_by_department = (
        df_trnsct_prod.groupby("DEPARTMENT")["SALES_VALUE"].sum().reset_index()
    )
    top_10_departments = sales_by_department.nlargest(10, "SALES_VALUE") # Get the top 10 elements with the highest sales value
    st.dataframe(top_10_departments, use_container_width=True, hide_index=True) # Display the top 10 elements

# -- By Commodity --
with col_commodity:
    st.write("###### By Commodity:")
    st.caption("Lower Level")
    sales_by_commodity = (
        df_trnsct_prod.groupby("COMMODITY_DESC")["SALES_VALUE"].sum().reset_index()
    )
    top_10_commodities = sales_by_commodity.nlargest(10, "SALES_VALUE")
    st.dataframe(top_10_commodities, use_container_width=True, hide_index=True)

# -- By Sub_Commodity --
with col_subcommodity:
    st.write("######  By Sub_Commodity:")
    st.caption("Lowest Level")
    sales_by_subcommodity = (
        df_trnsct_prod.groupby("SUB_COMMODITY_DESC")["SALES_VALUE"].sum().reset_index()
    )
    top_10_subcommodities = sales_by_subcommodity.nlargest(10, "SALES_VALUE")
    st.dataframe(top_10_subcommodities, use_container_width=True, hide_index=True)

st.divider()
# -- Product Sales / Product Price --
st.write("- ##### Product Sales / Product Price: ")
st.write(
    "###### We explore the relationship between the sales value and the price of the products"
)
# Group sales by product and calculate total sales value
sales_by_product = (
    df_trnsct_prod.groupby("PRODUCT_ID")["SALES_VALUE"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)
# Merge the sales data with the product data to add the product shelf prices to the sales data
sales_by_product["PRODUCT_SHELF_PRICE"] = sales_by_product.merge(
    df_products, on="PRODUCT_ID", how="left"
)["PRODUCT_SHELF_PRICE"]
sales_by_product = sales_by_product[(sales_by_product["SALES_VALUE"] > 1)]

# Create sliders to control the range of sales and product prices to explore
col_sales, col_space, col_price = st.columns([10, 1, 10]) # Create columns for the sliders with a space in between

with col_sales:
    sales_range = st.slider(
        "Select the range of sales value to explore", # Slider Text
        sales_by_product["SALES_VALUE"].min(), # Minimum value of the slider
        sales_by_product["SALES_VALUE"].max() * 2, # Maximum value of the slider set as the double maximum to allow correct vertical axis labeling
        (
            sales_by_product["SALES_VALUE"].min(), # Default range for the slider
            sales_by_product["SALES_VALUE"].max() * 2, # Default range for the slider
        ),
    )
with col_space:
    st.write("")
with col_price:
    product_range = st.slider(
        "Select the range of product price to explore",
        sales_by_product["PRODUCT_SHELF_PRICE"].min(),
        sales_by_product["PRODUCT_SHELF_PRICE"].max() * 2,
        (
            sales_by_product["PRODUCT_SHELF_PRICE"].min(),
            sales_by_product["PRODUCT_SHELF_PRICE"].max() * 2,
        ),
    )

st.plotly_chart(
    graph_product_sales_price(sales_by_product, np.log10(sales_range), product_range) # Display the scatter plot of product sales value vs. product shelf price
)
