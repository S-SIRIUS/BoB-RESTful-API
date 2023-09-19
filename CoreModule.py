from MatchingModule import Matching
from VotingModule import Voting
import pandas as pd

df = pd.read_csv("test_instruction_bob_v1.csv")
def Core(text, model):
    # 문장 단위로 토큰화
    token_dict={}
    token = text.split('\n')
    cumulative_length = 0
    token_dict = {}
    for item in token:
        token_dict[item] = cumulative_length  # 현재 누적 길이를 딕셔너리에 저장
        cumulative_length += len(item)+1 

    
    # 못찾은 rule들(-1)을 다시 Voting형식으로 해서 2차 추출
    sorted_items, match_rule = Matching(df, token_dict)
    filtered_items = {k: v for k, v in sorted_items.items() if v == -1}
    sorted_items2 = Voting(df, token_dict, filtered_items, model)
    sorted_items = sorted_items + sorted_items2 # 2차 추출한거 다시 합침


    df['keywords_matched']=""
    for i, (num, position) in enumerate(sorted_items):
        # 마지막 요소가 아니라면 end_idx를 설정, 마지막 요소라면 bob의 끝까지
        if i != len(sorted_items) - 1:
            end_idx = sorted_items[i+1][1] - 1
        else:
            end_idx = len(text)
    
        df['keywords_matched'][int(num)] = text[position:end_idx]
    
    return df #데이터 프레임 형태로 반환

