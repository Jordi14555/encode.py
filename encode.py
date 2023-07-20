#Jordania Jones
#encoding password function, adding 3 to each digit in password and printing out new one
def encoded_password(password):
    encoded_password = ""
    for digit in password:
        new_digit = str((int(digit) + 3) % 10)
        encoded_password += new_digit
    return encoded_password


def decode_pass(password):
    decoded_password = ""
    for digit in password:
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit
    return decoded_password


while True:
    print('Menu \n1. Encode\n2. Decode\n3. Quit')
    option = input("Please enter an option:")

    if option == '1':
        password = input("Please enter your password to encode:")
        encoded_password = encoded_password(password)
        print("Your password has been encoded and stored!")
    elif option == "2":
        if not encoded_password:
            print("Please encode a password first.")
        else:
            print(f"The encoded password is {encoded_password}, and the original password is {decode_pass(encoded_password)}.")
    elif option == "3":
        break
    else:
        print("Invalid option. Please try again.")
