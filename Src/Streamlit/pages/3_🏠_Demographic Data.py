import pandas as pd
from config import *
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt


def dmg_graph(df_demographic, color_palette="deep"):
    """
    This function creates a set of pie charts showing the demographic distribution of customers.

    Parameters:
    df_demographic (DataFrame): The DataFrame containing the demographic data.
    color_palette (str): The color palette to use for the pie charts. Default is "deep".

    Returns:
    dmg_figs: The matplotlib figure object containing the pie charts.
    """
    # Create a grid of pie charts for various demographic attributes
    dmg_figs, dmg_axis = plt.subplots(2, 3, figsize=(20, 10))

    # -- Age distribution --
    dmg_axis[0, 0].pie(
        df_demographic["AGE_DESC"]
        .value_counts()
        .sort_index(ascending=False),  # Count the number of customers in each age group
        labels=df_demographic["AGE_DESC"]
        .value_counts()  # Set the labels to the age groups
        .sort_index(ascending=False)  # Sort the labels in descending order
        .index,  # Get the index of the sorted labels as the pie chart labels
        autopct="%1.1f%%",  # Set the percentage format
        startangle=90,  # Set the start angle of the pie chart for better visibility
        colors=sns.color_palette(
            color_palette
        ),  # Set the color palette for the pie chart
    )
    dmg_axis[0, 0].set_title(
        "Age distribution of customers"
    )  # Set the title of the pie chart

    # -- Household composition --
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

    # -- Household size --
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

    # -- Number of kids in the household --
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

    # -- Marital status --
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

    # -- Income distribution --
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
    return dmg_figs  # Return the figure object containing the pie charts


# Initialize the Streamlit page settings
page_init()

st.title("🏠 Demographic Data")

# Read the cleaned demographic data from a CSV file
df_demographic = pd.read_csv(CLEAN_DATA_PATH + "hh_demographic_cleaned.csv")

st.write(" ")  # Insert a space in the Streamlit app for better layout
st.write(
    f"##### The dataset contains the demographic information of a sample of {len(df_demographic)} households from the 2500 the study was conducted on" # Display the number of households in the dataset
)
st.write("- ##### Demographic Descriptive Statistics: ")
st.write(
    "###### We explore several statistics around the demographic distribution and characteristics of the sample of households"
)

# Display a dataframe with descriptive statistics for selected columns
st.dataframe(
    df_demographic.describe()[
        [
            "HOUSEHOLD_SIZE_DESC",
            "KID_CATEGORY_DESC",
            "MEAN_AGE",
            "MEAN_INCOME",
        ]  # The `describe()` method provides summary statistics
    ].rename(
        columns={"MEAN_AGE": "AGE_DESC", "MEAN_INCOME": "INCOME_DESC"}
    ),  # We rename some columns for better readability
    use_container_width=True,
)

st.write(" ")  # Insert a space for better layout
st.write("- ##### Demographic distribution of households:")
# Display the subplots of the demographic distribution
st.pyplot(
    dmg_graph(df_demographic, color_palette="muted"),
    use_container_width=True,  # `use_container_width=True` ensures the plot fits the container width in the Streamlit app
)
