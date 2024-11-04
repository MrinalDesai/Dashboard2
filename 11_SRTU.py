import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import plotly.graph_objects as go
from plotly.subplots import make_subplots


#st.title('Motorised vehicle developments')
st.header('STRU stats', divider="gray")
st.subheader("#️⃣SRTU Performance,Public vs Private comparison📌 ", divider="gray")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("#️⃣Best vs Worst Performers Fleet held/Fleet Age/ Accidents Revenue/Profit Loss etc 2015-2019📌 ")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")

st.write("This gives a glimpse of how the Performance of SRTU's is evaluated")
df_per_main_best=pd.read_excel(f'datasets/SRTU/best worst 15-19.xlsx',sheet_name='Main Best')
df_per_main_worst=pd.read_excel(f'datasets/SRTU/best worst 15-19.xlsx',sheet_name='Main Worst')
df_per_grp=pd.read_excel(f'datasets/SRTU/best worst 15-19.xlsx',sheet_name='Group')

df_per_main_best.set_index('Year', inplace=True)

df_per_main_worst.set_index('Year', inplace=True)

st.write("Best Performers")
st.write(df_per_main_best)

st.write("Worst Performers")
st.write(df_per_main_worst)



##############################################################################################################

st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("#️⃣SRTUs wise physical performance of SRTUs for the years ending March 2017, 2018 and 2019📌 ")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("""This gives a glimpse Average Fleet Held/Operated,Fleet Utilisation,Fleet Age,Fuel efficiency,Staff Strength/Productivity,
         Occupancy Ratio,Passengers carried.""")

df_PP=pd.read_excel(f'datasets/SRTU/SRTUs wise physical performance of SRTUs for the years ending March 2017, 2018 and 2019.xlsx',sheet_name='SRTUs wise physical performance')
df_PP_grp=pd.read_excel(f'datasets/SRTU/SRTUs wise physical performance of SRTUs for the years ending March 2017, 2018 and 2019.xlsx',sheet_name='Group')


PP_grp=df_PP_grp.groupby('Group')['S. No.'].apply(list).reset_index(name='Items')

PP_grp.set_index('Group', inplace=True)
dct_PP = PP_grp.T.to_dict()

PP_grp_items=list(df_PP_grp['Group'].unique())

PP_grp=st.selectbox("Finance Parameter Group",PP_grp_items,placeholder="Select a Option to Display Data")

PP_grp_items_col=dct_PP[PP_grp]['Items']
PP_grp_items_col.insert(0,'Name of State Road Transport Undertaking (SRTU)')
df_PP_display=df_PP[PP_grp_items_col]


fig_PP_display = go.Figure(data=[go.Table(
    
    columnwidth = [700,600,600,600,600,600],
    header=dict(values=list(df_PP_display.columns),
                fill_color='darkturquoise',
                # fill_color='#b9e2ff',
                line_color='darkslategray',
                font = dict(family="Arial", size=10, color="black"),
                align='left'),
    cells=dict(values=df_PP_display.transpose().values.tolist(),
               fill_color='lightgray',
                font = dict(family="Arial", size=10, color="black"),
               align='left'))
])
# Add fig_subure title
fig_PP_display.update_layout(
    title_text="Physical performance of SRTU"
)
st.plotly_chart(fig_PP_display)



##############################################################################################################
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("#️⃣StatesUTs-wiseTotal Bus Fleet and Buses in Public Sector📌 ")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("""This gives info on buses owned.""")

df_Fleet=pd.read_excel(f'datasets/SRTU/StatesUTs-wiseTotal Bus Fleet and Buses in Public Sector (SRTUs)(As on 31st March, 2014-2020).xlsx',sheet_name='StatesUTs-wiseTotal Bus Fleet a')
df_Fleet_grp=pd.read_excel(f'datasets/SRTU/StatesUTs-wiseTotal Bus Fleet and Buses in Public Sector (SRTUs)(As on 31st March, 2014-2020).xlsx',sheet_name='Group')

