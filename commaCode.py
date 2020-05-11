def commaCode(spam):
    if len(spam)>1:
        for i in range(len(spam)-1) :
            print(spam[i], end= ', ')
        print('and', spam[len(spam)-1])
    elif len(spam) == 1:
        print(spam[len(spam) - 1])
    else:
        print()

empty = ['mango']
ham = ['apples', 'bananas', 'tofu', 'cats']
commaCode(ham)
