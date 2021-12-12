from dataclasses import dataclass, field

from sommet import Sommet

@dataclass(frozen=True, order=True)
class Page(Sommet):
    admins: list = field(default_factory=list, compare=False)
    followers: list = field(default_factory=list, compare=False)

    # REQUETES

    def __str__(self):
        return self.name.capitalize()

    def getDegreIn(self):
        return len(self.followers)

    def getDegreOut(self):
        return 0

    def getNeighboursIn(self):
        return self.followers

    def getNeighboursOut(self):
        return []

    def isUser(self):
        return False

    def saveCellFormat(self):
        return self.name

    def saveLineFormat(self):
        line = [self.saveCellFormat()]
        line.extend([el.saveCellFormat() for el in self.admins])
        return line

    # COMMANDES

    def link(self, s):
        if s not in self.admins: self.admins.append(s)

    def unlink(self, s):
        if s in self.admins: self.admins.remove(s)

    def delete(self):
        for f in self.admins: self.unlink(f)
        for f in self.followers: f.unlink(self)
