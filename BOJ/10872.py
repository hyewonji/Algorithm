'''
N의 펙토리얼 N!구하기
'''

N = int(input())
i = 1
j = 1

if N != 0 and N != 1:
  while i < N:
    j *= i
    i += 1
    if i == N:
      j *= i
      break
  print(j)
elif N == 1 or N ==0:
  print(1)
