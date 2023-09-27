# bfs로 구현한 Search ToT
# max_depth = 3 -> 추후 이 부분에 대해서는 논의 예정

import sys
import os

sys.path.append("C://Users//scw10//PycharmProjects//rest_test//venv//config")
import config
api_key = os.getenv("OPENAI_API_KEY")

# Module
#from .Search_ToT_Prompt_Template import *
from .Rule_Validation.Rule_Validation import checking_list
from .Search_Title import Search_Title

from collections import deque


def Search_ToT(docs, rule):
    return Search_Title(docs, rule)
