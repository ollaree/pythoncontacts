# tests.py
import unittest
from utils import aggiungi_contatto, elimina_contatto, cerca_contatto, vedi_tutti_contatti

class TestContactsApp(unittest.TestCase):

    def setUp(self):
        """Prepariamo l'ambiente di test, resettando i contatti."""
        global contatti
        contatti = {}

    def test_aggiungi_contatto(self):
        aggiungi_contatto("Luca Verdi", "345678901")
        self.assertIn("Luca Verdi", contatti)
        self.assertEqual(contatti["Luca Verdi"], "345678901")

    def test_aggiungi_contatto_esistente(self):
        aggiungi_contatto("Giulia Bianchi", "987654321")
        aggiungi_contatto("Giulia Bianchi", "123456789")  # Deve fallire
        self.assertEqual(contatti["Giulia Bianchi"], "987654321")

    def test_elimina_contatto(self):
        aggiungi_contatto("Marco Neri", "123123123")
        elimina_contatto("Marco Neri")
        self.assertNotIn("Marco Neri", contatti)

    def test_elimina_contatto_non_esistente(self):
        elimina_contatto("Paola Gialli")  # Non esiste
        self.assertNotIn("Paola Gialli", contatti)

    def test_cerca_contatto(self):
        aggiungi_contatto("Anna Blu", "456789012")
        result = cerca_contatto("Anna Blu")
        self.assertEqual(result, "Contatto trovato: Anna Blu - 456789012")

    def test_cerca_contatto_non_esistente(self):
        result = cerca_contatto("Non Esiste")
        self.assertEqual(result, "Contatto Non Esiste non trovato.")

    def test_vedi_tutti_contatti(self):
        aggiungi_contatto("Marco Rossi", "1122334455")
        aggiungi_contatto("Elena Fabbri", "6677889900")
        result = vedi_tutti_contatti()
        self.assertTrue("Marco Rossi" in result)
        self.assertTrue("Elena Fabbri" in result)

if __name__ == "__main__":
    unittest.main()
