'''
주어진 점수들의 최고점을 이용해 모든점수를
'점수/M*100'로 바꿈
ex) 
3
40 80 60
-> 75.0
'''

'''
N = list(input().split() for _ in range(2))
print(N)
result = []
for i in N:
  for j in range(len(i)):
    i[j] = int(i[j])

for i in N[1]:
  result.append(i/max(N[1])*100)


print(sum(result)/N[0][0])'''


M=int(input())
T=list(map(int,input().split()))
print(sum(T)/M*100/max(T))
