from organizer.classifier import classificar

def test_imagem():
    assert classificar(".png") == "Imagem"
def test_documento():
    assert classificar(".pdf") == "Documento"
def test_video():
    assert classificar(".mp4") == "Video"
def test_executavel():
    assert classificar(".exe") == "Executavel"
def test_desconhecido():
    assert classificar(".xyz") == "Outros"