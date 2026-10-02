def circle(radius):
    circumference = 2 * 3.14 * radius
    area = 3.14 * radius ** 2
    return circumference, area
c,a = circle(3)
print("Circumference:",c,"Area:",a)