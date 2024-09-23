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
    temp = ""
    for i in range(len(text)):
        letter = (a * alpha.index(text[i]) + b) % 26
        temp += alpha[letter]
    return temp


def affine_decode(text, a, b):
    temp = ""

    for i in range(len(text)):
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
    temp = 0
    for i in range(len(ngram)):
        index = alpha.index(ngram[i])
        index = 26 ** i * index
        temp += index
    return temp

def convert_to_text(num, n):
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