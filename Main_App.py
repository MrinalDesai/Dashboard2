import streamlit as st

##--- PAGE SETUP ---
Intro_pg = st.Page(
    "1_Intro.py",
    title="Introduction👋 | WELCOME",
    
    default=True,
)

##--- PAGE SETUP ---
Intro_Infra = st.Page(
    "1_GInfra.py",
    title="Road Infra🛣️",
    
    
)



project_nw_page = st.Page(
    "2_NW2.py",
    title="🚌Network Analysis ",
    
)

project_lastmile_page = st.Page(
    "3_Last Mile.py",
    title="🚏Request a New Stop",
    
)


project_feedback_page = st.Page(
    "4_Feedback.py",
    title="📝Feedback",
    
)


project_chatbot_page = st.Page(
    "5_Chatbot.py",
    title="💬AI Document Chatbot",
    
)

project_analyst =st.Page(
    "6_cortex_analyst.py",
    title="🕵🏻Analyst",
    
)

project_eco_mon = st.Page(
    "7_India_Economic_Monitor.py",
    title="💵India Economic Monitor",
    
)

project_soc_imp = st.Page(
    "8_INDIA_SOCIAL_IMPACT_DATA_SET.py",
    title="👨‍👨‍👦‍👦🇮🇳India Social Impact Dataset",
    
)

project_bright = st.Page(
    "9_Bright.py",
    title="🌐Bright Dataset",
   
)

project_finance = st.Page(
    "10_Finance.py",
    title="💰Finance",
    
)

project_STRU = st.Page(
    "11_SRTU.py",
    title="🚎SRTU",
    
)

project_transport = st.Page(
    "12_transport_stats.py",
    title="🚍Transport Stats",
   
)

project_rail = st.Page(
    "14_rail.py",
    title="🛤️Rail",
    
)


project_road = st.Page(
    "15_road_surface_quality.py",
    title="🛣️Road Surface Quality",
    
)

project_ML = st.Page(
    "16_ML.py",
    title="🤖🧠🇦🇮👾Machine Learning",
    
)


project_MM = st.Page(
    "17_Waterways.py",
    title="🛥️Waterways",
    
)

project_recommendation = st.Page(
    "18_Recommendation.py",
    title="💡Recommendation",
    
)


# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Introduction": [Intro_pg,Intro_Infra],
        
        
        "Feedback": [project_finance,project_STRU,project_transport,project_rail,project_MM ],
        "Marketplace Data": [project_eco_mon,project_soc_imp,project_bright],
        "Transport Management Apps": [project_nw_page,project_lastmile_page,project_feedback_page,project_chatbot_page,project_analyst],
        "AI Apps": [project_road,project_ML],

        "Recommendation": [project_recommendation],
    }
)



# --- RUN NAVIGATION ---
pg.run()