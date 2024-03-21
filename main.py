global alphabet
values = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'
word = input("Enter word: ")
shift = int(input("Enter shift: "))

def assign():
  global values
  for i in alphabet:
    values.append(i)

def encrypt(word):
  global encrypted
  encrypted = []
  for i in word:
    for k in values:
      if i == k:
        index = (values.index(k) - shift)%26
        encrypted.append(index)

def decrypt(encrypted):
  global decrypted
  decrypted = ""
  for i in encrypted:
    for k in values:
      if i != "." and int(i) == int(values.index(k)):
        decrypted += str(k)


assign()
encrypt(word)
decrypt(encrypted)

print(decrypted)