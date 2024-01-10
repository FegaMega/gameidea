import vector2
def pointCollision(Ax, Ay, Bx, By, Bwidth, Bheight):
    return (Ax >= Bx and Ax <= Bx + Bwidth) and (Ay >= By and Ay <= Ay <= By + Bheight)
    
def rectCollision(Ax, Ay, Awidth, Aheight, Bx, By, Bwidth, Bheight):
    return (Ax + Awidth > Bx) and (Ax < Bx + Bwidth) and (Ay + Aheight > By) and (Ay < By + Bheight)

def lineCollision(Alines, Bx, By, Bwidth, Bheight):
    for line in Alines:
        if rectCollision(line[0], line[1], line[2], line[3], Bx, By, Bwidth, Bheight):
            return line[4]
def collideVelx(obj1, obj2):
    vandm = (obj1.vec2.vel[0] * obj1.weight) - (obj2.vec2.vel[0] * obj2.weight)
    m = obj1.weight + obj2.weight
    obj2.vec2.vel[0] = vandm / m
    obj1.vec2.vel[0] = vandm / m
def collideVely(obj1, obj2):
    vandm = (obj1.vec2.vel[0] * obj1.weight) - (obj2.vec2.vel[0] * obj2.weight)
    m = obj1.weight + obj2.weight
    obj2.vec2.vel[0] = vandm / m
    obj1.vec2.vel[0] = vandm / m
def collideVel(obj1, obj2):
    vandm = vector2.Vec2sub(vector2.Intmul(obj1.vec2.vel, obj1.weight), vector2.Intmul(obj2.vec2.vel, obj2.weight))
    m = obj1.weight + obj2.weight
    obj2.vec2.vel = vector2.Intdiv(vandm, m)
    obj1.vec2.vel = vector2.Intdiv(vandm, m)

def cubePlayerCollision(player, cube):
    rightOfPlayer = player.vec2.pos[0]+player.size[0]
    bottomOfPlayer = player.vec2.pos[1]+player.size[1]
    rightOfCube = cube.vec2.pos[0] + cube.size[0]
    bottomOfCube = cube.vec2.pos[1] + cube.size[1]

    playerPushingcuberight = rightOfPlayer < cube.vec2.pos[0]+(cube.size[0]/2) and player.vec2.vel[0] > cube.vec2.vel[0]
    playerPushingcubeleft = player.vec2.pos[0] > cube.vec2.pos[0]+(cube.size[0]/2) and player.vec2.vel[0] < cube.vec2.vel[0]
    playerPushingcubedown = bottomOfPlayer < cube.vec2.pos[1]+(cube.size[1]/2) and player.vec2.vel[1] > cube.vec2.vel[1]
    playerPushingcubeup = player.vec2.pos[1] > cube.vec2.pos[1]+(cube.size[1]/2) and player.vec2.vel[1] < cube.vec2.vel[1]
    
    
    
    cubePushingplayerright = rightOfCube < player.vec2.pos[0]+(player.size[0]/2) and cube.vec2.vel[0] > player.vec2.vel[0]
    cubePushingplayerleft = cube.vec2.pos[0] > player.vec2.pos[0]+(player.size[0]/2) and cube.vec2.vel[0] < player.vec2.vel[0]
    cubePushingplayerup = cube.vec2.pos[1] > player.vec2.pos[1]+(player.size[1]/2) and cube.vec2.vel[1] < player.vec2.vel[1]
    cubePushingplayerdown = bottomOfCube < player.vec2.pos[1]+(player.size[1]/2) and cube.vec2.vel[1] > player.vec2.vel[1]
    
    if rectCollision(player.vec2.pos[0], player.vec2.pos[1], player.size[0], player.size[1], cube.vec2.pos[0], cube.vec2.pos[1], cube.size[0], cube.size[1]):
        if playerPushingcubeleft or playerPushingcuberight or cubePushingplayerright or cubePushingplayerleft:
            for hit in cube.hit:
                if hit == player:
                    playerhit = True
            if playerhit == False:
                collideVelx(player, cube)
                cube.hit.append(player)
            else:
                cube.vec2.vel[0] = player.vec2.vel[0]
        if playerPushingcubeup or playerPushingcubedown or cubePushingplayerdown or cubePushingplayerup:
            for hit in cube.hit:
                if hit == player:
                    playerhit = True
            if playerhit == False:
                collideVely(player, cube)
                cube.hit.append(player)
            else:
                cube.vec2.vel[1] = player.vec2.vel[1]
    else:
        cube.hit = False