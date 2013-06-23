""" Title: Inventory.py

    Purpose/Overview: Contains Inventory class, which is the BasicSprite
                      image at the bottom of the three ExploreScenes

    Author: Lillian

"""

from BasicSprite import BasicSprite

class Inventory(BasicSprite):
    """ Creates a subscene within each explore scene so that the character
        can store his/her objects"""

    def __init__(self, SuperScene):
        """Initializes Inventory, which calls BasicSprite __init__."""
        BasicSprite.__init__(self, SuperScene,'data/Inventory.png')
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = SuperScene.width/2
        self.y = SuperScene.height - int(0.5*self.height)
