'''

DP

n을 입력받아 n번째 피보나치 수 출력하기
'''

----------------------------------------------------

n = int(input())
i = 2
arry = [0,1]

if n != 1:
  while i <= n:
    arry.append(arry[i-2]+arry[i-1])
    i += 1
print(arry[-1])

''' 72ms '''

----------------------------------------------------

n = int(input())
arry = [0,1]

try:
  for i in range(n-1):
    arry.append(arry[i]+arry[i+1])
except:
  pass
print(arry[-1])

''' 68ms  - 시간 단축'''
