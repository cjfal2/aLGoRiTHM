def vigenere_encrypt(key, plaintext):
    ciphertext = []
    key_len = len(key)
    
    for i in range(len(plaintext)):
        p = ord(plaintext[i]) - ord('A')
        k = ord(key[i % key_len]) - ord('A') + 1
        c = (p + k) % 26
        ciphertext.append(chr(c + ord('A')))
    
    return ''.join(ciphertext)

def main():
    while True:
        key = input().strip()
        if key == "0":
            break
        plaintext = input().strip()
        print(vigenere_encrypt(key, plaintext))

if __name__ == "__main__":
    main()
