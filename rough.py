s = 'nqeujyparzpuwbenliuprxvn'

max_str = ''
curr_str = ''
number = 0

while number < len(s):
    if s[number] >= s[number-1] :
        curr_str += s[number]
        number += 1
        if len(curr_str) > len(max_str):
            max_str = curr_str
        continue

    curr_str = s[number]
    number += 1
    
print('Longest substring in alphabetical order is: ' + max_str)
