import random

def obter_mensagem_aleatoria():
    mensagens = [
        "Olá, Mundo!",
        "Python é uma linguagem de programação poderosa.",
        "Vamos aprender a programar em Python!",
        "Python é uma liguagem de programação interpretada.",
        "Python é uma liguagem de programação de alto nível."
    ]

    return random.choice(mensagens)
