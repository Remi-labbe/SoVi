from abc import abstractmethod
from dataclasses import dataclass

@dataclass(frozen=True, order=True)
class Sommet:
    name: str

    # REQUETES

    @abstractmethod
    def getDegreIn(self):
        pass

    @abstractmethod
    def getDegreOut(self):
        pass

    @abstractmethod
    def getNeighboursIn(self):
        pass

    @abstractmethod
    def getNeighboursOut(self):
        pass

    @abstractmethod
    def isUser(self):
        pass

    @abstractmethod
    def saveCellFormat(self):
        pass

    @abstractmethod
    def saveLineFormat(self):
        pass

    # COMMANDES

    @abstractmethod
    def link(self, s):
        pass

    @abstractmethod
    def unlink(self, s):
        pass

    @abstractmethod
    def delete(self):
        pass
