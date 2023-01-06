import os
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
length_of_alphabet = len(alphabet)

#Ceaser function which takes the text and shift each letter of the text by the given shift amount and the cipher_direction indicates whether you want to encode or decode the text.

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  #for decoding, we substruct the shift amount from the letter's position. given rule is followed, a - b = a + (-b)
  if cipher_direction == "decode":
    shift_amount *= -1
  #looping through each character of the given text.
  for char in start_text:
    # If the character is in the alphabet list then we will cipher the character, otherwise the character will be the same. e.g. start_text = "meet me at 3". end_text = "•••• •• •• 3"
    if char in alphabet:
        position = alphabet.index(char)            
        check_position = position + shift_amount
        #the shift amount can be greater that the index of the alphabet list. To loop the alphabet list, modulo operator is used. 
        new_position = check_position % length_of_alphabet 
        end_text += alphabet[new_position]
    else: end_text += char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")


#Start the program. The program will run as long as start remains true. user can restart the cipher program if they want to. If they type yes the start remain true and if they type no then start is false and the program will be stopped. 

if __name__ == "__main__":
    start = True
    while start:
        #Importing logo from art.py module
        from art import logo
        print(logo)
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
        ask = input("Do you want to restart the cypher program? Type 'yes' or  'no'.\n").lower()
        if ask == "yes":
            #Clearing the screen. We can also clear the screen without importing os. by using "print("\033c")"
            os.system("clear")
            start = True
        else:
            start = False
            os.system("clear")
            print("Thank you for using caesar cipher. Wish to see you soon!")

