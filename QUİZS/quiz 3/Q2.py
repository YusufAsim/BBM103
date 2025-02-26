import math
b = int(input("please enter a number:"))
c = int(input("please enter a number:"))
delta = (b**2 - 4*c)
if delta > 0:
    x = (-b + math.sqrt(delta)) / 2
    y = (-b - math.sqrt(delta)) / 2
    print("This equation has two different roots.\nFirst root is {} and second root is {}.".format(x, y))
elif delta == 0:
    x = (-b + math.sqrt(delta)) / 2
    print("This equation has two same roots.\nBoth of roots equal to {}".format(x))
else:
    print("This equation has no reel root")

