# 1번 문제
'''
proglam: line
flag-type-list: ["-s STRING", "-n NUMBER", "-e NULL"]
flag-text-list: ["line -n 102 -s hi -e", "line -n id -n 100"]

flag-text-list의 논리값 리스트를 출력해라.


예를들어 
1. 첫번째 인자: -n의 테스트값이 100 이므로 참, -s의 테스트의 값이 'hi'이므로 참
2. 두번째 인자: -n의 테스트의 값이 id로 문자열이므로 거짓이다.
결과는 [True, False]가 나와야한다. 
'''

def solution(program, flag_rules, commands):
    rule_dic = {}
    result = []
    for flag_rule in flag_rules:
        rule_arr = flag_rule.split()
        rule_dic[rule_arr[0]]= rule_arr[1]
        
    for i in range(1,len(command_arr),2):
      if(command_arr[0] == program):
          command_result = True
          command_arr = command.split()
          try:
            if rule_dic[command_arr[i]] == 'NULL':
                command_arr.insert(i+1, '')
            elif rule_dic[command_arr[i]] == 'STRING':
              try:
                int(command_arr[i+1])
                command_result = False
                break
              except: 
                pass
            elif rule_dic[command_arr[i]] == 'NUMBER':
              try:
                int(command_arr[i+1])
                pass
              except: 
                command_result = False
                break
            
          except:
              command_result = False
      else:
        command_result = False
        
      result.append(command_result)
      return result



# 2번
'''
1번에서 flag-type-list가 추가된 문제이다.

proglam: line
flag-type-list: ["-s STRING","-ss STRINGS", "-n NUMBER", "-nn NUMBERS", "-e NULL"]
flag-text-list: ["line -n 100 102 -s hi -e", "line -n id pwd -n 100"]

STRINGS는 테스트 값이 복수개의 문자이고,
NUMBERS는 테스트 갑시 복수개의 숫자이다.
'''

def solution(program, flag_rules, commands):
    rule_dic = {}
    result = []
    for flag_rule in flag_rules:
        rule_arr = flag_rule.split()
        rule_dic[rule_arr[0]]= rule_arr[1]

    for command in commands:
      command_result = True
      command_arr = command.split()

      if(command_arr[0] == program):
        i = 1
        while i<len(command_arr):
          flag_list = []
          if(command_arr[i] in rule_dic):
            flag_type = rule_dic[command_arr[i]]
          else: 
            print(flag_type)
            if flag_type == 'NULL':
                if(command_arr[i] in rule_dic):
                  pass
                else:
                  break
            elif flag_type == 'STRING' or flag_type ==  'STRINGS':
              try:
                int(command_arr[i])
                command_result = False
                break
              except: 
                flag_list.append(command_arr[i])
                if(flag_type == 'STRING' and len(flag_list) > 1):
                  command_result = False
                  break
                pass
            elif flag_type == 'NUMBER' or flag_type == 'NUMBERS':
              try:
                int(command_arr[i])
                flag_list.append(command_arr[i])
                if(flag_type == 'NUMBER' and len(flag_list) > 1):
                  command_result = False
                  break
                pass
              except: 
                command_result = False
                break
            i += 1
          
      result.append(command_result)
      return result
