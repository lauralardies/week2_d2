class Soldier():
    def __init__(self, health, strength) -> None:
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage

class Viking(Soldier):
    def __init__(self, name, health, strength) -> None:
        super().__init__(health, strength)
        self.name = name

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            sol = str(self.name) + ' has received ' + str(damage) + ' points of damage'
            return sol
        else:
            sol = str(self.name) + ' has died in act of combat'
            return sol
    
    def battleCry(self):
        return ('Odin Owns You All!')