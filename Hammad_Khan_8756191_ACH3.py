numinput = 0
compare = 0
sumofsquares = 0

numinput = int(input("Please enter in a number:  "))

while (compare <= numinput):
    sumofsquares += compare**2
    compare += 2

print(sumofsquares)
