
from app.models import Position, Velocity, Acceleration

def calculateVelocity(pos1, pos2):
    print(pos1.X)
    print(pos2.X)
    vel = Velocity()
    print(pos2.created)
    print(pos1.created)
    deltaT = (pos2.created-pos1.created) / 1000
    print("Delta T")
    print(deltaT)

    vel.Vx = (pos2.X - pos1.X) / (deltaT)
    vel.Vy = (pos2.Y - pos1.Y) / (deltaT)
    vel.Vz = (pos2.Z - pos1.Z) / (deltaT)
    print(vel)
    return vel


