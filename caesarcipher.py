def caesar_cipher(text, shift, mode='encrypt'):
        
    result = ''
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
        elif char.isdigit():
            shifted_char = str((int(char) + shift) % 10)
        else:
            shifted_char = char
        result += shifted_char    
    
    return result
# Getting the user input
text = input("Enter the text to encrypt(en)/decrypt(denc): ")
shift = int(input("Enter the  value (1-25): "))
mode = input("Enter mode ('encrypt' or 'decrypt'): ").lower()

# Performing encryption/decryption
result = caesar_cipher(text, shift, mode)

# Printing  the result

print("Result:", result)