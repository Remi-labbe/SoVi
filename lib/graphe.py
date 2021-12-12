from dataclasses import dataclass, field
import math

@dataclass(frozen=True)
class Graphe:
    sommets: dict = field(default_factory=dict)
    arcs: dict = field(default_factory=dict)

    # REQUETES

    def getNbSommets(self):
        return len(self.getAllSommets())

    def getNbArcs(self):
        return sum(len(self.arcs[s]) for s in self.sommets)

    def getAllSommets(self):
        return self.sommets.values()

    def getAllSommetsNameSorted(self):
        return sorted(self.sommets.values(), key=lambda e: e.name)

    def getAllSommetsDegreSorted(self):
        return sorted(self.sommets.values(), key=lambda e: e.getDegreOut())

    def getallArcs(self):
        res = []
        for s in self.arcs: res.extend([(s,d) for d in self.arcs[s]])
        return res

    def getAllAdmins(self):
        res = [s.admins for s in self.sommets if not s.isUser()]
        return list(set(res))

    def getMoyAge(self):
        sum = 0
        count = 0
        for s in self.sommets:
            if s.isUser():
                sum += s.age
                count += 1
        count = 1 if count == 0 else count
        return sum / count

    def tableFormat(self):
        return [e.saveLineFormat() for e in self.sommets.values()]

    def pageRank(self):
        prs = dict()
        for s in self.sommets: prs[s] = 1
        for _ in range(0, 100):
            for s in self.sommets:
                somme = sum((prs[u] / u.getDegreOut()) for u in s.getNeighboursIn())
                prs[s] = 0.15 / len(prs) + 0.85 * somme
        return prs

    def shortestDistance(self, src):
        dist = dict()
        for s in self.sommets: dist[s] = 0 if s == src else math.inf
        p = sorted(self.getAllSommets(), key=lambda e: dist[e])
        while len(p) != 0:
            u = p.pop(0)
            for v in u.getNeighboursOut():
                dist[v] = min(dist[u] + 1, dist[v])
            p = sorted(self.getAllSommets(), key=lambda e: dist[e])
        return dist

    # COMMANDES

    def addSommet(self, s):
        self.sommets[s] = s
        self.arcs[s] = []

    def removeSommet(self, s):
        s = self.sommets.pop(s)
        sArcs = self.arcs.pop(s)
        for a in sArcs:
            s.unlink(a)

    def addArc(self, src, dest):
        src = self.sommets.pop(src)
        sArcs = self.arcs.pop(src)
        dest = self.sommets.pop(dest)
        src.link(dest)
        sArcs.append(dest)
        self.arcs[src] = sArcs
        self.sommets[src] = src
        self.sommets[dest] = dest

    def removeArc(self, src, dest):
        src = self.sommets.pop(src)
        sArcs = self.arcs.pop(src)
        dest = self.sommets.pop(dest)
        src.unlink(dest)
        sArcs.remove(dest)
        self.arcs[src] = sArcs
        self.sommets[src] = src
        self.sommets[dest] = dest

    # OUTILS

