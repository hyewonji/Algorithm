'''
input N에 해당하는 크기, 높이의 나무 출력
'''

N = int(input())
for i in range(N):
  s=''
  for j in range(N):
    if j<=i:
      s+='*'
  print(s.rjust(N))
