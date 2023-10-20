#   a212_rsa_encrypt.py
import rsa as rsa

x=1
while x>0:
  key = input("Enter the Encryption Key: " )
  mod_value = input("Enter the Modulus: " )

  if key.isdigit() and mod_value.isdigit() is True:
    plaintext = input("Enter a message to encrypt: ")
    encrypted_msg = rsa.encrypt(int(key), int(mod_value), plaintext)
    print("Encrypted Message:", encrypted_msg)
    x = -1
  else: 
    print("Please insert only integers")
    x = 1
