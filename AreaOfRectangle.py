print("Welcome, To find the area of the rectangle fill the following info:")
while True:
    try:
        #input for lenght
        #errors for lenght
        lenght = float(input("lenght: "))
        if lenght > 0:
            break
        print(f"Invaild input, The lenght you entered is "+lenght)
    except Exception as e:
            print(e)
while True:
    try:
        #input for width
        #errors fow width
        width = float(input("width: "))
        if width > 0:
            break
        print(f"Invaild input, The width you entered is "+width)
    except Exception as e:
            print(e)
area = lenght * width #formula of area of rectangle
print("The area of rectangle is: %.2f" %area)
