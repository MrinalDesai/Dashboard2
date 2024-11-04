import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#st.title('Motorised vehicle developments')
st.header('Vehicle demographics and Growth', divider="gray")
st.subheader("#️⃣Registered and Commercial Vehicles and Licences in cities📌 ", divider="gray")

st.write("""
This section shows the Data.gov information regarding various Vehicles and Licences Demographisc and the Growth in Automobile Sector. It end with 
         propotionate growth in Population and Roads and Vehicle data""")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("#️⃣Total Registered Motor Vehicles-Million Plus Cities📌 ")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
df_reg_veh=pd.read_csv(f'datasets/transport/Cities-wise total Registered Motor Vehicles In Million Plus Cities of India from 2010 to 2020 (as on 31st March)-done.csv')
cities_list=list(df_reg_veh['Million Plus Cities'].unique())
city_op=st.selectbox("Select a City",cities_list,placeholder="Select a City",index=cities_list.index("Total "))
city_datareg_veh=df_reg_veh[df_reg_veh['Million Plus Cities']==city_op].reset_index().T.rename_axis('Year').reset_index().iloc[1:].rename({0: 'No'}, axis=1)
fig_no=px.bar(city_datareg_veh,x="Year",y="No",height=400,width=500, text_auto='.2s',title='Total Registered Motor Vehicles-Million Plus Cities')

st.plotly_chart(fig_no)

###################################################################################################################

st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("#️⃣Total Registered Transport Vehicles-Million+ Cities📌 ")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
df_reg_veh_type=pd.read_csv(f'datasets/transport/Cities-wise total Registered Motor Vehicles (Transport) in Million Plus Cities of India as on 31st March, 2020-done.csv')
cities_list_type=list(df_reg_veh_type['Million Plus Cities'].unique())
city_op_type=st.selectbox("Cities",cities_list_type,placeholder="Select a City",index=cities_list.index("Total "))
city_datareg_veh_type=df_reg_veh_type[df_reg_veh_type['Million Plus Cities']==city_op_type].reset_index().T.rename_axis('Type').reset_index().iloc[1:].rename({0: 'No'}, axis=1)
st.write("Total")
st.write(str(city_datareg_veh_type[city_datareg_veh_type['Type']=='Transport - Total Transport']['No'].iloc[0]))
city_datareg_veh_type=city_datareg_veh_type[city_datareg_veh_type['Type']!='Transport - Total Transport']
st.plotly_chart(px.bar(city_datareg_veh_type,x="Type",y="No",height=1000,width=500, text_auto='.2s',title="Total Registered Transport Vehicles-Million+ Cities"))




###################################################################################################################
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("#️⃣StatesUTs-wise Number of Commercial Vehicles in Use 📌 ")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
df_reg_veh_inuse=pd.read_csv(f'datasets/transport/StatesUTs-wise Number of Commercial Vehicles in Use (As per Primary Permit Valid As on 31.3.2020)-done.csv')


fig_veh_inuse=px.bar(df_reg_veh_inuse[df_reg_veh_inuse["States/UTs"]!='Total'],x="States/UTs",y="2019-20",height=800,width=1000, text_auto='.2s',title="StatesUTs-wise Number of Commercial Vehicles")


st.plotly_chart(fig_veh_inuse)


###################################################################################################################
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("#️⃣StatesUTs-wise and category-wise number of Commercial Vehicles in Use 📌 ")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
df_com_veh_inuse=pd.read_csv(f'datasets/transport/StatesUTs-wise and category-wise number of Commercial Vehicles in Use as per Primary Permit Valid as on 31.3.2020-done.csv')


com_veh_inuse_list=list(df_com_veh_inuse['States/Union Territories'].unique())

com_veh_inuse_sel=st.selectbox("Cities",com_veh_inuse_list,placeholder="Select a City",index=com_veh_inuse_list.index("Total"))


df_com_veh_inusesel=df_com_veh_inuse[df_com_veh_inuse['States/Union Territories']==com_veh_inuse_sel].reset_index()


df_com_veh_inusesel=df_com_veh_inusesel.T.rename_axis('Category').reset_index().iloc[1:].rename({0: 'No'}, axis=1).reset_index()

