import plotly.express as px 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import streamlit as st

st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.header('India Social Impact Data Set', divider="gray")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("Some data may be blank based on its availability.")
df = pd.read_csv(f'datasets/india_sid/India Social Impact Data Set - Examples.csv')
st.subheader("Road Infrastructure")
st.write("""The Infrastructure and Road Construction details are mentioned in the below Datasets""")
df_filter_roadInfra=pd.read_excel(f'datasets/india_sid/INDIA_SOCIAL_IMPACT_DATA_SET SELECT DISTINCT identifier,TITLE from HACKATHON.IDH_DATA;.xlsx',sheet_name='Road_Infra', engine='openpyxl')
df_filter_watCargo=pd.read_excel(f'datasets/india_sid/INDIA_SOCIAL_IMPACT_DATA_SET SELECT DISTINCT identifier,TITLE from HACKATHON.IDH_DATA;.xlsx',sheet_name='water_cargo', engine='openpyxl')
df_filter_RailInfra=pd.read_excel(f'datasets/india_sid/INDIA_SOCIAL_IMPACT_DATA_SET SELECT DISTINCT identifier,TITLE from HACKATHON.IDH_DATA;.xlsx',sheet_name='Rail_Infra', engine='openpyxl')
df_filter_RailPass=pd.read_excel(f'datasets/india_sid/INDIA_SOCIAL_IMPACT_DATA_SET SELECT DISTINCT identifier,TITLE from HACKATHON.IDH_DATA;.xlsx',sheet_name='Rail_Pass', engine='openpyxl')
df_filter_RailEco=pd.read_excel(f'datasets/india_sid/INDIA_SOCIAL_IMPACT_DATA_SET SELECT DISTINCT identifier,TITLE from HACKATHON.IDH_DATA;.xlsx',sheet_name='Rail_Eco', engine='openpyxl')
df_filter_AirPass=pd.read_excel(f'datasets/india_sid/INDIA_SOCIAL_IMPACT_DATA_SET SELECT DISTINCT identifier,TITLE from HACKATHON.IDH_DATA;.xlsx',sheet_name='AirPass', engine='openpyxl')
df_filter_AirFreight=pd.read_excel(f'datasets/india_sid/INDIA_SOCIAL_IMPACT_DATA_SET SELECT DISTINCT identifier,TITLE from HACKATHON.IDH_DATA;.xlsx',sheet_name='Freight', engine='openpyxl')
df_filter_PortCargo=pd.read_excel(f'datasets/india_sid/INDIA_SOCIAL_IMPACT_DATA_SET SELECT DISTINCT identifier,TITLE from HACKATHON.IDH_DATA;.xlsx',sheet_name='Port_Cargo', engine='openpyxl')
df_filter_Fuel=pd.read_excel(f'datasets/india_sid/INDIA_SOCIAL_IMPACT_DATA_SET SELECT DISTINCT identifier,TITLE from HACKATHON.IDH_DATA;.xlsx',sheet_name='Fuel', engine='openpyxl')
df_filter_STATE=pd.read_excel(f'datasets/india_sid/INDIA_SOCIAL_IMPACT_DATA_SET SELECT DISTINCT identifier,TITLE from HACKATHON.IDH_DATA;.xlsx',sheet_name='India_State', engine='openpyxl')



ident_roadInfra=list(df_filter_roadInfra['IDENTIFIER'])
ident_watCargo=list(df_filter_watCargo['IDENTIFIER'])
ident_RailInfra=list(df_filter_RailInfra['IDENTIFIER'])
ident_RailPass=list(df_filter_RailPass['IDENTIFIER'])
ident_RailEco=list(df_filter_RailEco['IDENTIFIER'])
ident_AirPass=list(df_filter_AirPass['IDENTIFIER'])
ident_AirFreight=list(df_filter_AirFreight['IDENTIFIER'])
ident_PortCargo=list(df_filter_PortCargo['IDENTIFIER'])
ident_Fuel=list(df_filter_Fuel['IDENTIFIER'])


st_india_roadInfra=list(df_filter_STATE['India/State'])
st_india_watCargo=list(df_filter_STATE['India/State'])
st_india_RailInfra=list(df_filter_STATE['India/State'])
st_india_RailPass=list(df_filter_STATE['India/State'])
st_india_RailEco=list(df_filter_STATE['India/State'])
st_india_AirPass=list(df_filter_STATE['India/State'])
st_india_AirFreight=list(df_filter_STATE['India/State'])
st_india_PortCargo=list(df_filter_STATE['India/State'])
st_india_Fuel=list(df_filter_STATE['India/State'])


