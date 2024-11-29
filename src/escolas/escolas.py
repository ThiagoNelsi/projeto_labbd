import streamlit as st 
import database.connection
import folium
from folium.plugins import MarkerCluster

st.header("Escolas")

query = f"""
    SELECT * FROM v_escola
"""

turmas_df = database.connection.run_query(query, True)
# Subistituir municipio 3543907 por `Rio Claro`
turmas_df.loc[turmas_df['Municipio'] == 3543907, 'Municipio'] = 'Rio Claro'

st.dataframe(turmas_df, use_container_width=True)

st.divider()
st.header('Detalhar escola')

escola = st.selectbox('Selecione a escola', turmas_df['Nome_Escola'].unique())
escola_df = turmas_df[turmas_df['Nome_Escola'] == escola]

print(escola_df.keys())

st.text(f"{escola_df['Codigo_Escola'].values[0]} - {escola_df['Nome_Escola'].values[0]}")
st.text(f"Situação: {escola_df['Situacao'].values[0]}")
st.text(f"Municipio: {escola_df['Municipio'].values[0]}")
st.text(f'Dependencia: {escola_df["Dependencia"].values[0]}')

if escola_df['Etapas_Ensino'].values[0] is not None:
  etapas = escola_df['Etapas_Ensino'].values[0].split(',')

  st.text('Etapas de ensino:')
  for etapa in etapas:
      st.text(f" - {etapa}")

mapa = folium.Map(location=[-22.4134, -47.5696], zoom_start=10)
marker_cluster = MarkerCluster().add_to(mapa)

folium.Marker(
    location=[escola_df['Latitude'].values[0], escola_df['Longitude'].values[0]],
    popup=f'{escola_df["Nome_Escola"].values[0]}',
    icon=folium.Icon(color='blue', icon='chalkboard-user', prefix='fa')
).add_to(marker_cluster)

st.components.v1.html(mapa._repr_html_(), height=600)