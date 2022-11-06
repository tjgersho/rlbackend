
from app.models import Position, Velocity, Acceleration

def calculateVelocity(pos1, pos2):
    vel = Velocity()
    deltaT = (pos2.created-pos1.created)
    vel.Vx = (pos2.X - pos1.X) / (deltaT)
    vel.Vy = (pos2.Y - pos1.Y) / (deltaT)
    vel.Vz = (pos2.Z - pos1.Z) / (deltaT)
    vel.created = pos2.created
    vel.rocket = pos2.rocket
    return vel

def calculateAcceleration(vel1, vel2):
    accel = Acceleration()
    deltaT = (vel2.created-vel1.created)
    accel.Ax = (vel2.Vx - vel1.Vx) / (deltaT)
    accel.Ay = (vel2.Vy - vel1.Vy) / (deltaT)
    accel.Az = (vel2.Vz - vel1.Vz) / (deltaT)
    accel.created = vel2.created
    accel.rocket = vel2.rocket
    return accel
