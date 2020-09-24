'''
2007년 1월 1일은 월요일이다.
2007년 x월 y일은 무슨요일인지 출력

**
1, 3, 5, 7, 8, 10, 12월은 31일까지, 
4, 6, 9, 11월은 30일까지, 
2월은 28일까지 있다.
**
'''

'''
another solutin : 
  import datetime
  week = ["MON", "TUE", "WED", "THU", "FRI","SAT" ,"SUN"]

  M, D = map(int, input().split())
  dt = datetime.datetime(2007, M, D)
  print(week[dt.weekday()])
'''

a =list(map(int,input().split()))
days=0
dayss=['SUN','MON','TUE','WED','THU','FRI','SAT']

for i in range(a[0]):
  if i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
    days+=31
  elif i==4 or i==6 or i==9 or i==11:
    days+=30
  elif i==2:
    days+=28

print(dayss[(days+a[1])%7])

