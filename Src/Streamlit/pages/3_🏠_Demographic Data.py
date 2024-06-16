import pandas as pd
from config import *
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt


# def graph_age(df_demographic):
#     age_counts = (
#         df_demographic["AGE_DESC"]
#         .replace("55-64", "55-65+")
#         .replace("65+", "55-65+")
#         .value_counts()
#         .sort_index(ascending=False)
#     )
#     labels = [
#         f"{age} ({count})" for age, count in zip(age_counts.index, age_counts.values)
#     ]
#     colors = sns.color_palette("muted")
#     fig, ax = plt.subplots(figsize=(4,4))
#     ax.pie(
#         age_counts,
#         labels=labels,
#         autopct="%1.1f%%",
#         colors=colors,
#         textprops={"fontsize": 12, "fontweight": 500},
#     )
#     fig.suptitle("Age distribution of customers", fontsize=15, fontweight=500)
#     return fig


# def graph_marital_status(df_demographic):
#     statuts_code_counts = (
#         df_demographic["MARITAL_STATUS_CODE"]
#         .replace({"A": "Married", "B": "Single"})
#         .value_counts()
#     )
#     labels = [
#         f"{statut} ({count})"
#         for statut, count in zip(statuts_code_counts.index, statuts_code_counts.values)
#     ]
#     colors = sns.color_palette("muted")
#     fig, ax = plt.subplots(figsize=(4,4))
#     ax.pie(
#         statuts_code_counts,
#         labels=labels,
#         autopct="%1.1f%%",
#         colors=colors,
#         textprops={"fontsize": 12, "fontweight": 500},
#     )
#     fig.suptitle("Marital status of customers", fontsize=15, fontweight=500)
#     return fig


# def graph_kid_composition(df_demographic):
#     kid_counts = df_demographic["KID_CATEGORY_DESC"].value_counts().sort_index()
#     labels = [
#         f"{kid} ({count})" for kid, count in zip(kid_counts.index, kid_counts.values)
#     ]
#     colors = sns.color_palette("muted")
#     fig, ax = plt.subplots(figsize=(4,4))
#     ax.pie(
#         kid_counts,
#         labels=labels,
#         autopct="%1.1f%%",
#         colors=colors,
#         textprops={"fontsize": 12, "fontweight": 500},
#     )
#     fig.suptitle("Number of kids in the household", fontsize=15, fontweight=500)
#     return fig


# def graph_income(df_demographic):
#     income_counts = df_demographic["INCOME_DESC_REDUCED"].value_counts()[
#         ["150K+", "100-149K", "50-99K", "25-49K", "<25K"]
#     ]

#     income_percentages = income_counts / len(df_demographic) * 100

#     labels = [
#         f"{income} ({count})"
#         for income, count in zip(income_counts.index, income_counts.values)
#     ]
#     colors = sns.color_palette("muted")
#     fig, ax = plt.subplots(figsize=(4,4))
#     ax.pie(
#         income_percentages,
#         labels=labels,
#         autopct="%1.1f%%",
#         colors=colors,
#         textprops={"fontsize": 12, "fontweight": 500},
#     )
#     fig.suptitle(
#         "Income distribution of customers", fontsize=15, fontweight=500, x=0.55
#     )
#     return fig


# def graph_household_composition(df_demographic):
#     comp_desc_counts = df_demographic["HH_COMP_DESC"].value_counts()
#     labels = [
#         f"{comp_desc}\n({count})"
#         for comp_desc, count in zip(comp_desc_counts.index, comp_desc_counts.values)
#     ]
#     colors = sns.color_palette("muted")
#     fig, ax = plt.subplots(figsize=(4,4))
#     ax.pie(
#         comp_desc_counts,
#         labels=labels,
#         autopct="%1.1f%%",
#         colors=colors,
#         textprops={"fontsize": 12, "fontweight": 500},
#     )
#     fig.suptitle("Household composition of customers", fontsize=15, fontweight=500)
#     return fig


# def graph_household_size(df_demogrpahic):
#     comp_desc_counts = df_demographic["HOUSEHOLD_SIZE_DESC"].value_counts().sort_index()
#     labels = [
#         f"{comp_desc} ({count})"
#         for comp_desc, count in zip(comp_desc_counts.index, comp_desc_counts.values)
#     ]
#     colors = sns.color_palette("muted")
#     fig, ax = plt.subplots(figsize=(4, 4))
#     ax.pie(
#         comp_desc_counts,
#         labels=labels,
#         autopct="%1.1f%%",
#         colors=colors,
#         textprops={"fontsize": 12, "fontweight": 500},
#     )
#     fig.suptitle("Household Size Distribution", fontsize=15, fontweight=500)
#     return fig


def dmg_graph(df_demographic, color_palette="deep"):
    dmg_figs, dmg_axis = plt.subplots(2, 3, figsize=(20, 10))

    dmg_axis[0, 0].pie(
        df_demographic["AGE_DESC"].value_counts().sort_index(ascending=False),
        labels=df_demographic["AGE_DESC"]
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
        colors=sns.color_palette(color_palette),
    )
    dmg_axis[1, 1].set_title("Marital status of customers")

    dmg_axis[1, 2].pie(
        df_demographic["INCOME_DESC_REDUCED"].value_counts()[
            ["150K+", "100-149K", "50-99K", "25-49K", "<25K"]
        ],
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
st.title("🏠 Demographic Data")
df_demographic = pd.read_csv(CLEAN_DATA_PATH + "hh_demographic_cleaned.csv")
st.write(" ")
st.write(
    f"##### The dataset contains the demographic information of a sample of {len(df_demographic)} households from the 2500 the study was conducted on"
)
st.write("- ##### Demographic Descriptive Statistics: ")
st.write("###### We explore several statistics around the demographic distribution and characteristics of the sample of households")
st.dataframe(
    df_demographic.describe()[
        ["HOUSEHOLD_SIZE_DESC", "KID_CATEGORY_DESC", "MEAN_AGE", "MEAN_INCOME"]
    ].rename(columns={"MEAN_AGE": "AGE_DESC", "MEAN_INCOME": "INCOME_DESC"})
)
st.write(" ")
st.write("- ##### Demographic distribution of households:")
st.pyplot(dmg_graph(df_demographic, color_palette="muted"), use_container_width=True)

# col1, col2, col3 = st.columns(3)
# with col1:
#    st.pyplot(graph_age(df_demographic), use_container_width=True)
#    st.pyplot(graph_household_size(df_demographic), use_container_width=True)
# with col2:
#    st.pyplot(graph_income(df_demographic), use_container_width=True)
#    st.pyplot(graph_household_composition(df_demographic), use_container_width=True)
# with col3:
#    st.pyplot(graph_marital_status(df_demographic), use_container_width=True)
#    st.pyplot(graph_kid_composition(df_demographic), use_container_width=True)
