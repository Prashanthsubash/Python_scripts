number = input("Enter a 5-digit decimal number: ")

if len(number) == 5 and number.isdigit():
    reversed_number = ""
    for digit in number:
        reversed_number = digit + reversed_number
    print(f"The reverse number is: {reversed_number}")
else:
    print("Error, Please enter valid 5 digit number")
 