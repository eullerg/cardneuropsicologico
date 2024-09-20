import mysql.connector
from config import db_config

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
groups = {
    "Ansiedade": group_a,
    "Depressão": group_b,
    "Estresse": group_c,
    "Insegurança": group_d,
    "Solidão": group_e
}

def populate_database():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    for category, texts in groups.items():
        for text in texts:
            cursor.execute(
                "INSERT INTO cards (category, text) VALUES (%s, %s)",
                (category, text)
            )

    conn.commit()
    cursor.close()
    conn.close()
    print("Banco de dados preenchido com sucesso!")

if __name__ == "__main__":
    populate_database()