# Get some data
df_roadInfra = df[df['IDENTIFIER'].isin(ident_roadInfra)]
df_watCargo=df[df['IDENTIFIER'].isin(ident_watCargo)]
df_RailInfra=df[df['IDENTIFIER'].isin(ident_RailInfra)]
df_RailPass=df[df['IDENTIFIER'].isin(ident_RailPass)]
df_RailEco = df[df['IDENTIFIER'].isin(ident_RailEco)]
df_AirPass=df[df['IDENTIFIER'].isin(ident_AirPass)]
df_AirFreight=df[df['IDENTIFIER'].isin(ident_AirFreight)]
df_PortCargo=df[df['IDENTIFIER'].isin(ident_PortCargo)]
df_Fuel=df[df['IDENTIFIER'].isin(ident_Fuel)]




cat_sel_roadInfra=st.selectbox('Category Infra:',list(df_roadInfra['TITLE'].unique()),placeholder="Select a Option to Display Data")
state_sel_roadInfra=st.selectbox('Category  state:',st_india_roadInfra,placeholder="Select a Option to Display Data",key="roadInfra")
df_roadInfra_vis = df_roadInfra[df_roadInfra['TITLE']==cat_sel_roadInfra]
df_roadInfra_vis=df_roadInfra_vis.sort_values(by=['DATE'], ascending=False)
df_roadInfra_vis=df_roadInfra_vis.drop_duplicates(subset='DATE', keep="last")
roadInfra_vis_cat=df_roadInfra_vis['CATEGORY'].unique()
roadInfra_vis_sc=df_roadInfra_vis['SUBCATEGORY'].unique()
roadInfra_vis_source=df_roadInfra_vis['SOURCE'].unique()
roadInfra_vis_unit=df_roadInfra_vis['UNIT'].unique()

# Get some data
st.write("Category:"+roadInfra_vis_cat[0])
st.write("Sub Category:"+roadInfra_vis_sc[0])
st.write("Info Source:"+roadInfra_vis_source[0])
st.write("Unit of Value:"+roadInfra_vis_unit[0])
# Plot 
figroadInfra = px.line(df_roadInfra_vis, x='DATE', y=state_sel_roadInfra, labels={'Total Quarterly Usage - Current (PB)': "hello"})
# Set x-axis title
figroadInfra.update_xaxes(title_text="Duration")
# Set y-axes titles
figroadInfra.update_yaxes(title_text="Measure", secondary_y=False)
figroadInfra.update_layout(showlegend=True)
figroadInfra.update_layout(showlegend=True)
# Show plot 

st.plotly_chart(figroadInfra)

#######################################################################################################################################
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.subheader("Cargo Moved through Ports and Inland waterways")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("""The Infrastructure and Road Construction details are mentioned in the below Datasets""")


cat_sel_watCargo=st.selectbox('Category Infra:',list(df_watCargo['TITLE'].unique()),placeholder="Select a Option to Display Data")
state_sel_watCargo=st.selectbox('Category  state:',st_india_watCargo,placeholder="Select a Option to Display Data",key="watCargo")
df_watCargo_vis = df_watCargo[df_watCargo['TITLE']==cat_sel_watCargo]
df_watCargo_vis=df_watCargo_vis.sort_values(by=['DATE'], ascending=False)
df_watCargo_vis=df_watCargo_vis.drop_duplicates(subset='DATE', keep="last")
watCargo_vis_cat=df_watCargo_vis['CATEGORY'].unique()
watCargo_vis_sc=df_watCargo_vis['SUBCATEGORY'].unique()
watCargo_vis_source=df_watCargo_vis['SOURCE'].unique()
watCargo_vis_unit=df_watCargo_vis['UNIT'].unique()

# Get some data
st.write("Category:"+watCargo_vis_cat[0])
st.write("Sub Category:"+watCargo_vis_sc[0])
st.write("Info Source:"+watCargo_vis_source[0])
st.write("Unit of Value:"+watCargo_vis_unit[0])
# Plot 
figwatCargo = px.line(df_watCargo_vis, x='DATE', y=state_sel_watCargo, labels={'Total Quarterly Usage - Current (PB)': "hello"})
# Set x-axis title
figwatCargo.update_xaxes(title_text="Duration")
# Set y-axes titles
figwatCargo.update_yaxes(title_text="Measure", secondary_y=False)
figwatCargo.update_layout(showlegend=True)
figwatCargo.update_layout(showlegend=True)
# Show plot 
st.plotly_chart(figwatCargo)



