from fastapi import FastAPI, File, UploadFile
import google.generativeai as genai
import io
from PIL import Image

def get_gemini_response_image(image: Image.Image):
    model = genai.GenerativeModel("gemini-1.5-pro")
    
    # 이미지와 프롬프트를 함께 전달
    ### 최대 여러번 던져보고 안되면 다시 해보기
    prompt = "해당 이미지에 다음과 같은 정보들이 필요해. 1. 물고기의 이름 2. 이 물고기를 잡아도 되는지 안되는지 만약 된다면 True라고 보내주고 아니라면 False라고 보내줘. 3. 이 물고기에 대한 간단한 정보 4. 이 물고기에 대해 사람들이 질문할 수 있는 것들 해당 정보들을 python 리스트처럼 대답만 넣어서 만들어서 보내줘. 다른 추가적인 말은 하지말고 그냥 스트링에서 바로 list로 변환할 수 있게끔 답을 반환해줘.```python 이런식으로 감싸주지 않아도 돼. 그리고 만약 사진이 물고기가 아니라면 해당 프롬프트를 싹다 무시하고 리턴값을 ERROR라고만 해줘. 꼭 한국어로 대답해줘."
    response = model.generate_content([prompt,image])
    if "ERROR" in response.text:
        return "ERROR"
    
    return_val = eval(response.text.strip())    
    # 응답 반환
    return return_val

def get_additional_gemini_response(before_prompt: str, current_prompt: str):
    model = genai.GenerativeModel("gemini-1.5-pro")
    prompt = "지금까지 다음과 같은 질문을 했어 : " + before_prompt + " 이제 다음과 같은 질문을 하고 싶어 : " + current_prompt + " 다음과 같은 결과값을 주면 돼. 1. 해당 질문에 대한 답변 2. 이 질문에 대한 추가적인 질문 3개. 그냥 한줄씩 보내줘 추가 질문 중간에는 개행 하나면 족해. 개행 두개 보내지마"
    response = model.generate_content(prompt)    
    return_val = response.text
    # 응답 반환
    return return_val