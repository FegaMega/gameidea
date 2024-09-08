import JH, Objects, pygame

class Map:
    def __init__(self) -> None:
        self.LevelPixelSize = [8192, 8192]
        self.BackroundLevel = ["data/img/floor.png", "data/img/wall.png"]
        self.BackroundLevelsize = [256, 256]
        self.BackroundLevelPartSize = [32, 32]
        self.BackroundNames = [None, "data/img/floor.png", "data/img/wall.png"]
        self.JsonLevel = JH.JsonReader("data/level/level.json")["backround"]
        self.Level = []
        self.movingLevel = []
        self.chunkSize = [64, 64]
        self.loadedChunks = []
        self.loadedChunksPos = [0, 0]
        self.doors = []


        self.map = [
            pygame.Surface(self.LevelPixelSize),
            [[]],
            [[]],
            [[]]
        ]

    def addToLevel(self, posX, posY, layer: int, add):
        if layer > 3 or layer < 1:
            print("layer invalid", layer)
            return 1
        levelPos = [posX//self.chunkSize[0], posY//self.chunkSize[1]]
        self.Level[layer][levelPos[0]][levelPos[1]].append(add)
        return 0


    def setUpLevel(self, screenSize):
        surfaceFloor = pygame.image.load(self.BackroundLevel[0])
        surfaceWall = pygame.image.load(self.BackroundLevel[1])
        #Self.Level
        for y in range(0, int(self.LevelPixelSize[1]/self.BackroundLevelPartSize[1])):
            for x in range(0, int(self.LevelPixelSize[0]/self.BackroundLevelPartSize[0])):
                pos = [x*self.BackroundLevelPartSize[0], y*self.BackroundLevelPartSize[1]]
                if self.JsonLevel[y][x] == 0:
                    continue
                if self.JsonLevel[y][x] == 1:
                    self.map[0].blit(surfaceFloor, pos)
                if self.JsonLevel[y][x] == 2:
                    self.map[0].blit(surfaceWall, pos)
        #Adds doors

        for y in range(0, int(self.LevelPixelSize[1]/self.chunkSize[1])):
            self.Level.append([])
            for x in range(0, int(self.LevelPixelSize[0]/self.chunkSize[0])):
                self.Level[y].append([
                    [],                                                                                                                                   #Layer 0 Backround
                    [],                                                                                                                                   #Layer 1
                    [],                                                                                                                                   #Layer 2
                    []                                                                                                                                    #Layer 3 Above player
                    ])

        for door in self.doors:
            self.addToLevel(door.vec2.pos[0], door.vec2.pos[1], door.layer, door)
        
        
        #LoadedChunks
        left = 0
        right = int((screenSize[0] + (4*self.chunkSize[0])) / self.chunkSize[0])
        top = 0
        bottom = int((screenSize[1] + (4*self.chunkSize[1])) / self.chunkSize[1])
        chunkY = 0
        for y in range(top, bottom):
            chunkX = 0
            self.loadedChunks.append([])
            for x in range(left, right):
                self.loadedChunks[chunkY].append(self.Level[y][x])
                chunkX += 1
            chunkY +=1
        self.JsonLevel = []
        return 0
    

        


    def draw(self, screen, shift:list):
        screen.blit(self.map[0], (-shift[0], -shift[1]))
        surfaceFloor = pygame.image.load(self.BackroundLevel[0])
        surfaceWall = pygame.image.load(self.BackroundLevel[1])
        for layer in range(1, 3):
            for y in range(0, len(self.loadedChunks)):
                for x in range(0, len(self.loadedChunks[y])):
                    for part in self.loadedChunks[y][x][layer]:
                        if type(part) == list:
                            for loadedY in range(0, len(part)):
                                for loadedX in range(0, len(part[loadedY])):

                                    if type(part[loadedY][loadedX]) == int:
                                        pos = [self.loadedChunksPos[0]+((x)*self.chunkSize[0])+(loadedX*32)-shift[0], self.loadedChunksPos[1]+((y)*self.chunkSize[1])+(loadedY*32)-shift[1]]
                                             
                                        if part[loadedY][loadedX] == 0:
                                            continue
                                        if part[loadedY][loadedX] == 1:
                                            screen.blit(surfaceFloor, pos)

                                        if part[loadedY][loadedX] == 2:
                                            screen.blit(surfaceWall, pos)
                        else:
                            part.draw(screen, shift)
        return 0
    def collion(self, player):
        player.vec2.pos[0]// 32
    def drawAbovePlayer(self, screen, shift:list):
        surfaceFloor = pygame.image.load(self.BackroundLevel[0])
        surfaceWall = pygame.image.load(self.BackroundLevel[1])
        for layer in range(3, 4):
            for y in range(0, len(self.loadedChunks)):
                for x in range(0, len(self.loadedChunks[y])):
                    for part in self.loadedChunks[y][x][layer]:
                        if type(part) == list:
                            for loadedY in range(0, len(part)):
                                for loadedX in range(0, len(part[loadedY])):

                                    if type(part[loadedY][loadedX]) == int:
                                        if part[loadedY][loadedX] == 0:
                                            continue
                                        if part[loadedY][loadedX] == 1:
                                            pos = [self.loadedChunksPos[0]+((x)*self.chunkSize[0])+(loadedX*32)-shift[0], self.loadedChunksPos[1]+((y)*self.chunkSize[1])+(loadedY*32)-shift[1]]
                                            if pos[0]<0:
                                                pos[0]=0
                                            if pos[1]<0:
                                                pos[1]=0
                                            screen.blit(surfaceFloor, pos)

                                        if part[loadedY][loadedX] == 2:
                                            pos = [self.loadedChunksPos[0]+((x)*self.chunkSize[0])+(loadedX*32)-shift[0], self.loadedChunksPos[1]+((y)*self.chunkSize[1])+(loadedY*32)-shift[1]]

                                            screen.blit(surfaceWall, pos)
                        else:
                            part.draw(screen, shift)
        return 0
    def getCloseLevelparts(self, camera, screenSize):
        cameraPos = [(camera.vec2.pos[0] - (screenSize[0] / 2)), (camera.vec2.pos[1] - (screenSize[1] / 2))]

        left = int((cameraPos[0] - 1*self.chunkSize[0]) // self.chunkSize[0])
        right = int((screenSize[0] + (2*self.chunkSize[0]) + cameraPos[0]) // self.chunkSize[0])
        top = int((cameraPos[1] - 1*self.chunkSize[1]) // self.chunkSize[1])
        bottom = int((screenSize[1] + (2*self.chunkSize[1]) + cameraPos[1]) // self.chunkSize[1])
        self.loadedChunksPos = [left*self.chunkSize[0], top*self.chunkSize[1]]
        chunkY = 0
        for y in range(top, bottom):
            chunkX = 0
            for x in range(left, right):
                try:
                    if self.loadedChunks[chunkY][chunkX] != self.Level[y][x]:
                        self.loadedChunks[chunkY][chunkX] = self.Level[y][x]
                except:
                    IndexError
                chunkX += 1
            chunkY +=1
        return 0