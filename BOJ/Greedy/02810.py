'''
Greedy

다음과 같은 규칙을 따를때, 컵홀더에 컵을 꽂을 수 있는 최대 사람의 수를 구하라.
1. 극장의 한 줄에는 자리가 N개가 있다. 
2. 서로 인접한 좌석 사이에는 컵홀더가 하나씩 있고, 양 끝 좌석에는 컵홀더가 하나씩 더 있다. 
3. 커플석이 있는데 커플석 사이에는 컵홀더가 없다.(S는 일반 좌석, L은 커플석이며 항상 두개씩 쌍으로 주어진다.)
4. 자신의 좌석의 양 옆에 있는 컵홀더에만 컵을 꽂을 수 있다.
'''

N = int(input())
arry = input()
n = 0

for i in arry:
  if i == "L":
    n += 1

if N == 1:
  print(1)
elif n == 0:
  print(int(len(arry)))
else:
  print(int(len(arry)-(n/2-1)))
