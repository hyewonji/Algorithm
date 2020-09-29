'''
각 테스트 케이스마다 가능한 모든 쌍의 GCD의 합을 출력한다.
첫째줄(t) : 테스트 케이스 개수

ex)
3
4 10 20 30 40
3 7 5 12
3 125 15 25
->
70
3
35

import math
import itertools
t = int(input())

for i in range(t):
  line = list(map(int,input().split()))[1:]
  case = list(itertools.combinations(line,2))
  GCD=0
  for j in case :
    GCD += math.gcd(j[0],j[1])

  print(GCD)