#######################################################################################################################################
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.subheader("Indian Railway Infra and Manpower")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("""The Infrastructure and Road Construction details are mentioned in the below Datasets""")

cat_sel_RailInfra=st.selectbox('Category Infra:',list(df_RailInfra['TITLE'].unique()),placeholder="Select a Option to Display Data")
state_sel_RailInfra=st.selectbox('Category  state:',st_india_RailInfra,placeholder="Select a Option to Display Data",key="RailInfra")
df_RailInfra_vis = df_RailInfra[df_RailInfra['TITLE']==cat_sel_RailInfra]
df_RailInfra_vis=df_RailInfra_vis.sort_values(by=['DATE'], ascending=False)
df_RailInfra_vis=df_RailInfra_vis.drop_duplicates(subset='DATE', keep="last")
RailInfra_vis_cat=df_RailInfra_vis['CATEGORY'].unique()
RailInfra_vis_sc=df_RailInfra_vis['SUBCATEGORY'].unique()
RailInfra_vis_source=df_RailInfra_vis['SOURCE'].unique()
RailInfra_vis_unit=df_RailInfra_vis['UNIT'].unique()

# Get some data
st.write("Category:"+RailInfra_vis_cat[0])
st.write("Sub Category:"+RailInfra_vis_sc[0])
st.write("Info Source:"+RailInfra_vis_source[0])
st.write("Unit of Value:"+RailInfra_vis_unit[0])
# Plot 
figRailInfra = px.line(df_RailInfra_vis, x='DATE', y=state_sel_RailInfra, labels={'Total Quarterly Usage - Current (PB)': "hello"})
# Set x-axis title
figRailInfra.update_xaxes(title_text="Duration")
# Set y-axes titles
figRailInfra.update_yaxes(title_text="Measure", secondary_y=False)
figRailInfra.update_layout(showlegend=True)
figRailInfra.update_layout(showlegend=True)
# Show plot 
st.plotly_chart(figRailInfra)



#######################################################################################################################################
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.subheader("Indian Railway Passengers")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("""The Indian Railway Passengers details are mentioned below. """)

cat_sel_RailPass=st.selectbox('Category Infra:',list(df_RailPass['TITLE'].unique()),placeholder="Select a Option to Display Data")
state_sel_RailPass=st.selectbox('Category  state:',st_india_RailPass,placeholder="Select a Option to Display Data",key="RailPass")
df_RailPass_vis = df_RailPass[df_RailPass['TITLE']==cat_sel_RailPass]
df_RailPass_vis=df_RailPass_vis.sort_values(by=['DATE'], ascending=False)
df_RailPass_vis=df_RailPass_vis.drop_duplicates(subset='DATE', keep="last")
RailPass_vis_cat=df_RailPass_vis['CATEGORY'].unique()
RailPass_vis_sc=df_RailPass_vis['SUBCATEGORY'].unique()
RailPass_vis_source=df_RailPass_vis['SOURCE'].unique()
RailPass_vis_unit=df_RailPass_vis['UNIT'].unique()

# Get some data
st.write("Category:"+RailPass_vis_cat[0])
st.write("Sub Category:"+RailPass_vis_sc[0])
st.write("Info Source:"+RailPass_vis_source[0])
st.write("Unit of Value:"+RailPass_vis_unit[0])
# Plot 
figRailPass = px.line(df_RailPass_vis, x='DATE', y=state_sel_RailPass, labels={'Total Quarterly Usage - Current (PB)': "hello"})
# Set x-axis title
figRailPass.update_xaxes(title_text="Duration")
# Set y-axes titles
figRailPass.update_yaxes(title_text="Measure", secondary_y=False)
figRailPass.update_layout(showlegend=True)
figRailPass.update_layout(showlegend=True)
# Show plot 
st.plotly_chart(figRailPass)




#######################################################################################################################################
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.subheader("Indian Railway Earnings")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("""The Indian Railway Earnings details are mentioned below. """)


