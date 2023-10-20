#   a212_rsa_encrypt.py
import rsa as rsa

#user inputs the values
key = input("Enter the Encryption Key: " )
mod_value = input("Enter the Modulus: " )

#this is executed if there aren't only integers 
while key.isdigit() and mod_value.isdigit() is False:
  print("not valid")
  key = input("Enter the Encryption Key: " )
  mod_value = input("Enter the Modulus: " )

#this executes if there are only integers
plaintext = input("Enter a message to encrypt: ")
encrypted_msg = rsa.encrypt(int(key), int(mod_value), plaintext)
print("Encrypted Message:", encrypted_msg)

#varible.isalpha() functions the same way as variable.isdigit,
#except isalpha measures if there are only letters present





'''
#orig
x=1
while x>0:
  key = input("Enter the Encryption Key: " )
  mod_value = input("Enter the Modulus: " )

  if key.isdigit() and mod_value.isdigit() is True:
    plaintext = input("Enter a message to encrypt: ")
    encrypted_msg = rsa.encrypt(int(key), int(mod_value), plaintext)
    print("Encrypted Message:", encrypted_msg)
    x = -1

  if key.isalpha() and mod_value.isalpha is True:
    print("Please type only numbers, NOT letters!")
    x = 1
    
  else: 
    print("Please insert only integers")
    x = 1
'''

'''
#Generalized
import rsa as rsa
x=1
while x>0:
  value1 = input("Enter value 1: " )
  value2 = input("Enter value 2: " )

  if value1.isdigit() and value2.isdigit() is True:
    value1 = int(value1)
    value2 = int(value2)
    #execute integer command:
    x = -1
  if value1.isalpha() and value2.isalpha() is True:
    #execute alphabet command:
    x = -1
  else: 
    print("If you want integer command to execute, please insert only integer values (numbers)")
    print("If you want alphabet command to execute, please insert only alpha values (letters)")
    x = 1
'''