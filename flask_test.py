from flask import Flask, request, Response
import json
import openai
from concurrent.futures import ThreadPoolExecutor
import functools
import os
import sys

# Module
from Find_Question_Model.Search_Match_Omission_Model import Search_Match_Omission_Model

from Customized_ALGO.Cutting import *
from Customized_ALGO.Matching import *
from Find_Answer_Model.Answer_Model import *
from Find_Answer_Model.Answer_CoT_SC import *
from Find_Question_Model.User_Input_Check import *




app = Flask(__name__)

@app.route('/process-text', methods=['POST'])



def process_text():
    answer_text = ""

    if not request.json or 'text' not in request.json:
        return jsonify({'error': 'Data must be in JSON format and contain a "text" field.'}), 400

    text = request.json.get('text')
    print("들어온 text: ", text)
    print("\n")
    user_input = request.json.get('user_input')

    if user_input is not None and isinstance(user_input, list):
        print("들어온 유저의 체크박스: ", user_input)


    # 임시로 내가 직접 저장 -> 나중에 파일 직접 업로드로 바꿀 예정
    with open("bob.txt", "w", encoding="utf-8") as file:
        file.write(text)

    title_dict, title_dict2, omission_text = Search_Match_Omission_Model(user_input)

    result_dict = Cutting(text, title_dict, title_dict2)
    df = Matching(result_dict)
    answer_text = Answer_CoT_SC(df)

    omission_text = "*<누락 관련 사항>*\n" + omission_text+"\n\n"
    answer_text = omission_text + answer_text
    print(answer_text)


    #### 마지막에 백엔드와 연동하면서 json 형태도 바꿀 예정
    response_data = json.dumps({'result': answer_text}, ensure_ascii=False)
    return Response(response_data, content_type="application/json; charset=utf-8")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=50)

