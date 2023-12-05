from django.db import models



### modele

class Personnage(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64, default='pacman')
    skin = models.CharField(max_length=64, default='pacman')
    pos_x = models.IntegerField(default=0)
    pos_y = models.IntegerField(default=0)

    def __str__(self):
        return "ID={} | Nom={} | Skin={} | X={} | Y={}".format(
            self.id,
            self.name, 
            self.skin, 
            self.pos_x, 
            self.pos_y)
    
    def get_id(self):
        return self.id

    def get_position(self):
        return self.pos_x, self.pos_y

    def get_name(self):
        return self.name
    
    def get_skin(self):
        return self.skin

