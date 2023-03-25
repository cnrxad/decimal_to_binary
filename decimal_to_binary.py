def binary(decimal):
    binary = ""
    while decimal // 2 != 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return str(decimal) + binary

number = int(input("Enter the number you want to translate to binary: "))
print(binary(number))
