# Read the instructions to see what you need to do here!

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+{}|:"<>?'


def sub_encode(text, codebet):
    """
    Encodes the text with substitution cipher and using the alphabet codebet to compare indices and add together to get the final indice.
    :param text: text to be encoded
    :param codebet: Alphabet used to compare indices.
    :return: encoded text
    """
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
    """
    Decodes the text with substitution cipher and using the alphabet codebet to compare indices and add together to get the final indice.
    :param text: text to be decoded.
    :param codebet: Alphabet used to compare indices.
    :return: decoded text.
    """
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
