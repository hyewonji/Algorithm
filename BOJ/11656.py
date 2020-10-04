'''
나올 수 있는 접미사를 모두 나타내고 알바벳 순으로 정렬헤라

**print(''.join(S)), print('/n'.join(S)를 배웠다
'''

S = list(input())
s = []

for i in range(len(S)):
  if i >= 1:
    del S[0]
  s.append(''.join(S))

print('\n'.join(s))

'''
for i in sorted(s):
  print(i)
'''