cat_sel_RailEco=st.selectbox('Category Infra:',list(df_RailEco['TITLE'].unique()),placeholder="Select a Option to Display Data")
state_sel_RailEco=st.selectbox('Category loan state:',st_india_RailEco,placeholder="Select a Option to Display Data",key="RailEco")
df_RailEco_vis = df_RailEco[df_RailEco['TITLE']==cat_sel_RailEco]
df_RailEco_vis=df_RailEco_vis.sort_values(by=['DATE'], ascending=False)
df_RailEco_vis=df_RailEco_vis.drop_duplicates(subset='DATE', keep="last")
RailEco_vis_cat=df_RailEco_vis['CATEGORY'].unique()
RailEco_vis_sc=df_RailEco_vis['SUBCATEGORY'].unique()
RailEco_vis_source=df_RailEco_vis['SOURCE'].unique()
RailEco_vis_unit=df_RailEco_vis['UNIT'].unique()

# Get some data
st.write("Category:"+RailEco_vis_cat[0])
st.write("Sub Category:"+RailEco_vis_sc[0])
st.write("Info Source:"+RailEco_vis_source[0])
st.write("Unit of Value:"+RailEco_vis_unit[0])
# Plot 
figRailEco = px.line(df_RailEco_vis, x='DATE', y=state_sel_RailEco, labels={'Total Quarterly Usage - Current (PB)': "hello"})
# Set x-axis title
figRailEco.update_xaxes(title_text="Duration")
# Set y-axes titles
figRailEco.update_yaxes(title_text="Measure", secondary_y=False)
figRailEco.update_layout(showlegend=True)
figRailEco.update_layout(showlegend=True)
# Show plot 
st.plotly_chart(figRailEco)


#######################################################################################################################################
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.subheader("Airway Passenger Details Domestic and International")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("""Airway Passenger Details Domestic and International are mentioned below. """)


cat_sel_AirPass=st.selectbox('Category Infra:',list(df_AirPass['TITLE'].unique()),placeholder="Select a Option to Display Data")
state_sel_AirPass=st.selectbox('Category loan state:',st_india_AirPass,placeholder="Select a Option to Display Data",key="AirPass")
df_AirPass_vis = df_AirPass[df_AirPass['TITLE']==cat_sel_AirPass]
df_AirPass_vis=df_AirPass_vis.sort_values(by=['DATE'], ascending=False)
df_AirPass_vis=df_AirPass_vis.drop_duplicates(subset='DATE', keep="last")
AirPass_vis_cat=df_AirPass_vis['CATEGORY'].unique()
AirPass_vis_sc=df_AirPass_vis['SUBCATEGORY'].unique()
AirPass_vis_source=df_AirPass_vis['SOURCE'].unique()
AirPass_vis_unit=df_AirPass_vis['UNIT'].unique()

# Get some data
st.write("Category:"+AirPass_vis_cat[0])
st.write("Sub Category:"+AirPass_vis_sc[0])
st.write("Info Source:"+AirPass_vis_source[0])
st.write("Unit of Value:"+AirPass_vis_unit[0])
# Plot 
figAirPass = px.line(df_AirPass_vis, x='DATE', y=state_sel_AirPass, labels={'Total Quarterly Usage - Current (PB)': "hello"})
# Set x-axis title
figAirPass.update_xaxes(title_text="Duration")
# Set y-axes titles
figAirPass.update_yaxes(title_text="Measure", secondary_y=False)
figAirPass.update_layout(showlegend=True)
figAirPass.update_layout(showlegend=True)
# Show plot 
st.plotly_chart(figAirPass)





#######################################################################################################################################
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.subheader("International Cargo and Freight")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("""Statewise International Cargo and Freight. """)

cat_sel_AirFreight=st.selectbox('Category Infra:',list(df_AirFreight['TITLE'].unique()),placeholder="Select a Option to Display Data")
state_sel_AirFreight=st.selectbox('Category loan state:',st_india_AirFreight,placeholder="Select a Option to Display Data",key="AirFreight")
df_AirFreight_vis = df_AirFreight[df_AirFreight['TITLE']==cat_sel_AirFreight]
df_AirFreight_vis=df_AirFreight_vis.sort_values(by=['DATE'], ascending=False)
df_AirFreight_vis=df_AirFreight_vis.drop_duplicates(subset='DATE', keep="last")
AirFreight_vis_cat=df_AirFreight_vis['CATEGORY'].unique()
AirFreight_vis_sc=df_AirFreight_vis['SUBCATEGORY'].unique()
AirFreight_vis_source=df_AirFreight_vis['SOURCE'].unique()
AirFreight_vis_unit=df_AirFreight_vis['UNIT'].unique()

