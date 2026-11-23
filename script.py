import os
from art import logo, logo1
from morse_code_dict import morse_code_dict


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def morse_code_tx():
    print(logo1)
    msg = list(input("Enter text: ").upper())
    morse_code = " "
    for n in msg:
        if n in morse_code_dict:
            morse_code += morse_code_dict[n] + ' '
        elif n == ' ':
            morse_code += '/ '
        else:
            morse_code += "  "

    print(f'Text in Morse Code = {morse_code}')

while True:
    morse_code_tx()

    if input("Continue? Enter '/end' to exit. Anything else to continue. ") == '/end':
        break
    if input("Clear screen? Enter Y for 'Yes' and N for 'No': ").upper() == "Y":
        clear()

print("Goodbye!")

