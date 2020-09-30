'''
나이와 이름이 가입한 순서대로 주어진다. 
나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬해라.

ex)
3
21 Junkyu
21 Dohyun
20 Sunyoung
->
20 Sunyoung
21 Junkyu
21 Dohyun
'''

N = int(input()) 
arry = list(input().split() for _ in range(N))
arry.sort(key=lambda x:int(x[0]))
for i in arry:
  print(*i)
