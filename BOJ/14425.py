'''
Tree

총 N개의 문자열로 이루어진 집합 S가 주어진다.
입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.
'''

'''
1. set(), add() 와 dic(), append()개념을 알았다.
2. 2번째 시도에서 `input() = sys.stdin.readline`으로 변수정의를 했더니,
   시간이 3852s에서 164s로 줄었다.
'''

'''
import sys

N, M = map(int,input().split())
chk = []
n = 0

for i in range(N):
  word = sys.stdin.readline().rstrip()
  chk.append(word)

for i in range(M):
  if sys.stdin.readline().rstrip() in chk:
    n += 1
print(n)
'''

import sys

input = sys.stdin.readline
N, M = map(int,input().split())
chk = []
n = 0

for i in range(N):
  chk.append(input.rstrip())

for i in range(M):
  if input.rstrip() in chk:
    n += 1
print(n)
