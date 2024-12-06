from fastapi import APIRouter, UploadFile, File
from typing import Union, Optional
from PIL import Image
import io

from ..schema.main_schema import FishingZone, Return_FishDescription, Return_CheckFishingZone, Return_AdditionalFishInfo
from ..core.image import upload_to_s3
from ..core.gemini import get_gemini_response_image, get_additional_gemini_response
router = APIRouter()

@router.get("/")
async def read_root():
    return {"Hello": "World"}


@router.post("/check-fishing-zone",response_model=Return_CheckFishingZone)
async def check_fishing_zone(FishingZone: FishingZone):
    # 해당 위치가 어획 가능한 구역인지 판단하는 API
        
    # 위도 경도를 받아오면 편하게 이 위치에서 가능한지 판별해서 가능한지 불가능한지 return 해주기
    return_val = Return_CheckFishingZone(fishing_avaliability=True, fishing_description="이곳은 어획 가능한 구역입니다.")

    return return_val

@router.post("/check-fish",response_model=Return_FishDescription)
async def check_fish(fish_image: UploadFile, device_id: Optional[str] = None):
    # 물고기 사진을 찍으면 이 물고기를 잡아도 되는지 안되는지, 물고기에 대한 이름과 간단한 정보, 거기서 파생될 수 있는 질문들을 리턴
    # 1. 물고기 사진을 gemini api로 보내서 물고기 종류를 받아온다.

    # 2. 물고기 종류에 따라서 물고기가 잡아먹어도 되는지 안되는지 판별한다.
    # 3. 물고기 종류에 따라서 물고기에 대한 간단한 정보를 저장한다.
    # 4. 물고기 종류에 따라서 물고기에 파생될 수 있는 질문들을 저장한다
    # 물고기 정보
    try:
        contents = fish_image.file.read()
        image = Image.open(io.BytesIO(contents))
        fish_info = get_gemini_response_image(image=image)

        if(fish_info == "ERROR"):
            fish_info = Return_FishDescription(fish_name="ERROR", fishing_avaliability=False, fish_description="ERROR", fish_questions=["ERROR"])
            return fish_info

        fish_name = fish_info[0]
        fishing_avaliability = fish_info[1]
        fish_description = fish_info[2]
        fish_questions = fish_info[3:]

        # Fish_Description 객체 생성
        fish_info = Return_FishDescription(
            fish_name=fish_name,
            fishing_avaliability=fishing_avaliability,
            fish_description=fish_description,
            fish_questions=fish_questions,
        )
        # upload_to_s3(file=fish_image.file, bucket_name="realthon", file_name=fish_image.filename) # fish_image.filename으로 저장    
        return fish_info
    except Exception as e:
        print(e)
        return {"error": "이미지를 처리하는 중에 오류가 발생했습니다."}
    
@router.post("/additional-fish-info",response_model=Return_AdditionalFishInfo)
async def additional_fish_info(before_prompt: str, current_prompt: str):
    try:
        response = get_additional_gemini_response(before_prompt, current_prompt)
        print(response)
        return_val = response.split("\n")
        print(return_val)
        return Return_AdditionalFishInfo(additional_result=return_val[0], additional_fish_info=return_val[2:])
    except Exception as e:
        print(e)
        return {"error": "이미지를 처리하는 중에 오류가 발생했습니다."}