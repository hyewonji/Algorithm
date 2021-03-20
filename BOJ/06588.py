'''
소수 찾기

4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다는 골드바흐의 추측을 검증하는 프로그램을 작성해라.

1. 입력은 하나 또는 그 이상의 테스트 케이스로 이루어져 있다. 테스트 케이스의 개수는 100,000개를 넘지 않는다.
2. 각 테스트 케이스는 짝수 정수 n 하나로 이루어져 있다. (6 ≤ n ≤ 1000000)
3. 입력의 마지막 줄에는 0이 하나 주어진다.
------------------------------------------------------------------------------------------------------

Solution
1. n의 최대값 1,000,000 이하의 홀수 중 소수를 구해 배열안에 false로 저장해놓는다.
2. 합이 n인 두 홀수를 생성된 배열의 인덱스로 값을 검색했을 때 모두 false이면 값을 반환한다.

시간제한이 있기 때문에 다음 코드를 사용해서 시간을 측정했다.
import timeit
start_time = timeit.default_timer() # 시작 시간 체크
terminate_time = timeit.default_timer() # 종료 시간 체크  
print("%f초 걸렸습니다." % (terminate_time - start_time)) #런타임 측정
'''

import sys
import math
 
n_max = 1000000
arry = [True]*(n_max+1)

# 에라토스테네스의 체 : n의 개수가 많을 때 효율적인 소수찾기 방법이다.(시간복잡도 : O(NloglogN))
# 검색하지 않아도 되는 0, 1, 짝수는 건너 뛰었다.
for i in range(3, int(math.sqrt(n_max)) + 1,2): 
  if arry[i] == True:
    j = 2
    while i * j <= n_max:
      arry[i * j] = False
      j += 1

while True:
  n = int(sys.stdin.readline())
  if n == 0:
    break
  for j in range(3,n-2,2):
    if arry[j] == True and arry[n-j] == True:
      print(f'{n} = {j} + {n-j}')
      break
    if j == n-3:
      print("Goldbach's conjecture is wrong.")