Fleet_grp=df_Fleet_grp.groupby('Category')['S. No.'].apply(list).reset_index(name='Items')

Fleet_grp.set_index('Category', inplace=True)
dct_Fleet = Fleet_grp.T.to_dict()

Fleet_grp_items=list(df_Fleet_grp['Category'].unique())

Fleet_grp=st.selectbox("Fleet Group",Fleet_grp_items,placeholder="Select a Option to Display Data",key="Fleet")

Fleet_grp_items_col=dct_Fleet[Fleet_grp]['Items']
Fleet_grp_items_col.insert(0,'STATES / UTs')
df_Fleet_display=df_Fleet[Fleet_grp_items_col]



fig_Fleet_display = go.Figure(data=[go.Table(
    
    columnwidth = [700,600,600,600,600,600],
    header=dict(values=list(df_Fleet_display.columns),
                fill_color='darkturquoise',
                # fill_color='#b9e2ff',
                line_color='darkslategray',
                font = dict(family="Arial", size=10, color="black"),
                align='left'),
    cells=dict(values=df_Fleet_display.transpose().values.tolist(),
               fill_color='lightgray',
                font = dict(family="Arial", size=10, color="black"),
               align='left'))
    
])
# Add fig_subure title
fig_Fleet_display.update_layout(
    title_text="Bus Fleet and Buses in Public Sector (SRTUs)"
)
st.plotly_chart(fig_Fleet_display)




##############################################################################################################
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("#️⃣StateUnion Territory-wise Spread of SRTUs📌 ")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("""This gives info on buses owned Across States.""")

df_den_SRTU=pd.read_csv(f'datasets/SRTU/StateUnion Territory-wise Spread of SRTUs.csv')
df_den_SRTU=df_den_SRTU[['States/Uts','Number of Persons per SRTU bus','Number of Persons per SRTU bus','Number of Buses per 10 lakh population']]



fig_den_SRTU = go.Figure(data=[go.Table(
    
    columnwidth = [700,600,600,600,600,600],
    header=dict(values=list(df_den_SRTU.columns),
                fill_color='darkturquoise',
                # fill_color='#b9e2ff',
                line_color='darkslategray',
                font = dict(family="Arial", size=10, color="black"),
                align='left'),
    cells=dict(values=df_den_SRTU.transpose().values.tolist(),
               fill_color='lightgray',
                font = dict(family="Arial", size=10, color="black"),
               align='left'))
    
])
# Add fig_subure title
fig_den_SRTU.update_layout(
    title_text="Spread of SRTUs"
)
st.plotly_chart(fig_den_SRTU)

########################################################################################################
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("#️⃣Year-wise Number of Buses Owned by the Public and Private Sectors in India from 1961 to 2019📌 ")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("""This gives info on buses owned Private vs Public Sectors. it shows us how Public Sector is way behind.""")
import plotly.graph_objs as go

# Get some data
df_pubpri = pd.read_csv(f'datasets/SRTU/Year-wise Number of Buses Owned by the Public and Private Sectors in India from 1961 to 2019.csv')


df_pubpri_no=df_pubpri[['Year (As on 31st March)','Public Sector(In thousands)','Private Sector(In thousands)','Total']]
df_pubpri_perc=df_pubpri[['Year (As on 31st March)',"%age share to total buses-Public",'%age share to total buses-Private']]


x_pubpri = df_pubpri_no['Year (As on 31st March)']
y_pubpri_1 = df_pubpri_no['Public Sector(In thousands)']
y_pubpri_2 = df_pubpri_no['Private Sector(In thousands)']
y_pubpri_3 = df_pubpri_no['Total']


tracepubpri_1 = go.Scatter(x=x_pubpri, y=y_pubpri_1, mode='lines', name='Public Sector(In thousands)')
tracepubpri_2 = go.Scatter(x=x_pubpri, y=y_pubpri_2, mode='lines', name='Private Sector(In thousands)')
tracepubpri_3 = go.Scatter(x=x_pubpri, y=y_pubpri_3, mode='lines', name='Total')

