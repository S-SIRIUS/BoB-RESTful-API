import pandas as pd
df = pd.read_csv("./test_instruction_bob_v1.csv")

def Matching(result_dict):
    df['matched_part'] = ''
    for key, value in result_dict.items():
        df.loc[df['part'] == key, 'matched_part'] = value
    return df
