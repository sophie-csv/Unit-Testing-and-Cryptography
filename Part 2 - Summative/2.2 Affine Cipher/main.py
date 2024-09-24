import math

# Read the instructions to see what to do!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# PART 1
# These functions are provided for you!
def mod_inverse_helper(a, b):
    q, r = a//b, a%b
    if r == 1:
        return (1, -1 * q)
    u, v = mod_inverse_helper(b, r)
    return (v, -1 * q * v + u)

def mod_inverse(a, m):

    assert math.gcd(a, m) == 1, "You're trying to invert " + str(a) + " in mod " + str(m) + " and that doesn't work!"
    return mod_inverse_helper(m, a)[1] % m


# These are the functions you'll need to write:
def affine_encode(text, a, b):
    """
    Encodes text using the affine cipher rules and ceasar shift.
    :param text: Text wanted o be encoded with the affine cipher rules.
    :param a: a is less than 26 and shares no factors in common with the number 26
    :param b: n number of letter to shift right (ceasar shift) wanted
    :return: encoded text
    """
    temp = ""
    text.upper()
    for i in range(len(text)):
        if text[i] in alpha:
            letter = (a * alpha.index(text[i]) + b) % 26
            temp += alpha[letter]
    return temp


def affine_decode(text, a, b):
    """
    Decodes text using the affine cipher rules and ceasar shift.
    :param text: Text wanted to be decoded with the affine cipher rules.
    :param a: a is less than 26 and shares no factors in common with the number 26.
    :param b: n number of letter to shift left (ceasar shift) wanted
    :return: decoded text 
    """
    temp = ""
    text.upper()
    for i in range(len(text)):
        if text[i] in alpha:
            letter = (mod_inverse(a,26) * (alpha.index(text[i]) - b)) % 26
            temp += alpha[letter]
    return temp

test = "HELLOWORLD"
a = 3
b = 9
enc = affine_encode(test, a, b)
dec = affine_decode(enc, a, b)
print(enc)
print(dec)
# If this worked, dec should be the same as test!



# PART 2
# These  are the functions you'll need to write:
def convert_to_num(ngram):
    """
    Converting the ngram text to an integer equivalent.
    :param ngram: ngram text to convert.
    :return: integer equivalent of the ngram text.
    """
    temp = 0
    for i in range(len(ngram)):
        index = alpha.index(ngram[i])
        index = 26 ** i * index
        temp += index
    return temp

def convert_to_text(num, n):
    """
    Converting the integer to a ngram text.
    :param num: the integer wanted to convert to text.
    :param n: n-grams in text.
    :return: text version of the ngram int.
    """
    temp = ""
    for i in range(n):
        temp += alpha[int(num % 26)]
        num = num // 26

    return temp

test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
l = len(test)
num = convert_to_num(test)
answer = convert_to_text(num, l)
print(num)
print(answer)
# If this worked, answer should be the same as test!



# PART 3

# These are the functions you'll need to write:
def affine_n_encode(text, n, a, b):
    """
    Encodes text using a combination of ceasar shift and affine cipher with n-grams.
    :param text: Text wanted to be encoded with affine rules and split into n-grams
    :param n: number of n-grams
    :param a: a is less than 26 and shares no factors in common with the number 26.
    :param b: n number of letters to shift right (ceasar shift) wanted
    :return: encoded text.
    """
    temp = ""
    index = 0
    while len(text) % n != 0:
        text += "X"
    for i in range(0, len(text), n):
        ngram = text[i: i + n]
        x = convert_to_num(ngram)
        number = (a * x + b) % (26**n)
        temp += convert_to_text(number, n)
    return temp


def affine_n_decode(text, n, a, b):
    """
    Decodes text using a combination of ceasar shift and affine cipher with n-grams.
    :param text: Text wanted to be decoded with affine rules and split into n-grams
    :param n: number of n-grams
    :param a: a is less than 26 and shares no factors in common with the number 26.
    :param b: n number of letters to shift left (ceasar shift) wanted
    :return: decoded text.
    """
    temp = ""
    index = 0
    while len(temp) < len(text):
        ngram = text[index: index + n]
        x = convert_to_num(ngram)
        number = (x - b) * mod_inverse(a, (26**n)) % 26**n
        temp += convert_to_text(number, n)
        index += n
    return temp


test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
n = 2
a = 5
b = 121
enc = affine_n_encode(test, n, a, b)
dec = affine_n_decode(enc, n, a, b)
print(enc, dec)
# If this worked, dec should be the same as test!