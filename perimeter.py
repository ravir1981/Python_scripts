try:
    length = float(input("Enter the Length:"))
    width = float(input("Enter the width:"))

    if length == width:
        exit("This calculation will yield square. We want rectangle")

    perimeter = (length + width) * 2
    area = length * width

    print(f"Perimeter value is {perimeter} and total area is {area}")
except (RuntimeError, TypeError, NameError, ValueError):
    print("Enter numerical value.")
finally:
    print("Program Completed")