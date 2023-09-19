import pandas as pd
def FirstShort_Weight(token, df, filtered_items):
    for filtered_key in filtered_items:
            keyword_list = [x.strip() for x in df['main_keywords'][int(filtered_key)].split(',')]
            for i in keyword_list:
                if (i in token and len(token)<35): # First and Short
                    df['weight'][int(filtered_key)] += 2
                    return df