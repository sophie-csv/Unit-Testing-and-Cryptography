# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar_encode(text, n):
    temp = ""
    for i in range(len(text)):
        for y in range(len(alpha)):
            if text[i] == alpha[y]:
                if y > len(alpha) - n:
                    temp += alpha[n - 26 % y]
                else:
                    temp += alpha[y + n]
    return temp



def caesar_decode(text, n):
    temp = ""
    for i in range(len(text)):
        for y in range(len(alpha)):
            if text[i] == alpha[y]:
                if y > len(alpha) + n:
                    temp += alpha[n - 26 % y]
                else:
                    temp += alpha[y - n]
    return temp


test = "HELLOWORLD"
shift = 5
enc = caesar_encode(test, shift)
dec = caesar_decode(enc, shift)
print(enc)
print(dec)
#If this worked, dec should be the same as test!
