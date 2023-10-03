def isPalindrome(string):
  return string == string[::-1]

while True:
  state=input("Please input a statement: ")
  if state == "":
    if isPalindrome(state):
      print("Reversed: " + state[::-1])
      print("Palindrome: True")
    else:
      print("Palindrome: False")

    print("Bye!")
    break

  print("Reversed: " + state[::-1])

  if isPalindrome(state):
    print("Palindrome: True")
  else:
    print("Palindrome: False")
  print()