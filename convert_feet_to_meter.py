from Modules.converter import convert_meter
from Modules.feet_inch import get_feet_inch

feet_inch = input("Enter feet and inch:")

feet_inch = get_feet_inch(feet_inch)
meter = convert_meter(feet_inch['feet'], feet_inch['inch'])
print(f"{feet_inch['feet']} feet and {feet_inch['inch']} inches is equal to {meter} meter.")

if meter > 1:
    print(f"{meter} height is eligible for ride")
else:
    print(f"{meter} height is not eligible for ride")
