'''
가장 많이 팔린 책의 제목을 출력해라
가장 많이 팔린 책이 여러개일 경우, 
사전 순으로 가장 앞서는 제목 출력
'''

import sys
from collections import Counter

N = int(input())
n = []

for i in range(N):
  n.append(sys.stdin.readline())

c = Counter(n).most_common()
maximum = c[0][1]
modes =[]

for i in c:
  if i[1] == maximum:
    modes.append(i)
print(sorted(modes)[0][0].replace("\n",""))
