
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
flag = True
while flag:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def caesar(text, shift, direction):
        tmp = ""
        for char in text:
            if 'a' <= char <= 'z':
                tmp += char
        text = tmp

        if direction == "encode":
            for i in text:
                idx = alphabet.index(i) + shift
                print(alphabet[idx])
        else:
            for i in text:
                idx = alphabet.index(i) - shift
                print(alphabet[idx])

    shift = shift % 26

    caesar(text=text, shift=shift, direction=direction)

    answer = input("Done? ")
    if answer == "yes":
        print("Good Bye!")
        flag = False

