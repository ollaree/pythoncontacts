# utils.py
# Dizionario per memorizzare i contatti
contatti = {}

# Funzione per aggiungere un contatto
def aggiungi_contatto(nome, telefono):
    if nome not in contatti:
        contatti[nome] = telefono
        print(f"Contatto {nome} aggiunto con successo!")
    else:
        print(f"Il contatto {nome} esiste già.")

# Funzione per eliminare un contatto
def elimina_contatto(nome):
    if nome in contatti:
        del contatti[nome]
        print(f"Contatto {nome} eliminato con successo!")
    else:
        print(f"Contatto {nome} non trovato.")

# Funzione per cercare un contatto
def cerca_contatto(nome):
    if nome in contatti:
        print(f"Contatto trovato: {nome} - {contatti[nome]}")
    else:
        print(f"Contatto {nome} non trovato.")

# Funzione per vedere tutti i contatti
def vedi_tutti_contatti():
    if contatti:
        print("Lista dei contatti:")
        for nome, telefono in contatti.items():
            print(f"{nome}: {telefono}")
    else:
        print("Nessun contatto presente.")

