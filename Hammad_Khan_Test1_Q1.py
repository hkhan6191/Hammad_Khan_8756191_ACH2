alphinput = (input("Enter in your word: "))

if alphinput.isdigit():
    print("Sorry, try using letters! ")


elif alphinput.isalpha():
    print("Original: " + alphinput)
    print("Converted: " + alphinput.swapcase())