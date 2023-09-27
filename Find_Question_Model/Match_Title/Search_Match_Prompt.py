
# 제목 추출 프롬프트(토큰수 초과하면 잘릴 위험이 있다.)
def title_create_prompt_only(docs, rule):
    target= "너는 여기서 대제목을 뽑아주는 추출기야!"
    target += '\"'+ docs +'\"'+"은 한 회사의 개인정보처리 방침이야"
    target += '\"'+ str(rule) +'\"'+"은 '규칙의 대제목'을 리스트 형태로 만들어놓은거야"
    target += "이 리스트를 참고해서, '대제목'을 회사의 개인정보처리 방침에서 추출해"
    target += "그리고 수식어 붙이지 말고 딱 파이썬 리스트 형태로 출력만 해줘!"
    return target

def title_create_prompt_part(docs):
    target= "너는 여기서 대제목을 뽑아주는 추출기야!"
    target += '\"'+ docs +'\"'+"은 한 회사 개인정보처리 방침의 일부분이고 반드시 기억하고 있어야 해!"
    return target

def title_create_prompt_part_last(docs, rule):
    target= "너는 여기서 대제목을 뽑아주는 추출기야!"
    target += '\"'+ docs +'\"'+"은 한 회사의 개인정보처리 방침의 마지막 부분이야, 이제 기억해두라고 한거랑 이 마지막 부분까지가 한 회사의 개인정보처리방침이야"
    target += '\"'+ str(rule) +'\"'+"은 '규칙의 대제목'을 리스트 형태로 만들어놓은거야"
    target += "이 리스트를 참고해서, '대제목'을 회사의 개인정보처리 방침에서 추출해"
    target += "그리고 수식어 붙이지 말고 딱 파이썬 리스트 형태로 출력만 해줘!"
    return target


# 매치하는 프롬프트(토큰 초과할 일 없음)
def match_create_prompt(title_list, rule):
    target= "너는 비슷한 단어를 이해하고 매칭시키는 기계야!"
    target += '\"'+ str(title_list) +'\"'+"은 한 회사의 개인정보처리 방침 대제목 리스트야"
    target += '\"'+ str(rule) +'\"'+"은 규칙의 대제목 리스트야"
    target += "규칙의 대제목 리스트의 값들과 방침의 대제목 리스트 값들을 비교해, 그리고 의미가 비슷한 것들끼리 매칭해서 딕셔너리 형태로 출력해줘!"
    target += "예를 들면 {'개인정보의 보유 및 이용기간'(개인정보처리방침 대제목):'개인정보의 처리 및 보유 기간'(규칙 대제목)} 이런 형식이 되는거지!"
    target += "그리고 수식어 붙이지 말고 딱 파이썬 딕셔너리 형태로 출력만 해줘!"
    return target
