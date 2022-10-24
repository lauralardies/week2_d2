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
        return super().attack()
    
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

class Saxon(Soldier):

    def __init__(self, health, strength) -> None:
        super().__init__(health, strength)
    
    def attack(self):
        return super().attack()

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            sol = 'A Saxon has received ' + str(damage) + ' points of damage'
            return sol
        else:
            sol = 'A Saxon has died in combat'
            return sol

class War():
    def __init__(self) -> None:
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        Saxon.receiveDamage(self, Viking.self.strength)
        if Saxon.self.health <= 0:
            self.saxonArmy.remove(Saxon)
        return (Saxon.receiveDamage(self, Viking.self.strength), Viking.self.strength)
    
    def saxonAttack(self):
        Viking.receiveDamage(self, Saxon.self.strength)
        if Viking.self.health <= 0:
            self.vikingArmy.remove(Viking)
        return (Viking.receiveDamage(self, Saxon.self.strength), Saxon.self.strength)
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return 'Vikings have won the war of the century!'
        elif len(self.vikingArmy) == 0:
            return 'Saxons have fought for their lives and survive another day...'
        else:
            return 'Vikings and Saxons are still in the thick of battle.'
