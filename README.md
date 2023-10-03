# BoB-RESTful-API

📌 예외사항
## 1) Cutting 동작시 매치되는 문장 "1.개인정보처리방침의 의의", "2.수집하는 개인정보 (필수 안내사항)" 등이 처음 목차에 있어서 이상하게 잘림

![스크린샷 2023-10-03 162532](https://github.com/S-SIRIUS/BoB-RESTful-API/assets/109223193/9fa290ca-7c56-48cd-962e-f185d532f4c3)
출처: 토스: https://toss.im/privacy-policy?id=22662

-> Rule예외사항 많을거같아서 LLM으로 해결하는 것으로!


## 2) 2개의 항목이 겹쳐 있는 경우(프롬프트 실험해보면서 해야할듯)
   ex> 개인정보의 수집*이용목적, 수집하는 개인정보의 항목 및 수집방법
![image-20230919-033557](https://github.com/S-SIRIUS/BoB-RESTful-API/assets/109223193/fc88f609-8030-49f0-946c-168369e79bf6)
출처: 포켓몬코리아: https://pokemonkorea.co.kr/privacy

-> 중복 있을수 있음을 체이닝으로 한번 다시 검사(Match_Title)파트, 딕셔너리의 value에 2개 들어감(title_dict에 2개 생성됨)
{"개인정보의 수집*이용목적, 수집하는 개인정보의 항목 및 수집방법" : "개인정보의 처리 목적"}
{"개인정보의 수집*이용목적, 수집하는 개인정보의 항목 및 수집방법" : "처리하는 개인정보의 항목"}

## 3) 앞에서 같이 나열한 후 뒤에서 공백으로 있는 경우 







