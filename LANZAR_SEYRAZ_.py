import math

point_x1 = float(input("enter x1: "))
point_x2 = float(input("enter x2: "))
point_y1 = float(input("enter y1: "))
point_y2 = float(input("enter y2: "))
#asks to input values for calculation

point_x = point_x2 - point_x1
point_y = point_y2 - point_y1
#calculates values

point_xy = pow(point_x, 2) + pow(point_y,2)
#using calculated values to calculate for the distance

distance = math.sqrt(point_xy)
print("the distance is ", distance)
#tells you the final distance value
