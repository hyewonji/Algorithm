'''
첫 줄 : A, B
둘째 줄 : A진수 자릿수 m
셋째 줄 : A진수 각자리 숫자
-> B진법으로 변환 후 각 자리수 출력
'''

A, B =list(map(int,input().split()))
m = int(input())
numA = list(map(int,input().split()))[::-1]
numB = []
dec = 0

def function():
  dec = 0
  for i in range(m):
    dec += numA[i]*A**(i)

  while dec != 0:
    numB.append(str(dec%B))
    dec = int(dec/B)

  print(*numB[::-1])

function()
