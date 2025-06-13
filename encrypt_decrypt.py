def caesar_cipher(text, shift):
    """
    Encrypts or decrypts text using the Caesar cipher.

    Args:
        text: The text to encrypt/decrypt.
        shift: The shift value (positive for encryption, negative for decryption).

    Returns:
        The encrypted or decrypted text.
    """
    result = ''
    for char in text:
        if 'a' <= char <= 'z':
            start = 'a'
        elif 'A' <= char <= 'Z':
            start = 'A'
        else:
            result += char  # Don't encrypt non-alphabetic characters
            continue

        shifted_char = chr(((ord(char) - ord(start) + shift) % 26) + ord(start))
        result += shifted_char
    return result


def xor_cipher(text, key):
    """
    Encrypts or decrypts text using XOR encryption.

    Args:
        text: The text to encrypt/decrypt.
        key: The secret key (string).

    Returns:
        The encrypted or decrypted text.
    """
    key_len = len(key)
    key_index = 0
    result = ''
    for char in text:
        key_char = key[key_index % key_len]
        # XOR-ing the character code with the key character's code.
        # chr() converts the integer (the result of XOR) back to a character.
        shifted_char = chr(ord(char) ^ ord(key_char))
        result += shifted_char
        key_index += 1
    return result


def main():
    """
    The main function for the cipher/decipher program.
    """
    print("Welcome to the Cipher/Decipher Program!")

    while True:
        action = input("Choose an action (e - encrypt, d - decrypt, q - quit): ").lower()

        if action == 'q':
            print("Goodbye!")
            break
        elif action == 'e' or action == 'd':
            algorithm = input("Choose an algorithm (c - Caesar, x - XOR): ").lower()
            if algorithm == 'c':
                text = input("Enter the message: ")
                try:
                    shift = int(input("Enter the shift (integer): "))
                except ValueError:
                    print("Invalid shift input. Please enter an integer.")
                    continue

                if action == 'e':
                    encrypted_text = caesar_cipher(text, shift)
                    print("Encrypted message:", encrypted_text)
                else:
                    decrypted_text = caesar_cipher(text, -shift)  # Reverse shift for decryption
                    print("Decrypted message:", decrypted_text)

            elif algorithm == 'x':
                text = input("Enter the message: ")
                key = input("Enter the secret key: ")
                if action == 'e':
                    encrypted_text = xor_cipher(text, key)
                    print("Encrypted message:", encrypted_text)
                else:
                    decrypted_text = xor_cipher(text, key)  # XOR encryption - symmetric, uses same key
                    print("Decrypted message:", decrypted_text)
            else:
                print("Invalid algorithm choice.")
        else:
            print("Invalid action choice.")


if __name__ == "__main__":
    main()