figpubpri = go.Figure([
    tracepubpri_1, tracepubpri_2,tracepubpri_3
])
figpubpri.update_layout(
    title = 'Number of Buses Owned by the Public and Private Sectors',
    width = 1100,
    xaxis_title = 'Duration',
    yaxis_title = 'No (In thousands) '
)

st.plotly_chart(figpubpri)



x_pubpri_per = df_pubpri_perc['Year (As on 31st March)']
y_pubpri_1_per = df_pubpri_perc["%age share to total buses-Public"]
y_pubpri_2_per = df_pubpri_perc['%age share to total buses-Private']



tracepubpri_1_per = go.Scatter(x=x_pubpri_per, y=y_pubpri_1_per, mode='lines', name='Public Sector')
tracepubpri_2_per = go.Scatter(x=x_pubpri_per, y=y_pubpri_2_per, mode='lines', name='Private Sector')


figpubpri_per = go.Figure([
    tracepubpri_1_per, tracepubpri_2_per
])
figpubpri_per.update_layout(
    title = 'Number of Buses Owned by the Public and Private Sectors',
    width = 1100,
    xaxis_title = 'Duration',
    yaxis_title = 'Percentage'
)

st.plotly_chart(figpubpri_per,key="percetage")

import matplotlib.pyplot as plt
from PIL import Image 


image = plt.imread(f"datasets/Buses Owned 2001-2012.jpg")
st.image(image, caption="Buses Owned by the Public and Private Sectors during 2001-2012")



########################################################################################################
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("#️⃣StateUTsCity-wise Details of the Electric and Hybrid Buses, Sanctioned and Deployed under first phase of the FAME India Scheme📌 ")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("""This gives effort Govt is taking to incorporate Electric Transportation System.""")

# Get some data
df_elec = pd.read_csv(f'datasets/SRTU/StateUTsCity-wise Details of the Electric and Hybrid Buses, Sanctioned and Deployed under first phase of the FAME India Scheme.csv')

st.write(df_elec)



########################################################################################################
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("#️⃣StatesUTs-wise Number of Conductors Licences Issued as on 31.3.2020 and during 2019-20📌 ")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("""Total of 3.3 Million Licences were issued.""")

df_licence = pd.read_csv(f'datasets/SRTU/StatesUTs-wise Number of Conductors Licences Issued as on 31.3.2020 and during 2019-20.csv')


state_op=list(df_licence['STATES/UTs'].unique())

state_sel=st.selectbox("STATES/UTs",state_op,placeholder="Select a Option to Display Data",index=state_op.index('Total'))



licen=df_licence[df_licence['STATES/UTs']==state_sel].reset_index()

st.write('Licences valid at the end of the year i.e upto 31.3.2020 (Cummulative) - Male')
st.write("➡️"+str(licen['Licences valid at the end of the year i.e upto 31.3.2020 (Cummulative) - Male'][0]))
st.write('Licences valid at the end of the year i.e upto 31.3.2020 (Cummulative) - Female')
st.write("➡️"+str(licen['Licences valid at the end of the year i.e upto 31.3.2020 (Cummulative) - Female'][0]))
st.write('Licences valid at the end of the year i.e upto 31.3.2020 (Cummulative) - Total')
st.write("➡️"+str(licen['Licences valid at the end of the year i.e upto 31.3.2020 (Cummulative) - Total'][0]))
st.write('New licences issued during the year i.e during 2019-20 (Incremental) - Male')
st.write("➡️"+str(licen['New licences issued during the year i.e during 2019-20 (Incremental) - Male'][0]))
st.write('New licences issued during the year i.e during 2019-20 (Incremental) - Female')
st.write("➡️"+str(licen['New licences issued during the year i.e during 2019-20 (Incremental) - Female'][0]))
st.write('New licences issued during the year i.e during 2019-20 (Incremental) - Total')
st.write("➡️"+str(licen['New licences issued during the year i.e during 2019-20 (Incremental) - Total'][0]))