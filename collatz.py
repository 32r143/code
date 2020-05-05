def collatz(number):
    if number %2 ==0:
        result = number //2
    else :
        result = 3*number+1
    print(result)
    return result
random = int(input('Enter an integer'))
while random != 1:
    random = collatz(random)
    
