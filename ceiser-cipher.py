import random
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def caesar(input_text, input_shift,coding ):
    plain_text=""
    if coding=="decode":
        input_shift*=-1
    for letter in input_text:
        position = alphabets.index(letter)
        new_position=(position+input_shift)%26
        plain_text+=alphabets[new_position]
    print(plain_text)

status=True

while status:
    coding_nature=input('Enter "code" for coding and decode for "decode" for decoding:')
    text = input("Enter the text: ")
    shift = int(input("Enter the number of shifts: "))
    caesar(input_text=text, input_shift=shift, coding=coding_nature)
    new_status=input("do you want to continue no/yes")
    if new_status == "no":
        status=False
        print("Goodbye")


