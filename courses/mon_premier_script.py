import unittest
from typing import List

def count_long_names(names_list: List[str], length_threshold: int = 7) -> int:
    """
    Compte le nombre de prénoms dépassant un certain nombre de caractères.

    :param names_list: Liste des prénoms à analyser.
    :param length_threshold: Seuil de longueur pour définir un prénom long (par défaut 7).
    :return: Nombre total de prénoms dépassant le seuil.
    """
    return sum(1 for name in names_list if len(name) > length_threshold)

def display_name_lengths(names_list: List[str], length_threshold: int = 7) -> None:
    """
    Affiche si chaque prénom dépasse ou non le seuil défini.

    :param names_list: Liste des prénoms à analyser.
    :param length_threshold: Seuil de longueur pour définir un prénom long.
    """
    for name in names_list:
        status = "supérieur" if len(name) > length_threshold else "inférieur ou égal"
        print(f"{name} est un prénom avec un nombre de lettres {status} à {length_threshold}")

class TestCountLongNames(unittest.TestCase):
    """Tests unitaires pour la fonction count_long_names."""

    def test_count_long_names(self):
        """
        Vérifie que la fonction retourne le bon nombre de prénoms ayant plus de 7 lettres.
        """
        names_list = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        result = count_long_names(names_list)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    # Liste de prénoms test
    sample_names = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]

    # Affichage des prénoms et de leur longueur
    display_name_lengths(sample_names)

    # Exécution des tests unitaires
    unittest.main()
