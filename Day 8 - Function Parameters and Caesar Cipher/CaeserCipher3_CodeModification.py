alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(start_text, shift_amount, cipher_direction):
    final_text = ""
    if cipher_direction == "decode":
        shift_amount = shift_amount * -1

    for ch in start_text:
        if ch in alphabet:
            index = alphabet.index(ch)
            new_index = (index + shift_amount)%26      # For cyclic indexing -> so that shift in ending letters like x,y,z are possible
            final_text += alphabet[new_index]
        else:
            final_text += ch
            
    print(f"The {cipher_direction}d text is {final_text}")
        
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
# def encrypt(text, shift):
#     cipher_text = ""
#     for ch in text:
#         index = alphabet.index(ch)
#         new_index = (index + shift)%26      # For cyclic indexing -> so that shift in ending letters like x,y,z are possible
#         cipher_text += alphabet[new_index]
#     print(f"The encoded text is {cipher_text}")
  
# def decrypt(cipher_text, shift):
#     original_text = ""
#     for ch in cipher_text:
#         index = alphabet.index(ch)
#         new_index = (index - shift)%26      # For cyclic indexing -> so that shift in ending letters like x,y,z are possible
#         original_text += alphabet[new_index]
#     print(f"The decoded text is {original_text}")

# if direction == "encode":
#     encrypt(text, shift)
# else:
#     decrypt(text, shift)