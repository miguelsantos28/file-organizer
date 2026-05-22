import os
from datetime import datetime
from config import PASTA_LOG

def registrar(nome_arquivo, categoria):
    
    nome_arquivo_log = "registro_atividades.txt"
    caminho_completo_log = os.path.join(PASTA_LOG, nome_arquivo_log)

    os.makedirs(PASTA_LOG, exist_ok=True)

    with open(caminho_completo_log, "a", encoding="utf-8") as arquivo:
        horario_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        arquivo.write(f"[{horario_atual}] {nome_arquivo} -> {categoria}\n")