st.write(df_com_veh_inusesel.iloc[-1][1])
st.write(str(df_com_veh_inusesel.iloc[-1][2]))

fig_veh_inusesel=px.bar(df_com_veh_inusesel.iloc[:-1],x="Category",y="No",height=800,width=1000, text_auto='.2s')
# st.write(df_com_veh_inusesel.iloc[-1][0])
# st.write(str(df_com_veh_inusesel.iloc[-1][1]))
st.plotly_chart(fig_veh_inusesel)


###################################################################################################################
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("#️⃣StatesUTs-wise total registered vehicles and their Percentage Share 📌 ")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
df_com_reg_veh_share=pd.read_csv(f'datasets/transport/StatesUTs-wise total registered vehicles and their Percentage Share during 2018-19 and 2019-20-done.csv')
st.write(df_com_reg_veh_share.iloc[-1][0])
st.write("Total registered motor vehicles (As on 31.03.2019)")
st.write(str(df_com_reg_veh_share.iloc[-1][1]))
st.write("Total registered motor vehicles (As on 31.03.2020)")
st.write(str(df_com_reg_veh_share.iloc[-1][3]))
# st.write(df_com_reg_veh_share.iloc[-1])
df_com_reg_veh_share=df_com_reg_veh_share.iloc[:-1]
import plotly.graph_objects as go
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("#️⃣StatesUTs-wise total registered vehicles  📌 ")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
fig_registered_vehicles = go.Figure()
fig_registered_vehicles.add_trace(go.Bar(
    x=list(df_com_reg_veh_share['Total registered motor vehicles (As on 31.03.2019)']),
    y=list(df_com_reg_veh_share['States/UTs']),
    name='2019',
    orientation='h',
    marker=dict(
        color='rgba(246, 78, 139, 0.6)',
        line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
    )
))
fig_registered_vehicles.add_trace(go.Bar(
    x=list(df_com_reg_veh_share['Total registered motor vehicles (As on 31.03.2020)']),
    y=list(df_com_reg_veh_share['States/UTs']),
    name='2020',
    orientation='h',
    marker=dict(
        color='rgba(58, 71, 80, 0.6)',
        line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
    )
))

fig_registered_vehicles.update_layout(barmode='stack',autosize=False,width=800,
    height=1000)
st.plotly_chart(fig_registered_vehicles)

st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("#️⃣StatesUTs-wise registered vehicles Percentage Share 📌 ")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
fig_registered_vehicles_PER = go.Figure()
fig_registered_vehicles_PER.add_trace(go.Bar(
    x=list(df_com_reg_veh_share['%age share (2018-19)']),
    y=list(df_com_reg_veh_share['States/UTs']),
    name='2019',
    orientation='h',
    marker=dict(
        color='rgba( 78,246, 139, 0.6)',
        line=dict(color='rgba( 78,246, 139, 1.0)', width=3)
    )
))
fig_registered_vehicles_PER.add_trace(go.Bar(
    x=list(df_com_reg_veh_share['%age share (2019-20)']),
    y=list(df_com_reg_veh_share['States/UTs']),
    name='2020',
    orientation='h',
    marker=dict(
        color='rgba(71,58,  80, 0.6)',
        line=dict(color='rgba(71,58,  80, 1.0)', width=3)
    )
))

fig_registered_vehicles_PER.update_layout(barmode='stack',autosize=False,width=800,
    height=1000)
st.plotly_chart(fig_registered_vehicles_PER)


#########################################################################
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("#️⃣Category-wise Number of Newly Registered and Total Registered Motor Vehicles (Category-wise) 📌 ")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("Within 25 million incraese total vehicles crossed 325 million in 2020.")

df_cate_var=pd.read_csv(f'datasets/transport/Category-wise Number of Newly Registered and Total Registered Motor Vehicles (Category-wise) in all StatesUTs during 2019-20 and as on 31st March 2020-done.csv')


