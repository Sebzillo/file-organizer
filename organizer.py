import os
import shutil
import sys
from datetime import datetime

# Definizione categorie file
FILE_CATEGORIES = {
    'Documenti': ['.pdf', '.doc', '.docx', '.txt', '.rtf'],
    'Immagini': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Video': ['.mp4', '.avi', '.mkv', '.mov'],
    'Audio': ['.mp3', '.wav', '.flac', '.m4a'],
    'Archivi': ['.zip', '.rar', '.7z', '.tar'],
    'Codice': ['.py', '.js', '.html', '.css', '.java']
}

def trova_categoria(estensione):
    estensione_lower = estensione.lower()
    for categoria, lista_estensioni in FILE_CATEGORIES.items():
        if estensione_lower in lista_estensioni:
            return categoria
    return 'Altri'

def crea_cartelle_categorie(cartella_base):
    print(f"\nCreazione cartelle in: {cartella_base}")
    for categoria in FILE_CATEGORIES.keys():
        percorso_cartella = os.path.join(cartella_base, categoria)
        if not os.path.exists(percorso_cartella):
            os.makedirs(percorso_cartella)
            print(f"Creata cartella: {categoria}")
        else:
            print(f"Cartella già esistente: {categoria}")
    
    percorso_altri = os.path.join(cartella_base, "Altri")
    if not os.path.exists(percorso_altri):
        os.makedirs(percorso_altri)
        print(f"Creata cartella: Altri")

def sposta_file(file_sorgente, cartella_destinazione, categoria):
    nome_file = os.path.basename(file_sorgente)
    percorso_destinazione = os.path.join(cartella_destinazione, categoria, nome_file)
    try:
        shutil.move(file_sorgente, percorso_destinazione)
        print(f"Spostato: {nome_file} -> {categoria}")
        return True
    except Exception as e:
        print(f"Errore spostando {nome_file}: {e}")
        return False

def organizza_cartella(cartella_sorgente, dry_run=False, backup=False):
    
    if dry_run:
        print("=== MODALITÀ SIMULAZIONE - NESSUN FILE VERRÀ SPOSTATO ===")
    
    crea_cartelle_categorie(cartella_sorgente)
    lista_elementi = os.listdir(cartella_sorgente)
    
    for elemento in lista_elementi:
        percorso_completo = os.path.join(cartella_sorgente, elemento)
        
        if not os.path.isfile(percorso_completo):
            continue
            
        nome, estensione = os.path.splitext(elemento)
        categoria = trova_categoria(estensione)
        
        if dry_run:
            print(f"SIMULAZIONE: {elemento} -> {categoria}")
        else:
            sposta_file(percorso_completo, cartella_sorgente, categoria)

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 organizer.py <cartella> [--dry-run] [--backup]")
        return
    
    cartella = sys.argv[1]
    dry_run = "--dry-run" in sys.argv
    backup = "--backup" in sys.argv
    
    
    if not os.path.exists(cartella):
        print(f"Errore: cartella '{cartella}' non esiste")
        return
        
    organizza_cartella(cartella, dry_run, backup)

if __name__ == "__main__":
    main()