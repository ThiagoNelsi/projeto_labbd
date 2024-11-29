import streamlit as st
import database.connection
import mysql.connector
from mysql.connector import errorcode
import time
from datetime import date

with st.form("cadastro_usuario"):
  st.header("Cadastro de usuário")
  nome = st.text_input('Nome:')
  email = st.text_input('Email:')
  senha = st.text_input('Senha:', type='password')
  data_de_nascimento = st.date_input('Data de Nascimento:', min_value=date(1900, 1, 1), max_value=date.today())
  administrador = st.checkbox('Administrador')
  submit = st.form_submit_button("Enviar")

def validar(nome, email, senha, data_de_nascimento):
  if nome == '' or email == '' or senha == '' or not data_de_nascimento:
    return False
  return True

def cadastra_usuario(nome, email, senha, data_de_nascimento, administrador):
  try:
    admin_value = 1 if administrador else 0
    query = f"""
      INSERT INTO usuario (NOME, EMAIL, SENHA, DATA_DE_NASCIMENTO, ADMINISTRADOR) 
      VALUES ('{nome}', '{email}', sha('{senha}'), '{data_de_nascimento}', {admin_value})
    """
    database.connection.run_query(query)
    st.success("Cadastrado com sucesso")
    time.sleep(.7)
    st.rerun()
  except mysql.connector.Error as err:
    st.error(f"Erro: {err}")

if submit and validar(nome, email, senha, data_de_nascimento):
  cadastra_usuario(nome, email, senha, data_de_nascimento, administrador)
elif submit:
  st.warning("Dados inválidos!")