def main():
  import random
  inputPasses = input("Enter whatever potential words you would like to be in your passwords, separated by a space.")
  listPasses = inputPasses.split(" ")

# now will get a random word of the list to be chosen to be used for the password
  passWord = random.choice(listPasses)

# now let's get some random numbers that the user wants and put them in a random order
  desiredNumAmt = int(input("How many numbers would you like in your password?"))
  inputNums = str(input("Enter whichever numbers you'd like to have in your password, 0-9, separated by a space"))
  listNums = inputNums.split(" ")
  passNums = random.choices(listNums, k=desiredNumAmt)

# print final password
  finalPass = str(passWord) + str(passNums)
  print(finalPass)

main()