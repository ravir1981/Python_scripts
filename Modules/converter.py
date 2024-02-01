def convert_meter(feet, inch):
    meter_local = feet * 0.3048 + inch * 0.0254
    return meter_local


print(__name__)
if __name__ == "__main__":
    print(convert_meter(3, 5))
    print(__name__)