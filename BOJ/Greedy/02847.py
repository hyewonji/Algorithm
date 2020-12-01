'''
Greedy

N개의 level이 있는 게임에서 각 level을 clear하면 얻는 score가 주어진다. 
level이 높아질수록 높은 점수를 받게 하기 위해 감소 시켜야할 점수는 몇점인지 구하라
'''

import sys

N = int(input())
score = list(int(sys.stdin.readline().rstrip()) for _ in range(N))[::-1]
r = 0

for i in range(1,N):
  m = score[i]-score[i-1]
  if m >= 0:
    r += m + 1
    score[i] -= m +1

print(r)
