import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="Transforming India’s Road Infrastructure",
                   page_icon="🚗",
                   )
st.title("""Transforming India’s Road Infrastructure
""")
st.header('Connecting India Like Never Before', divider="gray")
st.subheader("#️⃣Govt Initiative📌 ", divider="gray")

st.write("""India's road infrastructure has seen significant advancements over the past decade, driven by the Government’s 
         dedicated efforts and strategic initiatives. From enhancing national highways and promoting environmental 
         sustainability to improving rural connectivity and road safety, the government has implemented a multi-faceted 
         approach to develop a robust and efficient transportation network. This comprehensive overview highlights key 
         programs and investments that showcase the nation's commitment to building a safe, sustainable, 
         and interconnected road infrastructure for the future.""")


st.subheader("""Capital Expenditure Surge:""")
st.write("""\n:blue[The National Highways Authority of India (NHAI)] has significantly increased its capital expenditure over 
             the past five years, reflecting the government's commitment in enhancing the national highways network and infrastructure.]

Details of Capital Expenditure incurred by National Highways Authority of India (NHAI) in last five years is as under:
""")

st.image(f"datasets/infra/Infra_Expenditure.jpg")
st.image(f"datasets/infra/Roads_Constructed.jpg")

st.write("""This increase in expenditure coupled with timely maintenance, has significantly expanded the National Highways (NH) 
         network in the country, growing from about 91,287 km in March, 2014 to about 1,46,126 km, as on July 25, 2024. 
         This growth is driven by various government initiatives aimed at enhancing road connectivity across the country.""")

st.subheader("Road Network Expansion")

st.write("""A key component of this effort is the :blue[Bharatmala Pariyojana], under which projects are executed in categories such as 
         Economic Corridors Development, Inter-corridor and Feeder Routes Development, National Corridors Efficiency Improvement, 
         Border and International Connectivity Roads, Coastal and Port Connectivity Roads, and Expressways. 
         This flagship program has awarded 26,425 km and constructed 17,411 km of roads until March 2024, with an 
         expenditure of Rs. 4.59 lakh crore as of March 31, 2024.""")

##########################################################################################################################

df_bm=pd.read_csv(f"datasets/infra/StateUT-wise Details of Projects under Bharatmala Pariyojana as on 31-03-2024-done.csv")
df_bmex=pd.read_csv(f"datasets/infra/Year-wise Details of the Expenditure incurred for the Road Construction under the Bharatmala Pariyojana from 2019-20 to 2022-23-done.csv")

bm_list=list(df_bm['State/UT'].unique())
bm_list_sel=st.selectbox("Select State",bm_list,key="bm_list",index=bm_list.index('Grand Total'))
df_bm_sel=df_bm[df_bm['State/UT']==bm_list_sel]
fig_bm_list = go.Figure(data=[go.Table(
    columnwidth = [300,500,500,500],
    header=dict(values=list(df_bm_sel.columns),
                fill_color='darkturquoise',
                # fill_color='#b9e2ff',
                line_color='darkslategray',
                font = dict(family="Arial", size=14, color="black"),
                align='left'),
    cells=dict(values=df_bm_sel.transpose().values.tolist(),
               fill_color='lightgray',
                font = dict(family="Arial", size=14, color="black"),
               align='left'))
])
# Add fig_subure title
fig_bm_list.update_layout(
    title_text="Projects under Bharatmala Pariyojana"
)
st.plotly_chart(fig_bm_list)

st.write("Year-wise Details of the Expenditure incurred for the Road Construction under the Bharatmala Pariyojana from 2019-20 to 2022-23")
st.write(df_bmex)
##########################################################################################################################
st.write("""In last 5 years, NHAI has constructed 24,050 km of NHs with estimated 45 Crore man days of direct employment, 
         57 Crore man days of indirect employment and 532 Crore man days of induced employment. This substantial job 
         creation highlights the socio-economic benefits of infrastructure development. Furthermore, 5 Expressways and 
         22 Access Controlled Highways, having total length of 9,860 km with approved / estimated project cost of 
         Rs. 4,19,130 crore have been taken up by NHAI as greenfield corridors.

         \nThe Ministry is making all efforts to expedite the process of awarding new NH projects. 
         Regular meetings are held with all concerned at various levels for the availability of 
         necessary clearances/approvals and fulfilment of conditions precedent.""")


st.write("StateUT-wise Details of Expenditure Incurred by (NHAI) for (LA) and Related Activities for the Development of National Highways (NHs)")
df_nhai_ex=pd.read_csv(f"datasets/infra/StateUT-wise Details of Expenditure Incurred by (NHAI) for (LA) and Related Activities for the Development of National Highways (NHs)-done.csv")

st.write(df_nhai_ex)


##########################################################################################################################

df_yr_nh=pd.read_csv(f"datasets/infra/Year-wise National Highway (NHs) Constructed by National Highways Authority of India (NHAI) from 2014-15 to 2021-22-done.csv")


fig_yr_nh=px.bar(df_yr_nh,x="Financial Year",y="Length of NH Constructed (in km)",height=400,width=500, text_auto='.2s',title='National Highway Constructed (NHAI)')

st.plotly_chart(fig_yr_nh)


##########################################################################################################################

