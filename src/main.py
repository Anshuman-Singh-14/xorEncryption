import encrypt as e


def main():

    message = input("Enter a message to encrypt: ").strip()

    key = input("Enter upto to a 5 digit key (or press Enter to generate a random key): ").strip()

    if key == "":
        key = 0
    else:
        key = int(key)

    encrypted_message, final_key = e.encrypt(message, key)
    print("Encrypted message:", encrypted_message, sep = "\n\n")
    print("Key used:", final_key)


    m2 = input("Enter a message to decrypt: ").strip()
    k2 = int(input("Enter the key used to encrypt the message: "))
    decrypted_message, _ = e.encrypt(m2, k2)
    print("Decrypted message:", decrypted_message, sep = "\n\n")

main()