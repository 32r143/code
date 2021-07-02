import string

l = [i for i in string.ascii_lowercase]
L = [i for i in string.ascii_uppercase]
d = [i for i in string.digits]
dic = {}
start = 0
for i in L:
    dic[start]= i
    start += 1
for i in l:
    dic[start] = i
    start += 1
for i in d:
    dic[start] = i
    start += 1

res = int('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706'
          'f69736f6e6f7573206d757368726f6f6d', 16)
answer = ''
new_dic = {}

while res > 0:
    i = res % 64
##    print(i)
##    print()
    answer = dic[i] + answer
##    print(answer)
    res = res // 64
print(answer)
