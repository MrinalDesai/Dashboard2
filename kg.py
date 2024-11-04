import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config

# Set Page Configuration
st.set_page_config(layout="wide")

st.title("Test Title")

# Define the nodes
nodes = [
    Node(id="id1", label="label1", color="#4B0082"),
    Node(id="id2", label="label2", color="#4B0082")
]

# Define the edges
edges = [
    Edge(source="id1", target="id2")
]

# Configure the graph
config = Config(
    width=900,
    height=900,
    directed=True,
    nodeHighlightBehavior=True,
    highlightColor="#F7A7A6",
    collapsible=False,
    node={'labelProperty': 'label'},
    link={'labelProperty': 'label', 'renderLabel': False},
    hierarchical=True,
    hierarchicalSorting=True,
    layout={
        "hierarchical": {
            "enabled": True,
            "levelSeparation": 150,
            "nodeSpacing": 100,
            "treeSpacing": 200,
            "direction": "UD",  # UD for top to bottom
            "sortMethod": "directed"
        }
    },
        # Set initial zoom level
    zoom=1.2  # Adjust as needed
)


# Display the graph
agraph(nodes=nodes, edges=edges, config=config)