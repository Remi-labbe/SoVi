from dataclasses import dataclass


@dataclass
class State:
    state: bool

    # REQUETES

    def check(self):
        return self.state

    # COMMANDES

    def flip(self):
        self.state = not self.state
