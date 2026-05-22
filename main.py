from organizer.classifier import classificar
from organizer.mover import mover_arquivo
from organizer.logger import registrar
from config import PASTA_ORIGEM
from organizer.scanner import listar_arquivos
import os

def main():
    arquivos_pasta = listar_arquivos(PASTA_ORIGEM)
    for arquivo in arquivos_pasta:
        if os.path.isfile(os.path.join(PASTA_ORIGEM, arquivo)):
            nome_limpo, extensao = os.path.splitext(arquivo)
            categoria = classificar(extensao.lower())

            print(f"Nome: {nome_limpo} | Extensão: {extensao} | Categoria: {categoria}")

            mover_arquivo(arquivo, categoria)
            registrar(arquivo, categoria)

if __name__ == "__main__":
    main()