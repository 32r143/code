s = 'cwafermhffuvpff'

max_str = ''
curr_str = ''
number = 0

for number in range(len(s)):
    if s[number] >= s[number-1] :
        curr_str += s[number]
        if len(curr_str) > len(max_str):
            max_str = curr_str
        continue

    curr_str = s[number]
    
print('Longest substring in alphabetical order is: ' + max_str)

