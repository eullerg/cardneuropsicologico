import streamlit as st
import mysql.connector
from cardneuropsicologico import get_random_text
from config import markdown_config, db_config


st.set_page_config(page_title="Card Neuropsicológico", page_icon="🧠", initial_sidebar_state="collapsed")

st.markdown(markdown_config, unsafe_allow_html=True)

st.title("Card Neuropsicológico")

def get_categories():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT category FROM cards")
    categories = [row[0] for row in cursor.fetchall()]

    cursor.close()
    conn.close()

    print("Categories fetched from database:", categories)
    return categories

if 'initialized' not in st.session_state:
    st.session_state.initialized = True
    st.session_state.current_card = ""
    st.session_state.current_card_id = None
    st.session_state.current_category = ""
    st.session_state.resolvido_count = 0
    st.session_state.para_depois_count = 0
    st.session_state.descartado_count = 0
    st.session_state.resolvido_cards = []
    st.session_state.para_depois_cards = []
    st.session_state.descartado_cards = []
    st.session_state.selected_deck = ""
    st.session_state.history_visible = False

def gerar_card():
    if st.session_state.selected_deck:
        card_id, card_text, card_category = get_random_text(st.session_state.selected_deck)
        st.session_state.current_card_id = card_id
        st.session_state.current_card = card_text
        st.session_state.current_category = card_category
    else:
        st.warning("Selecione um baralho primeiro.")

def acao_botao(action):
    if action == 'resolvido':
        st.session_state.resolvido_count += 1
        st.session_state.resolvido_cards.append(st.session_state.current_card)
    elif action == 'para_depois':
        st.session_state.para_depois_count += 1
        st.session_state.para_depois_cards.append(st.session_state.current_card)
    elif action == 'descartado':
        st.session_state.descartado_count += 1
        st.session_state.descartado_cards.append(st.session_state.current_card)

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO interacoes_usuario (user_id, card_id, action) VALUES (%s, %s, %s)",
        ('default_user', st.session_state.current_card_id, action)
    )
    conn.commit()
    cursor.close()
    conn.close()

    gerar_card()

def limpar_historico():
    st.session_state.resolvido_count = 0
    st.session_state.para_depois_count = 0
    st.session_state.descartado_count = 0
    st.session_state.resolvido_cards = []
    st.session_state.para_depois_cards = []
    st.session_state.descartado_cards = []
    st.success("Histórico limpo!")

nome_baralhos = get_categories()
st.session_state.selected_deck = st.selectbox("Selecione um baralho:", nome_baralhos)

if st.button("Gerar Card Neuropsicológico"):
    gerar_card()

if st.session_state.current_card:
    st.markdown(f"""
    <div class="card">
        <h2>Card Gerado:</h2>
        <p class="big-font">{st.session_state.current_card}</p>
        <p>Categoria: <span style="color: #50C878;">{st.session_state.current_category}</span></p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("Resolvido", on_click=acao_botao, args=('resolvido',))
    with col2:
        st.button("Para depois", on_click=acao_botao, args=('para_depois',))
    with col3:
        st.button("Descartar", on_click=acao_botao, args=('descartado',))

    st.write(f"**Resolvidos:** {st.session_state.resolvido_count}")
    st.write(f"**Para depois:** {st.session_state.para_depois_count}")
    st.write(f"**Descartados:** {st.session_state.descartado_count}")

    if st.button("Mostrar Históricos"):
        st.session_state.history_visible = not st.session_state.history_visible

    if st.session_state.history_visible:
        st.subheader("Histórico de Cards")

        if st.session_state.resolvido_cards:
            st.markdown("### Resolvidos")
            for card in st.session_state.resolvido_cards:
                st.markdown(f"<p class='history-text'>{card}</p>", unsafe_allow_html=True)

        if st.session_state.para_depois_cards:
            st.markdown("### Para Depois")
            for card in st.session_state.para_depois_cards:
                st.markdown(f"<p class='history-text'>{card}</p>", unsafe_allow_html=True)

        if st.session_state.descartado_cards:
            st.markdown("### Descartados")
            for card in st.session_state.descartado_cards:
                st.markdown(f"<p class='history-text'>{card}</p>", unsafe_allow_html=True)


    st.button("Limpar Histórico", on_click=limpar_historico)

else:
    st.write("Clique no botão acima para gerar um card!")
