'''
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

ex)
3
->
  *
 **
***
 **
  *
'''

N = int(input())
for i in range(N*2-1):
  if (i+1)<=N:
    print(('*'*(i+1)).rjust(N))
  else:
    print(('*'*(2*N-(i+1))).rjust(N))
