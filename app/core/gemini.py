from fastapi import FastAPI, File, UploadFile
import google.generativeai as genai
from PIL import Image
import io

def get_gemini_response_image(file: UploadFile = File(...)):
    image_data = file.read()
    model = genai.GenerativeModel("gemini-1.5-pro")
    image = Image.open(io.BytesIO(image_data))

    # 이미지와 프롬프트를 함께 전달
    response = model.generate_content()

    # 응답 반환
    return response