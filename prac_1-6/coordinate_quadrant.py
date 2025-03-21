x = int(input("Enter x-coordinate: "))
y = int(input("Enter y-coordinate: "))

if x > 0 and y > 0:
    print("The point is in Quadrant I.")
elif x < 0 and y > 0:
    print("The point is in Quadrant II.")
elif x < 0 and y < 0:
    print("The point is in Quadrant III.")
elif x > 0 and y < 0:
    print("The point is in Quadrant IV.")
elif x == 0 and y != 0:
    print("The point is on the Y-axis.")
elif y == 0 and x != 0:
    print("The point is on the X-axis.")
else:
    print("The point is at the origin.")
