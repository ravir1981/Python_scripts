def get_average():
    with open("Files/temperature.txt", 'r') as file:
        temp = file.readlines()

    temp = temp[1:]
    temp = [float(number) for number in temp]
    average_local = sum(temp) / len(temp)
    return average_local


average = get_average()
print("Average is ", average)
