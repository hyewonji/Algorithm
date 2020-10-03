'''
영어 알파벳 13글자씩 밀어 쓰기
알파벳 소문자와 대문자에만 적용
'''

S = input()
s = ''

for i in S:
  if i != ' ' and i.isdigit()==False:
    if (ord(i)>=97 and ord(i)<=109) or (ord(i)>=65 and ord(i)<=77):
      s += chr(ord(i)+13)
    else:
      s += chr(ord(i)+13-26)
  else:
    s += i
    
print(s)
