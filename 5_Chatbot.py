import os
# Import the necessary module
from dotenv import load_dotenv
import os
load_dotenv()

from snowflake.connector.errors import DatabaseError, ProgrammingError
#from streamlit_pdf_viewer import pdf_viewer
from snowflake import connector
from snowflake.snowpark import Session
from snowflake.cortex import Summarize, Complete, ExtractAnswer, Sentiment, Translate
import streamlit as st


############################################################

# Import the necessary module
# from dotenv import load_dotenv
# import os
# load_dotenv()
# PASSWORD = os.getenv('PASSWORD')
# USER2 = os.getenv('USER2')
# ACCOUNT2 = os.getenv('ACCOUNT2')

PASSWORD = "passSNOW@1234"

USER2 = "MRINALSNOW02"
# "mrinalsnowtrial" "izoakvy-jbb52986" 
#USER2 = "MRINALSNOW02"
ACCOUNT2 = "kakvlqh-cmb74873" 
#ACCOUNT2 ="kakvlqh-cmb74873",

############################################################

st.set_page_config(page_title="Simplifying Traffic rules",
                   page_icon="🧠",
                   )

# Load environment variables from .env
# load_dotenv()



connection_params = {
    "account": ACCOUNT2,
    "user": USER2,
    "password": PASSWORD,
    "database":"CC_QUICKSTART_CORTEX_DOCS",
    "schema": "DATA"
    # "role":"ACCOUNTADMIN"
}

##############################################

import snowflake.connector
import pandas as pd
try:
    con = snowflake.connector.connect(
        user=USER2,       # <-------- Bad user
        password=PASSWORD,   # <-------- Bad pass
        account=ACCOUNT2 , # <-------- This is correct
        database="CC_QUICKSTART_CORTEX_DOCS",
        schema= "DATA"
    )
except DatabaseError as db_ex:
    if db_ex.errno == 250001:
        st.write(f"Invalid username/password, please re-enter username and password...")
        # code for user to re-enter username & pass
    else:
        raise
except Exception as ex:
    # Log this
    st.write(f"Some error you don't know how to handle {ex}")
    raise
else:
    try:
        session = Session.builder.configs(connection_params).create()
        ctx = snowflake.connector.connect(
        user=USER2,
        password=PASSWORD,
        account=ACCOUNT2
        
        )
        
        ctx.cursor().execute('USE CC_QUICKSTART_CORTEX_DOCS.DATA')
        # cur = ctx.cursor().execute(query)


    except ProgrammingError as pr_ex:
        if pr_ex.errno == 1003:
            st.write(f"Programming error: {pr_ex}")
        elif pr_ex.errno == 90105:
            st.write('Connection Error')
            st.write(f"Programming error: {pr_ex}")
        elif pr_ex.errno == 2043:
            st.write('Connection Error')
            st.write(f"Programming error: {pr_ex}")
            
        else:
            raise
    finally:

