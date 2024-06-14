import base64
from config import *
import streamlit as st
from display_graph import display_dataset_graph

page_init()

st.title("Dunhumby The complete Journey Dashboard")
st.image(
    BANNER_PATH,
    use_column_width=True,
)

st.divider()
st.markdown("## Introduction")
st.markdown(
    "##### This dataset contains household level transactions over two years from a group of 2,500 households who are frequent shoppers at a retailer. It contains all of each household’s purchases, not just those from a limited number of categories. For certain households, demographic information as well as direct marketing contact history are included."
)
st.divider()
st.markdown("## Objective")
st.markdown(
    "##### The objective of this dashboard is to present relevant metrics about the financials of the stores, the demographic distribution of the customers and other key metrics."
)
st.divider()

st.markdown("## Dataset Contents")
st.caption("Note: Colored Nodes represent the datasets used in this analysis")
display_dataset_graph()
down_doc, down_data, _ = st.columns([1, 1, 3])
with down_doc:
    # Assuming your PDF file is named "example.pdf" and located in the same directory as your Streamlit script
    with open(DOC_PATH, "rb") as pdf_file:
        st.download_button(
            "Download Dataset Documentation",
            data=pdf_file.read(),
            file_name="dunnhumby_The_Complete_Journey_User_Guide.pdf",
            mime="application/pdf",
            type="primary",
        )
st.divider()

#with down_data:
#    with open(DATA_ARCHIVE_PATH, "rb") as data_file:
#        st.download_button(
#            "Download Dataset",
#            data=data_file.read(),
#            file_name="dunnhumby-The_Complete _Journey_Dataset.zip",
#            mime="application/zip",
#        )