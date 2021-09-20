from vpython import*

carro = box(pos=vector(0,0,0), size = vector(3,0.5,1), color = color.yellow)

solo = box(pos=vector(0,-0.3,0), size = vector(30,0.1,10), color = color.blue)

t = 2
t0 = 0

dt = 0.01

FRAME= 1/dt

carro.velocity1 = vector(6,0,0)
carro.velocity0 = vector (0,0,0)
carro.acel1 = vector(1,0,0)
carro.pos0 = vector(0,0,0)


while (t < 6):
    
	rate(FRAME)

	#carro.pos += carro.velocity * dt
	#carro.acel = carro.velocity/dt

	#a=(vf-vi)/(tf-ti)
	carro.acel = ((carro.velocity1 - carro.velocity0)/(t-t0))

	#v=vi + a*t
	carro.velocity = carro.velocity0 + carro.acel1 * t

	#S= pi + vi*t + ((a*(t*t)/2)
	carro.pos = carro.pos0 + carro.velocity0 * t + (carro.acel1 * (t * t)) / 2

	print ("Posição do Carro:", carro.pos)

	print ("Acelaração do Carro:", carro.acel)

	print ("Velocidade do Carro:", carro.velocity)

	print ("Tempo:", t," \n")

	t=t+dt
