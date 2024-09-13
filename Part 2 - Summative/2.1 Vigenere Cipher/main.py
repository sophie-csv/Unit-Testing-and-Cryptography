# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# go down the column and add the index of t + t index and find the sum from the alpha
def vig_encode(text, keyword):
  temp = ""
  for i in range(len(text)):
    for y in range(len(alpha)):
      if text[i] == alpha[y]:
        index1 = y
        index2 = alpha.index(keyword[i % len(keyword)])
        letter = alpha[(index1 + index2) % 26]
        temp += letter
  return temp


def vig_decode(text, keyword):
  temp = ""
  for i in range(len(text)):
    for y in range(len(alpha)):
      if text[i] == alpha[y]:
        index1 = y
        index2 = alpha.index(keyword[i % len(keyword)])
        letter = alpha[(index1 - index2) % 26]
        temp += letter
  return temp


test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
vig_key = "TEST"
enc = vig_encode(test, vig_key)
dec = vig_decode(enc, vig_key)
print(enc)
print(dec)
# If this worked, dec should be the same as test!