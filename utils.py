import pygame
class utils:
    def __init__(self) -> None:
        #DELTA TIME 
        self.deltaTime = 0
        self.lastFrameTime = 0
        self.get_ticks = pygame.time.get_ticks
        #SCREEN
        self.screenSize = [640, 640]
        self.screen = pygame.display.set_mode(self.screenSize, 0, 0, 0, 1)
        self.FPS = 144
        self.running = True
        self.friction = .9
        self.Keys = [[pygame.K_w, False]]
    def DeltaTime(self):
        self.deltaTime = self.get_ticks() - self.lastFrameTime
        self.lastFrameTime = self.get_ticks()
        return self.deltaTime

    def newScreen(self, screenSize, flags=0, depth=0, display=0, vsync=0):
        self.screen = pygame.display.set_mode(screenSize, flags, depth, display, vsync)
        self.screenSize = screenSize
        return self.screen