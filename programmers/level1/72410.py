  
'''
1. new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2. new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3. new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4. new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5. new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6. new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7. new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
'''

import re

def solution(new_id):

    first = new_id.lower()
    second = re.sub(r"[^a-z0-9-_.]","",first)
    third = re.sub('(([.])\\2{1,})', '.', second)

    if third[0] == '.':
      fourth = third[1:]
    else:
      fourth = third

    if third[-1] == '.':
      fourth = fourth[:-1]
    else:
      fourth = fourth

    fifth = 'a' if fourth == '' else fourth
    sixth = (fifth[:14] if fifth[14] == '.' else fifth[:15]) if len(fifth) >= 16 else fifth
    seventh = (sixth+sixth[-1]*3)[:3] if len(sixth) <= 2 else sixth
    
    answer = seventh
    return answer
