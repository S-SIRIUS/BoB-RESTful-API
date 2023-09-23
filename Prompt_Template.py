#PromptTemplate & chain
import config
import os
api_key = os.getenv("OPENAI_API_KEY")

from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
)

chat = ChatOpenAI(model_name='gpt-4',temperature=0)

# 번역하는거 해라하는 프롬프트
template='''
너는 개인정보처리방침을 진단하는 솔루션이야. 
{policy}는 이 회사의 방침이야 그리고 {instruction}은 개인정보처리 지침이야.
개인정보처리 지침을 보고 이 회사의 방침에서 잘못된 부분이 있다면 찾아서 설명해줘!
'''

#시스템 메시지로
system_message_prompt = SystemMessagePromptTemplate.from_template(template)

# 휴먼 메시지 추가 가능!
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt])

chatchain = LLMChain(llm=chat, prompt=chat_prompt)