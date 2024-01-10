import pygame, vector2
#class BackRoundPiece:
#    def __init__(self, pos: list, img: str):
#        self.pos = pos
#        self.size = [32, 32]
#        self.surface = pygame.image.load(img)
#        self.rect = pygame.Rect(self.pos, self.size)
#    def draw(self, screen, shift):
#        screen.blit(self.surface, (self.pos[0]-shift[0], self.pos[1]-shift[1]))

class door:
    def __init__(self, pos: list, layer: int):
        self.vec2 = vector2.Vec2(pos[0], pos[1])
        self.layer = layer
        self.size = [32, 32] 
        #self.surfaceClosed = pygame.image.load("data/img/Tiles_063.png")
        #self.surfaceHalfOpen = pygame.image.load("data/img/Tiles_064.png")
        #self.surfaceOpen = pygame.image.load("data/img/Tiles_065.png")
        self.rect = pygame.Rect(self.vec2.pos, self.size)
        self.open = False
    #def draw(self, screen, shift):
        #screen.blit(self.surfaceClosed, (self.vec2.pos[0]-shift[0], self.vec2.pos[1]-shift[1]))

class MovingCube:
    def __init__(self, pos: list, layer: int, weight):
        self.vec2 = vector2.Vec2(pos[0], pos[1])
        self.layer = layer
        self.size = [32, 32] 
        self.surface = pygame.image.load("data/img/black.png")
        self.rect = pygame.Rect(self.vec2.pos, self.size)
        self.weight = weight
        self.hit = []
    def update(self, deltaTime, friction):
        if self.hit == []:
            self.vec2.vel = vector2.Intmul(self.vec2.vel, friction)
        self.vec2.addVelwithDeltaTime(deltaTime)
    def draw(self, screen, shift):
        self.rect.x = self.vec2.pos[0]-shift[0]
        self.rect.y = self.vec2.pos[1]-shift[1]
#        screen.blit(self.surface, (self.vec2.pos[0]-shift[0], self.vec2.pos[1]-shift[1]))
        pygame.draw.rect(screen, (0, 0, 0), self.rect)
        self.rect.x = self.vec2.pos[0]
        self.rect.y = self.vec2.pos[1]
    