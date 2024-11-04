import plotly.express as px 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import streamlit as st

#st.title('Motorised vehicle developments')
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.header('BRIGHT DATASET', divider="gray")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.subheader('Myntra DATASET', divider="gray")
st.write(""" This section focuses revenue that can be generated from participating in the Ecommerce Revolution. e-commerce, 
         shipping costs typically amount to 10-15% of the total ordered value.
         If SRTU's participate in this a simple parcel would on an average charge around 100. These over a no of 
         days and location could be another way of boosting revenue of Public Transport.

""")


df = pd.read_csv(f'datasets/bright/PUBLIC.MYNTRA_PRODUCTS.csv')
# df['INITIAL_PRICE1'] = df['INITIAL_PRICE'].str.extract('([0-9][,.]*[0-9]*)')
# df['INITIAL_PRICE1'] = df['INITIAL_PRICE1'].replace(',','', regex=True)
# df['INITIAL_PRICE1'] = df['INITIAL_PRICE'].replace({'\$': '', ',': ''}, regex=True)
df=df.loc[:,['PRODUCT_DESCRIPTION','INITIAL_PRICE','TITLE','FINAL_PRICE','CURRENCY','DELIVERY_OPTIONS']]
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
average_price=df['FINAL_PRICE'].mean()
st.write('Average Price of products test] ordred online:')
st.write("RS: "+":blue["+str(average_price)+"]")



st.write(df.style.background_gradient(cmap="Blues"))
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.subheader('Google Play Store Dataset', divider="gray")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")

st.write("""Below is an example of App that gives users an Interactive way of finding routes accross a city. 
         Such Apps not only raise awareness among people""")
df_mytoursapp = pd.read_csv(f'datasets/bright/Google Play Store Dataset - Examples.csv')
st.write(df_mytoursapp.style.background_gradient(cmap="Blues"))
st.write('https://play.google.com/store/apps/details/Kootenay_Lake_Road_Trip?id=com.mytoursapp.android.app3722&hl=en_US')
st.image(f'datasets/bright/kootenay1.jpg')

st.write("""The Kootenay Lake Road Trip App is an immersive audio guided tour you can enjoy in your vehicle or on your bike.  
         It tells the story of this region from forests to First Nations, and attractions to amenities.
          If you are curious to learn about the region you are in the right place. 
         This collection of exciting sights and fun facts is sure to delight you as you discover what makes this place awesome.
         With over 180km of gorgeous highway driving, close to 100 sights, sounds and stories, and three different directional 
         routes, we have created an informative journey that fits with your travels. The tour can begin from anywhere around 
         Kootenay Lake and you can use the app for a guided tour.""")

