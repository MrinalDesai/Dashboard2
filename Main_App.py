import streamlit as st

##--- PAGE SETUP ---
Intro_pg = st.Page(
    "1_Intro.py",
    title="Introduction",
    
    default=True,
)

##--- PAGE SETUP ---
Intro_Infra = st.Page(
    "1_GInfra.py",
    title="Infra",
    
    
)



project_nw_page = st.Page(
    "2_NW2.py",
    title="Network Analysis of Transport",
    
)

project_lastmile_page = st.Page(
    "3_Last Mile.py",
    title="Request a New Stop",
    
)


project_feedback_page = st.Page(
    "4_Feedback.py",
    title="Feedback",
    
)


project_chatbot_page = st.Page(
    "5_Chatbot.py",
    title="Chatbot",
    
)

project_analyst =st.Page(
    "6_cortex_analyst.py",
    title="Analyst",
    
)

project_eco_mon = st.Page(
    "7_India_Economic_Monitor.py",
    title="7_India_Economic_Monitor",
    
)

project_soc_imp = st.Page(
    "8_INDIA_SOCIAL_IMPACT_DATA_SET.py",
    title="INDIA_SOCIAL_IMPACT_DATA_SET",
    
)

project_bright = st.Page(
    "9_Bright.py",
    title="Bright",
   
)

project_finance = st.Page(
    "10_Finance.py",
    title="Finance",
    
)

project_STRU = st.Page(
    "11_SRTU.py",
    title="SRTU",
    
)

project_transport = st.Page(
    "12_transport_stats.py",
    title="12_transport_stats",
   
)

project_rail = st.Page(
    "14_rail.py",
    title="14_rail",
    
)


project_road = st.Page(
    "15_road_surface_quality.py",
    title="15_road_surface_quality",
    
)

project_ML = st.Page(
    "16_ML.py",
    title="16_ML",
    
)


# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Introduction": [Intro_pg,Intro_Infra],
        "Apps": [project_nw_page,project_lastmile_page,project_feedback_page,project_chatbot_page,project_analyst],
        "Market": [project_eco_mon,project_soc_imp,project_bright],
        "Feedback": [project_finance,project_STRU,project_transport,project_rail],
        "AI_Apps_Feedback": [project_road,project_ML],
    }
)



# --- RUN NAVIGATION ---
pg.run()