import streamlit as st

st.set_page_config(
    page_title='Antonio Moura',
    layout='centered'
)

st.markdown("<h1 style='text-align: center; color: darkviolet;'>Antonio Moura</h1>", unsafe_allow_html=True)

c1 = st.container(height=600, border=False)

st.markdown("<h2 style='text-align: center; color: darkviolet;'>Areas de Experiência</h2", unsafe_allow_html=True)

c2 = st.container(height=80, border=False)

col21, col22 = st.columns(2)

col21.markdown("<h3 style='text-align: center; color: violet;'>Habilidades</h3", unsafe_allow_html=True)
col22.markdown("<h3 style='text-align: center; color: violet;'>Ferramentas</h3", unsafe_allow_html=True)

c421 = col21.container(height=380, border=True)
c422 = col22.container(height=380, border=True)

c421.markdown('\nProgramação, R\n\n---\nModelagem de Dados\n\n---\nAprendizagem de Maquina\n\n---\nVisualização de Dados\n\n---\nAplicações\n\n')
c422.markdown('\nPython, R\n\n---\nPandas, Numpy\n\n---\nScykit, Statsmodels, Regressão(ridge, Lasso)\n\n---\nMatplotlib, Seaborn\n\n---\nStreamlit\n\n')

c3 = st.container(height=300, border=False)

st.markdown("<h2 style='text-align: center; color: darkviolet;'>Projetos</h2'", unsafe_allow_html=True)

col31, col32, col33 = st.columns(3)

project_container_height = 200

c531, c532, c533 = col31.container(height=project_container_height), col32.container(height=project_container_height), col33.container(height=project_container_height)

c531.markdown("<h5 style='text-align: center; color: violet;'>projeto 1</h5>", unsafe_allow_html=True)
c532.markdown("<h5 style='text-align: center; color: violet;'>projeto 2</h5>", unsafe_allow_html=True)
c533.markdown("<h5 style='text-align: center; color: violet;'>projeto 3</h5>", unsafe_allow_html=True)

c531.markdown("texto referente ao projeto 1, com resultados obtidos etc etc")
c532.markdown("texto referente ao projeto 2, com muitos ganhos utilizando habilidades descritas")
c533.markdown("texto referente ao projeto 3, foi adiquirido experiencias resultantes")

col31.link_button('Projeto 1', 'url', use_container_width=True)
col32.link_button('Projeto 2', 'url', use_container_width=True)
col33.link_button('Projeto 3', 'url', use_container_width=True)

c4 = st.container(height=500, border=False)

c5 = st.container(height=500, width=600, border=False)

c5.markdown('# :rainbow[O futuro é orientado por dados. E começa hoje!]')

c5.markdown('[Linkedin](https://www.linkedin.com/in/antoniomourajr/)')
c5.markdown('[Kaggle](https://www.kaggle.com/antoniojunior1998)')
c5.markdown('[GitHub](https://github.com/0ace-jk)')

