# BoB-RESTful-API

📌 Chaining형식의 LLM과 모듈화된 알고리즘 그리고 Flask 기반의 RESTful API로 구성
[모델 구조 추후 작성]





---


## 📂 파일 구성

### 🌐 flask_test.py
- 📜: 이 파일은 Flask 기반의 RESTful API 기능을 포함함
- 🔗 API Endpoints**: 
  - `GET /endpoint1`: 엔드포인트1에 대한 설명
  - `POST /endpoint2`: 엔드포인트2에 대한 설명
### 📂 Customized_ALGO Package
- 📜: 이 파일은 모듈화된 주요 알고리즘을 포함함, Output 토큰 수를 최대한 줄이기 위함..(비용문제)
- 🛠 : ~~~ (추후 작성)

### 📂 Find_Question_Model Package
- 📜: 이 파일은 모듈화된 주요 알고리즘을 포함함
- 🛠 : ~~~ (추후 작성)

### 📂 Find_Answer_Model Package
- 📜: 이 파일은 모듈화된 주요 알고리즘을 포함함
- 🛠 : ~~~ (추후 작성)
---

## 🚀 시작하기

### 🔧 필요한 라이브러리 설치
```bash
! pip install openai
! pip install langchain
! pip install gensim
! pip install pandas
! pip install numpy
