numBeer = 99
while True:
  print(numBeer,"bottles of beer on the wall,")
  print(numBeer,"bottles of beer.")
  print("Take one down and pass it around,")
  numBeer-=1

  if numBeer == 1:
    print(numBeer,"bottle of beer on the wall.")
    print()
    print(numBeer,"bottle of beer on the wall,")
    print(numBeer,"bottle of beer.")
    print("Take it down and pass it around,")
    numBeer-=1
    print("no more bottles of beer on the wall.")
    break
  else:
    print(numBeer,"bottles of beer on the wall.")
    print()


def wordForm(num):
  sub = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
  tens = ["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]

  if num < 20:
    return sub[num]
  elif 20 <= num < 100:
    tens_place = num // 10
    ones_place = num % 10
    if ones_place == 0:
      return tens[tens_place]
    else:
      return tens[tens_place] + "-" + sub[ones_place].lower()

numBeer = 99

while numBeer >= 0:
  beerWords = wordForm(numBeer)
  print(beerWords,"bottles of beer on the wall,")
  print(beerWords.lower(),"bottles of beer.")
  print("Take one down and pass it around,")
  numBeer -= 1
  beerWords = wordForm(numBeer)


  if numBeer == 1:
    print(beerWords.lower(),"bottle of beer on the wall.")
    print()
    print(beerWords,"bottle of beer on the wall,")
    print(beerWords.lower(),"bottle of beer.")
    print("Take it down and pass it around,")
    print("No more bottles of beer on the wall.")
    print()
    break
  else:
    print(beerWords.lower(),"bottles of beer on the wall.")
    print()