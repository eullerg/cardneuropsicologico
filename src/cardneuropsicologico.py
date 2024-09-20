"""
Cards Neuro Psicologicos

Authors: @eullerg @dimasgb7
"""
# TODO: Criar um novo repositorio chamado src e dentro dele adicionar os modulos .py
# TODO: Criar um arquivo Makefile com os comandos necessários para execução do app
# TODO: Diminuir a complexidade do requirements.txt, remover as bibliotecas adicionadas indiretamente e deixar apenas as necessárias para iniciar um novo projeto.
import mysql.connector
from config import db_config
import random

# TODO: Criar um modulo chamado config.py e adicionar essa config de markdown como uma variavel que será exportada no modulo principal do app.

# TODO: Remover os grupos da função e transformar em variaveis globais.
# TODO: Adaptar a lógica para ele pegar um texto aleátorio de um baralho especifico, ele deve ser capaz de receber a informação de qual baralho extrair a informação.

def get_random_text(nome_baralho):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id, text FROM cards WHERE category = %s", (nome_baralho,))
    cards = cursor.fetchall()

    if not cards:
        cursor.close()
        conn.close()
        raise ValueError(f"Baralho '{nome_baralho}' não encontrado ou vazio.")

    random_card = random.choice(cards)
    cursor.close()
    conn.close()
    return random_card['id'], random_card['text'], nome_baralho

# TODO: Mover essa sessão para um arquivo unico chamado app.py
# TODO: Nesse novo arquivo app.py deve ser importada a lógica de retorno de texto aleatorio em cardneuropsicologico.py
# TODO: Adicionar 3 novos botões : Resolvido, Para depois e Descartar
# TODO: Criar um Display para as quantidades de cards Resolvidos, Para depois e Descarta. O display deve mostrar a quantidade classificada pela ação de clique nos botões para cada umas das categorias durante a execução do jogo. 
