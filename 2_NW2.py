import pandas as pd
import streamlit as st
from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle
from snowflake import connector
from snowflake.snowpark import Session
from snowflake.cortex import Summarize, Complete, ExtractAnswer, Sentiment, Translate
from snowflake import connector
from snowflake.snowpark import Session
import snowflake.connector
import pandas as pd
import string
import plotly.express as px

st.set_page_config(page_title="Transportation Network Visualisation",
                   page_icon="🕸",layout="wide"
                   )


st.title("Visualise your Transportation Network, Find Alternate routes and ask AI for suggestions.")

st.write(""":blue[This section shows us how we can implement network analysis to Visualise Transport system.]
         
         \nWe can initially seggragate routes based on traffic and then feed them in the AI System.

         \nClick on Icons and Routes to get more details.
         
        """)
df=pd.read_csv("stop_data.csv")
df_r=pd.read_csv("route_data2.csv")

PASSWORD = "passSNOW@1234"
#USER2 = "mrinalsnowtrial"
#ACCOUNT2 = "izoakvy-jbb52986" 

USER2 ="MRINALSNOW02"
ACCOUNT2="kakvlqh-cmb74873"
connection_params = {
    "account": ACCOUNT2,
    "user": USER2,
    "password": PASSWORD
}

def complete(question):
    completion = Complete(
        model="snowflake-arctic",
        prompt=question,
        session=snowflake_session,
    )
    return completion


# Create a Snowflake session
snowflake_session = Session.builder.configs(connection_params).create()

# uploaded_file_stop = st.file_uploader(
#     "Choose a Stop CSV file", accept_multiple_files=True
# )

# if uploaded_file_stop is not None:
#    df=pd.read_csv(uploaded_file_stop)
# else:
#    df=pd.read_csv("stop_data.csv")

# uploaded_file_route = st.file_uploader(
#     "Choose a Route Stop CSV file", accept_multiple_files=True
# )

# if uploaded_file_route is not None:
#    df_r=pd.read_csv(uploaded_file_route)
# else:
#    df_r=pd.read_csv("route_data2.csv")
st.subheader("Upload your CSV file(please maintain the same format). Refer Format of file below and Visualise your network.")
uploaded_files = st.file_uploader(
    "Choose a CSV file", accept_multiple_files=True
)

try:
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        if uploaded_file.name=="stop_data.csv":
            st.write("filename:", uploaded_file.name)
            df=pd.read_csv("stop_data.csv")
        else:
            df_r=pd.read_csv(uploaded_file.name)
except:
    st.write("File Format not Supported.Using Default data")
    df=pd.read_csv("stop_data.csv")
    df_r=pd.read_csv("route_data2.csv")

#df=pd.read_csv("stop_data.csv")
v = df.values.tolist()
c = df.columns.values.tolist()
final=[dict(zip(c, x)) for x in v]

New_Dict=[]
for i in final:
  Dict = { }
  Dict['data'] = i
  New_Dict.append(Dict)

#df_r=pd.read_csv("route_data2.csv")
vr = df_r.values.tolist()
cr = df_r.columns.values.tolist()
finalr=[dict(zip(cr, x)) for x in vr]

New_Dictr=[]
for i in finalr:
  Dictr = { }
  Dictr['data'] = i
  New_Dictr.append(Dictr)

elements={}
elements["nodes"] = New_Dict
elements["edges"] = New_Dictr

node_styles = [
    NodeStyle(label='high_traffic', color='#FF4B4B', caption='caption', icon='train'),
    NodeStyle(label="medium_traffic", color="#2A629A", caption="caption", icon="train"),
    NodeStyle(label='low_traffic', color='#FF7F3E', caption='caption', icon='train'),
    
]

edge_styles = [
    EdgeStyle("high_traffic", color='#FF4B4B', caption='caption', directed=False),
    EdgeStyle("medium_traffic", caption='caption', directed=False),
    EdgeStyle("low_traffic", caption='caption', directed=False),
]

layout = {"name": "cose", "animate": "end", "nodeDimensionsIncludeLabels": False}



# Render the component
#st.markdown("### st-link-analysis: Example")
st.markdown("### Network Model")
st_link_analysis(elements, layout, node_styles, edge_styles, key="xyz")


# st.write(df.style.background_gradient(cmap="Blues"))

# st.write(df_r.style.background_gradient(cmap="Blues"))


st.write("Stops Data")
st.write(df.style.set_properties(subset = ["label"],
                        **{"background-color": "lightblue",  
                           "color" : "blue",
                           "border" : "0.5px solid white"}))
st.write("Route Data")
st.write(df_r.style.set_properties(subset = ["label"],
                        **{"background-color": "lightblue",  
                           "color" : "blue",
                           "border" : "0.5px solid white"}))



state_route= df_r['id'].unique().tolist() 

va_sel=st.selectbox('Route:',state_route,placeholder="Select a Route to Display Data",index=0)

df_f_fil=df_r[df_r['id']==va_sel]
route_label=df_f_fil['label'].reset_index(drop=True)
st.write(route_label[0])
if route_label[0]=="high_traffic":
   st.write("manage traffic")
   question="How to reduce high traffic congestion on roads?"
elif route_label[0]=="low_traffic":
   st.write("remove this route")
   question="How to manage low traffic roads?"
else:
   st.write("Do nothing")
   question="How to manage medium traffic roads?"


bttn=st.button("Ask AI for suggestions regarding this route", type="primary")

if bttn:
    # Create a Snowflake session
    
    session = Session.builder.configs(connection_params).create()
    ctx = snowflake.connector.connect(
    user=USER2,
    password=PASSWORD,
    account=ACCOUNT2
       
    )

    st.write(complete(question))


########################################################################
st.subheader("Stuck in traffic?? We can help you find alternate routes")
st.write(":red[Find Alternate Routes]")
series1 = pd.Series(df_r['source'])
series2 = pd.Series(df_r['target'])
df_unique = pd.concat([series1, series2], axis = 0)
df1 = df_r[['source','target']].melt(value_name='New_column')[['New_column']]
df1.drop_duplicates(inplace=True)
df1=df1.sort_values(by=['New_column'], ascending=True)
df1['new_col'] = range(1, len(df1) + 1)
dict1=df1.set_index('New_column').T.to_dict('list')



df_r['source_code'] = df_r['source'].map(dict1)
df_r['target_code'] = df_r['target'].map(dict1)
df_r['edges'] = df_r['source_code'] + df_r['target_code']
input_edges=list(df_r['edges'])

stop_unique= df1['New_column'].unique().tolist() 

near_stop=st.selectbox('Nearest Stop:',stop_unique,placeholder="Select a Nearest Stop",index=1)
stop_unique.remove(near_stop)
dest_stop=st.selectbox('Destination:',stop_unique,placeholder="Select a Destination",index=1)

import networkx as nx

bttnx=st.button("Find Alternate Routes between two stations", type="primary")
res=''
if bttnx:
    G = nx.Graph()
    G.add_edges_from(input_edges)
    X = nx.shortest_simple_paths(G, [dict1[near_stop]][0][0], [dict1[dest_stop]][0][0]) #generator to find paths from 0 to 3 in order from shortest to longest.
    ro_string=[]
    for k in range(5):
        temp=[]
        ele=next(X)
        #st.write((ele))
        for i in ele:
            res = [key for key, value in dict1.items() if value == [i]]
            if i == ele[-1]:
               
               temp.append("  "+str(res[0])+" 🚍"+" ")
            else:
                
                temp.append("  "+str(res[0])+" ➡️"+" ")
        '-'.join(temp)
        st.write(('-'.join(temp)))    
    





