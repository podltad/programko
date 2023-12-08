import string
def je_to_pangram(str):
   abeceda = "abcdefghijklmnopqrstuvwxyz"
   for char in abeceda:
      if char not in str.lower():
         return False
   return True
string = 'The quick brown fox jumps over the lazy dog'
if(je_to_pangram(string) == True):
   print("je to pangram")
else:
   print("není to pangram")