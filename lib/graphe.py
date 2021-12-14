from dataclasses import dataclass, field
import math

from pyvis.network import Network

@dataclass(frozen=True)
class Graphe:
    sommets: dict = field(default_factory=dict)
    arcs: dict = field(default_factory=dict)

    # REQUETES

    def getNbSommets(self):
        """
        Renvoie le nombre de sommets dans le graphe
        """
        return len(self.getAllSommets())

    def getNbArcs(self):
        """
        Renvoie le nombre d'arcs dans le graphe
        """
        return sum(len(self.arcs[s]) for s in self.sommets)

    def getAllSommets(self):
        """
        Renvoie la liste des sommets du graphe
        """
        return list(self.sommets.values())

    def getAllSommetsNameSorted(self):
        """
        Renvoie la liste des sommets du graphe tries par nom croissant
        Les sommets sont deja tries par nom puisqu'on utilise un dictionnaire
        """
        return sorted(self.sommets.values(), key=lambda e: e.name)

    def getAllSommetsDegreSorted(self):
        """
        Renvoie la liste des sommets du graphe tries par degre sortant
        """
        return sorted(self.sommets.values(), key=lambda e: e.getDegreOut())

    def getAllUsers(self):
        """
        Renvoie la liste de tous les utilisateurs
        """
        return [s for s in self.sommets if s.isUser()]

    def getAllPages(self):
        """
        Renvoie la liste de tous les pages
        """
        return [s for s in self.sommets if not s.isUser()]

    def getallArcs(self):
        """
        Renvoie la liste des arcs du graphe
        """
        res = []
        for s in self.arcs: res.extend([(s,d) for d in self.arcs[s]])
        return res

    def getAllAdmins(self):
        """
        Renvoie la liste de tous les utilisateurs qui sont des administrateurs
        """
        res = [s.admins for s in self.sommets if not s.isUser()]
        return list(set(res))

    def getMoyAge(self):
        """
        Renvoie la moyenne d'age des utilisateurs
        """
        sum = 0
        count = 0
        for s in self.sommets:
            if s.isUser():
                sum += s.age
                count += 1
        count = 1 if count == 0 else count
        return sum / count

    def tableFormat(self):
        """
        Renvoie une liste formattant les donnees du graphe pour la sauvegarde
        """
        return [e.saveLineFormat() for e in self.sommets.values()]

    def pageRank(self):
        """
        Renvoie un dictionnaire associant chaque sommets a son pageRank
        """
        prs = dict()
        for s in self.sommets: prs[s] = 1
        for _ in range(0, 100):
            for s in self.sommets:
                somme = sum((prs[u] / u.getDegreOut()) for u in s.getNeighboursIn())
                prs[s] = 0.15 / len(prs) + 0.85 * somme
        return prs

    def shortestDistance(self, src):
        """
        Renvoie un dictionnaire contenant les plus courte distances de s a
        tous les autres sommets
        """
        dist = dict()
        for s in self.sommets: dist[s] = 0 if s == src else math.inf
        p = sorted(self.getAllSommets(), key=lambda e: dist[e])
        while len(p) != 0:
            u = p.pop(0)
            for v in u.getNeighboursOut():
                dist[v] = min(dist[u] + 1, dist[v])
            p = sorted(self.getAllSommets(), key=lambda e: dist[e])
        return dist

    def show(self):
        """
        Affiche le graphe
        """
        idxs = dict()
        prs = self.pageRank()
        n = 0
        net = Network('720', '720', directed=True)
        for s in self.sommets:
            net.add_node(n,
                        label=f"{s}",
                        value=prs[s],
                        shape='dot' if s.isUser() else 'square',
                        color='#cc99ff' if s.isUser() else '#a64dff')
            idxs[s] = n
            n += 1
        arcs = [(idxs[s1], idxs[s2]) for (s1, s2) in self.getallArcs()]
        net.add_edges(arcs)
        net.repulsion(0, 0, 0, 0)
        net.show("index.html")

    # COMMANDES

    def addSommet(self, s):
        """
        Ajoute un nouveau sommet au graphe s'il n'existe pas deja
        """
        if s not in self.sommets:
            self.sommets[s] = s
            self.arcs[s] = []

    # TODO: FIX THIS
    def removeSommet(self, s):
        """
        Retire un sommet du graphe s'il existe
        """
        if s in self.sommets:
            for a in [f for f in self.sommets[s].follows]:
                self.removeArc(s, self.sommets[a])
            for f in [f for f in self.sommets[s].followers]:
                self.removeArc(self.sommets[f], s)
            self.sommets.pop(s)
            self.arcs.pop(s)

    def addArc(self, src, dest):
        """
        Ajoute un arc entre src et dest si src est un utilisateur
        """
        if src in self.sommets and dest in self.sommets and dest not in self.arcs[src]:
            src = self.sommets.pop(src)
            sArcs = self.arcs.pop(src)
            dest = self.sommets.pop(dest)
            src.link(dest)
            if src.isUser(): sArcs.append(dest)
            self.arcs[src] = sArcs
            self.sommets[src] = src
            self.sommets[dest] = dest

    def removeArc(self, src, dest):
        """
        Retire l'arc entre src et dest du graphe s'il existe
        """
        if src in self.sommets and dest in self.sommets or src.isUser() and dest in self.arcs[src]:
            src = self.sommets.pop(src)
            sArcs = self.arcs.pop(src)
            dest = self.sommets.pop(dest)
            src.unlink(dest)
            if src.isUser(): sArcs.remove(dest)
            self.arcs[src] = sArcs
            self.sommets[src] = src
            self.sommets[dest] = dest
