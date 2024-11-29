import streamlit as st 
import database.connection

query = f'''
  SELECT * FROM v_bookmarks_usuario WHERE user_id = {st.session_state.usuario['id']}
'''
df = database.connection.run_query(query, True)

st.header('Remover bookmark')
bookmark_selecionado = st.selectbox(
    "Selecione o bookmark que deseja remover",
    options=df.itertuples(index=False),
    format_func=lambda u: u.nome_escola
)
if st.button('Remover'):
    if bookmark_selecionado:
        delete_query = f'DELETE FROM bookmark WHERE id = {bookmark_selecionado.id} AND user_id = {st.session_state.usuario['id']}'
        try:
            database.connection.run_query(delete_query, False)
            st.success('Bookmark removido com sucesso!')
            st.rerun()
        except Exception as e:
            st.error(f'Erro ao remover o bookmark: {e}')

st.divider()
st.text('Seus bookmarks')

query = f'''
  SELECT * FROM v_bookmarks_usuario WHERE user_id = {st.session_state.usuario['id']} ORDER BY id DESC
'''

df = database.connection.run_query(query, True)

if df.size > 0:
  st.dataframe(df, use_container_width=True)