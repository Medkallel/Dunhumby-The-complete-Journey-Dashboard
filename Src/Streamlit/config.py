import streamlit as st

DATASET_INFO_PATH = "./Doc/dataset_description.json"
BANNER_PATH = "./Assets/banner.jpg"
DOC_PATH = "./Doc/dunnhumby - The Complete Journey User Guide.pdf"
DATA_ARCHIVE_PATH = "./Data/archive.zip"
DATASET_PATH = "./Data/"
NOTEBOOK_PATH = "./Src/Data_Exploration-Preprocessing.ipynb"
CLEAN_DATA_PATH = "./Export/"

footer_note = """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        z-index: 100;
        color: #9f9f9f9f;
        text-align: right;
        padding-right: 2%;
        font-size: 10px;
    }
    </style>
    <div class="footer">
    <p>By Mohamed Kallel & Maud Mayousse-Aumiphin</p>
    </div>
    """


def page_init():
    st.set_page_config(
        layout="wide",
        page_icon="📊",
        page_title="The complete Journey Dashboard ",
        initial_sidebar_state="expanded",
    )
    st.sidebar.info("Select a Page from Above")
    st.sidebar.download_button(
        "Download Dataset",
        data=open(DATA_ARCHIVE_PATH, "rb").read(),
        file_name="dunnhumby-The_Complete _Journey_Dataset.zip",
        mime="application/zip",
        use_container_width=True,
    )
    st.sidebar.download_button(
        "Download Dataset Documentation",
        data=open(DOC_PATH, "rb").read(),
        file_name="dunnhumby_The_Complete_Journey_User_Guide.pdf",
        mime="application/pdf",
        use_container_width=True,
    )
    st.sidebar.download_button(
        "Download Data Processing Notebook",
        data=open(NOTEBOOK_PATH, "rb").read(),
        file_name="Data_Exploration-Preprocessing.ipynb",
        mime="application/zip",
        use_container_width=True,
    )
    st.markdown(footer_note, unsafe_allow_html=True)
