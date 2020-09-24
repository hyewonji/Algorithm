'''
N입력받아 
N, N-1, N-2, ... , 1개의 별 
오른쪽 정렬로 출력
'''

N = int(input())
for i in range(N): 
  print(('*'*(N-i)).rjust(N))