fig_Fines_display = go.Figure(data=[go.Table(
    
    columnwidth = [700,600,600,600,600,600],
    header=dict(values=list(df_cate_var.columns),
                fill_color='darkturquoise',
                # fill_color='#b9e2ff',
                line_color='darkslategray',
                font = dict(family="Arial", size=10, color="black"),
                align='left'),
    cells=dict(values=df_cate_var.transpose().values.tolist(),
               fill_color='lightgray',
                font = dict(family="Arial", size=10, color="black"),
               align='left'))
])
# Add fig_subure title
fig_Fines_display.update_layout(
    title_text="Category-wise Newly Registered and Total Registered Motor Vehicles"
)
st.plotly_chart(fig_Fines_display)



#################################################################################################################
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("#️⃣Category-wise Number of Commercial Vehicles in 2018-20 📌 ")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("Within a span of three years commercial vehicles have surged from 12 to 14 million.")

df_cate_trans=pd.read_csv(f'datasets/transport/Category-wise Number of Commercial Vehicles in 2018-20-done.csv')


fig_Fines_display = go.Figure(data=[go.Table(
    
    columnwidth = [700,600,600,600,600,600],
    header=dict(values=list(df_cate_trans.columns),
                fill_color='darkturquoise',
                # fill_color='#b9e2ff',
                line_color='darkslategray',
                font = dict(family="Arial", size=10, color="black"),
                align='left'),
    cells=dict(values=df_cate_trans.transpose().values.tolist(),
               fill_color='lightgray',
                font = dict(family="Arial", size=10, color="black"),
               align='left'))
])
# Add fig_subure title
fig_Fines_display.update_layout(
    title_text="Category-wise Number of Commercial Vehicles in 2018-20"
)
st.plotly_chart(fig_Fines_display)

#################################################################################################################
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("#️⃣StatesUTs-wise and category wise number of Newly Registered Transport Motor Vehicles during 2019-20 📌 ")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("Indias has more than 325 million vehicles as of 2020 which has grown from 25 million from 2019.")


df_st_cate_trans=pd.read_csv(f'datasets/transport/StatesUTs-wise and category wise number of Newly Registered Transport Motor Vehicles during 2019-20 and till 31.3.3.2020-done.csv')

st_cate_trans_state=list(df_st_cate_trans['States/Union Territories'].unique())

st_cate_trans_se=st.selectbox("States/Union Territories",st_cate_trans_state,st_cate_trans_state.index('Total'))

df_st_cate_trans_sel=df_st_cate_trans[df_st_cate_trans['States/Union Territories']==st_cate_trans_se].reset_index(drop=True)




fig_cate_trans_se = go.Figure(data=[go.Table(
    
    columnwidth = [700,600,600,600,600,600],
    header=dict(values=list(df_st_cate_trans_sel.columns),
                fill_color='darkturquoise',
                # fill_color='#b9e2ff',
                line_color='darkslategray',
                font = dict(family="Arial", size=10, color="black"),
                align='left'),
    cells=dict(values=df_st_cate_trans_sel.transpose().values.tolist(),
               fill_color='lightgray',
                font = dict(family="Arial", size=10, color="black"),
               align='left'))
])
# Add fig_subure title
fig_cate_trans_se.update_layout(
    title_text="Newly Registered Transport Motor Vehicles"
)
st.plotly_chart(fig_cate_trans_se)


#################################################################################################################
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("#️⃣StatesUTs-wise Total Registered Motor Vehicles in India from 2010 to 2020 📌 ")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("Indias motor vehicles have been steadily growing.")



df_reg_10=pd.read_csv(f'datasets/transport/StatesUTs-wise Total Registered Motor Vehicles in India from 2010 to 2020 (Figures as on as on 31st March of respective years)-done.csv')
st_reg_10_state=list(df_reg_10['STATES / UTs'].unique())

st_reg_10_se=st.selectbox("STATES / UTs",st_reg_10_state,st_reg_10_state.index('GRAND TOTAL '))

df_reg_10_sel=df_reg_10[df_reg_10['STATES / UTs']==st_reg_10_se].reset_index(drop=True)

df_reg_10_sel_fig=df_reg_10_sel.T.rename_axis('Category').reset_index().iloc[1:].rename({0: 'GRAND TOTAL','Category':'Year'}, axis=1)
st.plotly_chart(px.bar(df_reg_10_sel_fig,x="Year",y="GRAND TOTAL",height=500,width=500, text_auto='.2s',color="GRAND TOTAL"))



