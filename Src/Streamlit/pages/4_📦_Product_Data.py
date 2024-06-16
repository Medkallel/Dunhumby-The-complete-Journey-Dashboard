import pandas as pd
from config import *
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import plotly.express as px
import seaborn as sns
from PIL import Image


def graph_product_sales_price(sales_by_product,sales_range,product_range):
    sales_by_product["SALES_VALUE_LOG"] = np.log10(sales_by_product["SALES_VALUE"])
    fig = px.scatter(
        sales_by_product,
        x="PRODUCT_SHELF_PRICE",
        y=sales_by_product["SALES_VALUE"],
        title="Product Sales Value vs Product Shelf Price",
        log_y=True,
        labels={
            "PRODUCT_SHELF_PRICE": "Product Shelf Price",
            "SALES_VALUE": "Sales Value",
            #"color": "Sales Value",
        },
        hover_data={"PRODUCT_ID": True,"SALES_VALUE": ':,.2f' ,"SALES_VALUE_LOG":False,
                    },
        color="SALES_VALUE_LOG",

    )
    fig.update_layout(coloraxis_colorbar=dict(title='Sales Value', ticksuffix='00 K $'),yaxis=dict(tickprefix='$',range=sales_range),xaxis=dict(tickprefix='$',range=product_range))
    fig.update_traces(marker=dict(size=3))
    return fig


def graph_word_cloud(df_trnsct_prod, df_products):
    frequence_produits = df_trnsct_prod["DEPARTMENT"]
    frequence_produits = " ".join(v for v in frequence_produits)
    # Preprocess the text to make it all lower case and remove leading/trailing spaces
    frequence_produits = np.log(
        df_trnsct.merge(df_products, how="left", on="PRODUCT_ID")[
            "DEPARTMENT"
        ].value_counts()
    )

    mask = np.invert(np.array(Image.open("./Assets/WordCloudMask.png")))[::, 150:850]
    wordcloud = WordCloud(
        background_color="white",
        mask=mask,
        contour_color="#263238",
        contour_width=10,
        # color_func= sns.color_palette("Blues", ).as_hex()[2:],
    ).generate_from_frequencies(frequence_produits)

    fig = plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    return fig


page_init()
st.title("📦 Product Data")

# Load the product data
df_products = pd.read_csv(CLEAN_DATA_PATH + "product_cleaned.csv")
df_trnsct = pd.read_csv(CLEAN_DATA_PATH + "transaction_data_cleaned.csv")
df_trnsct_prod = df_trnsct.merge(df_products, on="PRODUCT_ID", how="left")
st.write(
    f"##### The dataset contains the product data of {df_products['PRODUCT_ID'].nunique():,} unique products sold by the retailer"
)
st.divider()

st.write("- ##### General Product Statistics: ")
st.write("###### We explore several statistics around the product data")
st.dataframe(df_products.describe(include="all")[:4], use_container_width=True)
st.write("- ##### Product Presence: ")
st.write(
    "##### We explore the presence of each deprtment of products in the catalogue of sold products"
)
col_wordcloud, col_stat_presence_products = st.columns(2)
with col_wordcloud:
    st.pyplot(graph_word_cloud(df_trnsct_prod, df_products))
with col_stat_presence_products:
    st.dataframe(
        df_trnsct_prod["DEPARTMENT"]
        .replace(df_trnsct_prod["DEPARTMENT"].value_counts().index[11], pd.NA)
        .value_counts(),
        height=700,
        use_container_width=True,
    )
st.divider()
st.write("- ##### Product Categories and Sales: ")
col_department, col_commodity, col_subcommodity = st.columns(3)
with col_department:
    st.write("###### By Department:")
    st.caption("High Level")
    sales_by_department = (
        df_trnsct_prod.groupby("DEPARTMENT")["SALES_VALUE"].sum().reset_index()
    )
    top_10_departments = sales_by_department.nlargest(10, "SALES_VALUE")
    st.dataframe(top_10_departments, use_container_width=True, hide_index=True)
with col_commodity:
    st.write("###### By Commodity:")
    st.caption("Lower Level")
    sales_by_commodity = (
        df_trnsct_prod.groupby("COMMODITY_DESC")["SALES_VALUE"].sum().reset_index()
    )
    top_10_commodities = sales_by_commodity.nlargest(10, "SALES_VALUE")
    st.dataframe(top_10_commodities, use_container_width=True, hide_index=True)
with col_subcommodity:
    st.write("######  By Sub_Commodity:")
    st.caption("Lowest Level")
    sales_by_subcommodity = (
        df_trnsct_prod.groupby("SUB_COMMODITY_DESC")["SALES_VALUE"].sum().reset_index()
    )
    top_10_subcommodities = sales_by_subcommodity.nlargest(10, "SALES_VALUE")
    st.dataframe(top_10_subcommodities, use_container_width=True, hide_index=True)
st.divider()
st.write("- ##### Product Sales / Product Price: ")
st.write(
    "###### We explore the relationship between the sales value and the price of the products"
)

sales_by_product = (
        df_trnsct_prod.groupby("PRODUCT_ID")["SALES_VALUE"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
sales_by_product["PRODUCT_SHELF_PRICE"] = sales_by_product.merge(
    df_products, on="PRODUCT_ID", how="left"
)["PRODUCT_SHELF_PRICE"]
sales_by_product = sales_by_product[(sales_by_product["SALES_VALUE"] >1) ]

col_sales,col_space,col_price = st.columns([10,1,10])
with col_sales:
    sales_range = st.slider("Select the range of sales value to explore",sales_by_product["SALES_VALUE"].min(),sales_by_product["SALES_VALUE"].max()*2,(sales_by_product["SALES_VALUE"].min(),sales_by_product["SALES_VALUE"].max()*2),)
with col_space:
    st.write("")
with col_price:
    product_range = st.slider("Select the range of product price to explore",sales_by_product["PRODUCT_SHELF_PRICE"].min(),sales_by_product["PRODUCT_SHELF_PRICE"].max()*2,(sales_by_product["PRODUCT_SHELF_PRICE"].min(),sales_by_product["PRODUCT_SHELF_PRICE"].max()*2))

st.plotly_chart(graph_product_sales_price(sales_by_product,np.log10(sales_range),product_range))
