import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.title('Introduction')
st.header('Inland Waterways Infrastructure', divider="gray")
st.subheader("#️⃣Development📌 ", divider="gray")

st.image(f"water/news1.jpg")


st.write("""The suggestion by NITI Ayog is the widespread integration of  bus and water transport along the coast.
         
         \nDue to loss making in SRTU's mostly state tries to reduce these services. But a well-planned bus and ferry transport reduces congestion and
         lowers air pollution while also solving last mile connectivity issue.

""")

##################################################################################################
st.write("State-wise List of Waterways declared as National Waterways under National Waterways Act, 2016")
df_st_wat=pd.read_csv(f"water/State-wise List of Waterways declared as National Waterways under National Waterways Act, 2016 (in reply to Unstarred Question on 19 September, 2020) (From Ministry of Shipping).csv",encoding='cp1252')
st.write(df_st_wat.set_index(df_st_wat.columns[0]))



##################################################################################################


st.write("National Waterways Operational with Inland Water Transport during 2019-20")
df_st_wat_in=pd.read_csv(f"water/National Waterways Operational with Inland Water Transport during 2019-20 (From Ministry of Ports, Shipping and Waterways).csv",encoding='cp1252', index_col=0)
st.write(df_st_wat_in)


##################################################################################################


st.write("Waterways-wise List of 26 National Waterways (NWs) Projects for Development")
df_st_nat_Wat=pd.read_csv(f"water/Waterways-wise List of 26 National Waterways (NWs) Projects for Development (in reply to Unstarred Question on 19th December 2023).csv",encoding='cp1252', index_col=0)
st.write(df_st_nat_Wat)


##################################################################################################


st.write("National Waterways-wise New National Waterways Sanctioned under Phase-I Development")
df_st_nat_Wat=pd.read_csv(f"water/National Waterways-wise New National Waterways Sanctioned under Phase-I Development (in Reply to Unstarred Question on 30 July, 2024).csv",encoding='cp1252', index_col=0)
st.write(df_st_nat_Wat)


##################################################################################################


st.subheader("Multimodal Logistic Parks",divider="gray")
st.write("""Multi-Modal Logistics Parks (MMLPs) is a key policy initiative of the Government of India, 
         led by National Highways Logistics Management Limited under Ministry of Road Transport and Highways 
         (MoRTH) and the National Highways Authority of India (NHAI), to develop Multi-Modal Logistics Parks 
         in hub-and-spoke model to improve the country's freight logistics sector by lowering overall freight 
         costs and time, cutting warehousing costs, reducing vehicular pollution and congestion, improving 
         the tracking and traceability of consignments through infrastructural, procedural, and information technology interventions.

         \nSince, in 2017, India had comparatively high logistics costs, 13% of total price of goods compared with 8% in other 
      major economies and average 72% higher cost than China of exporting/importing a container in India.To make India globally 
      competitive by reducing these costs and time, the MoRTH is developing multi-modal logistics parks at selected locations in 
      the country under its Logistics Efficiency Enhancement Program (LEEP).""")

st.write("Location-wise Details of the Proposed Capacity and Investment in the Multi-Modal Logistics Parks (MMLP)")
df_st_nat_Wat=pd.read_csv(f"water/Location-wise Details of the Proposed Capacity and Investment in the Multi-Modal Logistics Parks (MMLP) in the Country (in Reply to Unstarred Question on 29 March, 2023).csv",encoding='cp1252', index_col=0)
st.write(df_st_nat_Wat)

##################################################################################################


st.write("Category-wise Details of Land Area, Already Decided for Some Multi Modal Logistics Parks (MMLPs) ")
df_st_nat_Wat=pd.read_csv(f"water/Category-wise Details of Land Area, Already Decided for Some Multi Modal Logistics Parks (MMLPs) Based on Feasibility Studies ( in reply to Unstarred Question on 24th March, 2023).csv",encoding='cp1252', index_col=0)
st.write(df_st_nat_Wat)

##################################################################################################

st.subheader("References",divider="gray")

st.write("""https://timesofindia.indiatimes.com/india/pm-launches-indias-1st-multi-modal-terminal/articleshow/66598089.cms""")