#################################################################################################################
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("#️⃣StatesUTs-wise Gender-Wise Number of Drivers Licences Issued 2020 (Cummulative) 📌 ")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("Indias Professional/Non-Professional Gnederwise data of licencies can be seen below.")

df_licen=pd.read_excel(f'datasets/transport/StatesUTs-wise Number of Valid Drivers Licences Issued as on 31.3.2020 (Cummulative)-done.xlsx',sheet_name='StatesUTs-wise Number of Valid ')


df_licen_grp=pd.read_excel(f'datasets/transport/StatesUTs-wise Number of Valid Drivers Licences Issued as on 31.3.2020 (Cummulative)-done.xlsx',sheet_name='Group')

licen_grp=df_licen_grp.groupby('Group')['States/UTs'].apply(list).reset_index(name='Items')
licen_grp.set_index('Group', inplace=True)
dctlicen = licen_grp.T.to_dict()

licen_grp_list=list(df_licen_grp['Group'].unique())

licen_grp_list_sel=st.selectbox("Licence",licen_grp_list,licen_grp_list.index("Total"))

lstlicen=dctlicen[licen_grp_list_sel]['Items']
lstlicen.insert(0,'States/UTs')

li_list=list(df_licen['States/UTs'].unique())

lic_state=st.selectbox("States/UTs",list(df_licen['States/UTs'].unique()),li_list.index("Total"))

df_licen_ind=df_licen[lstlicen]
df_licen_ind_single=df_licen_ind[df_licen_ind['States/UTs']==lic_state].reset_index(drop=True)
#st.write(df_licen_ind[df_licen_ind['States/UTs']==lic_state].drop('States/UTs', axis=1).reset_index(drop=True))

df_lc_final=df_licen_ind[df_licen_ind['States/UTs']==lic_state].drop('States/UTs', axis=1).reset_index(drop=True)
figlc_final = go.Figure(data=[go.Table(
    
    columnwidth = [700,600,600,600,600,600],
    header=dict(values=list(df_lc_final.columns),
                fill_color='darkturquoise',
                # fill_color='#b9e2ff',
                line_color='darkslategray',
                font = dict(family="Arial", size=10, color="black"),
                align='left'),
    cells=dict(values=df_lc_final.transpose().values.tolist(),
               fill_color='lightgray',
                font = dict(family="Arial", size=10, color="black"),
               align='left'))
])
# Add fig_subure title
figlc_final.update_layout(
    title_text="Newly Registered Transport Motor Vehicles"
)
st.plotly_chart(figlc_final)


#################################################################################################################
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("#️⃣StatesUTs-wise Number of Drivers Licences Issued 2019-20 (Incremental) 📌 ")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("Indias has more 16 million Drivers Licences Issued as of 2020.")

df_licenInc=pd.read_excel(f'datasets/transport/StatesUTs-wise Number of Drivers Licences Issued during 2019-20 (Incremental)-done.xlsx',sheet_name='StatesUTs-wise Number of Driver')


df_licen_grpInc=pd.read_excel(f'datasets/transport/StatesUTs-wise Number of Drivers Licences Issued during 2019-20 (Incremental)-done.xlsx',sheet_name='Group')

licen_grpInc=df_licen_grpInc.groupby('Group')['States/UTs'].apply(list).reset_index(name='Items')
licen_grpInc.set_index('Group', inplace=True)
dctlicenInc = licen_grpInc.T.to_dict()

licen_grp_listInc=list(df_licen_grpInc['Group'].unique())

licen_grp_list_selInc=st.selectbox("Licence",licen_grp_listInc,key='Inc',index=licen_grp_listInc.index("Total"))

lstlicenInc=dctlicenInc[licen_grp_list_selInc]['Items']
lstlicenInc.insert(0,'States/UTs')

li_listInc=list(df_licenInc['States/UTs'].unique())

lic_stateInc=st.selectbox("States/UTs",list(df_licenInc['States/UTs'].unique()),li_listInc.index("Total"))