df_nh_bor=pd.read_csv(f"datasets/infra/Year-wise Detail of Borrowing of National Highways Authority of India (NHAI) from 2018-19 to 2022-23-done.csv")


fig_nh_bor=px.bar(df_nh_bor,x="Year",y="Amount (Principal)",height=400,width=500, text_auto='.2s',title='Borrowing of  (NHAI) ')

st.plotly_chart(fig_nh_bor)


##########################################################################################################################

st.subheader("Road Connectivity in North-East Region")

st.write("""Several road and transport infrastructure development projects have been taken up by the concerned Ministries and Departments 
of the Central Government in North Eastern Region (NER). The total length of National Highways (NHs) constructed in North Eastern Region 
(NER) during the last ten years is 9,984 km with an expenditure of Rs.1,07,504 crore while 265 NH projects are under implementation at 
a cost of Rs.1,18,894 crore with total length of 5,055 km. Ministry pays special attention to the development of NHs in the NER and 
10% of the total budget is earmarked for NER. Further, Government has taken the specific initiative for improvement of connectivity 
within the region through East-West Corridor program.


\nIn addition, the Ministry of DoNER under Prime Minister's Development Initiative for North East Region (PM-DevINE), North East Special
 Infrastructure Development Scheme (NESIDS) and North East Road Sector Development Scheme (NERSDS) has sanctioned 80 road projects 
 amounting to Rs 5894.44 crore during last five years.""")
###################################################################################################
st.write("State-wise Funds Disbursed under North Eastern Council (NEC) and North East Road Sector Development Scheme (NERSD) from 2019-20 to 2021-22")
df_ne_fun=pd.read_csv(f"datasets/infra/State-wise Funds Disbursed under North Eastern Council (NEC) and North East Road Sector Development Scheme (NERSD) from 2019-20 to 2021-22-done.csv")

st.write(df_ne_fun)

###################################################################################################
st.subheader("Rural Road Connectivity")

st.write(""":blue[The Pradhan Mantri Gram Sadak Yojana (PMGSY)] has significantly enhanced rural road connectivity. 
Under this scheme, 8,10,250 km of road length was sanctioned, out of which 7,65,601 km (94%) has been constructed. 
As of July 26, 2024, the total expenditure on this initiative stands at Rs. 3,24,186 crore.

\nFurther, the Union Budget 2024-25 announced the launch of Phase IV of PMGSY to provide all-weather connectivity to 
25,000 rural habitations, which have become eligible due to population increase. This next phase will continue the 
momentum of rural infrastructure development, ensuring that more remote areas gain vital road access, thereby 
fostering economic growth and improving the quality of life for rural populations.

""")

###################################################################################################
st.write(":blue[Pradhan Mantri Gram Sadak Yojana (PMGSY)]")

df_ne_fun=pd.read_csv(f"datasets/infra/StateUTs-wise Road Length Completed under Pradhan Mantri Gram Sadak Yojana (PMGSY) as on 28.07.2022-done.csv")


list_ne_fun=list(df_ne_fun['State/UT'].unique())


ne_fun_sel=st.selectbox("State/UT",list_ne_fun,key="ne_fun",index=list_ne_fun.index('Total'))


df_ne_fun_sel=df_ne_fun[df_ne_fun["State/UT"]==ne_fun_sel]

st.write(df_ne_fun_sel)
###################################################################################################

###################################################################################################
st.write("StateUT-wise and Year-wise Details of Road Length Constructed from 2018-19 to 2021-22-(PMGSY)")

df_high=pd.read_excel(f"datasets/infra/StateUT-wise National Highways Constructed Across the Country from 2014-15 to 2018-19 (From Ministry of Road Transport and Highways)-done.xlsx")


list_high_fun=list(df_high['State/UT'].unique())



high_sel=st.selectbox("State/UT",list_high_fun,key="high",index=list_high_fun.index('Total'))


df_high_sel=df_high[df_high["State/UT"]==high_sel].reset_index(drop="True")

st.write(df_high_sel)
###################################################################################################
st.subheader("Electric Charging Stations")

st.write("""Additionally, in a significant step towards supporting electric mobility, a total of 5,293 Electric Vehicle (EV) 
charging stations have been established along National Highways. This includes 4,729 stations set up by the Ministry of 
Petroleum and Natural Gas at an investment of Rs. 178 Crore. Additionally, the Ministry of Heavy Industries has targeted 
the establishment of 5,833 EV charging stations as part of a broader plan to deploy 7,432 stations. A capital subsidy 
of Rs. 800 Crore has been allocated to oil companies to achieve this goal, further advancing the infrastructure 
for electric vehicles.""")
st.write("CityHighway-wise Electric Vehicle (EV) Charging Stations")
df_elec_EV=pd.read_csv(f"datasets/infra/CityHighway-wise Electric Vehicle (EV) Charging Stations out of which 479 Charging Stations have been Installed as on 07-12-2022-done.csv")

st.write(df_elec_EV)
###################################################################################################

st.write("StateUt-wise Operational charging stations under FAME-II scheme")
df_elec_FAME=pd.read_csv(f"datasets/infra/StateUt-wise Operational charging stations under FAME-II scheme as on 15.07.2022-done.csv")
st.write(df_elec_FAME)