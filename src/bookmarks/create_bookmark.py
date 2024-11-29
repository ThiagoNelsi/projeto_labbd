import streamlit as st 
import database.connection
import mysql.connector
from mysql.connector import errorcode
import time

query_escolas = "SELECT * FROM v_escola"
escolas_df = database.connection.run_query(query_escolas, True)

def criar_bookmark(escola_selecionada):
  try:
    query = f'''
      INSERT INTO bookmark (user_id, escola_id)
      VALUES ({st.session_state.usuario['id']}, {escola_selecionada.Codigo_Escola});
    '''
    database.connection.run_query(query)
    st.success("Bookmark cadastrado com sucesso")
    time.sleep(1)
    st.rerun()
  except mysql.connector.Error as err:
    st.error(f"Erro: {err}")

with st.form("create_bookmark"):
  st.title("Criar um bookmark")
  escola_selecionada = st.selectbox(
    "Selecione a escola que deseja adicionar aos seus bookmarks",
    options=escolas_df.itertuples(index=False),
    format_func=lambda u: u.Nome_Escola
  )
  submit = st.form_submit_button("Criar")

  if submit and escola_selecionada:
    criar_bookmark(escola_selecionada)
  elif submit:
    st.warning("Dados inválidos!")

st.divider()
st.text('Seus bookmarks')

query = f'''
  SELECT * FROM v_bookmarks_usuario WHERE user_id = {st.session_state.usuario['id']} ORDER BY id DESC
'''

df = database.connection.run_query(query, True)

if df.size > 0:
  st.dataframe(df, use_container_width=True)