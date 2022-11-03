
from app.models import Position, Velocity, Acceleration

def calculateVelocity(pos1, pos2):
    print(pos1.X)
    print(pos2.X)
    vel = Velocity()
    deltaT = (pos2.created-pos1.created).total_seconds()
    print("Delta T")
    print(deltaT)

    vel.Vx = (pos2.X - pos1.X) / (deltaT)
    print(vel)
    return vel


