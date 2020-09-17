'''
윤년이면 '1', 아니면 '0' 출력하는 알고리즘 작성
'''

year = input()
if int(year)%4 == 0 and (int(year)%100 != 0 or int(year)%400 == 0):
  print(1)
else:
  print(0)
