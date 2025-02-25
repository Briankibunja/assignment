# area of circle triangle and rectangle and perimeters
print("choose option 1 ,2 or 3")
print("1.Area and circumference of a circle")
print("2.Area and perimeter of a triangle")
print("3.Area and perimeter of a rectangle ")
choice=int(input("Choose one among the choices : "))

from math import pi
if choice==1:
        radius= float(input("Enter radius of the circle: "))
        area=float(pi*radius*radius)
        circumference= float(2*pi*radius)
        print("area of circle ",area)
        print("circumference of circle" ,circumference)
elif choice==2:
        base=float(input("enter the base: "))
        height= float( input("enter the height: "))
        hypotenuse=float(input("enter the hypotenuse : "))
        area= float(base*height*0.5)
        perimeter= float(base+height+hypotenuse)
        print("area of triangle " ,area)
        print("perimeter of triangle " ,perimeter)
elif choice==3:
        length=float(input("Enter the length : "))
        width=float(input("enter the width : "))
        area= float (length*width)
        perimeter=float(length*2 + width*2)
        print("area of rectangle ",area )
        print("perimeter of rectangle" ,perimeter)

else:
     print("invalid opton select option 1 or 2")
