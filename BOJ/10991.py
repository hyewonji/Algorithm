'''
주어진 N값의 층과 길이를 가진 트리 만들기
ex)
  N=3 일경우
    *
   * *
  * * *
'''

N = int(input())
for i in range(N):
  print(' '*(N-(i+1)),end='')
  for j in range(N):
    if j<=i:
        print('* ',end='')
  print()
