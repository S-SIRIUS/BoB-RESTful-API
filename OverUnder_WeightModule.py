def OverUnder_Weight(token, df, filtered_items):
    for filtered_key in filtered_items:
            keyword_list = [x.strip() for x in df["main_keywords"][int(filtered_key)].split(" ")]
            # 선택한 키워드 기준 윗 데이터와 아랫 데이터가 공백인지 확인, 공백이라면 가중치 1 추가
            if df["main_keywords"][int(filtered_key)-1] == " " or df["main_keywords"][int(filtered_key)-1] == "":
                df["weight"][int(filtered_key)] += 0.5
            if df["main_keywords"][int(filtered_key)+1] == " " or df["main_keywords"][int(filtered_key)+1] == "":
                df["weight"][int(filtered_key)] += 0.5

            # 선택한 키워드 기준 윗 데이터와 아랫 데이터가 공백이 아니라면, 키워드가 포함되어 있는지 확인
            else:
                for keyword in keyword_list:
                    if keyword in df["main_keywords"][int(filtered_key)-1]:
                        df["weight"][int(filtered_key)] += 0.5
                    if keyword in df["main_keywords"][int(filtered_key)+1]:
                        df["weight"][int(filtered_key)] += 0.5
    return token
