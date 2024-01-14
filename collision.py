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
    vandm = (obj1.vec2.vel[1] * obj1.weight) - (obj2.vec2.vel[1] * obj2.weight)
    m = obj1.weight + obj2.weight
    obj2.vec2.vel[1] = vandm / m
    obj1.vec2.vel[1] = vandm / m
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

            if cube.playerHit == False:
                collideVelx(player, cube)
                cube.playerHit = True
            else:
                cube.vec2.vel[0] = player.vec2.vel[0]
        if playerPushingcubeup or playerPushingcubedown or cubePushingplayerdown or cubePushingplayerup:
            if cube.playerHit == False:
                collideVely(player, cube)
                cube.playerHit = True
            else:
                cube.vec2.vel[1] = player.vec2.vel[1]
    else:
        i = 0
        cube.playerHit = False


def cubeCubeCollision(cube, cube2):
    rightOfCube2 = cube2.vec2.pos[0]+cube2.size[0]
    bottomOfCube2 = cube2.vec2.pos[1]+cube2.size[1]
    rightOfCube = cube.vec2.pos[0] + cube.size[0]
    bottomOfCube = cube.vec2.pos[1] + cube.size[1]

    cube2Pushingcuberight = rightOfCube2 < cube.vec2.pos[0]+(cube.size[0]/2) and cube2.vec2.vel[0] > cube.vec2.vel[0]
    cube2Pushingcubeleft = cube2.vec2.pos[0] > cube.vec2.pos[0]+(cube.size[0]/2) and cube2.vec2.vel[0] < cube.vec2.vel[0]
    cube2Pushingcubedown = bottomOfCube2 < cube.vec2.pos[1]+(cube.size[1]/2) and cube2.vec2.vel[1] > cube.vec2.vel[1]
    cube2Pushingcubeup = cube2.vec2.pos[1] > cube.vec2.pos[1]+(cube.size[1]/2) and cube2.vec2.vel[1] < cube.vec2.vel[1]
    
    
    
    cubePushingcube2right = rightOfCube < cube2.vec2.pos[0]+(cube2.size[0]/2) and cube.vec2.vel[0] > cube2.vec2.vel[0]
    cubePushingcube2left = cube.vec2.pos[0] > cube2.vec2.pos[0]+(cube2.size[0]/2) and cube.vec2.vel[0] < cube2.vec2.vel[0]
    cubePushingcube2up = cube.vec2.pos[1] > cube2.vec2.pos[1]+(cube2.size[1]/2) and cube.vec2.vel[1] < cube2.vec2.vel[1]
    cubePushingcube2down = bottomOfCube < cube2.vec2.pos[1]+(cube2.size[1]/2) and cube.vec2.vel[1] > cube2.vec2.vel[1]
    

    cubehit = False

    if rectCollision(cube2.vec2.pos[0], cube2.vec2.pos[1], cube2.size[0], cube2.size[1], cube.vec2.pos[0], cube.vec2.pos[1], cube.size[0], cube.size[1]):
        if cube2Pushingcubeleft or cube2Pushingcuberight or cubePushingcube2right or cubePushingcube2left:
            for hit in cube.hit:
                if hit == cube2:
                    cubehit = True
            for hit in cube.hit:
                if hit == cube2:
                    cubehit = True
            if cubehit == False:
                collideVelx(cube2, cube)
                cube.hit.append(cube2)
                cube2.hit.append(cube)
            elif cube.vec2.vel[0] < 0 and cube2.vec2.vel[0] < 0 or cube2.vec2.vel[0] > 0 and cube.vec2.vel[0] > 0:
                if cube2Pushingcuberight or cube2Pushingcubeleft:
                    cube.vec2.vel[0] = cube2.vec2.vel[0]
                elif cubePushingcube2right or cubePushingcube2left:
                    cube2.vec2.vel[0] = cube.vec2.vel[0]
        if cube2Pushingcubeup or cube2Pushingcubedown or cubePushingcube2down or cubePushingcube2up:
            for hit in cube.hit:
                if hit == cube2:
                    cubehit = True
            for hit in cube.hit:
                if hit == cube2:
                    cubehit = True
            if cubehit == False:
                collideVely(cube2, cube)
                cube.hit.append(cube2)
                cube2.hit.append(cube)
            elif cube.vec2.vel[1] < 0.1 and cube2.vec2.vel[1] < 0.1 or cube2.vec2.vel[1] > -0.1 and cube.vec2.vel[1] > -0.1:
                if cube2Pushingcubedown or cube2Pushingcubeup:
                    cube.vec2.vel[1] = cube2.vec2.vel[1]
                elif cubePushingcube2down or cubePushingcube2up:
                    cube2.vec2.vel[1] = cube.vec2.vel[1]
    else:
        i = 0
        for hit in cube.hit:
            if hit == cube2:
                del cube.hit[i]
            i +=1
        i = 0
        for hit in cube2.hit:
            if hit == cube:
                del cube2.hit[i]
            i +=1
        print(cube2.hit, cube.hit)