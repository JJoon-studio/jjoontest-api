import os
import google.generativeai as genai
from fastapi import FastAPI
from pydantic import BaseModel

# --- 1. 설정 영역 ---
# Github에 API 키가 노출되지 않도록, Render의 'Secret File' 기능을 사용할 겁니다.
# 먼저, API 키를 설정합니다.
try:
    # Render 배포 환경에서는 Secret File에서 키를 읽어옵니다.
    with open("/etc/secrets/GEMINI_API_KEY") as f:
        api_key = f.read().strip()
    genai.configure(api_key=api_key)
except FileNotFoundError:
    # 로컬 개발 환경에서는 이 부분을 비워두거나, 직접 키를 넣고 테스트할 수 있습니다.
    # (단, 이 상태로 Github에 올리면 절대 안 됩니다!)
    print("API 키 파일이 없습니다. 로컬 테스트 시에는 직접 키를 설정해야 합니다.")
    pass

# 사용할 Gemini 모델 설정
model = genai.GenerativeModel('gemini-1.5-flash')


# --- 2. 데이터 모델 정의 영역 ---
# 친구가 우리에게 보낼 데이터의 형식을 미리 정해둡니다.
class Topic(BaseModel):
    topic: str


# --- 3. FastAPI 앱 생성 ---
app = FastAPI()


# --- 4. API 엔드포인트(기능) 정의 영역 ---
@app.get("/")
def read_root():
    return {"message": "AI 설명서 생성 API에 오신 것을 환영합니다!"}


@app.post("/generate-document")
def generate_document(item: Topic):
    # 친구가 보낸 주제(topic)를 받아서 새로운 프롬프트를 만듭니다.
    prompt = f"'{item.topic}'에 대한 기술 설명서를 IT 전문가 및 기술 문서 작성가 스타일로, 레스토랑 비유를 활용하여 알기 쉽게 작성해줘."

    try:
        # Gemini 모델에게 프롬프트로 질문을 던지고 응답을 받습니다.
        response = model.generate_content(prompt)

        # 성공적으로 답변을 받으면, 그 텍스트를 반환합니다.
        return {"document_text": response.text}
    except Exception as e:
        # 만약 AI 모델 호출 중 에러가 발생하면, 에러 메시지를 반환합니다.
        return {"error": f"AI 모델을 호출하는 중 에러가 발생했습니다: {e}"}