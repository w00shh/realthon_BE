from fastapi import APIRouter, UploadFile, File
from typing import Union, Optional

from app.schema.main_schema import FishingZone, Return_FishDescription, Return_CheckFishingZone
from app.core.image import upload_to_s3
from app.core.gemini import get_gemini_response_image
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
    # fish_name = get_gemini_response_image(file=fish_image)
    # upload_to_s3(file=fish_image.file, bucket_name="realthon", file_name=fish_image.filename) # fish_image.filename으로 저장

    # fish_name = "연어"
    fishing_avaliability = True
    fish_description = "연어는 맛있어"
    fish_questions = ["연어는 먹어도 되나요?", "연어는 무엇을 먹나요?"]

    # Fish_Description 객체 생성
    fish_info = Return_FishDescription(
        fish_name=fish_name,
        fishing_avaliability=fishing_avaliability,
        fish_description=fish_description,
        fish_questions=fish_questions,
    )
    
    return fish_info