##############################################


            # Create a Snowflake session
            session = Session.builder.configs(connection_params).create()


            import pandas as pd

            pd.set_option("max_colwidth",None)
            num_chunks = 3 # Num-chunks provided as context. Play with this to check how it affects your accuracy

            def create_prompt (myquestion, rag):

                if rag == 1:    

                    cmd = """
                    with results as
                    (SELECT RELATIVE_PATH,
                    VECTOR_COSINE_SIMILARITY(docs_chunks_table.chunk_vec,
                                SNOWFLAKE.CORTEX.EMBED_TEXT_768('e5-base-v2', ?)) as similarity,
                    chunk
                    from docs_chunks_table
                    order by similarity desc
                    limit ?)
                    select chunk, relative_path from results 
                    """
                
                    df_context = session.sql(cmd, params=[myquestion, num_chunks]).to_pandas()      
                    
                    context_lenght = len(df_context) -1

                    prompt_context = ""
                    for i in range (0, context_lenght):
                        prompt_context += df_context._get_value(i, 'CHUNK')

                    prompt_context = prompt_context.replace("'", "")
                    relative_path =  df_context._get_value(0,'RELATIVE_PATH')
                
                    prompt = f"""
                    'You are an expert assistance extracting information from context provided. 
                    Answer the question based on the context. Be concise and do not hallucinate. 
                    If you don´t have the information just say so.
                    Context: {prompt_context}
                    Question:  
                    {myquestion} 
                    Answer: '
                    """
                    cmd2 = f"select GET_PRESIGNED_URL(@docs, '{relative_path}', 360) as URL_LINK from directory(@docs)"
                    df_url_link = session.sql(cmd2).to_pandas()
                    url_link = df_url_link._get_value(0,'URL_LINK')

                else:
                    prompt = f"""
                    'Question:  
                    {myquestion} 
                    Answer: '
                    """
                    url_link = "None"
                    relative_path = "None"
                    
                return prompt, url_link, relative_path

            def complete(myquestion, model_name, rag = 1):

                prompt, url_link, relative_path =create_prompt (myquestion, rag)
                cmd = f"""
                        select SNOWFLAKE.CORTEX.COMPLETE(?,?) as response
                    """
                
                df_response = session.sql(cmd, params=[model_name, prompt]).collect()
                return df_response, url_link, relative_path

            def display_response (question, model, rag=0):
                response, url_link, relative_path = complete(question, model, rag)
                res_text = response[0].RESPONSE
                st.markdown(res_text)
                if rag == 1:
                    display_url = f"Link to [{relative_path}]({url_link}) that may be useful"
                    st.markdown(display_url)

            #Main code

            st.title("Simplifying Traffic Regulations using :red[Cortex]🤖 🧠:")
            st.subheader("#️⃣Lets use AI to find out relevant sections and understand Legal Jargon behind traffic rules")
            st.write("How can users use this App to better understand trffi rules and regulations")
            st.write("""Below 📃Report is used to provide Context""")
            with st.expander("THE MOTOR VEHICLES ACT, 1988"):
                st.image(f"cortex_document/motorvehicleact.jpg")
            with st.expander("The Motor Vehicles Driving Regulations 2017"):
                st.image(f"cortex_document/motordrivingregulation.jpg")
            # st.subheader("📄Report on UNIFIED DISTRICT INFORMATION SYSTEM FOR EDUCATION 2021-22📄:Wait till it loads")
            # with st.form("Input"):
            #         # queryText = st.text_area("SQL to execute:", height=3, max_chars=None)
            #         btnResult = st.form_submit_button('View Report')

            #         if btnResult:
            #             pdf_viewer("udise_21_22.pdf")
            st.write("https://indiankanoon.org/doc/96869172/")
            st.write("""You can ask questions and decide if you want to use Govt Report for context or allow the model to create their own response.""")

            st.subheader("🚩👣Steps to Use")
            st.write("""🚩Select your Model on the Left Pane.Check if you want to use the Document as Context""")
            st.subheader("Here are some sample Questions")
            st.write("❓Which section speaks about Cancellation of registration")
            st.write("❓What does section 52 say")
            st.write("❓As per THE-MOTOR-VEHICLES-DRIVING-REGULATIONS what is the definition of a road")
            st.write("📃This is the list of documents you already have")
            docs_available = session.sql("ls @docs").collect()
            list_docs = []
            for doc in docs_available:
                list_docs.append(doc["name"])
            st.dataframe(list_docs)

            #Here you can choose what LLM to use. Please note that they will have different cost & performance
            model = st.sidebar.selectbox('Select your model:',(
                                                'mixtral-8x7b',
                                                'snowflake-arctic',
                                                'mistral-large',
                                                'llama3-8b',
                                                'llama3-70b',
                                                'reka-flash',
                                                'mistral-7b',
                                                'llama2-70b-chat',
                                                'gemma-7b'))
            st.subheader("✏️Type your question here✏️")
            question = st.text_input("What does the document say", placeholder="As per THE-MOTOR-VEHICLES-DRIVING-REGULATIONS what is the definition of a road", label_visibility="collapsed")

            rag = st.sidebar.checkbox('🚩Use the Report as context?')

            print (rag)

            if rag:
                use_rag = 1
            else:
                use_rag = 0

            if question:
                display_response (question, model, use_rag)


