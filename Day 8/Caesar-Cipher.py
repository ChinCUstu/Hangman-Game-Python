import art as a
print(a.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(start_text, shift_amount, cipher_direction):
    end_text = []
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == 'encode':
            new_position = position + shift_amount
            if new_position > len(alphabet):
                newer_position = new_position - len(alphabet)
                end_text += alphabet[newer_position]
            else:
                new_letter = alphabet[new_position]
                end_text += new_letter
        elif cipher_direction == 'decode':
            new_position = position - shift_amount
            new_letter = alphabet[new_position]
            end_text += new_letter
    return f"The {cipher_direction}d is {''.join(end_text)}"


print(caesar(start_text=text, shift_amount=shift, cipher_direction=direction))
