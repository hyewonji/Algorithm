'''
첫째 줄 : 1m2당 사람의 수 L (1 ≤ L ≤ 10), 파티가 열렸던 곳의 넓이 P (1 ≤ P ≤ 1000) 주어짐.
둘째 줄 : 10^6보다 작은 정수 5개 주어짐.

참가자의 수와 각 둘째줄 정수들의 차이를 출력해라.
'''

N = list(input().split() for _ in range(2))
result=[]
ans = 1

for x in N[0]:
  ans *= int(x)

for x in N[1]:
  result.append(int(x)-ans)
  
for i in result:
    print(i, end = ' ')
