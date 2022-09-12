# Caesar Cipher is a program that takes a user input and encrypts it by shifting its position in the alphabet. The program then outputs the encrypted text to the user. 

#Create list to hold alphabet, alphabet is listed twice to prevent error for large shifts in position
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Create function with statements to run through each character of the user input, encrypt the alphabet characters only, then provide the output.
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

#While loop to prompt the user to continue if they want to keep encrypting or decoding other text
should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt,  type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  
  result = input("Type 'yes' if you want to continue. Otherwise, type 'no'.\n")
  if result == "no":
    should_continue = False
    print("Goodbye")
    

