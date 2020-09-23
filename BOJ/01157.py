'''
알파벳 대소문자로 된 단어가 주어지면, 
이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력
단, 가장 많이 사용된 알파벳이 2개 이상이면 '?'출력
'''

a=input().upper()
A=list(set(a))
arr=[]

for i in A:
  arr.append(a.count(i))

if len(a)==1:
  print(A[0])
elif max(arr)==1 or arr.count(max(arr))>=2:
  print('?')
else:
  print(A[arr.index(max(arr))])
