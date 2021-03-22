'''
지구, 태양, 달의 연도 범위는 다음과 같다.
1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19

예를들어,
15년은 15 15 15로 나타낼 수 있다. 
하지만, 1년이 지나서 16년이 되면 16 16 16이 아니라 1 16 16이 된다.

E, S, M으로 표시되는 가장 빠른 연도를 출력한다.
'''

E, S, M = map(int,input().split())

while True:
  if E == S == M:
    break
  min_planet = min(E,S,M)
  if (min_planet == E):
    E += 15
  elif (min_planet == S):
    S += 28
  else:
    M += 19

print(E)
