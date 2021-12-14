import csv
from dataclasses import dataclass

from lib.graphe import Graphe
from lib.page import Page
from lib.utilisateur import Utilisateur

@dataclass(frozen=True)
class BadDataFormatException(Exception):
    error: str = ""

class DataLoader:

    @staticmethod
    def load(path : str):
        """
        Reads data from the file {path}
        Must be CSV
        """
        def readCell(s: str):
            """ Reads a cell of the CSV file and return a User or Page """
            data = s.split(';')
            if len(data) == 3: # Utilisateur
                # lstrip removes leading spaces
                # rstrip removes trailing spaces
                name = data[0].lstrip().rstrip()
                firstName = data[1].lstrip().rstrip()
                age = int(data[2].lstrip().rstrip())
                return Utilisateur(name, firstName, age)
            elif len(data) == 1: # Page
                return Page(data[0].lstrip().rstrip())
            else:
                raise BadDataFormatException(s)

        try:
            with open(path, mode='r') as f:
                reader = csv.reader(f)
                g = Graphe()
                for line in reader:
                    if line == []: raise BadDataFormatException("Ligne vide")
                    leadCell = readCell(line[0])
                    g.addSommet(leadCell)
                    # if User then it is the list of the nodes he follows
                    # if Page node then it is the list of the admins
                    for i in range(1, len(line)):
                        if line[i] == "": break
                        cell = readCell(line[i])
                        g.addSommet(cell)
                        g.addArc(leadCell, cell)
                if g.getNbSommets() == 0: raise BadDataFormatException("Fichier vide")
                return g
        except Exception as e:
            print(f"Error: {e}")
            return None

    @staticmethod
    def save(path: str, data: list) -> None:
        """ Saves the data in the file {path}"""
        try:
            with open(path, mode='w') as f:
                writer = csv.writer(f)
                writer.writerows(data)
        except Exception as e:
            print(e)
            return None
