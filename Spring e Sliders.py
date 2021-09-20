springLength = 0.05    # meters 
springStiffness = 20   # Newtons per meter
spring = helix( pos = vec(0, 0, 0), axis = -vec(0, 2*springLength, 0))
spring.radius = 0.008
spring.coils = 15

table = box( pos = vec(0,0,0), size = vec(0.2, 0.02, 0.1), color = color.red)
floor = box( pos = vec(0, -5*springLength, 0), size = vec(0.3, 0.01, 0.2))
floor.opacity = 0.4

bobMass = 0.20            
gravField = 10             
velocity = vec(0,0,0)   
bob = cylinder(color = color.yellow) 
bob.pos = spring.pos + spring.axis
bob.axis = vec(0, 0.02, 0)
bob.radius = 0.02

t = 0        
dt = 0.01   

scene.center = bob.pos   

while(True):

    rate(1/dt)        
    t = t + dt  

    # calculate forces acting on weight
    forceOfGravity = vec( 0, -bobMass * gravField, 0)  
    springForce = -springStiffness * (bob.pos - springLength * bob.pos.norm())  
    netForce = springForce + forceOfGravity            

    # adjust velocity and position using Newton's 2nd Law & kinematics
    velocity = velocity + (netForce / bobMass) * dt    
    bob.pos = bob.pos + velocity * dt      

    # reset the spring stretch visibly 
    spring.axis = bob.pos   

    # set the angle of the bob appropriately
    bob.axis = bob.axis.mag * (spring.pos - bob.pos).norm()