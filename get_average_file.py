def get_average(file_name):
    with open(file_name, 'r') as file:
        temp = file.readlines()

    temp = temp[1:]
    temp = [float(number) for number in temp]
    average_local = sum(temp) / len(temp)
    return average_local


filename = "Files/temperature.txt"
average = get_average(filename)
print("Average is ", average)
