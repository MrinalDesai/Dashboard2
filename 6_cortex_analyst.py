from typing import Any, Dict, List, Optional

import pandas as pd
import requests
import snowflake.connector
import streamlit as st

st.set_page_config(page_title="'Analyst'",
                   page_icon="🕵🏻",layout="wide"
                   )
st.header(':blue[CORTEX ANALYST]', divider="gray")
st.subheader('Ask Your questions related to daily route and find your answers')
st.subheader('The data will be parked in tables in Snowflake')
st.write("""This is a synthetic data created to demonstrate how Transport authorities can use AI to keep track of 
route data. It includes times series data for revenue, COGS,and forecasted revenue for each day the year of 2023 and 2024 for each route and regions.

\nThis data model is designed to help you analyze daily revenue and expenses. 
You can explore revenue and cost trends over time, compare performance across different routes and regions, 
and evaluate the accuracy of forecasted revenue. You can ask questions like 'What was the total revenue for a 
specific route last quarter?' or 'How does the profit margin vary across different regions?' 

\nThis semantic data model is designed to analyze daily revenue data, sliced by route and region, along with cost of 
goods sold and forecasted revenue. You can use it to explore revenue trends, compare actual vs forecasted revenue, 
and calculate profit and absolute error. You can ask questions about specific routes, regions, or dates, and get 
insights into daily, weekly, monthly, or yearly performance.

""")



st.write(":blue[SAMPLE QUESTIONS:]")
st.write(":red[1.What was the total revenue for each route in the last quarter of 2023?]")
st.write(":green[2.How does the profit margin vary across different regions over the entire available time period?]")
st.write(":orange[3.For each month, what was the lowest daily revenue and on what date did that lowest revenue occur?]")
st.write(":rainbow[4.Please create a bar graph for the total profit of each month for the year 2024.]")
st.write(":rainbow[4.What is the percentage change of revenue between 2024 and 2023?.]")
st.write("SAMPLE DATA")

df_main= pd.read_csv("cortex ai files/daily_revenue_combined.csv")
df_main=df_main.head(5)
st.write(df_main)


df_main_reg= pd.read_csv("cortex ai files/daily_revenue_by_region_combined.csv")
df_main_reg=df_main_reg.head(5)
st.write(df_main_reg)

df_main_route= pd.read_csv("cortex ai files/daily_revenue_by_route_combined.csv")
df_main_route=df_main_route.head(5)
st.write(df_main_route)

#HOST = "izoakvy-jbb52986.snowflakecomputing.com"
#HOST = "kakvlqh-cmb74873.snowflakecomputing.com"
HOST = "kjssull-lvb47542.snowflakecomputing.com"


DATABASE = "CORTEX_ANALYST_DEMO"
SCHEMA = "REVENUE_TIMESERIES"
STAGE = "RAW_DATA"
FILE = "revenue_timeseries.yaml"

PASSWORD = st.secrets["SPASSWORD"]
USER2 = st.secrets['SUSER'] 
ACCOUNT2 = st.secrets['SACCOUNT'] 

if 'CONN' not in st.session_state or st.session_state.CONN is None:
    st.session_state.CONN = snowflake.connector.connect(
        #user="MRINALSNOW02",
        #user="mrinalsnowtrial",
        password=PASSWORD,
        #account="izoakvy-jbb52986",
        #account="kakvlqh-cmb74873",
        user=USER2,
        account=ACCOUNT2,
        
        host=HOST,
        port=443,
        warehouse="CORTEX_ANALYST_WH",
        role="ACCOUNTADMIN",
    )


