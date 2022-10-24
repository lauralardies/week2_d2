from email.base64mime import header_length


class Soldier():
    def __init__(self, health, strength) -> None:
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def recieve_damage(self, damage):
        self.health = self.health - damage