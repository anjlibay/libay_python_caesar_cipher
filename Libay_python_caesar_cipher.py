letters = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if not letter == ' ' :
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = (index + key) % 26  
                ciphertext += letters[new_index]
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        if not letter == ' ' :
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = (index - key) % 26  
                plaintext += letters[new_index]
    return plaintext

while True:
    print()
    print('*** CAESAR CIPHER PROGRAM ***')
    print()

    print('Do you want to encrypt or decrypt? (Type "e" for encrypt, "d" for decrypt, or "exit" to quit)')
    user_input = input('e/d/exit: ').lower()
    print()

    if user_input == 'exit':
        print('Exiting the program...')
        break
    elif user_input == 'e':
        print('ENCRYPTION MODE SELECTED')
        print()
        key = int(input('Enter the key (1 through 26): '))
        text = input('Enter the text to encrypt: ')
        ciphertext = encrypt(text, key)
        print(f'CIPHERTEXT: {ciphertext}')
    elif user_input == 'd':
        print('DECRYPTION MODE SELECTED')
        print()
        key = int(input('Enter the key (1 through 26): '))
        text = input('Enter the text to decrypt: ')
        plaintext = decrypt(text, key)
        print(f'PLAINTEXT: {plaintext}')
    else:
        print('Invalid input. Please type "e" for encrypt, "d" for decrypt, or "exit" to quit.')
