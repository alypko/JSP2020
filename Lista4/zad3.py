from math import pi
def convert(deg="None", rad = "None"):
    if deg is not None:
        return deg * pi/180
    else: 
        return rad * 180/pi

print(convert(30, 0.52))