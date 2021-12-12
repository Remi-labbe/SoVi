from dataclasses import dataclass, field

from lib.sommet import Sommet

@dataclass(frozen=True, order=True)
class Utilisateur(Sommet):
    firstName: str
    age: int
    follows: list = field(default_factory=list, compare=False)
    followers: list = field(default_factory=list, compare=False)

    # REQUETES

    def __str__(self):
        initals = ''.join([m[0].capitalize() for m in self.name.split(' ')])
        return f"{self.firstName.capitalize()} {initals}."

    def getDegreIn(self):
        return len(self.followers)

    def getDegreOut(self):
        return len(self.follows)

    def getNeighboursIn(self):
        return self.followers

    def getNeighboursOut(self):
        return self.follows

    def isUser(self):
        return True

    def saveCellFormat(self):
        return f"{self.name};{self.firstName};{self.age}"

    def saveLineFormat(self):
        line = [self.saveCellFormat()]
        line.extend([el.saveCellFormat() for el in self.follows])
        return line

    # COMMANDES

    def link(self, s):
        if s not in self.follows:
            self.follows.append(s)
            s.followers.append(self)

    def unlink(self, s):
        if s in self.follows:
            self.follows.remove(s)
            s.followers.remove(self)

    def delete(self):
        for f in self.follows: self.unlink(f)
        for f in self.followers: f.unlink(self)
