import streamlit as st 
import database.connection

st.header("Total de Alunos, Professores e Turmas por Escola")
query = f"""
  SELECT 
    e.Nome_Escola,
    ( 	
      SELECT COUNT(DISTINCT m.codigo) 
      FROM v_matricula m 
          WHERE m.codigo_escola = e.Codigo_Escola
    ) AS alunos,
    (
      SELECT COUNT(DISTINCT d.codigo) 
      FROM v_docente d 
      WHERE d.codigo_escola = e.Codigo_Escola
    ) AS professores,
    (
      SELECT COUNT(DISTINCT t.codigo) 
      FROM v_turma t 
      WHERE t.codigo_escola = e.Codigo_Escola
    ) AS turmas
  FROM v_escola e;
"""
df = database.connection.run_query(query, True)
st.dataframe(df, use_container_width=True)