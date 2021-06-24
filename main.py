    class Chien(object):
        def __init__(self, race):
    	self.race = race
     
        @property
        def taille(self):
    	return 100
     
    class Chihuahua(Chien):
        def __init__(self, nom):
    	super().__init__("Chihuahua")
    	self.nom = nom
     
    chien = Chihuahua("Lily")
    print(chien.race)
