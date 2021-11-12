def factorial():
    factorial = 1
    numInput = int(input("Please enter in a number you want to get the factorial of: "))
    for i in range (numInput):
        factorial = factorial * (i+1)
        print(factorial)

factorial() 