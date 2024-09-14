import pygame
from pygame.locals import *
import Map2
import inputHandler
import player
import utils
import collision
import vector2
class game:
    def __init__(self):
        pygame.init()
        self.utilities = utils.utils()
        self.map = Map2.Map()
        self.player = player.player([320, 320], self.utilities, self.map)
        self.InputHandler = inputHandler.InputHandler(self.player, self.utilities)
        self.deltaTime = 0
        self.debug = False
        

    def setUp(self):
        self.map.setUpLevel(self.utilities.screenSize)
    
    def isRunning(self):
        return self.utilities.running

    def HandleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.utilities.running = False
            if event.type == KEYDOWN:
                for i in self.utilities.Keys:
                    if i[0] == event.key:
                        if event.key == K_o:
                            self.debug = not self.debug
                        
                        i[1] = True
                        break
                    elif i == self.utilities.Keys[len(self.utilities.Keys)-1]:
                        self.utilities.Keys.append([event.key, True])
            if event.type == KEYUP:
                for i in self.utilities.Keys:
                    if i[0] == event.key:
                        
                        i[1] = False
                        
        self.map.collision(self.player)
        self.InputHandler.KeyboardHandler()


            
    def Update(self):
        self.player.update(self.utilities.friction)
        self.map.getCloseLevelparts(self.player.camera, self.utilities.screenSize)
        self.utilities.DeltaTime()
        

        
    def Render(self):
        shift = [self.player.camera.vec2.pos[0] - (self.utilities.screenSize[0] / 2), self.player.camera.vec2.pos[1] - (self.utilities.screenSize[1] / 2)]

        self.map.draw(self.utilities.screen, shift)
        self.player.draw(self.utilities.screen, shift)
        self.map.drawAbovePlayer(self.utilities.screen, shift)
        if self.debug == True:
            self.utilities.screen.blit(self.map.debugWindow(self.utilities.Font), (0, 0))
        pygame.display.update()
    def FinishCalculations(self):
        pygame.time.Clock().tick(self.utilities.FPS)

    def Exit(self):
        pygame.quit()
        return 0
