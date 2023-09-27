import openai
import ast

# lang chain
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

# Module

from .User_Input_Check.User_Input_Check import *

from .Search_Title.Search_ToT import Search_ToT

from .Match_Title.Match_ToT import Match_ToT


import sys
import os

sys.path.append(os.path.abspath('../config'))
import config

openai.api_key = os.getenv("OPENAI_API_KEY")

rule = ['제목 및 서문', '개인정보의 처리 목적', '개인정보의 처리 및 보유 기간', '처리하는 개인정보의 항목',
        '만 14세 미만 아동의 개인정보 처리에 관한 사항','개인정보의 제3자 제공에 관한 사항','개인정보 처리업무의 위탁에 관한 사항','개인정보의 국외 이전에 관한 사항',
        '개인정보의 파기 절차 및 방법에 관한 사항','미이용자의 개인정보 파기 등에 관한 조치','정보주체와 법정대리인의 권리·의무 및 행사방법에 관한 사항','개인정보의 안전성 확보조치에 관한 사항','개인정보를 자동으로 수집하는 장치의 설치·운영 및 그 거부에 관한 사항',
        '행태정보의 수집·이용·제공 및 거부 등에 관한 사항','추가적인 이용·제공 관련 판단 기준','가명정보 처리에 관한 사항','개인정보 보호책임자에 관한 사항','국내대리인 지정에 관한 사항','개인정보의 열람청구를 접수·처리하는 부서','정보주체의 권익침해에 대한 구제방법',
        '영상정보처리기기 운영·관리에 관한 사항','개인정보 처리방침의 변경에 관한 사항']



def Search_Match_Omission_Model(user_input):
    # 저장한 txt파일(사용자 인풋) 불러옴
    loader = TextLoader("./bob.txt", encoding='utf-8')
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=4096, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    # 1> Search
    # 대제목 추출을 ToT 방식으로 구현(랭체인 적용한 체이닝)

    title_list = Search_ToT(docs, rule)

    # 2> Match
    # 추출한 대제목을 매칭하는 것을 ToT 방식으로 구현(랭체인 적용한 체이닝)

    title_dict = Match_ToT(title_list, rule)
    title_dict2 = {value: key for key, value in title_dict.items()}

    # 3> UserInput 반영 검증

    # 1) 사용자 입력으로 검사할 필요 없는 항목들 제거
    title_dict2, user_input_text = Reflect_Userinput(user_input, title_dict2)
    title_dict = {value: key for key, value in title_dict2.items()}

    # 2) Omission Check 해서 그 결과 반환(나중에 반환 요소)
    omission_text= Alert_Omission(title_dict2, user_input_text)

    return title_dict, title_dict2, omission_text  # 딕셔너리 형태로 2개 반환

    ##################
    ### title_dict = {방침의 대제목: 지침의 대제목}
    ### title_dict2 = {지침의 대제목: 방침의 대제목}