df_licen_indInc=df_licenInc[lstlicenInc]
df_licen_ind_singleInc=df_licen_indInc[df_licen_indInc['States/UTs']==lic_stateInc].reset_index(drop=True)
#st.write(df_licen_ind[df_licen_ind['States/UTs']==lic_state].drop('States/UTs', axis=1).reset_index(drop=True))

df_lc_finalInc=df_licen_indInc[df_licen_indInc['States/UTs']==lic_stateInc].drop('States/UTs', axis=1).reset_index(drop=True)
figlc_finalInc = go.Figure(data=[go.Table(
    
    columnwidth = [700,600,600,600,600,600],
    header=dict(values=list(df_lc_finalInc.columns),
                fill_color='darkturquoise',
                # fill_color='#b9e2ff',
                line_color='darkslategray',
                font = dict(family="Arial", size=10, color="black"),
                align='left'),
    cells=dict(values=df_lc_finalInc.transpose().values.tolist(),
               fill_color='lightgray',
                font = dict(family="Arial", size=10, color="black"),
               align='left'))
])
# Add fig_subure title
figlc_finalInc.update_layout(
    title_text="(Incremental)StatesUTs-wise Number of Drivers Licences Issued during 2019-20 "
)
st.plotly_chart(figlc_finalInc)


##################################################################################################################
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("#️⃣StatesUTs-wise/Category wise Newly Registered Transport Motor Vehicles 2019-20 📌 ")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("Indias has over two million Motor Vehicles as of 2020.")

df_nw_rg_list=pd.read_csv(f"datasets/transport/StatesUTs-wise and category wise number of Newly Registered Transport Motor Vehicles during 2019-20-done.csv")
df_nw_rg_list_op=list(df_nw_rg_list['States/Union Territories'].unique())
df_nw_rg_list_sel=st.selectbox("States/Union Territories",df_nw_rg_list_op,df_nw_rg_list_op.index('Total'),key="df_nw_rg")
df_nw_rg_final=df_nw_rg_list[df_nw_rg_list["States/Union Territories"]==df_nw_rg_list_sel].reset_index(drop=True)

df_nw_rg_final=df_nw_rg_final.T.rename_axis('Year').reset_index().iloc[1:].rename({0: 'No'}, axis=1)

# st.write(df_nw_rg_final)
# fignw_rg=px.bar(df_com_veh_inusesel.iloc[:-1],x="Category",y="No",height=800,width=1000, text_auto='.2s')


fig_nw_rg_final = go.Figure(data=[go.Table(
    
    columnwidth = [700,600,600,600,600,600],
    header=dict(values=list(df_nw_rg_final.columns),
                fill_color='darkturquoise',
                # fill_color='#b9e2ff',
                line_color='darkslategray',
                font = dict(family="Arial", size=10, color="black"),
                align='left'),
    cells=dict(values=df_nw_rg_final.transpose().values.tolist(),
               fill_color='lightgray',
                font = dict(family="Arial", size=10, color="black"),
               align='left'))
])
# Add fig_subure title
fig_nw_rg_final.update_layout(
    title_text="StatesUTs-wise and category wise number of Newly Registered Transport Motor Vehicles"
)
st.plotly_chart(fig_nw_rg_final)


#################################################################################################################
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("#️⃣Year-wise Total Number of Registered Motor Vehicles in India from 1951 to 2020 📌 ")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("Indias has seen an exponencial growth in Registered Motor Vehicles.")


df5120=pd.read_csv(f"datasets/transport/Year-wise Total Number of Registered Motor Vehicles in India from 1951 to 2020-done.csv")

df5120_columns=list(df5120.columns)
df5120_columns.remove("Year (As on 31st March)")



sel_5120_=st.selectbox("Options",df5120_columns)
sel_5120_lst=[sel_5120_]
#df5120_bar=df5120[sel_5120_lst]
sel_5120_lst.insert(0,"Year (As on 31st March)")
#df5120[sel_5120_lst]

fig_veh_inusesel=px.bar(df5120[sel_5120_lst],x="Year (As on 31st March)",y=sel_5120_,height=800,width=1000, text_auto='.2s',title="Year-wise Total No Registered Motor Vehicles-1951 to 2020")
# st.write(df_com_veh_inusesel.iloc[-1][0])
# st.write(str(df_com_veh_inusesel.iloc[-1][1]))
st.plotly_chart(fig_veh_inusesel)


