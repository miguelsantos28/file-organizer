#  File Organizer

Script Python que organiza automaticamente os arquivos de uma pasta, movendo-os para subpastas por categoria e registrando tudo em um arquivo de log.

##  Como usar

**1. Clone o repositório**
```bash
git clone https://github.com/miguelsantos28/file-organizer.git
cd file-organizer
```

**2. Configure a pasta de origem**

Abra o `config.py` e ajuste as variáveis:
```python
PASTA_ORIGEM = r"C:\Users\SeuUsuario\Downloads"
PASTA_LOG = r"C:\caminho\para\file_organizer\logs"
```

**3. Execute**
```bash
python main.py
```

##  Estrutura do projeto

```
file-organizer/
├── organizer/
│   ├── scanner.py       # lê os arquivos da pasta
│   ├── classifier.py    # classifica por extensão
│   ├── mover.py         # move para a pasta correta
│   └── logger.py        # registra as operações
├── logs/                # gerado automaticamente
├── tests/
│   └── test_classifier.py
├── main.py
├── config.py
└── README.md
```

##  Categorias suportadas

| Categoria | Extensões |
|---|---|
| Imagem | `.png`, `.jpg`, `.jfif` |
| Documento | `.pdf` |
| Documento Word | `.docx` |
| Documento Excel | `.xls`, `.xlsx` |
| Video | `.mp4` |
| Executavel | `.exe` |
| Arquivo compactado | `.zip`, `.rar` |

> Arquivos com extensões não mapeadas são movidos para a pasta **Outros**.

##  Testes

```bash
python -m pytest tests/
```

##  Adicionando categorias

Edite o dicionário `TIPOS` no `config.py`:

```python
TIPOS = {
    "Audio": [".mp3", ".wav"],
    ...
}
```
