import os
from config import PASTA_ORIGEM
import shutil

def mover_arquivo(nome_arquivo, categoria):
    caminho_completo = os.path.join(PASTA_ORIGEM, nome_arquivo)
    caminho_destino = os.path.join(PASTA_ORIGEM, categoria)

    os.makedirs(caminho_destino, exist_ok = True)
        
    shutil.move(caminho_completo, caminho_destino)