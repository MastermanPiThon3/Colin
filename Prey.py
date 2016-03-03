import pygame
from pygame.locals import *
from MathFunctions import *

class Prey:
    def __init__(self, playerPosition, startPosition):
        self.Position = startPosition
        
