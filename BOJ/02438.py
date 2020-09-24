'''
첫째 줄에는 별 1개, 
둘째 줄에는 별 2개, 
N번째 줄에는 별 N개 찍기
'''


N = int(input())
for i in range(N):
  for j in range(N):
    if j<=i:
      print('*',end='')
  print()
