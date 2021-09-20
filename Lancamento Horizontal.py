from vpython import *
grav = vector(0,-10,0)
solo = box(pos = vector(0,0,0), size = vector(55,0.5,15), texture=textures.wood_old)
caixa = box(pos = vector(-25,4,0), size = vector(25,8.6,15), texture=textures.wood_old)
bol = sphere(pos = vector(-9,9,0), radius = 0.5, color = color.orange)

t = 0
dt = 0.001
FRAME = 1/dt
bol.velocity = vector(20,0,0)

while True:
    rate(FRAME)

    #x = bol.pos.x + bol.velocity * t
    bol.pos += bol.velocity * dt
    #y = bol.velocity.y - (1/2)*grav * (dt*dt)
    bol.velocity += grav * dt
    bol.velocity += vector(0.01,0,0)


    t+=dt
    print('gravidade', grav)
    print('gravidadedt', gravdt)
    print('Velocidade da bola= ', bol.velocity)
    print('tempo= ', t)
    if (bol.pos.y <= solo.pos.y - (bol.radius + solo.size.y/2.0)
       or bol.pos.y <= solo.pos.y + (bol.radius + solo.size.y/2.0)):
        print ('a velocidade em funcao do tempo e: ', bol.velocity.x*t)
        break