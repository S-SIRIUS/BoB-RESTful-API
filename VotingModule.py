from FirstShort_WeightModule import FirstShort_Weight
from CosineSimilarity_WeightModule import CosineSimilarity_Weight
from OverUnder_WeightModule import OverUnder_Weight


def Voting(df, token_dict, filtered_items, model):

    # 각 rule 별 가중치 변수(문장들에 대해서 이 rule들 단어로 검사)
    df['weight']=0

    match_rule = []
    # 검사하는 반복문: 전달받은 filterd_items에서 
    for token in token_dict: # 문장하나에 모든 rule검색해서 가중치로 픽스. 픽스못하면 어떤 룰도해당안됨

        # 1 첫번째로 찾은것 문장짧은지 검사해서 해당하는 rule에 가중치 추가
        df = FirstShort_Weight(token, df, filtered_items)

        # 2 코사인 유사도 검사해서 일정치 이상인것들 해당하는 rule에 가중치 추가(유사단어)
        df = CosineSimilarity_Weight(token, df, filtered_items, model)

        ## 3 앞뒤검사
        df = OverUnder_Weight(token, df, filtered_items)



        # 조건해당하면 문장에 해당하는 rule을 match_rule에 문장인덱스랑 같이 저장 (rule, index)
        if(max(df['weight'])>=3):
            match_rule.append((str(df['weight'].idxmax()), token_dict[token]))
        return match_rule
        