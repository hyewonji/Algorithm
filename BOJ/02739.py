'''
숫자 인풋 -> 구구단 작성
for문 이용
'''

N=input()
arry=[1,2,3,4,5,6,7,8,9]
for i in arry:
  result = int(N)*i
  print(N + ' * '  + str(i) + ' = ' + str(result))
