'''
자료구조

먼저, 문자열 S는 아래와과 같은 규칙을 지킨다.
1. 알파벳 소문자('a'-'z'), 숫자('0'-'9'), 공백(' '), 특수 문자('<', '>')로만 이루어져 있다.
2. 문자열의 시작과 끝은 공백이 아니다.
3. '<'와 '>'가 문자열에 있는 경우 번갈아가면서 등장하며, '<'이 먼저 등장한다. 또, 두 문자의 개수는 같다.
4. 태그는 단어가 아니다.
5. 단어는 공백으로 구분한다.

단어만 뒤집는 프로그램을 작성하라
'''



# 1번 풀이

s = input()
ans = ''
reverse = ''

tag = 0
for i in range(len(s)-1,-1,-1):
  if s[i] == '>':
    tag = 1
  
  if tag == 1:
    ans = s[i] + ans
  else:
    reverse += s[i]
    if s[i-1] == '>' or s[i-1] == ' ' or reverse == ' ' or i == 0:
      ans = reverse + ans
      reverse = ''

  if s[i] == '<':
    tag = 0

print(ans)



# 2번 풀이
# for idx, c in enumerate(s) : 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환한다.
# "".join(arry) : 특정 문자열을 문자 사이에 삽입해 합칠 수 있다.

s = input()
rev = True
start = 0
end = 0
ret = []

for idx, c in enumerate(s):
  end=idx
  if c == '<':
      ret.append("".join(reversed(s[start:end])))
      start=idx
      rev=False
  if c == '>':
      ret.append(s[start:end+1])
      start=idx+1
      rev=True
  if c == ' ' and rev:
      ret.append("".join(reversed(s[start:end])))
      ret.append(' ')
      start=idx+1

ret.append("".join(reversed(s[start:end+1])))
print("".join(ret))
