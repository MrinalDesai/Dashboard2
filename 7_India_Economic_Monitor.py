import plotly.express as px 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import streamlit as st
# Get some data

st.header('INDIA ECONOMIC MONITOR', divider="gray")
st.write("Some data may be blank based on its availability.")
df = pd.read_excel(f'datasets/india_em/output1.xlsx')

df_filter_loan=pd.read_excel(f'datasets/india_em/INDIA_ECONOMIC_MONITOR SELECT DISTINCT identifier,TITLE from ECONOMY.IDH_DATA;.xlsx',sheet_name='Loans')
df_filter_credit=pd.read_excel(f'datasets/india_em/INDIA_ECONOMIC_MONITOR SELECT DISTINCT identifier,TITLE from ECONOMY.IDH_DATA;.xlsx',sheet_name='Credit')
df_filter_fuel=pd.read_excel(f'datasets/india_em/INDIA_ECONOMIC_MONITOR SELECT DISTINCT identifier,TITLE from ECONOMY.IDH_DATA;.xlsx',sheet_name='Fuel')
df_filter_reg=pd.read_excel(f'datasets/india_em/INDIA_ECONOMIC_MONITOR SELECT DISTINCT identifier,TITLE from ECONOMY.IDH_DATA;.xlsx',sheet_name='Registrations')
df_filter_STATE=pd.read_excel(f'datasets/india_em/INDIA_ECONOMIC_MONITOR SELECT DISTINCT identifier,TITLE from ECONOMY.IDH_DATA;.xlsx',sheet_name='state')

ident_loan=list(df_filter_loan['IDENTIFIER'])
ident_credit=list(df_filter_credit['IDENTIFIER'])
ident_fuel=list(df_filter_fuel['IDENTIFIER'])
ident_reg=list(df_filter_reg['IDENTIFIER'])
st_india_loan=list(df_filter_STATE['INDIA/STATE'])
st_india_credit=list(df_filter_STATE['INDIA/STATE'])
st_india_fuel=list(df_filter_STATE['INDIA/STATE'])
st_india_reg=list(df_filter_STATE['INDIA/STATE'])

# Get some data
df_loan = df[df['IDENTIFIER'].isin(ident_loan)]
df_credit=df[df['IDENTIFIER'].isin(ident_credit)]
df_fuel=df[df['IDENTIFIER'].isin(ident_fuel)]
df_reg=df[df['IDENTIFIER'].isin(ident_reg)]

st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.header('Vehicle Related Loans', divider="gray")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("This data consists of Various Loan Categories as well as Non Performing Loans.")

cat_sel_loan=st.selectbox('Category loan:',list(df_loan['TITLE'].unique()),placeholder="Select a Option to Display Data")
state_sel_loan=st.selectbox('Category loan state:',st_india_loan,placeholder="Select a Option to Display Data")
df_loan_vis = df_loan[df_loan['TITLE']==cat_sel_loan]
df_loan_vis=df_loan_vis.sort_values(by=['DATE'], ascending=False)
df_loan_vis=df_loan_vis.drop_duplicates(subset='DATE', keep="last")
loan_vis_cat=df_loan_vis['CATEGORY'].unique()
loan_vis_sc=df_loan_vis['SUBCATEGORY'].unique()
loan_vis_source=df_loan_vis['SOURCE'].unique()
loan_vis_unit=df_loan_vis['UNIT'].unique()

# Get some data
st.write("Category:"+loan_vis_cat[0])
st.write("Sub Category:"+loan_vis_sc[0])
st.write("Info Source:"+loan_vis_source[0])
st.write("Unit of Value:"+loan_vis_unit[0])
# Plot 
figloan = px.line(df_loan_vis, x='DATE', y=state_sel_loan, labels={'Total Quarterly Usage - Current (PB)': "hello"})
# Set x-axis title
figloan.update_xaxes(title_text="Duration")
# Set y-axes titles
figloan.update_yaxes(title_text="Measure", secondary_y=False)
figloan.update_layout(showlegend=True)
figloan.update_layout(showlegend=True)
# Show plot 
st.plotly_chart(figloan)



st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.header('Credit related to Vehicle Industry', divider="gray")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("Statewise Credit related to Vehicle Industry.")

