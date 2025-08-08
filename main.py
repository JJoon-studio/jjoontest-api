from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    from fastapi import FastAPI

# v3.4 프롬프트의 결과물을 여기에 변수로 저장합니다.
# (실제로는 훨씬 길겠지만, 지금은 예시로 간단하게 작성합니다.)
V3_4_DOCUMENT_TEXT = """
# AI 프롬프트 보호를 위한 접근 제어 시스템 설명서

## 1. 개념 이해: '무엇'을 만들어야 하는지 알게 됩니다.
이 시스템은 AI의 핵심 자산인 프롬프트를 보호하기 위한 것입니다...

## 2. 구조 파악: '어떻게' 구성해야 하는지 알게 됩니다.
시스템은 사용자 인증, API 게이트웨이, 로깅 시스템으로 구성됩니다...
"""

app = FastAPI()

# 기본 접속 주소 (테스트용으로 그대로 둡니다)
@app.get("/")
def read_root():
    return {"Hello": "World"}

# === 여기부터 새로운 코드를 추가합니다! ===
@app.post("/generate-document")
def generate_document():
    return {"document_text": V3_4_DOCUMENT_TEXT}