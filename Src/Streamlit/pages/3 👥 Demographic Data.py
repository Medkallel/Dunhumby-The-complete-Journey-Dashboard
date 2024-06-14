import pandas as pd
from config import *
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt


def dmg_graph(df_demographic,color_palette = "deep"):
    dmg_figs, dmg_axis = plt.subplots(2, 3, figsize=(20, 10))
    
    dmg_axis[0, 0].pie(
        df_demographic["AGE_DESC_REDUCED"].value_counts().sort_index(ascending=False),
        labels=df_demographic["AGE_DESC_REDUCED"]
        .value_counts()
        .sort_index(ascending=False)
        .index,
        autopct="%1.1f%%",
        startangle=90,
        colors=sns.color_palette(color_palette),
    )
    dmg_axis[0, 0].set_title("Age distribution of customers")

    dmg_axis[0, 1].pie(
        df_demographic["HH_COMP_DESC"].value_counts().sort_index(ascending=False),
        labels=df_demographic["HH_COMP_DESC"]
        .value_counts()
        .sort_index(ascending=False)
        .index,
        autopct="%1.1f%%",
        startangle=90,
        colors=sns.color_palette(color_palette),
    )
    dmg_axis[0, 1].set_title("Household composition of customers")

    dmg_axis[0, 2].pie(
        df_demographic["HOUSEHOLD_SIZE_DESC"]
        .value_counts()
        .sort_index(ascending=False),
        labels=df_demographic["HOUSEHOLD_SIZE_DESC"]
        .astype("str")
        .replace("5", "5+")
        .value_counts()
        .sort_index(ascending=False)
        .index,
        autopct="%1.1f%%",
        startangle=90,
        colors=sns.color_palette(color_palette),
    )
    dmg_axis[0, 2].set_title("Household size of customers")

    dmg_axis[1, 0].pie(
        df_demographic["KID_CATEGORY_DESC"].value_counts().sort_index(ascending=False),
        labels=df_demographic["KID_CATEGORY_DESC"]
        .astype("str")
        .replace("3", "3+")
        .value_counts()
        .sort_index(ascending=False)
        .index,
        autopct="%1.1f%%",
        startangle=90,
        colors=sns.color_palette(color_palette),
    )
    dmg_axis[1, 0].set_title("Number of kids in the household")

    dmg_axis[1, 1].pie(
        df_demographic["MARITAL_STATUS_CODE"]
        .replace({"A": "Married", "B": "Single"})
        .value_counts()
        .sort_index(ascending=False),
        labels=df_demographic["MARITAL_STATUS_CODE"]
        .replace({"A": "Married", "B": "Single"})
        .value_counts()
        .sort_index(ascending=False)
        .index,
        autopct="%1.1f%%",
        startangle=90,
        colors=sns.color_palette(color_palette),
    )
    dmg_axis[1, 1].set_title("Marital status of customers")

    dmg_axis[1, 2].pie(
        df_demographic["INCOME_DESC_REDUCED"].value_counts().sort_index(ascending=True),
        labels=df_demographic["INCOME_DESC_REDUCED"]
        .value_counts()
        .sort_index(ascending=True)
        .index,
        autopct="%1.1f%%",
        startangle=90,
        colors=sns.color_palette(color_palette),
    )
    dmg_axis[1, 2].set_title("Income Distribution of customers")
    return dmg_figs


page_init()
st.title("👥 Demographic Data")
df_demographic = pd.read_csv(CLEAN_DATA_PATH + "hh_demographic_cleaned.csv")
st.write(" ")
st.write(f"##### The dataset contains the demographic information of a sample of {len(df_demographic)} households from the 2500 the study was conducted on")
st.write("- ##### Demographic Descriptive Statistics: ")
st.dataframe(
    df_demographic.describe()[
        ["HOUSEHOLD_SIZE_DESC", "KID_CATEGORY_DESC", "MEAN_AGE", "MEAN_INCOME"]
    ].rename(columns={"MEAN_AGE": "AGE_DESC", "MEAN_INCOME": "INCOME_DESC"})
)
st.write(" ")
st.write("- ##### Demographic distribution of households:")
st.pyplot(dmg_graph(df_demographic,color_palette="Paired"))
