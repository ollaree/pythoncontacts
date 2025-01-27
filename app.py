# app.py
from utils import aggiungi_contatto, elimina_contatto, cerca_contatto, vedi_tutti_contatti

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Vedere tutti i contatti")
        print("2. Aggiungere un contatto")
        print("3. Eliminare un contatto")
        print("4. Cercare un contatto")
        print("5. Esci")
        
        scelta = input("Scegli un'opzione (1-5): ")

        if scelta == "1":
            vedi_tutti_contatti()
        elif scelta == "2":
            nome = input("Nome del contatto: ")
            telefono = input("Numero di telefono: ")
            aggiungi_contatto(nome, telefono)
        elif scelta == "3":
            nome = input("Nome del contatto da eliminare: ")
            elimina_contatto(nome)
        elif scelta == "4":
            nome = input("Nome del contatto da cercare: ")
            cerca_contatto(nome)
        elif scelta == "5":
            print("Uscita in corso...")
            break
        else:
            print("Scelta non valida, riprova.")

# Avvia il menu
if __name__ == "__main__":
    menu()
