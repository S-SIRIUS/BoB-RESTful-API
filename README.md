# BoB-RESTful-API

📌 예외사항
## 1) Cutting 동작시 매치되는 문장 "1.개인정보처리방침의 의의", "2.수집하는 개인정보 (필수 안내사항)" 등이 처음 목차에 있어서 이상하게 잘림[구현완료 테스트 필요]

![스크린샷 2023-10-03 162532](https://github.com/S-SIRIUS/BoB-RESTful-API/assets/109223193/9fa290ca-7c56-48cd-962e-f185d532f4c3)
출처: 토스: https://toss.im/privacy-policy?id=22662
->

1) Search_Title에서 대제목을 리스트로 추출한다.
2) 추루한 대제목 리스트로 Chaining건다.(Input: chunk된 Text or One Text , 대제목리스트) -> Chaining은 랭체인 없이 수작업(LLM타고 바로 LLM가는게 아님)
- LLM에서 대제목을 기준으로 그 다음문장까지 추출한다.
따라서 자르는 기준을 [대제목\n대제목다음문장] 이렇게 잘라서 유니크한 값으로 고정한다.
유니크한 값은 SearchTitle 모듈에서 만든다.
SearchTitle에서 먼저 대제목을 찾은 후, 그 대제목을 다시 LLM에 Chaining하여  [대제목\n대제목다음문장]도 만든다.
SearchTitle에서의 출력물
   1> [대제목]
   2> [대제목\n대제목다음문장] -> 컷팅을 위한 데이터


## 2) 2개의 항목이 겹쳐 있는 경우(프롬프트 실험해보면서 해야할듯) [구현완료 테스트 예정]
   ex> 개인정보의 수집*이용목적, 수집하는 개인정보의 항목 및 수집방법
![image-20230919-033557](https://github.com/S-SIRIUS/BoB-RESTful-API/assets/109223193/fc88f609-8030-49f0-946c-168369e79bf6)
출처: 포켓몬코리아: https://pokemonkorea.co.kr/privacy

-> 중복 있을수 있음을 체이닝으로 한번 다시 검사(Match_Title)파트, 딕셔너리의 value에 2개 들어감(title_dict에 2개 생성됨) -> Langchain
{"개인정보의 수집*이용목적, 수집하는 개인정보의 항목 및 수집방법" : "개인정보의 처리 목적"}
{"개인정보의 수집*이용목적, 수집하는 개인정보의 항목 및 수집방법" : "처리하는 개인정보의 항목"}

## 3) 상당한 분량(토큰수 초과) [구현완료 테스트 예정]
https://policy.naver.com/policy/privacy.html
-> chunk로 쪼개서 리스트로 Title 뽑는다.
-> 오버랩을 통해서 그 다음문장 추출 못하는거방지한다.



## 4) 항목만 있고 내용이 없는 경우
각 항목은 unique 제목 찾는 알고리즘으로 찾을 수 있으니, 찾아서 공백인지 검사하는 Rule알고리즘 제작예정







