import streamlit as st

# Constants for file paths
DATASET_INFO_PATH = "./Doc/dataset_description.json"
BANNER_PATH = "./Assets/banner.jpg"
DOC_PATH = "./Doc/dunnhumby - The Complete Journey User Guide.pdf"
DATA_ARCHIVE_PATH = "./Data/archive.zip"
DATASET_PATH = "./Data/"
NOTEBOOK_PATH = "./Src/Data_Exploration-Preprocessing.ipynb"
CLEAN_DATA_PATH = "./Export/"

# Footer note with HTML styling
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
    <p>By Maud Mayousse-Aumiphin & Mohamed Kallel</p>
    </div>
    """


# Function to initialize the page configuration
def page_init():
    """
    Initializes the Streamlit page with a specific configuration, adds an information message to the sidebar,
    and adds download buttons for the dataset zip file, dataset documentation PDF, and data processing notebook.

    The page configuration includes the layout, icon, title, and initial sidebar state.

    The download buttons allow the user to download the dataset, its documentation, and the data processing notebook.
    """

    # Setting the page configuration (layout, icon, title, and sidebar state)
    st.set_page_config(
        layout="wide",
        page_icon="📊",
        page_title="The complete Journey Dashboard ",
        initial_sidebar_state="expanded",
    )

    # Sidebar information message
    st.sidebar.info("Select a Page from Above")

    # Download button for the dataset zip file
    st.sidebar.download_button(
        "Download Dataset",
        data=open(DATA_ARCHIVE_PATH, "rb").read(),
        file_name="dunnhumby-The_Complete _Journey_Dataset.zip",
        mime="application/zip",
        use_container_width=True,
    )

    # Download button for the dataset documentation PDF
    st.sidebar.download_button(
        "Download Dataset Documentation",
        data=open(DOC_PATH, "rb").read(),
        file_name="dunnhumby_The_Complete_Journey_User_Guide.pdf",
        mime="application/pdf",
        use_container_width=True,
    )

    # Download button for the data processing notebook
    st.sidebar.download_button(
        "Download Data Processing Notebook",
        data=open(NOTEBOOK_PATH, "rb").read(),
        file_name="Data_Exploration-Preprocessing.ipynb",
        mime="application/zip",
        use_container_width=True,
    )

    # Displaying the footer note with HTML content
    st.markdown(footer_note, unsafe_allow_html=True)
