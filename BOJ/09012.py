'''
한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다.
주어진 괄호 문자열이 VPS 이면 YES, 아니면 NO로 나타낸다.

ex)
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(
->
NO
NO
YES
NO
YES
NO
'''

'''
좋은 예시
for i in range(int(input())) :
    ps = input()
    while '()' in ps :
        ps = ps.replace('()','')
    if ps == '' :
        print('YES')
    else :
        print('NO')
'''

N = int(input())
result = []


for i in range(N):
  s = input()
  for j in range(int(len(s)/2)):
    s=s.replace('()','')
  if s == '':
    result.append('YES')
  else:
    result.append('NO')

for i in result:
  print(i)
