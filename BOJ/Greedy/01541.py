‘’’
Greedy

괄호를 적절히 사용해 입력된 식의 값을 최소로 만드는 프로그램을 작성해라.
**첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 
가장 처음과 마지막 문자는 숫자이다. 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 
5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다. 
입력으로 주어지는 식의 길이는 50보다 작거나 같다.**
‘’’

print(init-S)

M = input().split('-')
S = []
for i in M:
  try:
    S.append(int(i))
  except:
    S.append(sum(map(int,i.split("+"))))

print(S[0]*2-sum(S))

‘’’
2. 메모리를 줄여보려했는데 똑같이 나왔다.

M = input().split('-')
S = 0
for i in range(len(M)):
  if i != 0:
    try:
      S += int(M[i])
    except:
      S += sum(map(int,M[i].split("+")))
  else:
    try:
      init = int(M[i])
    except:
      init = sum(map(int,M[i].split("+")))

‘’’
