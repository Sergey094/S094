def is_valid_number(n):
    for digit in str(n):
        if int(digit) % 2 != 0:
            print("Not valid")
            return
    print("Valid")

number = int(input())
is_valid_number(number)
