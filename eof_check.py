try:
    value = "Enter:"
    n = int(input(value))
    print(n * 10)
except ValueError:
    print('That is an invalid specification.')
except EOFError as e:
    print("Print the error :", e)
