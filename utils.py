
# Funzione per vedere tutti i contatti
def vedi_tutti_contatti():
    if contatti:
        print("Lista dei contatti:")
        for nome, telefono in contatti.items():
            print(f"{nome}: {telefono}")
    else:
        print("Nessun contatto presente.")