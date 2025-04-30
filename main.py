import streamlit as st

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