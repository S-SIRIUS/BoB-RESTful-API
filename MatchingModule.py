def Matching(df, token_dict):
    # rule별 딕셔너리 초기화
    match_rule = {str(i): -1 for i in range(23)}

    for i in range(len(df)):
        temp = [x.strip() for x in df['keywords'][i].split(',')]
    
        # 중첩된 반복문 최적화
        for j in temp:
            matched = False
            for k, index_in_token in token_dict.items():
                if j in k:
                    print(j)
                    match_rule[str(i)] = index_in_token
                    matched = True
                    break
            if matched:
                break

    # 딕셔너리 정렬 및 필터링 통합
    sorted_items = sorted([(k,  v) for k, v in match_rule.items() if v != -1], key=lambda x: x[1])
    return sorted_items, match_rule