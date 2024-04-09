def generateKey(string, key):
  key = list(key)
  if len(string) == len(key):
    return (key)
  else:
    for i in range(len(string) - len(key)):
      key.append(key[i % len(key)])
  return ("".join(key))


def cypherText(string, key):
  cipher_text = []
  for i in range(len(string)):
    if string[i] == " ":
      cipher_text.append(" ")
    else:
      x = (ord(string[i]) + ord(key[i])) % 26
      x += ord('A')
      cipher_text.append(chr(x))
  return ("".join(cipher_text))


def originalText(cipher_text, key):
  orig_text = []
  for i in range(len(cipher_text)):
    if cipher_text[i] == " ":
      orig_text.append(" ")
    else:
      x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
      x += ord('A')
      orig_text.append(chr(x))
  return ("".join(orig_text))


if __name__ == "__main__":
  string = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
  keyword = "SECRET"
  key = generateKey(string, keyword)
  cipher_text = cypherText(string, key)
  print("Original String :", string)
  print("Encoded:", cipher_text)
  print("Decoded:", originalText(cipher_text, key))
