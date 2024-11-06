import folium
from folium.plugins import MousePosition
from snowflake.snowpark import Session
import streamlit as st
from streamlit_folium import folium_static
from streamlit_folium import st_folium
import streamlit_folium
from snowflake import connector
import snowflake.connector
import pandas as pd
import ast
import pickle
import streamlit as st
import pandas as pd

st.title('Introduction')
st.header('Last Mile Connectivity', divider="gray")
st.subheader("#️⃣Request a Stop on your nearest location📌 ", divider="gray")

# st.set_page_config(page_title="Last Mile Connectivity",
#                    page_icon="🚏",layout="wide"
#                    )

    #btnResult = st.form_submit_button('View All the Pothole Location')

PASSWORD = "passSNOW@1234"
# USER2 = "mrinalsnowtrial"
# ACCOUNT2 = "izoakvy-jbb52986" 
USER2 = "MRINALSNOW02"
ACCOUNT2 = "kakvlqh-cmb74873" 
connection_params = {
    "account": ACCOUNT2,
    "user": USER2,
    "password": PASSWORD
}

# Create a Snowflake session
snowflake_session = Session.builder.configs(connection_params).create()
global coordg
coordg=[]
#if btnResult:
        
# Create a Snowflake session
session = Session.builder.configs(connection_params).create()
ctx = snowflake.connector.connect(
user=USER2,
password=PASSWORD,
account=ACCOUNT2


)

ctx.cursor().execute('USE COORDINATES.PUBLIC')
cur = ctx.cursor().execute('SELECT * FROM LOCATION')
df = pd.DataFrame.from_records(iter(cur), columns=[x[0] for x in cur.description])
coord=df
df = df.drop(['ID', 'CREATED_AT'], axis=1)
st.write(df.style.background_gradient(cmap="Blues"))
coord_LIST=df['LATLONLIST'].tolist()
for i in coord_LIST:
    coordg.append(ast.literal_eval(i))

#################################################################################################
import pandas as pd
#coord=pd.read_csv('coordinate data (1).csv')

coord_clean=coord.drop(columns=['ID', 'LATLONLIST', 'CREATED_AT'])
coord_clean=coord_clean.sort_values(by=[ 'LATITUDE']).reset_index(drop=True)
coord_clean['LATITUDE_diff'] = abs(coord_clean['LATITUDE'].diff())
coord_clean['LATITUDE_diff'] = coord_clean['LATITUDE_diff'].fillna(0)
coord_clean['Group']=0
count=0
rw=len(coord_clean)
for x in range(rw):
    print(coord_clean.iloc[x]['LATITUDE_diff'])
    if coord_clean['LATITUDE_diff'][x]>0.1:
           count=count+1
           coord_clean['Group'][x]=count
    else:
           coord_clean['Group'][x]=count
coord_clean=coord_clean.groupby(['Group']).apply(lambda x: x.sort_values(["LONGITUDE"], ascending = True)).reset_index(drop=True)
coord_clean['LONGITUDE_diff'] = coord_clean.groupby(['Group'])['LONGITUDE'].diff().abs()
coord_clean['LONGITUDE_diff'] = coord_clean['LONGITUDE_diff'].fillna(0)
coord_clean['Group1']=0
count=0
rw=len(coord_clean)
for x in range(rw):
    print(coord_clean.iloc[x]['LONGITUDE_diff'])
    if coord_clean['LONGITUDE_diff'][x]>0.1:
           count=count+1
           coord_clean['Group1'][x]=count
    else:
           coord_clean['Group1'][x]=count
coord_clean['Group_F']=coord_clean['Group'].astype(str)+coord_clean['Group1'].astype(str)
coord_clean1 = coord_clean.groupby('Group_F') \
       .agg({'Group_F':'size', 'LATITUDE':'mean','LONGITUDE':'mean'}) \
       .rename(columns={'Group_F':'count'}) \
       .reset_index()

coord_clean2 = coord_clean.groupby('Group_F') \
       .agg({ 'LATITUDE':'max','LONGITUDE':'max'}) \
       .rename(columns={'LATITUDE':'LATITUDE_max','LONGITUDE':'LONGITUDE_max'}) \
       .reset_index()

coord_clean3 = coord_clean.groupby('Group_F') \
       .agg({ 'LATITUDE':'min','LONGITUDE':'min'}) \
       .rename(columns={'LATITUDE':'LATITUDE_min','LONGITUDE':'LONGITUDE_min'}) \
       .reset_index()

merged_Frame = pd.merge(coord_clean1,coord_clean2,  on = 'Group_F', how='inner')
merged_Frame = pd.merge(merged_Frame,coord_clean3,  on = 'Group_F', how='inner')

merged_Frame['Lat_diff']=merged_Frame['LATITUDE_max']-merged_Frame['LATITUDE_min']
merged_Frame['Lon_diff']=merged_Frame['LONGITUDE_max']-merged_Frame['LONGITUDE_min']
merged_Frame['Dist']=merged_Frame[['Lat_diff', 'Lon_diff']].max(axis=1)*100000
merged_Frame_Final=merged_Frame[merged_Frame['count']>3]


