# 방침에서 대제목을 반환하는 모듈
import openai
import ast

# Module
from .Search_Match_Prompt import title_create_prompt_only, title_create_prompt_part, title_create_prompt_part_last

import sys
import os

sys.path.append("C://Users//scw10//PycharmProjects//rest_test//venv//config")
import config
api_key = os.getenv("OPENAI_API_KEY")

def Search_Title(docs, rule):
    for i in range(0, len(docs)):
        if (len(docs) > 1):
            if (i == len(docs) - 1):
                gpt_prompt = title_create_prompt_part_last(docs[i].page_content, rule)
                message = [{"role": "user", "content": gpt_prompt}]
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=message,
                    temperature=0.2,
                    max_tokens=4096,
                    frequency_penalty=0.0
                )
                title_list = ast.literal_eval((response['choices'][0]['message']['content']))
            else:
                gpt_prompt = title_create_prompt_part(docs[i].page_content)

                message = [{"role": "user", "content": gpt_prompt}]
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=message,
                    temperature=0.2,
                    max_tokens=4096,
                    frequency_penalty=0.0
                )

        else:
            gpt_prompt = title_create_prompt_only(docs[i].page_content, rule)

            message = [{"role": "user", "content": gpt_prompt}]
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=message,
                temperature=0.2,
                max_tokens=4096,
                frequency_penalty=0.0
            )
            title_list = ast.literal_eval((response['choices'][0]['message']['content']))

    return title_list