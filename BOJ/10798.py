'''
주어진 5개의 글자를
새로로 읽어 출력
ex)
A A B C D D
a f z z 
0 9 1 2 1
a 8 E W g 6
P 5 h 3 k x
-> Aa0aPAf985Bz1EhCz2W3D1gkD6x
'''


a = list(input() for _ in range(5))
longest = max(map(len,a))
arry=[]
result=''

for i in range(longest):
  arry.append('')

for i in a:
  for j in range(len(i)):
    arry[j] += i[j]

for i in arry:
  result += i

print(result)
