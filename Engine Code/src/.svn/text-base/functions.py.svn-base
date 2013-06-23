""" Title: functions.py
    Purpose: Holds functions for adding sprites to scenes and inventories
    Author: Lillian
"""


def populate(scene, sprite, x, y):
    """Sets sprite coordinates and adds to scene's SpriteList group"""
    sprite.x = x
    sprite.y = y
    sprite.rect = sprite.image.get_rect(center = (sprite.x, sprite.y))
    scene.SpriteList.add(sprite)

def add_inventory(scene, sprite, x, y):
    """Sets sprite coordinates and adds to scene's Inventory group"""
    sprite.x = x
    sprite.y = y
    sprite.rect = sprite.image.get_rect(center = (sprite.x, sprite.y))
    scene.Inventory.add(sprite)
