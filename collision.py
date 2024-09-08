import vector2, Objects
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

