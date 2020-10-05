'''
N을 입력받 -2진법으로 변환해라

**1,0 입력 주의하기!
'''


import math
N = int(input())
n = ''

while True:
  if N == 1:
    n += '1'
    break
  elif N == 0:
    n += '0'
    break
  if N%(-2) == -1:
    n += '1'
    N = math.ceil((N)/(-2))
  elif N%(-2) == 0:
    n += '0'
    N /= (-2)
print(n[::-1])
