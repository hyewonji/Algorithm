'''
N을 입력받아 N, N-1, N-2, ... 1의 별찍기
'''

N = int(input())
for i in range(N): 
  print('*'*(N-i))
