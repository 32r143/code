import sys
def collatz(number):
    if number %2 == 0:
        result = number//2
    else:
        result = 3*number + 1
    print(result)
    return result

print("Enter an integer")
while True:
    try:
        userinput = int(input())
    except ValueError:
        print('Entered value is not an integer value')
        continue
    while userinput != 1:
        userinput = collatz(userinput)
    if userinput == 1:
        sys.exit()
