from email.base64mime import header_length


class Soldier():
    def __init__(self, health, strength) -> None:
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage

class Viking():
    def __init__(self, name, health, strength) -> None:
        Soldier.__init__(self, health, strength)
        self.name = name
    
    Soldier.attack()

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health <= 0:
            return (self.name, ' has received ', damage, ' points of damage')
        else:
            return (self.name, ' has died in act of combat')
    
    def battleCry(self):
        return ('Odin Owns You All!')