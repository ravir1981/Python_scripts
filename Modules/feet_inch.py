def get_feet_inch(feet_inch):
    feet, inch = feet_inch.split()
    feet = float(feet)
    inch = float(inch)
    return {"feet": feet, "inch": inch}
