import streamlit as st 
import database.connection
import mysql.connector
from mysql.connector import errorcode

st.header(f'Listagem de usuários')

query = f'''
  SELECT * FROM v_usuario
'''

df = database.connection.run_query(query, True)

st.dataframe(df, use_container_width=True)