def send_message(prompt: str) -> Dict[str, Any]:
    """Calls the REST API and returns the response."""
    request_body = {
        "messages": [{"role": "user", "content": [{"type": "text", "text": prompt}]}],
        "semantic_model_file": f"@{DATABASE}.{SCHEMA}.{STAGE}/{FILE}",
    }
    resp = requests.post(
        url=f"https://{HOST}/api/v2/cortex/analyst/message",
        json=request_body,
        headers={
            "Authorization": f'Snowflake Token="{st.session_state.CONN.rest.token}"',
            "Content-Type": "application/json",
        },
    )
    request_id = resp.headers.get("X-Snowflake-Request-Id")
    if resp.status_code < 400:
        return {**resp.json(), "request_id": request_id}  # type: ignore[arg-type]
    else:
        raise Exception(
            f"Failed request (id: {request_id}) with status {resp.status_code}: {resp.text}"
        )


def process_message(prompt: str) -> None:
    """Processes a message and adds the response to the chat."""
    st.session_state.messages.append(
        {"role": "user", "content": [{"type": "text", "text": prompt}]}
    )
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Generating response..."):
            response = send_message(prompt=prompt)
            request_id = response["request_id"]
            content = response["message"]["content"]
            display_content(content=content, request_id=request_id)  # type: ignore[arg-type]
    st.session_state.messages.append(
        {"role": "assistant", "content": content, "request_id": request_id}
    )


def display_content(
    content: List[Dict[str, str]],
    request_id: Optional[str] = None,
    message_index: Optional[int] = None,
) -> None:
    """Displays a content item for a message."""
    message_index = message_index or len(st.session_state.messages)
    if request_id:
        with st.expander("Request ID", expanded=False):
            st.markdown(request_id)
    for item in content:
        if item["type"] == "text":
            st.markdown(item["text"])
        elif item["type"] == "suggestions":
            with st.expander("Suggestions", expanded=True):
                for suggestion_index, suggestion in enumerate(item["suggestions"]):
                    if st.button(suggestion, key=f"{message_index}_{suggestion_index}"):
                        st.session_state.active_suggestion = suggestion
        elif item["type"] == "sql":
            with st.expander("SQL Query", expanded=False):
                st.code(item["statement"], language="sql")
            with st.expander("Results", expanded=True):
                with st.spinner("Running SQL..."):
                    df = pd.read_sql(item["statement"], st.session_state.CONN)
                    if len(df.index) > 1:
                        data_tab, line_tab, bar_tab = st.tabs(
                            ["Data", "Line Chart", "Bar Chart"]
                        )
                        data_tab.dataframe(df)
                        if len(df.columns) > 1:
                            df = df.set_index(df.columns[0])
                        with line_tab:
                            st.line_chart(df)
                        with bar_tab:
                            st.bar_chart(df)
                    else:
                        st.dataframe(df)


#st.title("Cortex Analyst")
st.markdown(f"Semantic Model: `{FILE}`")

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.suggestions = []
    st.session_state.active_suggestion = None

for message_index, message in enumerate(st.session_state.messages):
    with st.chat_message(message["role"]):
        display_content(
            content=message["content"],
            request_id=message.get("request_id"),
            message_index=message_index,
        )

if user_input := st.chat_input("What is your question?"):
    process_message(prompt=user_input)

if st.session_state.active_suggestion:
    process_message(prompt=st.session_state.active_suggestion)
    st.session_state.active_suggestion = None






########################################################################################################################
#https://quickstarts.snowflake.com/guide/getting_started_with_cortex_analyst/index.html#0
# USE ROLE sysadmin;

# /*--
# • database, schema, warehouse and stage creation
# --*/

# -- create demo database
# CREATE OR REPLACE DATABASE cortex_analyst_demo;

# -- create schema
# CREATE OR REPLACE SCHEMA revenue_timeseries;

# USE ROLE accountadmin;

# -- create warehouse
# CREATE OR REPLACE WAREHOUSE cortex_analyst_wh
#     WAREHOUSE_SIZE = 'large'
#     WAREHOUSE_TYPE = 'standard'
#     AUTO_SUSPEND = 60
#     AUTO_RESUME = TRUE
#     INITIALLY_SUSPENDED = TRUE
# COMMENT = 'warehouse for cortex analyst demo';


