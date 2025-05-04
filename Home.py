import streamlit as st
import pandas as pd

st.set_page_config(layout = 'wide')
col1, col2 = st.columns(2)


with col1:
    st.image('images/photo.jpg')

with col2:
    st.title('Portfolio')
    content1 = """Hola, mi nombre es José Andrés. Este es mi portfolio en el cual les presentaré todos mis proyectos, avances y proyectos e ideas de proyectos que están por venir
    VAYANSE TODOS A LA MRD"""
    st.info(content1)


st.text('Aquí estan los datos para que me contactes.')

col3, empty_col,col4 = st.columns([1.5,0.5,1.5]) # SI QUEREMOS UNA SEPARACION ENTRE COLUMNAS: PONER UN COLUMNA EXTRA Y UN RATIO
df = pd.read_csv('data.csv', sep=';') #NO OLVIDAR LA SEPARACIÓN

with col3:
    for index, row in df[:10].iterrows(): #INDEX (USADO PARA VER QUE FILA ES PAR, ETC) ROW(NOS DA LOS DATOS DE LA FILA)
        st.header(row['title']) #EL ITERROWS SE USA CUANDO QUIERES RECORRER FILA POR FILA
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f'[Sourcer]({row["url"]})') #NO DEJAR ESPACIO ENTRE EL ] Y EL (

with col4:
    for index, row in df[10:].iterrows(): #DE LA DECIMA FILA HASTA MÁS
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f'[Sourcer]({row["url"]})')




