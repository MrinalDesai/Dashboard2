from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle
import streamlit as st
node_styles = [
    NodeStyle(label='PERSON', color='#FF7F3E', caption='email', icon='train'),
    NodeStyle(label="POST", color="#2A629A", caption="created_at", icon="train")
]

edge_styles = [
    EdgeStyle("FOLLOWS", caption='label', directed=True),
    EdgeStyle("POSTED", caption='label', directed=True),
    EdgeStyle("QUOTES", caption='label', directed=True),
]

layout = {"name": "cose", "animate": "end", "nodeDimensionsIncludeLabels": False}

elements = {"nodes": [{'data': {"id": "n1", "label": "PERSON", "name": "Name One", "email": "n1@example.com", "join_date": "2024-01-01"}},
                       {"data": {"id": "n2", "label": "PERSON", "name": "Name Two", "email": "n2@example.com", "join_date": "2024-02-02"}}, 
                       {"data": {"id": "n3", "label": "PERSON", "name": "Name Three", "email": "n3@example.com", "join_date": "2024-03-03"}}, 
                       {"data": {"id": "n4", "label": "POST", "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.", "created_at": "2024-04-04 10:15:00", "tags": ["T1", "T5"]}}, 
                       {"data": {"id": "n5", "label": "POST", "content": "Quisque velit nisi, pretium ut lacinia in, elementum id enim. [QOUTE]", "created_at": "2024-04-04 10:20:00", "tags": ["T2"]}}],
            "edges": [{"data": {"id": "e1", "label": "FOLLOWS", "source": "n1", "target": "n2"}}, 
                      {"data": {"id": "e2", "label": "FOLLOWS", "source": "n2", "target": "n3"}}, 
                      {"data": {"id": "e3", "label": "POSTED", "source": "n3", "target": "n4"}}, 
                      {"data": {"id": "e4", "label": "POSTED", "source": "n1", "target": "n5"}}, 
                      {"data": {"id": "e5", "label": "QUOTES", "source": "n5", "target": "n4"}}]}

# Render the component
st.markdown("### st-link-analysis: Example")
st_link_analysis(elements, layout, node_styles, edge_styles, key="xyz")