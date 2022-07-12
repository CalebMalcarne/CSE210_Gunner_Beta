from casting.enemy import Enemy


class Boss(Enemy):
    #still need to put in values just making a skeleton 
    def __init__(self, body, image):

        self._body = body
        self.size = (80,70)
        self._image = image
        self.hitpoints = Enemy.set_hitpoints #multiplied by the difficulty
        self.color = self.boss_color(self.hitpoints)

    def boss_color(hitpoints):
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
        number_of_enemies = 0
        if number_of_enemies == 25:
            return True
        else:
            number_of_enemies += 1
            return False
            

        #if number of enemies is 25, return spawn boss as True 
        #else have number of enemies + 1