#################################################################################################################
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("#️⃣Year-wise Production of Motor Vehicles in India from 2010-11 to 2020-21 📌 ")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("Indias Automobile sector has been ramping up production to keep up with demand.However growth has stagnated in recent years.")
dfprod=pd.read_csv(f"datasets/transport/Year-wise Production of Motor Vehicles in India from 2010-11 to 2020-21-done.csv")
dfprod=dfprod.fillna(0)
prod_cat=list(dfprod['Category'].unique())

prod_cat_sel=st.selectbox("Category",prod_cat,prod_cat.index('Grand Total'))

dfprod_cat=dfprod[dfprod['Category']==prod_cat_sel].reset_index(drop=True)


dfprod_cat_sel=dfprod_cat.T.rename_axis('Category').reset_index().iloc[1:].rename({0: 'No','Category':"Year"}, axis=1)
#st.write(dfprod_cat_sel.reset_index(drop=True))
dfprod_cat_sel['Year']="Year "+dfprod_cat_sel['Year'].astype(str)
dfprod_cat_sel['No']=dfprod_cat_sel['No'].astype(int)
fig_prod=px.bar(dfprod_cat_sel.iloc[:-1],x='Year',y='No',color='Year')

st.plotly_chart(fig_prod)



#################################################################################################################
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("#️⃣Year-wise Sales of Motor Vehicles in India from 2007-08 to 2020-21 📌 ")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")

st.write("This shows that various categories of vehicles sales have been on rise")

dfsale0721=pd.read_csv(f"datasets/transport/Year-wise Sales of Motor Vehicles in India from 2007-08 to 2020-21-done.csv")
dfsale0721=dfsale0721.fillna(0)

sale0721_cat=list(dfsale0721['Category'].unique())

sale0721_cat_sel=st.selectbox("Category",sale0721_cat,sale0721_cat.index('Grand Total'),key="sale0721")


dfsale0721_cat=dfsale0721[dfsale0721['Category']==sale0721_cat_sel].reset_index(drop=True)

dfsale0721_cat_sel=dfsale0721_cat.T.rename_axis('Category').reset_index().iloc[1:].rename({0: 'No','Category':"Year"}, axis=1)

#st.write(dfsale0721_cat_sel.reset_index(drop=True))


dfsale0721_cat_sel['Year']="Year "+dfsale0721_cat_sel['Year'].astype(str)
dfsale0721_cat_sel['No']=dfsale0721_cat_sel['No'].astype(int)
fig_dfsale0721=px.bar(dfsale0721_cat_sel.iloc[:-1],x='Year',y='No',color='No')

st.plotly_chart(fig_dfsale0721)


#################################################################################################################
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
st.write("#️⃣Year-wise Vehicular Population per 1,000 Population and per 100 kms of National Highway and Road Length 📌 ")
st.write("#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣#️⃣")
df1000Pop=pd.read_csv(f"datasets/transport/Year-wise Vehicular Population per 1,000 Population and per 100 kms of National Highway and Road Length from 2001 to 2020-done.csv")
st.write("This show that with polpulation increasing propotionate increase in Length of Highways/Roads and Vehicles buses/cars has been observed")
df1000Pop=df1000Pop.fillna(0)

df1000Pop_cat=list(df1000Pop.columns)
df1000Pop_cat.remove("Year")
df1000Pop_cat_sel=[st.selectbox("Category",df1000Pop_cat,key="df1000Pop")]
df1000Pop_cat_sel.insert(0,"Year")
df1000Pop["Year"]="Year"+df1000Pop["Year"].astype('str')
# st.write(df1000Pop[df1000Pop_cat_sel])
# st.write(df1000Pop[df1000Pop_cat_sel])
fig_df1000Pop=px.bar(df1000Pop,x='Year',y=str(df1000Pop_cat_sel[1]),color='Year',labels=None)

st.plotly_chart(fig_df1000Pop)


# dfsale0721_cat=dfsale0721[dfsale0721['Category']==sale0721_cat_sel].reset_index(drop=True)