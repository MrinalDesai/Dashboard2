import os
# from dotenv import load_dotenv
import streamlit as st
from snowflake import connector
from snowflake.snowpark import Session
from snowflake.cortex import Summarize, Complete, ExtractAnswer, Sentiment, Translate
from snowflake import connector
from snowflake.snowpark import Session
import snowflake.connector
import pandas as pd
import string
import plotly.express as px

from dotenv import load_dotenv
import os
load_dotenv()
# PASSWORD = os.getenv('PASSWORD')
# USER2 = os.getenv('USER2')
# ACCOUNT2 = os.getenv('ACCOUNT2')

PASSWORD = "passSNOW@1234"
# USER2 = "mrinalsnowtrial"
# ACCOUNT2 = "izoakvy-jbb52986" 

USER2 = "MRINALSNOW02"
ACCOUNT2 = "kakvlqh-cmb74873" 

st.set_page_config(page_title="App Feedback",
                   page_icon="💬",
                   )
st.title("""Tell us how your Journey was and we will make sure your opinion counts """)
st.write("""We use your data to Do Some Sentiment Analysis 🗣 and Fetch Some Ratings⭐⭐⭐⭐ your Experience:""")

connection_params = {
    "account": ACCOUNT2,
    "user": USER2,
    "password": PASSWORD
}

# Create a Snowflake session
snowflake_session = Session.builder.configs(connection_params).create()


# Define the LLM functions
def summarize(user_text):
    summary = Summarize(text=user_text, session=snowflake_session)
    return summary


def complete(question):
    completion = Complete(
        model="snowflake-arctic",
        prompt=question,
        session=snowflake_session,
    )
    return completion


def extract_answer(user_text):
    answer = ExtractAnswer(
        from_text=user_text,
        question="How to deal with high traffic on a route",
        session=snowflake_session,
    )
    return answer


def sentiment(user_text):
    sentiment = Sentiment(text=user_text, session=snowflake_session)
    return sentiment


def translate(user_text):
    translation = Translate(
        text=user_text, from_language="en", to_language="de", session=snowflake_session
    )
    return translation




user_text1 = """
        Keep up the good Work. Loved the information
    """


        # summary_result = summarize(user_text)
        # print(
        #     f"Summarize() Snowflake Cortex LLM function result:\n{summary_result.strip()}\n"
        # )

        # completion_result = complete(user_text)
        # print(
        #     f"Complete() Snowflake Cortex LLM function result:\n{completion_result.strip()}\n"
        # )

        # answer_result = extract_answer(user_text)
        # print(
        #     f"ExtractAnswer() Snowflake Cortex LLM function result:\n{answer_result}\n"
        # )

# sentiment_result = sentiment(user_text1)
# print(
#     f"Sentiment() Snowflake Cortex LLM function result:\n{sentiment_result}\n"
# )

        # translation_result = translate(user_text)
        # print(
        #     f"Translate() Snowflake Cortex LLM function result:\n{translation_result.strip()}\n"
        # )
bus_no = st.text_input("Bus No", "111")
route_no = st.text_input("Route No", "111")

traffic_solution='''Dealing with high traffic routes can be challenging, but there are several strategies that can help manage the situation:

Implement traffic management measures: This can include measures such as traffic signal timing optimization, lane closures, and the addition of turn lanes or dedicated bus lanes.
Encourage alternative modes of transportation: Encouraging people to use alternative modes of transportation, such as biking, walking, or public transit, can help reduce the number of cars on the road.

Use technology to manage traffic: Intelligent transportation systems (ITS) can be used to monitor and manage traffic in real-time. This can include things like dynamic message signs, ramp meters, and traffic cameras.

Improve road infrastructure: Widening roads, adding lanes, and improving intersections can help alleviate congestion on high traffic routes.

Implement congestion pricing: Congestion pricing is a strategy that involves charging drivers a fee to use certain roads or enter certain areas during peak traffic times. This can help reduce the number of cars on the road and generate revenue that can be used to fund transportation improvements.

Encourage telecommuting and flexible work schedules: Allowing employees to work from home or have flexible work schedules can help reduce the number of cars on the road during peak traffic times.

Coordinate with neighboring jurisdictions: High traffic routes often cross municipal or county lines, so it is important to coordinate with neighboring jurisdictions to ensure that traffic management measures are consistent and effective.

Educate the public: Educating the public about traffic management measures, alternative modes of transportation, and the benefits of reducing traffic congestion can help encourage behavior change and increase support for transportation improvements.
It's important to note that there is no one-size-fits-all solution to managing high traffic routes, and that a combination of strategies is often necessary to effectively address the issue.'''

