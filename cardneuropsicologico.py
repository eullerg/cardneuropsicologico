import streamlit as st
import random

st.set_page_config(page_title="Card Neuropsicologico", page_icon="🧠", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    .stApp {
        background-color: black !important;
    }
    .stButton>button {
        color: black !important;
        background-color: #50C878 !important;
        border: 2px solid #50C878 !important;
    }
    .stButton>button:hover {
        color: #50C878 !important;
        background-color: black !important;
    }
    .big-font {
        font-size: 20px !important;
        color: #A020F0 !important;
    }
    h1, h2, h3, p {
        color: white !important;
    }
    .stApp header {
        background-color: #1E1E1E !important;
    }
    .stApp header .st-emotion-cache-1avcm0n {
        background-color: #1E1E1E !important;
    }
    
    .stApp header .st-emotion-cache-1avcm0n svg path {
        fill: #50C878 !important;
    }
    .card {
        background-color: #1E1E1E;
        border-radius: 15px;
        border: 2px solid #50C878;
        padding: 30px;
        margin: 20px auto;
        max-width: 400px;
        box-shadow: 0 10px 20px rgba(80, 200, 120, 0.3);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(80, 200, 120, 0.4);
    }
    .card h2 {
        color: #50C878 !important;
        font-size: 28px;
        margin-bottom: 20px;
        text-align: center;
    }
    .card p {
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

def get_random_text():
    group_a = [
        "Sinto que minha mente nunca para, e isso me esgota.",
        "Preocupo-me com coisas que ainda nem aconteceram, e isso me paralisa.",
        "Tenho dificuldade em relaxar, mesmo em momentos tranquilos.",
        "A sensação de estar sempre em alerta é constante para mim.",
        "Às vezes, sinto um aperto no peito que não consigo explicar."
    ]
    
    group_b = [
        "Por mais que eu tente, não consigo encontrar motivação para as coisas que antes me faziam feliz.",
        "Sinto como se uma nuvem escura estivesse sempre presente, não importa o que eu faça.",
        "Tenho dificuldade em sair da cama, mesmo sabendo que tenho coisas a fazer.",
        "A sensação de vazio é tão grande que parece que nada pode preenchê-la.",
        "É difícil acreditar que as coisas vão melhorar, mesmo que todos digam que sim."
    ]
    
    group_c = [
        "Sinto-me constantemente sobrecarregado com as demandas do dia a dia.",
        "Tenho a impressão de que nunca há tempo suficiente para fazer tudo o que preciso.",
        "A pressão para ser perfeito em tudo está me deixando exausto.",
        "Sinto que estou sempre correndo contra o relógio, sem conseguir relaxar.",
        "Às vezes, parece que estou carregando o peso do mundo nos ombros."
    ]
    
    group_d = [
        "Tenho medo de não ser bom o suficiente em tudo o que faço.",
        "Comparo-me constantemente com os outros e sempre me sinto inferior.",
        "Evito situações novas porque temo fracassar.",
        "A opinião dos outros sobre mim pesa mais do que a minha própria opinião.",
        "Sinto que estou sempre em dúvida sobre as minhas decisões."
    ]
    
    group_e = [
        "Mesmo rodeado de pessoas, sinto-me sozinho e desconectado.",
        "É difícil encontrar alguém com quem eu realmente possa conversar.",
        "Sinto que ninguém entende o que estou passando.",
        "Às vezes, parece que o mundo está seguindo em frente, mas eu estou ficando para trás.",
        "A solidão me faz questionar se sou importante para alguém."
    ]
    
    groups = [
        (group_a, "Ansiedade"),
        (group_b, "Depressão"),
        (group_c, "Estresse"),
        (group_d, "Insegurança"),
        (group_e, "Solidão")
    ]
    
    selected_group, category = random.choice(groups)
    return random.choice(selected_group), category

st.title("Card Neuropsicologico")

if 'text' not in st.session_state:
    st.session_state.text = ""
    st.session_state.group = ""

if st.button("Gerar Card Neuropsicologico"):
    st.session_state.text, st.session_state.group = get_random_text()

if st.session_state.text:
    st.markdown("""
    <div class="card">
        <h2>Card Gerado:</h2>
        <p class="big-font">{}</p>
        <p>Categoria: <span style="color: #50C878;">{}</span></p>
    </div>
    """.format(st.session_state.text, st.session_state.group), unsafe_allow_html=True)

st.write("Click no botão acima para gerar um card!")