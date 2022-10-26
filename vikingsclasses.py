import random

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
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        result = saxon.receiveDamage(viking.attack())
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return result
    
    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        result = viking.receiveDamage(saxon.attack())
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return result
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return 'Vikings have won the war of the century!'
        elif len(self.vikingArmy) == 0:
            return 'Saxons have fought for their lives and survive another day...'
        else:
            return 'Vikings and Saxons are still in the thick of battle.'
