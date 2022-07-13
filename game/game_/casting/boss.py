from game_.casting.enemy import Enemy

class Boss(Enemy):

    def __init__(self, body, image):

        self._body = body
        self._image = image

        self.size = (80,70)
        self.hitpoints = Enemy.set_hitpoints * 3 #3 times stronger than a normal enemy
        self.color = self.boss_color(self.hitpoints)

    def boss_color(hitpoints):
        #depending on the health, the color will change 
        boss_color = (250,0,0)
        if hitpoints > (hitpoints/3)*2:
            return boss_color(0,0,0) #decide on a color we want 
        elif hitpoints > (hitpoints/3):
            return boss_color(0,0,0)#decide on a color we want 
        elif hitpoints > 0:
            return boss_color(0,0,0)#decide on a color we want 
        else:
            return boss_color

    def spawn_boss():
        #once there have been 25 enemies then it will spawn the boss
        number_of_enemies = 0
        if number_of_enemies == 25:
            return True
        else:
            number_of_enemies += 1
            return False
            
    def take_damage(self, damage):
        self.hitpoints -= damage