# Get some data
st.write("Category:"+AirFreight_vis_cat[0])
st.write("Sub Category:"+AirFreight_vis_sc[0])
st.write("Info Source:"+AirFreight_vis_source[0])
st.write("Unit of Value:"+AirFreight_vis_unit[0])
# Plot 
figAirFreight = px.line(df_AirFreight_vis, x='DATE', y=state_sel_AirFreight, labels={'Total Quarterly Usage - Current (PB)': "hello"})
# Set x-axis title
figAirFreight.update_xaxes(title_text="Duration")
# Set y-axes titles
figAirFreight.update_yaxes(title_text="Measure", secondary_y=False)
figAirFreight.update_layout(showlegend=True)
figAirFreight.update_layout(showlegend=True)
# Show plot 
st.plotly_chart(figAirFreight)



#######################################################################################################################################
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.subheader(" Cargo handled by Ports")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("""Statewise Cargo handled by Ports. """)
cat_sel_PortCargo=st.selectbox('Category Infra:',list(df_PortCargo['TITLE'].unique()),placeholder="Select a Option to Display Data")
state_sel_PortCargo=st.selectbox('Category loan state:',st_india_PortCargo,placeholder="Select a Option to Display Data",key="PortCargo")
df_PortCargo_vis = df_PortCargo[df_PortCargo['TITLE']==cat_sel_PortCargo]
df_PortCargo_vis=df_PortCargo_vis.sort_values(by=['DATE'], ascending=False)
df_PortCargo_vis=df_PortCargo_vis.drop_duplicates(subset='DATE', keep="last")
PortCargo_vis_cat=df_PortCargo_vis['CATEGORY'].unique()
PortCargo_vis_sc=df_PortCargo_vis['SUBCATEGORY'].unique()
PortCargo_vis_source=df_PortCargo_vis['SOURCE'].unique()
PortCargo_vis_unit=df_PortCargo_vis['UNIT'].unique()

# Get some data
st.write("Category:"+PortCargo_vis_cat[0])
st.write("Sub Category:"+PortCargo_vis_sc[0])
st.write("Info Source:"+PortCargo_vis_source[0])
st.write("Unit of Value:"+PortCargo_vis_unit[0])
# Plot 
figPortCargo = px.line(df_PortCargo_vis, x='DATE', y=state_sel_PortCargo, labels={'Total Quarterly Usage - Current (PB)': "hello"})
# Set x-axis title
figPortCargo.update_xaxes(title_text="Duration")
# Set y-axes titles
figPortCargo.update_yaxes(title_text="Measure", secondary_y=False)
figPortCargo.update_layout(showlegend=True)
figPortCargo.update_layout(showlegend=True)
# Show plot 
st.plotly_chart(figPortCargo)



#######################################################################################################################################
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.subheader(" Consumption of Petrol and Diesel")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("""Annual and Monthly Consumption of Petrol and Diesel """)

cat_sel_Fuel=st.selectbox('Category Infra:',list(df_Fuel['TITLE'].unique()),placeholder="Select a Option to Display Data")
state_sel_Fuel=st.selectbox('Category loan state:',st_india_Fuel,placeholder="Select a Option to Display Data",key="Fuel")
df_Fuel_vis = df_Fuel[df_Fuel['TITLE']==cat_sel_Fuel]
df_Fuel_vis=df_Fuel_vis.sort_values(by=['DATE'], ascending=False)
df_Fuel_vis=df_Fuel_vis.drop_duplicates(subset='DATE', keep="last")
Fuel_vis_cat=df_Fuel_vis['CATEGORY'].unique()
Fuel_vis_sc=df_Fuel_vis['SUBCATEGORY'].unique()
Fuel_vis_source=df_Fuel_vis['SOURCE'].unique()
Fuel_vis_unit=df_Fuel_vis['UNIT'].unique()

# Get some data
st.write("Category:"+Fuel_vis_cat[0])
st.write("Sub Category:"+Fuel_vis_sc[0])
st.write("Info Source:"+Fuel_vis_source[0])
st.write("Unit of Value:"+Fuel_vis_unit[0])
# Plot 
figFuel = px.line(df_Fuel_vis, x='DATE', y=state_sel_Fuel, labels={'Total Quarterly Usage - Current (PB)': "hello"})
# Set x-axis title
figFuel.update_xaxes(title_text="Duration")
# Set y-axes titles
figFuel.update_yaxes(title_text="Measure", secondary_y=False)
figFuel.update_layout(showlegend=True)
figFuel.update_layout(showlegend=True)
# Show plot 
st.plotly_chart(figFuel)