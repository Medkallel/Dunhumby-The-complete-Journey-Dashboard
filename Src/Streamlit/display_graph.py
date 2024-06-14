import streamlit as st
import pandas as pd
import json
from streamlit_flow import streamlit_flow
from streamlit_flow.elements import StreamlitFlowNode, StreamlitFlowEdge
from config import *


def display_dataset_graph():
    dataset_ids = {
        "1": "HH_DEMOGRAPHIC",
        "2": "TRANSACTION_DATA",
        "3": "CAMPAIGN_TABLE",
        "4": "COUPON_REDEMPT",
        "5": "PRODUCT",
        "6": "COUPON",
        "7": "CAUSAL_DATA",
        "8": "CAMPAIGN_DESC",
    }

    # Load JSON data
    with open(DATASET_INFO_PATH, "r") as file:
        data = json.load(file)

    # Extract datasets information
    datasets = data["datasets"]

    nodes = [
        StreamlitFlowNode(
            id="1",
            pos=(100, 50),
            data={"label": "HH_DEMOGRAPHIC"},
            node_type="input",
            source_position="right",
            draggable=False,
            style={"background-color": "#0271a5", "color": "white"},
        ),
        StreamlitFlowNode(
            "2",
            (275, 50),
            {"label": "TRANSACTION_DATA"},
            "default",
            "right",
            "left",
            draggable=False,
            style={"background-color": "#0271a5", "color": "white"},
        ),
        StreamlitFlowNode(
            "3",
            (100, 200),
            {"label": "CAMPAIGN_TABLE"},
            "default",
            "right",
            "top",
            draggable=False,
        ),
        StreamlitFlowNode(
            "4",
            (275, 200),
            {"label": "COUPON_REDEMPT"},
            "default",
            "right",
            "left",
            draggable=False,
        ),
        StreamlitFlowNode(
            "5",
            (450, 50),
            {"label": "PRODUCT"},
            "default",
            target_position="left",
            draggable=False,
            style={"background-color": "#0271a5", "color": "white"},
        ),
        StreamlitFlowNode(
            "6",
            (450, 300),
            {"label": "COUPON"},
            "default",
            target_position="top",
            source_position="top",
            draggable=False,
        ),
        StreamlitFlowNode(
            "7",
            (625, 125),
            {"label": "CAUSAL_DATA"},
            "default",
            target_position="left",
            source_position="left",
            draggable=False,
        ),
        StreamlitFlowNode(
            "8",
            (275, 300),
            {"label": "CAMPAIGN_DESC"},
            "output",
            "right",
            "left",
            draggable=False,
        ),
    ]

    edges = [
        StreamlitFlowEdge(
            "1-2",
            "1",
            "2",
            animated=True,
        ),  # HH_DEMOGRAPHIC -> TRANSACTION_DATA
        StreamlitFlowEdge(
            "1-3",
            "1",
            "3",
            animated=True,
            edge_type="simplebezier",
        ),  # HH_DEMOGRAPHIC -> CAMPAIGN_TABLE
        StreamlitFlowEdge(
            "1-4", "1", "4", animated=True, edge_type="simplebezier"
        ),  # HH_DEMOGRAPHIC -> COUPON_REDEMPT
        StreamlitFlowEdge(
            "3-4", "3", "4", animated=True
        ),  # CAMPAIGN_TABLE -> COUPON_REDEMPT
        StreamlitFlowEdge(
            "2-5", "2", "5", animated=True
        ),  # TRANSACTION_DATA -> PRODUCT
        StreamlitFlowEdge("4-6", "4", "6", animated=True),  # COUPON_REDEMPT -> COUPON
        StreamlitFlowEdge("5-7", "5", "7", animated=True),  # PRODUCT -> CAUSAL_DATA
        StreamlitFlowEdge(
            "5-6", "5", "6", animated=True, edge_type="default"
        ),  # PRODUCT -> COUPON
        StreamlitFlowEdge("7-6", "7", "6", animated=True),  # CAUSAL_DATA -> COUPON
        StreamlitFlowEdge(
            "3-8", "3", "8", animated=True
        ),  # CAMPAIGN_TABLE -> CAMPAIGN_DESC
    ]

    # Create two columns
    col1, col2 = st.columns([3, 4])

    with col1:
        # Implement the flow
        selected_id = streamlit_flow(
            "ret_val_flow",
            nodes,
            edges,
            fit_view=True,
            get_node_on_click=True,
            get_edge_on_click=False,
        )

    with col2:
        # Display a dataframe based on the clicked node
        if selected_id:
            selected_id = dataset_ids[selected_id]
            dataset_info = datasets[selected_id]

            st.markdown(f"### {selected_id}")
            st.markdown(dataset_info["description"])

            columns_info = dataset_info["columns"]
            df = pd.read_json(json.dumps(columns_info)).rename(
                columns={"name": "Name", "type": "Type", "description": "Description"}
            )
            st.markdown(df.style.hide(axis="index").to_html(), unsafe_allow_html=True)
        else:
            st.info("Please select a dataset to view its contents.")