#################################################################################################     
st.subheader("See the requested Coordinates")
def get_pos(lat,lng):
    return lat,lng

formatter = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"
#m=folium.Map(location=[28.644800, 77.216721])
m=folium.Map(location=[18.5204, 73.8567])
MousePosition(
    position="topright",
    separator=" | ",
    empty_string="NaN",
    lng_first=True,
    num_digits=20,
    prefix="Coordinates:",
    lat_formatter=formatter,
    lng_formatter=formatter,
).add_to(m)
m.add_child(folium.LatLngPopup())

coord=[]

coord=[[18.5204, 73.8567],
[18.5, 73.9],
[18.4, 74.8],[18.42, 74.6]]


import pandas as pd
coord=pd.read_csv('coordinate data (1).csv')
coord_clean=coord.drop(columns=['ID', 'LATLONLIST', 'CREATED_AT'])

# folium.Circle(location=[18.492625, 73.851010], fill_color='#000', radius=23483.276958, weight=2, color="red").add_to(m)
# folium.Circle(location=[18.664363, 74.126798], fill_color='#000', radius=2883.9, weight=2, color="red").add_to(m)

rw=len(merged_Frame_Final)
for x in range(rw):
    print(merged_Frame_Final.iloc[x]['LATITUDE'])
    folium.Circle(location=[float(merged_Frame_Final.iloc[x]['LATITUDE']), float(merged_Frame_Final.iloc[x]['LONGITUDE'])], fill_color='#000', radius=float(merged_Frame_Final.iloc[x]['Dist']), weight=2, color="red").add_to(m)


# st.write(coordg)
# coord=coordg



for i in coordg:
   
   folium.Marker(i,
              icon=folium.Icon(color='blue',
                               prefix='fa',icon='111'),
                               ).add_to(m)
folium_static(m, width=900, height=950)
m.add_child(folium.ClickForMarker())

st.subheader("Request Coordinates")

st.write("1.Click on The Map")
st.write("2.Wait for Running Status of the App to Disappear.")
st.write("3.Once the Coordinates appear Click on :blue[Save Coordinates for New Stops]")
st.write("4.Once enough Coordinates appear The Map loaction will be encircled and Authorities will take a note of it")

global data_list
data_list=[]
map = st_folium(m, width=500, height=500)
data = None
if map.get("last_clicked"):
    data = get_pos(map["last_clicked"]["lat"], map["last_clicked"]["lng"])

    if data is not None:
        #st.write(data_list) # Writes to the app
        Lat=data[0]
        Lon=data[1]
        data_list.append([Lat,Lon])
if data is not None:
    #st.write(data_list) # Writes to the app
    Lat=data[0]
    Lon=data[1]
    #data_list.append([Lat,Lon])
    #st.write(data_list) # Writes to the app
    st.write("Latitude")
    st.write(Lat)
    st.write("Longitude")
    st.write(Lon)

with st.form("Input"):

    
    submit = st.form_submit_button('Save Coordinates for New Stops')


if submit:
    # Create a Snowflake session
    
    session = Session.builder.configs(connection_params).create()
    ctx = snowflake.connector.connect(
    user=USER2,
    password=PASSWORD,
    account=ACCOUNT2
    
    
    )

    #query_INS="INSERT INTO POLL (rating,review) VALUES ('"+rating+"','"+review+"');"
    if data is not None:
        for i in data_list:
            query_INS="INSERT INTO LOCATION (latitude,longitude,latlonlist) VALUES ("+str(i[0])+","+str(i[1])+",'"+str(i)+"');"
            st.write(query_INS)
            ctx.cursor().execute('USE COORDINATES.PUBLIC')
            ctx.cursor().execute(query_INS)
            snowflake_session.close()
    else:
        st.write("Please Click on MapLocation to Select Coordinates for PotHoles")























# Username: MRINALSNOW02
# Dedicated Login URL: https://kakvlqh-cmb74873.snowflakecomputing.com






# https://izoakvy-jbb52986.snowflakecomputing.com/console/login#/
# use coordinates.public
# CREATE OR REPLACE table poll (
#   id integer autoincrement, -- 
#   latitude NUMERIC(30,20),  -- variable string column
#   longitude NUMERIC(30,20), -- column used to store JSON type of data
#   latlonlist varchar (100),
#   created_at timestamp DEFAULT CURRENT_TIMESTAMP()
# );
# DESC TABLE poll;
# INSERT INTO POLL (latitude,longitude,latlonlist) VALUES (17.82450628753586,73.57543937414886,'[17.82450628753586,73.57543937414886]');
# SELECT * FROM poll





# CREATE OR REPLACE table location (
#   id integer autoincrement, -- 
#   latitude NUMERIC(30,20),  -- variable string column
#   longitude NUMERIC(30,20), -- column used to store JSON type of data
#   latlonlist varchar (100),
#   created_at timestamp DEFAULT CURRENT_TIMESTAMP()
# );




# DESC TABLE poll;
# ALTER TABLE  IF EXISTS  poll RENAME TO location;

# INSERT INTO location (latitude,longitude,latlonlist) VALUES (17.82450628753586,73.57543937414886,'[17.82450628753586,73.57543937414886]');

# SELECT * FROM location;