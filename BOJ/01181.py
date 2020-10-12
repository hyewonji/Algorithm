'''
알파벳 소문자로 이루어진 N개의 단어를 길이가 짧은 것부터 정렬.
길이가 같으면 사전 순으로 정렬
'''

import sys

N = int(input())
a=[]
for i in range(N):
  s = str(sys.stdin.readline().rsplit())
  s = s.replace("['","")
  s = s.replace("']","")
  a.append(s)

b=list(set(a))
b.sort()
b.sort(key=len)

for i in b:
  print(i)
