from config import TIPOS

def classificar(extensao):
    for chave, valor in TIPOS.items():
        if extensao in valor:
            return chave
    return "Outros"