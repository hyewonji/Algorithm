'''
정수 N이 주어진다.
N을 소인수분해한다.
'''


N = int(input())
n = 2

while True:
  while N%n == 0:
    N /= n
    print(n)
  n += 1
  if N == 1:
    break