# USE WAREHOUSE cortex_analyst_wh;

# CREATE STAGE raw_data DIRECTORY = (ENABLE = TRUE);




# /*--
# • table creation
# --*/
# CREATE OR REPLACE TABLE CORTEX_ANALYST_DEMO.REVENUE_TIMESERIES.DAILY_REVENUE (
# 	DATE DATE,
# 	REVENUE FLOAT,
# 	COGS FLOAT,
# 	FORECASTED_REVENUE FLOAT
# );

# CREATE OR REPLACE TABLE CORTEX_ANALYST_DEMO.REVENUE_TIMESERIES.DAILY_REVENUE_BY_ROUTE (
# 	DATE DATE,
# 	ROUTE VARCHAR(16777216),
# 	REVENUE FLOAT,
# 	COGS FLOAT,
# 	FORECASTED_REVENUE FLOAT
# );

# CREATE OR REPLACE TABLE CORTEX_ANALYST_DEMO.REVENUE_TIMESERIES.DAILY_REVENUE_BY_REGION (
# 	DATE DATE,
# 	REGION VARCHAR(16777216),
# 	REVENUE FLOAT,
# 	COGS FLOAT,
# 	FORECASTED_REVENUE FLOAT
# );





# COPY INTO CORTEX_ANALYST_DEMO.REVENUE_TIMESERIES.DAILY_REVENUE
# FROM @raw_data
# FILES = ('daily_revenue_combined.csv')
# FILE_FORMAT = (
#     TYPE=CSV,
#     SKIP_HEADER=1,
#     FIELD_DELIMITER=',',
#     TRIM_SPACE=FALSE,
#     FIELD_OPTIONALLY_ENCLOSED_BY=NONE,
#     REPLACE_INVALID_CHARACTERS=TRUE,
#     DATE_FORMAT=AUTO,
#     TIME_FORMAT=AUTO,
#     TIMESTAMP_FORMAT=AUTO
#     EMPTY_FIELD_AS_NULL = FALSE
#     error_on_column_count_mismatch=false
# )

# ON_ERROR=CONTINUE
# FORCE = TRUE ;




# COPY INTO CORTEX_ANALYST_DEMO.REVENUE_TIMESERIES.DAILY_REVENUE_BY_ROUTE
# FROM @raw_data
# FILES = ('daily_revenue_by_route_combined.csv')
# FILE_FORMAT = (
#     TYPE=CSV,
#     SKIP_HEADER=1,
#     FIELD_DELIMITER=',',
#     TRIM_SPACE=FALSE,
#     FIELD_OPTIONALLY_ENCLOSED_BY=NONE,
#     REPLACE_INVALID_CHARACTERS=TRUE,
#     DATE_FORMAT=AUTO,
#     TIME_FORMAT=AUTO,
#     TIMESTAMP_FORMAT=AUTO
#     EMPTY_FIELD_AS_NULL = FALSE
#     error_on_column_count_mismatch=false
# )

# ON_ERROR=CONTINUE
# FORCE = TRUE ;





# COPY INTO CORTEX_ANALYST_DEMO.REVENUE_TIMESERIES.DAILY_REVENUE_BY_REGION
# FROM @raw_data
# FILES = ('daily_revenue_by_region_combined.csv')
# FILE_FORMAT = (
#     TYPE=CSV,
#     SKIP_HEADER=1,
#     FIELD_DELIMITER=',',
#     TRIM_SPACE=FALSE,
#     FIELD_OPTIONALLY_ENCLOSED_BY=NONE,
#     REPLACE_INVALID_CHARACTERS=TRUE,
#     DATE_FORMAT=AUTO,
#     TIME_FORMAT=AUTO,
#     TIMESTAMP_FORMAT=AUTO
#     EMPTY_FIELD_AS_NULL = FALSE
#     error_on_column_count_mismatch=false
# )

# ON_ERROR=CONTINUE
# FORCE = TRUE ;