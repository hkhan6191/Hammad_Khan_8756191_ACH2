alphinput = (input("Enter a letter from the alphabet: "))


if alphinput.isdigit():
    print("Sorry, try using a letter!")
    alphinput = (input("Enter a letter from the alphabet: "))
    print(alphinput.swapcase())


elif alphinput.isalpha():
    print(alphinput.swapcase()) 