with st.form("Input"):
    review = st.text_area("Submit Review about your journey:", height=3, max_chars=100)
    
    
    submit = st.form_submit_button('Submit Review')
    btnResult = st.form_submit_button('View All the Reviews and Ratings')

if btnResult:
    # Create a Snowflake session
    session = Session.builder.configs(connection_params).create()
    ctx = snowflake.connector.connect(
    user=USER2,
    password=PASSWORD,
    account=ACCOUNT2
    
    
    )
    
    ctx.cursor().execute('USE SENTIMENT_DATA.PUBLIC')
    cur = ctx.cursor().execute('SELECT * FROM FEEDBACK')
    df = pd.DataFrame.from_records(iter(cur), columns=[x[0] for x in cur.description])
    df = df.drop(['ID', 'CREATED_AT'], axis=1)
    for index, row in df.iterrows():
            if (row['RATING']=='Highly Positive'):
                st.write("⭐⭐⭐⭐⭐⭐⭐⭐")
                st.write(row['REVIEW'])
            elif (row['RATING']=='Highly Negative'):
                st.write("⭐")
                st.write(row['REVIEW'])
            elif (row['RATING']=='Neutral'):
                st.write("⭐⭐")
                st.write(row['REVIEW'])
            elif (row['RATING']=='Negative'):
                st.write("⭐")
                st.write(row['REVIEW'])
            else:
                st.write("⭐⭐⭐⭐")
                st.write(row['REVIEW'])
            
    pie_data=df.groupby(['RATING']).size().reset_index(name='Count')
    st.subheader("The Final Report of Sentiment Analysis📋")
    fig = px.pie(pie_data, values='Count', names='RATING')
    st.plotly_chart(fig)
    st.write(df.style.background_gradient(cmap="Blues"))
    st.text('Fetched Results')
    snowflake_session.close()

    

if submit:
    # Create a Snowflake session
    
    session = Session.builder.configs(connection_params).create()
    ctx = snowflake.connector.connect(
    user=USER2,
    password=PASSWORD,
    account=ACCOUNT2
    
    
    )
    review=review.translate(str.maketrans('', '', string.punctuation))
    sentiment_result = sentiment(review)
    score=sentiment_result
    if (score>=0.6):
        rating='Highly Positive'
    elif (score <= -0.6):
        rating='Highly Negative'
    elif (score == 0):
        rating='Neutral'
    elif (-0.6 < score< 0):
        rating='Negative'
    else:
        rating='Positive'

    # st.write(extract_answer(traffic_solution))

    # st.write(complete("How to reduce high traffic congestion on roads?"))


    
    
    
    query_INS="INSERT INTO FEEDBACK (route,bus_no,rating,review) VALUES ('"+route_no+"','"+bus_no+"','"+rating+"','"+review+"');"
    ctx.cursor().execute('USE SENTIMENT_DATA.PUBLIC')
    ctx.cursor().execute(query_INS)
    snowflake_session.close()
    # run query
    # st.write(queryText)

# if snowflake_session:
#     # Close the Snowflake session
#     snowflake_session.close()







# ###################################################################################
# CREATE OR REPLACE table feedback (
#   id integer autoincrement,
#   route varchar (100),
#   bus_no varchar (100),
#   review varchar (100),  -- variable string column
#   rating varchar (100), -- column used to store JSON type of data
#   created_at timestamp DEFAULT CURRENT_TIMESTAMP()
# );


# SELECT * FROM feedback;
