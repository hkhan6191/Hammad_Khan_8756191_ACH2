class Calculator(object):
    def addition(num1, num2):
        addition = num1 + num2
        return addition

    def subtraction(num1, num2):
        subtraction = num1 - num2
        return subtraction

    def multiplication(num1, num2):
        multiplication = num1 * num2
        return multiplication

    def division(num1, num2):
        division = num1 / num2
        return division

    def modulusDivision(num1, num2):
        modulusDivision = num1 % num2
        return modulusDivision

mathInput = int(input("Press 1 for addition. Press 2 for subtraction. Press 3 for multiplication. Press 4 for division. Press 5 for modulus division.")) 

num1 = int(input("Please enter in your first number: "))
num2 = int(input("Please enter in your second number: "))

if mathInput == 1:
    sum = Calculator.addition(num1, num2)
    print(sum)

elif mathInput == 2:
    sum = Calculator.subtraction(num1, num2)
    print(sum)

elif mathInput == 3:
    sum = Calculator.multiplication(num1, num2)
    print(sum)

elif mathInput == 4:
    sum = Calculator.division(num1, num2)
    print(sum)

elif mathInput == 5:
    sum = Calculator.modulusDivision(num1, num2)
    print(sum)

else:
    print ("Error")
