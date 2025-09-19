import os

# Test step 1: estrarre estensione
def test_estensione():
    file_examples = ["foto.jpg", "presentazione.pptx", "README"]
    
    for nome_file in file_examples:
        nome, estensione = os.path.splitext(nome_file)
        print(f"File: {nome_file}")
        print(f"Nome: {nome}")
        print(f"Estensione: {estensione}")
        print("-" * 20)

# Esegui il test
test_estensione()