# -*-coding:Latin-1 -*
"""module multipli contenant la fonction table"""

def table(nb, maxi=10):
    """Fonction affichant la table de multiplication par nb de
    1 * nb jusqu'à maxi * nb"""
    i = 0
    while i < maxi:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1