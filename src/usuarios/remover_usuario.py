import time
import streamlit as st 
import database.connection
import mysql.connector
from mysql.connector import errorcode

query = f'''
  SELECT * FROM v_usuario
'''

df = database.connection.run_query(query, True)

st.header('Remover usuário')
usuario_selecionado = st.selectbox(
  "Selecione o usuário que deseja remover",
  options=df.itertuples(index=False),
  format_func=lambda u: f'{u.nome} ({u.email}) {' - ADM' if u.administrador == 'Sim' else ''}',
)

if st.button('Remover usuário'):
  if usuario_selecionado:
    delete_query = f'DELETE FROM usuario WHERE id = {usuario_selecionado.id}'
    try:
      database.connection.run_query(delete_query, False)
      st.success('Usuário removido com sucesso!')
      time.sleep(.7)
      st.rerun()
    except mysql.connector.Error as err:
      st.error(f"Erro: {err}")