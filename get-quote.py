import random
def primary():

   print("Keep it logically awesome.")
   rdn = random.randint(0, 13)
   f = open("quotes.txt")
   quotes = f.readlines()
   f.close()

   print(quotes[rdn])
  #f = open("quotes.txt")
  #quotes = f.readlines()
  #f.close()

  #print(quotes)

if __name__== "__main__":
  primary()
