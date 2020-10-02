'''
첫 줄 : N 
둘째 줄 - N째 줄 : 좌표(x,y)
->
x좌표가 증가하는 순으로, 
x좌표값이 같으면 y좌표값이 증가하는 순으로 정렬
'''

import sys
N = int(input())
result =[]
for i in range(N):
  result.append(list(map(int,sys.stdin.readline().split())))

result.sort(key=lambda x:(int(x[0]),int(x[1])))

for i in result:
  print(*i)
