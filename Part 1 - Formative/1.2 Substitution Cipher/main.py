# Read the instructions to see what you need to do here!

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+{}|:"<>?'


def sub_encode(text, codebet):
    if text.isdigit() or len(text) > len(codebet):
        return text
    text = text.upper()
    temp = ""
    for i in range(len(text)):
        if text[i] == " ":
            temp += " "
        for y in range(len(alpha)):
            if text[i] == alpha[y]:
                temp += cipher_alphabet[y]
    return temp


def sub_decode(text, codebet):
    if text.isdigit() or len(text) > len(codebet):
        return text
    text = text.upper()
    temp = ""
    for i in range(len(text)):
        if text[i] == " ":
            temp += " "
        for y in range(len(alpha)):
            if text[i] == cipher_alphabet[y]:
                temp += alpha[y]
    return temp


test = "HELLOWORLD"
cipher_alphabet = 'WJKUXVBMIYDTPLHZGONCRSAEFQ?"><:|}{+_)(*&^%$#@!)}'
enc = sub_encode(test, cipher_alphabet)
dec = sub_decode(enc, cipher_alphabet)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
