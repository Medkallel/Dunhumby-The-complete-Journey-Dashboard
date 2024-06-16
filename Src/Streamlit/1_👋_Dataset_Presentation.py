from config import *
import streamlit as st
from display_graph import display_dataset_graph

# Initialize the Streamlit page settings
page_init()

st.title("Dunhumby The complete Journey Dashboard")

# Display the banner image at the top of the page
st.image(
    BANNER_PATH,
    use_column_width=True,
)

st.divider()  # Add a divider line

# --Introduction section--
st.markdown("## Introduction")
st.markdown(
    "##### This dataset contains household level transactions over two years from a group of 2,500 households who are frequent shoppers at a retailer. It contains all of each household’s purchases, not just those from a limited number of categories. For certain households, demographic information as well as direct marketing contact history are included."
)
st.divider()

# --Objective section--
st.markdown("## Objective")
st.markdown(
    "##### The objective of this dashboard is to present relevant metrics about the financials of the stores, the demographic distribution of the customers and other key metrics."
)
st.divider()

# --Dataset Contents section--
st.markdown("## Dataset Contents")
st.caption(
    "Note: Colored Nodes represent the datasets used in this analysis <br/> You can move and zoom in/out in the graph below",
    unsafe_allow_html=True,
)

# Display the dataset graph
display_dataset_graph()
# Create columns for download buttons
down_doc, down_data, _ = st.columns([1, 1, 3])

# Download button for the dataset documentation
with down_doc:
    # Open the doc PDF file as binary and create a download button
    with open(DOC_PATH, "rb") as pdf_file:
        st.download_button(
            "Download Dataset Documentation",
            data=pdf_file.read(),
            file_name="dunnhumby_The_Complete_Journey_User_Guide.pdf",
            mime="application/pdf",
            type="primary",
        )
# Download button for the dataset as zip file
with down_data:
    with open(DATA_ARCHIVE_PATH, "rb") as data_file:
        st.download_button(
            "Download Dataset",
            data=data_file.read(),
            file_name="dunnhumby-The_Complete _Journey_Dataset.zip",
            mime="application/zip",
        )
st.divider()
