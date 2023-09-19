import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from konlpy.tag import Okt

# Korean tokenizer
tokenizer = Okt()

def get_sentence_embedding(sentence, model):
    words = tokenizer.morphs(sentence)
    vectors = [model.wv[w] for w in words if w in model.wv] # 추가: 모델 내에 단어가 있는 경우에만 벡터를 가져옵니다.
    if not vectors:
        return None
    sentence_vector = sum(vectors) / len(vectors)
    return sentence_vector.reshape(1, -1)

def cosine_sim(target_sentence, text, model):
     target_vector = get_sentence_embedding(target_sentence, model)
     sentence_vector = get_sentence_embedding(text, model)
     if target_vector is None or sentence_vector is None:
         return 0
     similarity = cosine_similarity(target_vector, sentence_vector)[0][0]
     return similarity

def CosineSimilarity_Weight(token, df, filtered_items, model):
    for filtered_key in filtered_items:
        keyword_list = [x.strip() for x in df['main_keywords'][int(filtered_key)].split(',')]
        for i in keyword_list:
            if cosine_sim(i, token, model) > 0.7:
                df['weight'][int(filtered_key)] += 1
    return df
