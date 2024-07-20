from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(StartText, shiftAmount, cipherDirection):
    endText = ""
    if cipherDirection == "decode":
        shiftAmount *= -1
    for char in StartText:
        if char in alphabet:
            position = alphabet.index(char)
            #Always return a number in the range of the alphabet
            newPosition = (position + shiftAmount) % len(alphabet)
            newLetter = alphabet[newPosition]
            endText += newLetter
        else:
            endText += char
    print(f"The {cipherDirection}d text is {endText}\n")

shouldContinue = True
while shouldContinue:
    direction = ""
    while direction not in ("encode", "decode"):
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    if not restart == "yes":
        shouldContinue = False
        print("Goodbye")


# def encrypt(plainText, shiftAmount):
#     encryptedText = ""
#     for char in plainText:
#         if char in alphabet:
#             position = alphabet.index(char)
#             newPosition = (position + shiftAmount) % len(alphabet)
#             newLetter = alphabet[newPosition]
#             encryptedText += newLetter
#         else:
#             encryptedText += char
#     print(f"The encoded text is {encryptedText}")

# def decrypt(encryptedText, shiftAmount):
#     decryptedText = ""
#     for char in encryptedText:
#         if char in alphabet:
#             position = alphabet.index(char)
#             newPosition = (position - shiftAmount) % len(alphabet)
#             newLetter = alphabet[newPosition]
#             decryptedText += newLetter
#         else:
#             decryptedText += char
#     print(f"The decoded text is {decryptedText}")

# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)