# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
# go down the column and add the index of t + t index and find the sum from the alpha
def vig_encode(text, keyword):
  text = text.upper()
  """
  Uses the keyword to encode text. Will take the index of both and add it to find corresponding alpha index.
  :param text: The text to be encoded
  :param keyword: The keyword to compare the text to
  :return: Encoded text
  """
  temp = ""
  for i in range(len(text)):
    if text[i] in alpha:
        index1 = alpha.index(text[i])
        index2 = alpha.index(keyword[i % len(keyword)])
        letter = alpha[(index1 + index2) % 27]
        temp += letter
    else:
      temp += text[i]



  return temp


def vig_decode(text, keyword):
  text = text.upper()
  """
  Decodes the text. Will take the index of both and add it to find corresponding alpha index.
  :param text: the text to be decoded
  :param keyword: The keyword to compare the text to
  :return: Decoded text
  """
  temp = ""
  for i in range(len(text)):
    if text[i] in alpha:
      index1 = alpha.index(text[i])
      index2 = alpha.index(keyword[i % len(keyword)])
      letter = alpha[(index1 - index2) % 27]
      temp += letter
    else:
      temp += text[i]
  return temp


test = "TEST"
vig_key = "THE QUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
enc = vig_encode(test, vig_key)
dec = vig_decode(enc, vig_key)
print(enc)
print(dec)
# If this worked, dec should be the same as test!