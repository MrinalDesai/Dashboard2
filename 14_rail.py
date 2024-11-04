import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.title('Introduction')
st.header('Rail Infrastructure', divider="gray")
st.subheader("#️⃣Development and Facilities📌 ", divider="gray")

df_Operations=pd.read_excel(f'datasets/RAIL/Operations of Indian Railways-done.xlsx')

# st.write(df_reg_veh)
st.write('''Over years Indian Govt has significantly worked n Electrification of Routes and increased the capacity
''')

fig_Operations = go.Figure(data=[go.Table(
    
    columnwidth = [700,600,600,600,600,600],
    header=dict(values=list(df_Operations.columns),
                fill_color='darkturquoise',
                # fill_color='#b9e2ff',
                line_color='darkslategray',
                font = dict(family="Arial", size=10, color="black"),
                align='left'),
    cells=dict(values=df_Operations.transpose().values.tolist(),
               fill_color='lightgray',
                font = dict(family="Arial", size=10, color="black"),
               align='left'))
])
# Add fig_subure title
fig_Operations.update_layout(
    title_text="Operations of Indian Railways"
)

st.plotly_chart(fig_Operations)


st.write("P Provisional")        
st.write("a Excluding Konkan Railways Corporation Limited Loading")  
st.write("b Excluding Metro Kolkata")  
st.write("c Includes Metro Railway/Kolkata's earnings")  


#####################################################################################################
st.subheader("Punctiality",divider="gray")
st.write('''Punctuality has to improve and reach above 90 percent
''')

df_punc=pd.read_csv(f'datasets/RAIL/Month-wise Indian Railways Punctuality of MailExpress Trains & Passenger trains from April-November 2018 (From  Ministry of Railways)-done.csv')

st.plotly_chart(px.bar(df_punc,x="Months",y="Mail/Express",height=300,width=500, text_auto='.2s',color="Mail/Express",title="Month-wise Indian Railways Punctuality-Passenger"))


st.plotly_chart(px.bar(df_punc,x="Months",y="Passenger",height=300,width=500, text_auto='.2s',color="Passenger",title="Month-wise Indian Railways Punctuality-MailExpress"))

#####################################################################################################
st.subheader("Railway Density",divider="gray")
st.write('''Railway Density has to improve in The Rural Sector.
''')

df_density=pd.read_csv(f'datasets/RAIL/Railway Density of India-done.csv')


df_density=df_density.transpose().reset_index()
new_header = df_density.iloc[0]
df_density=df_density[1:]
df_density.columns = new_header
df_density=df_density.rename({'Particulars':'Year'}, axis=1)
# st.write(df_density)


x_data_density = df_density['Year']

y_data_1_density = df_density['Railway Density: Train Kilometres per Running Track: Suburban']
y_data_2_density = df_density['Railway Density: Train Kilometres per Running Track: Non Suburban']


trace_1_density = go.Scatter(x=x_data_density, y=y_data_1_density, mode='lines', name='Suburban')
trace_2_density = go.Scatter(x=x_data_density, y=y_data_2_density, mode='lines', name='Non Suburban')


fig_density = go.Figure([
    trace_1_density, trace_2_density
])
fig_density.update_layout(
    title = 'Railway Density: Train Kilometres per Running Track',
    width = 1100,
    
    xaxis_title = 'Year',
    yaxis_title = 'Density'
)

fig_density.update_yaxes(range=[0, 100])
st.plotly_chart(fig_density)



#####################################################################################################
st.subheader("Railway Infrastructure Expansion",divider="gray")
st.write('''Government has Invested a lot to improve Connectivity.
''')

df_expansion=pd.read_csv(f'datasets/RAIL/Zonal Railway-wise Details of the New Line, Gauge Conversion and Doubling Projects included in the Budget to provide Connectivityareaswhichot ConnectedRailway Network2019-20 to 2022-23-done.csv')
st.write("Below table shows Zonal Railway-wise Details of the New Line, Gauge Conversion and Doubling Projects included in the Budget to provide Connectivityareaswhichot ConnectedRailway Network2019-20 to 2022-23")

