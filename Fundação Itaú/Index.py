import streamlit as st
from streamlit_navigation_bar import st_navbar
st.set_page_config(
    page_title='Fundação Itaú',
    page_icon='.\\imagens\\Logo_Fundação.png',
    layout="wide",
    initial_sidebar_state='auto',
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


st.markdown("""
    <style>
        
""", unsafe_allow_html=True)


pages = {
    "Navegação": [
        st.Page("inicial.py", title="Página Inicial", icon=":material/home:"),
        st.Page("organizacoes.py", title="Organizações", icon=":material/corporate_fare:"),
        st.Page("perfis.py", title="Meus Perfis", icon=":material/sell:"),
        st.Page("usuarios.py", title="Usuários", icon=":material/group:")
    ]
}

pg = st.navigation(pages)
pg.run()

st.logo('.\\imagens\\Logo.png',size='medium',icon_image='.\\imagens\\Logo.png')
