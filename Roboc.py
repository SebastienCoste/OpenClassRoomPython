# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

from roboc.RobocException import RobocException
from roboc.connector import Messages as m
import argparse
from roboc.network import Client as c, Server as s, StandAlone as sa

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.parse_args()
    parser.add_argument("-l", "--lan", help="language: 'fr'(default) or 'en'")
    parser.add_argument("-t", "--type", help="type: c for client, s for server or sa for standalone")
    args = parser.parse_args()
    lan = "FR"
    if args.lan:
        if args.lan.upper() in m.authorizedLan:
            lan = args.lan.upper()
        else:
            raise RobocException("Unrecognized language")
    
    network = None
    if args.type:
        if args.type.upper() == "C":
            network = c.Client(lan)
        elif args.type.upper() == "S":
            network = s.Server(lan)
        elif args.type.upper() == "SA":
            network = sa.StandAlone(lan)
    else:
        network = sa.StandAlone(lan)
        #raise RobocException("Unrecognized network type")
    
    network.run()
            







