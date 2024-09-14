import pygame, vector2
from pygame.locals import *
class InputHandler:
    def __init__(self, player, utils) -> None:
        self.player = player
        self.deltaTimeEstimate = 16
        self.utils = utils
    def KeyboardHandler(self):
        for key in self.utils.Keys:
            if key[0] ==  pygame.K_w:
                if key[1] == True:
                    self.player.vec2.vel[1] = self.player.vec2.vel[1] - ((self.player.accel/self.player.weight)/self.deltaTimeEstimate)
                else:
                    if self.player.vec2.vel[1] < 0:
                        self.player.vec2.vel[1] = self.player.vec2.vel[1]*self.player.notrunningFriction
                
            if key[0] == pygame.K_s:
                if key[1] == True:
                    self.player.vec2.vel[1] = self.player.vec2.vel[1] + ((self.player.accel/self.player.weight)/self.deltaTimeEstimate)
                else:
                    if self.player.vec2.vel[1] > 0:
                        self.player.vec2.vel[1] = self.player.vec2.vel[1]*self.player.notrunningFriction
                
            if key[0] == pygame.K_a:
                if key[1] == True:
                    self.player.vec2.vel[0] = self.player.vec2.vel[0] - ((self.player.accel/self.deltaTimeEstimate)/self.player.weight)
                else:
                    if self.player.vec2.vel[0] < 0:
                        self.player.vec2.vel[0] = self.player.vec2.vel[0]*self.player.notrunningFriction
                
            if key[0] == pygame.K_d:
                if key[1] == True:
                    self.player.vec2.vel[0] = self.player.vec2.vel[0] + ((self.player.accel/self.player.weight)/self.deltaTimeEstimate)
                else:
                    if self.player.vec2.vel[0] > 0:
                        self.player.vec2.vel[0] = self.player.vec2.vel[0]*self.player.notrunningFriction
            
                