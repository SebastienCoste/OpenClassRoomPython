# -*-coding:Latin-1 -*
inventaire = [
     ("pommes", 22),
     ("melons", 4),
     ("poires", 18),
     ("fraises", 76),
     ("prunes", 51),
]

inventaire_inverse = [(qtt, nom_fruit) for nom_fruit,qtt in inventaire]

inventaire = [(nom_fruit, qtt) for qtt,nom_fruit in sorted(inventaire_inverse, reverse=True) if qtt >5]

list = [1,2,3]
dic = {"sep":"\n"}
print (*list, **dic)