fig_expansion = go.Figure(data=[go.Table(
    
    columnwidth = [700,600,600,600,600,600],
    header=dict(values=list(df_expansion.columns),
                fill_color='darkturquoise',
                # fill_color='#b9e2ff',
                line_color='darkslategray',
                font = dict(family="Arial", size=10, color="black"),
                align='left'),
    cells=dict(values=df_expansion.transpose().values.tolist(),
               fill_color='lightgray',
                font = dict(family="Arial", size=10, color="black"),
               align='left'))
])
# Add fig_subure title
fig_expansion.update_layout(
    title_text="Expansion of Indian Railways"
)

st.plotly_chart(fig_expansion)

#####################################################################################################
st.subheader("Zonal Railway-wise Jan Ahaar Outlets",divider="gray")
st.write('''Government has provided facilities like Jan ahar for passengers.
''')

df_food=pd.read_csv(f'datasets/RAIL/Zonal Railway-wise Jan Ahaar Outlets are Run by Indian Railway Catering and Tourism Corporation through Private Contractors-done.csv')


fig_food = go.Figure(data=[go.Table(
    
    columnwidth = [700,600,600,600,600,600],
    header=dict(values=list(df_food.columns),
                fill_color='darkturquoise',
                # fill_color='#b9e2ff',
                line_color='darkslategray',
                font = dict(family="Arial", size=10, color="black"),
                align='left'),
    cells=dict(values=df_food.transpose().values.tolist(),
               fill_color='lightgray',
                font = dict(family="Arial", size=10, color="black"),
               align='left'))
])
# Add fig_subure title
fig_food.update_layout(
    title_text="Zonal Railway-wise Jan Ahaar Outlets"
)

st.plotly_chart(fig_food)


#####################################################################################################
st.subheader("Biotoilets",divider="gray")
st.image(f"writeup/biotoilets.jpg")
st.write('''Bio-toilets in Indian Railways.
''')

st.write("""To eliminate the previously open discharge toilet system, zero discharge Bio-toilet system with ventilation has been adopted for coaches of Indian Railways.

This was conceptualized during the year 2006. Further, the design has been evolved alongwith DRDE (Defence Research Development Establishment) after adequate trials and the same has been proliferated in coaches with minor modifications as per requirement

Initially complaints regarding choking of bio toilets in coaches were investigated and it was found that it was largely due to passengers throwing non Bio-degradable items like plastic bottles, huggies, tea cups, papers / polythene bags, napkin etc. in the toilet pans because of their unawareness about the provision of Bio-toilets in respective coaches which were resulting in choking and foul smell.

Accordingly, various steps were taken by Railway over the period of time for improvement. Some are enumerated as below:

\n👉Display of instructions in coaches to spread awareness among passengers.
\n👉Stickers/stainless steel plates were pasted/fitted on lavatory doors and inside coach lavatory 
to inform the passenger about installation of Bio-toilet and about its proper use and not to throw any waste material like bottles etc in lavatory pans.
\n👉The original design of Bio toilets of coach were fitted with P-trap. Subsequently the design was changed to S trap.
\n👉Regular announcement over PA system on stations are also being done.
\n👉To eliminate foul smell, Venturi type toilet ventilation systems are being provided in coach toilets.
To further address the issue of the foul smell in coach toilets and remove waste from toilet pan to Bio-tank, Bio-Vacuum toilet systems have been developed and are being fitted/retrofitted in coaches.
\n👉On Board Housekeeping Staff (OBHS) have been sensitized to make the toilet clean and to remove chocking enroute.
\n👉Rail Madad, a sole Indian Railway portal is working for passenger grievance redressal. The complaints received through this portal related to Bio Toilet are being timely resolved.
 

88 Numbers of Railway Stations have been provided with Bio-Toilets on Indian Railways.""")



st.subheader("Reference",divider="gray")
st.write("""https://cag.gov.in/webroot/uploads/download_audit_report/2017/Report_No.36_of_2017_-_Performance_Audit_on_Induction_of_bio-toilets_in_passenger_coaches_in_Indian_Railways_Union_Government.pdf""")