import streamlit as st 
import database.connection

st.header('Aqui estão seus bookmarks')

query = f'''
  SELECT * FROM v_bookmarks_usuario WHERE user_id = {st.session_state.usuario['id']}
'''

df = database.connection.run_query(query, True)

if df.size > 0:
  st.dataframe(df, use_container_width=True)
else:
  st.info('Você não possui nenhum bookmark adicionado')
