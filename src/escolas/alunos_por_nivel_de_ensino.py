import streamlit as st 
import database.connection

st.header("Número de Alunos por Nível de Ensino")

query = f"""
  SELECT 
	  e.nome AS etapa_ensino,
    COUNT(DISTINCT m.codigo_aluno) AS total_alunos
  FROM v_matricula m
  JOIN etapas e ON m.etapa_de_ensino = e.id
  GROUP BY e.nome
  ORDER BY total_alunos DESC;
"""

turmas_df = database.connection.run_query(query, True)
st.dataframe(turmas_df, use_container_width=True)