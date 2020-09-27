'''
B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.
10진법을 넘어가는 진법은 다음과 같이 알파벳 대문자를 사용한다.
A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

ex)
ZZZZZ 36
->
60466175
'''

arry = input().split()
N = arry[0][::-1]
B = int(arry[1])
result=0
idx=0

for i in N:
  if i.isalpha() == True:
    result += (ord(i)-55)*(B**idx)
    idx+=1
  else:
    result += int(i)*(B**idx)
    idx+=1

print(result)