#https://quickstarts.snowflake.com/guide/asking_questions_to_your_own_documents_with_snowflake_cortex/index.html#3

# CREATE DATABASE CC_QUICKSTART_CORTEX_DOCS;
# CREATE SCHEMA DATA;

# USE CC_QUICKSTART_CORTEX_DOCS.DATA;

# CREATE OR REPLACE WAREHOUSE XS_WH WAREHOUSE_SIZE = XSMALL;
# USE WAREHOUSE XS_WH;



# ##################################


# create or replace function pdf_text_chunker(file_url string)
# returns table (chunk varchar)
# language python
# runtime_version = '3.9'
# handler = 'pdf_text_chunker'
# packages = ('snowflake-snowpark-python','PyPDF2', 'langchain')
# as
# $$
# from snowflake.snowpark.types import StringType, StructField, StructType
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from snowflake.snowpark.files import SnowflakeFile
# import PyPDF2, io
# import logging
# import pandas as pd

# class pdf_text_chunker:

#     def read_pdf(self, file_url: str) -> str:
    
#         logger = logging.getLogger("udf_logger")
#         logger.info(f"Opening file {file_url}")
    
#         with SnowflakeFile.open(file_url, 'rb') as f:
#             buffer = io.BytesIO(f.readall())
            
#         reader = PyPDF2.PdfReader(buffer)   
#         text = ""
#         for page in reader.pages:
#             try:
#                 text += page.extract_text().replace('\n', ' ').replace('\0', ' ')
#             except:
#                 text = "Unable to Extract"
#                 logger.warn(f"Unable to extract from file {file_url}, page {page}")
        
#         return text

#     def process(self,file_url: str):

#         text = self.read_pdf(file_url)
        
#         text_splitter = RecursiveCharacterTextSplitter(
#             chunk_size = 4000, #Adjust this as you see fit
#             chunk_overlap  = 400, #This let's text have some form of overlap. Useful for keeping chunks contextual
#             length_function = len
#         )
    
#         chunks = text_splitter.split_text(text)
#         df = pd.DataFrame(chunks, columns=['chunks'])
        
#         yield from df.itertuples(index=False, name=None)
# $$;


# #######################################################################################################
# create or replace stage docs ENCRYPTION = (TYPE = 'SNOWFLAKE_SSE') DIRECTORY = ( ENABLE = true );


# ls @docs;


# ##############################################

# create or replace TABLE DOCS_CHUNKS_TABLE ( 
#     RELATIVE_PATH VARCHAR(16777216), -- Relative path to the PDF file
#     SIZE NUMBER(38,0), -- Size of the PDF
#     FILE_URL VARCHAR(16777216), -- URL for the PDF
#     SCOPED_FILE_URL VARCHAR(16777216), -- Scoped url (you can choose which one to keep depending on your use case)
#     CHUNK VARCHAR(16777216), -- Piece of text
#     CHUNK_VEC VECTOR(FLOAT, 768) );  -- Embedding using the VECTOR data type


# ##############################################


# insert into docs_chunks_table (relative_path, size, file_url,
#                             scoped_file_url, chunk, chunk_vec)
#     select relative_path, 
#             size,
#             file_url, 
#             build_scoped_file_url(@docs, relative_path) as scoped_file_url,
#             func.chunk as chunk,
#             SNOWFLAKE.CORTEX.EMBED_TEXT_768('e5-base-v2',chunk) as chunk_vec
#     from 
#         directory(@docs),
#         TABLE(pdf_text_chunker(build_scoped_file_url(@docs, relative_path))) as func;

# ##############################################

# select relative_path, size, chunk, chunk_vec from docs_chunks_table limit 5;


# select relative_path, count(*) as num_chunks 
#     from docs_chunks_table
#     group by relative_path;