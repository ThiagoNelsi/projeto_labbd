import streamlit as st
import database.connection
import time
from datetime import date

def listar_usuarios():
  try:
    query = "SELECT * FROM v_usuario WHERE nome != 'root'"
    df = database.connection.run_query(query, return_df=True)
    return df
  except Exception as err:
    st.error(f"Erro na listagem de usuários: {err}")
    return None

def get_usuario(usuario_id):
  try:
    query = f"SELECT * FROM v_usuario WHERE id = {usuario_id}"
    df = database.connection.run_query(query, return_df=True)
    if not df.empty:
      return df.iloc[0]
    return None
  except Exception as err:
    st.error(f"Erro ao buscar dados do usuário: {err}")
    return None

def atualizar_usuario(usuario_id, nome, email, data_de_nascimento, administrador):
  try:
    admin_value = 1 if administrador else 0
    query = f"""
      UPDATE usuario 
      SET NOME = '{nome}', EMAIL = '{email}', DATA_DE_NASCIMENTO = '{data_de_nascimento}', ADMINISTRADOR = '{admin_value}'
      WHERE ID = {usuario_id}
    """
    database.connection.run_query(query)
    st.success("Usuário atualizado com sucesso!")
    time.sleep(.7)
    st.rerun()
  except Exception as err:
    st.error(f"Erro ao atualizar o usuário: {err}")

st.header("Alteração de Usuário")

usuarios_df = listar_usuarios()
if usuarios_df is not None and not usuarios_df.empty:
  usuario_selecionado = st.selectbox(
    "Selecione um usuário para alterar",
    options=usuarios_df.itertuples(index=False),
    format_func=lambda u: u.nome
  )

  if usuario_selecionado:
    usuario_id = usuario_selecionado.id
    dados_usuario = get_usuario(usuario_id)

    if dados_usuario is not None:
      with st.form("alterar_usuario"):
        nome = st.text_input("Nome", value=dados_usuario["nome"])
        email = st.text_input("Email", value=dados_usuario["email"])
        data_de_nascimento = st.date_input("Data de nascimento", value=dados_usuario["data_de_nascimento"], min_value=date(1900, 1, 1), max_value=date.today())
        administrador = st.checkbox("Administrador", value=bool(dados_usuario["administrador"] == 'Sim'))
        submit = st.form_submit_button("Salvar")

        if submit:
          if nome and email and data_de_nascimento:
            atualizar_usuario(usuario_id, nome, email, data_de_nascimento, administrador)
          else:
            st.warning("Todos os campos são obrigatórios!")
    else:
      st.warning("Dados do usuário não encontrados no banco de dados.")
else:
  st.warning("Nenhum usuário encontrado no banco de dados.")