cat_sel_credit=st.selectbox('Category credit :',list(df_credit['TITLE'].unique()),placeholder="Select a Option to Display Data")
state_sel_credit=st.selectbox('Category credit state/india:',st_india_credit,placeholder="Select a Option to Display Data")
df_credit_vis=df_credit[df_credit['TITLE']==cat_sel_credit]
df_credit_vis=df_credit_vis.sort_values(by=['DATE'], ascending=False)
df_credit_vis=df_credit_vis.drop_duplicates(subset='DATE', keep="last")
credit_vis_cat=df_credit_vis['CATEGORY'].unique()
credit_vis_sc=df_credit_vis['SUBCATEGORY'].unique()
credit_vis_source=df_credit_vis['SOURCE'].unique()
credit_vis_unit=df_credit_vis['UNIT'].unique()


# Get some data
st.write("Category:"+credit_vis_cat[0])
st.write("Sub Category:"+credit_vis_sc[0])
st.write("Info Source:"+credit_vis_source[0])
st.write("Unit of Value:"+credit_vis_unit[0])
# Plot 
figcredit = px.line(df_credit_vis, x='DATE', y=state_sel_loan, labels={'Total Quarterly Usage - Current (PB)': "hello"})
# Set x-axis title
figcredit.update_xaxes(title_text="Duration")
# Set y-axes titles
figcredit.update_yaxes(title_text="Measure", secondary_y=False)
figcredit.update_layout(showlegend=True)
figcredit.update_layout(showlegend=True)
# Show plot 
st.plotly_chart(figcredit)


st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.header('Fuel Data', divider="gray")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("Diesel and Petrol Price.")
cat_sel_fuel=st.selectbox('Category fuel stats:',list(df_fuel['TITLE'].unique()),placeholder="Select a Option to Display Data")
state_sel_fuel=st.selectbox('Category fuel state/india:',st_india_fuel,placeholder="Select a Option to Display Data")
df_fuel_vis=df_fuel[df_fuel['TITLE']==cat_sel_fuel]
df_fuel_vis=df_fuel_vis.sort_values(by=['DATE'], ascending=False)
df_fuel_vis=df_fuel_vis.drop_duplicates(subset='DATE', keep="last")
fuel_vis_cat=df_fuel_vis['CATEGORY'].unique()
fuel_vis_sc=df_fuel_vis['SUBCATEGORY'].unique()
fuel_vis_source=df_fuel_vis['SOURCE'].unique()
fuel_vis_unit=df_fuel_vis['UNIT'].unique()

# Get some data
st.write("Category:"+fuel_vis_cat[0])
st.write("Sub Category:"+fuel_vis_sc[0])
st.write("Info Source:"+fuel_vis_source[0])
st.write("Unit of Value:"+fuel_vis_unit[0])
# Plot 
figfuel = px.line(df_fuel_vis, x='DATE', y=state_sel_loan, labels={'Total Quarterly Usage - Current (PB)': "hello"})
# Set x-axis title
figfuel.update_xaxes(title_text="Duration")
# Set y-axes titles
figfuel.update_yaxes(title_text="Measure", secondary_y=False)
figfuel.update_layout(showlegend=True)
figfuel.update_layout(showlegend=True)
# Show plot 
st.plotly_chart(figfuel)


st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.header('Vehicle Registration data', divider="gray")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("Vehicle Registration data")

cat_sel_reg=st.selectbox('Category registration:',list(df_reg['TITLE'].unique()),placeholder="Select a Option to Display Data")
state_sel_reg=st.selectbox('registration state/india:',st_india_reg,placeholder="Select a Option to Display Data")
df_reg_vis=df_reg[df_reg['TITLE']==cat_sel_reg]
df_reg_vis=df_reg_vis.sort_values(by=['DATE'], ascending=False)
df_reg_vis=df_reg_vis.drop_duplicates(subset='DATE', keep="last")
reg_vis_cat=df_reg_vis['CATEGORY'].unique()
reg_vis_sc=df_reg_vis['SUBCATEGORY'].unique()
reg_vis_source=df_reg_vis['SOURCE'].unique()
reg_vis_unit=df_reg_vis['UNIT'].unique()

# Get some data
st.write("Category:"+reg_vis_cat[0])
st.write("Sub Category:"+reg_vis_sc[0])
st.write("Info Source:"+reg_vis_source[0])
st.write("Unit of Value:"+reg_vis_unit[0])
#Plot 
figreg = px.bar(df_reg_vis, x='DATE', y=state_sel_reg, labels={'Total Quarterly Usage1 - Current (PB)': "hello"},color=state_sel_reg)
# Set x-axis title
figreg.update_xaxes(title_text="Duration")
# Set y-axes titles
figreg.update_yaxes(title_text="Measure", secondary_y=False)
figreg.update_layout(showlegend=True)
figreg.update_layout(showlegend=True)
# Show plot 
st.plotly_chart(figreg)

