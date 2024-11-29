import streamlit as st 
import database.connection
import folium
from folium import plugins
import geopandas as gpd
from folium.plugins import MarkerCluster
import matplotlib.pyplot as plt

# Título do app
st.subheader('Mapa de Geolocalização das escolas')

# Filtro por dependência administrativa
dependencia_dict = {
    0: 'Todas',
    1: 'Federal',
    2: 'Estadual',
    3: 'Municipal',
    4: 'Privada'
}

situacao_dict = {
    0: 'Todas',
    1: 'Em atividade',
    2: 'Paralisada',
    3: 'Extinta em Anos Anteriores',
    4: 'Extinta'
}


dependencia = st.selectbox('Selecione a dependência administrativa da escola', list(dependencia_dict.keys()), format_func=lambda x: dependencia_dict[x])
situacao = st.selectbox('Selecione a situação da escola', list(situacao_dict.keys()), format_func=lambda x: situacao_dict[x])

query_escolas = f'''
    SELECT e.CO_ENTIDADE, e.NO_ENTIDADE, e.TP_DEPENDENCIA, geo.LAT, geo.LON
    FROM escola e
    LEFT JOIN geolocalizacao geo ON e.CO_ENTIDADE = geo.ESCOLA_ID
    WHERE {f"e.TP_DEPENDENCIA = {dependencia}" if dependencia != 0 else "1=1"}
    AND {f"e.TP_SITUACAO_FUNCIONAMENTO = {situacao}" if situacao != 0 else "1=1"}
'''
escolas_df = database.connection.run_query(query_escolas, True)

escolas = [
    {
        'codigo': row['CO_ENTIDADE'], 
        'nome': row['NO_ENTIDADE'],
        'lat': row['LAT'],
        'lon': row['LON']
    }
    for _, row in escolas_df.iterrows()
]

mapa = folium.Map(location=[-22.4134, -47.5696], zoom_start=12)
marker_cluster = MarkerCluster().add_to(mapa)

for escola in escolas:
    folium.Marker(
        location=[escola['lat'], escola['lon']],
        popup=f'{escola['nome']}',
        icon=folium.Icon(color='blue', icon='chalkboard-user', prefix='fa')
    ).add_to(marker_cluster)

# Exibindo o mapa no Streamlit
st.components.v1.html(mapa._repr_html_(), height=600)