from fastapi import APIRouter, UploadFile, File
from typing import Union, Optional
from PIL import Image
import io
import uuid
from bson import ObjectId

from ..schema.main_schema import FishingZone, Return_FishDescription, Return_CheckFishingZone, Return_AdditionalFishInfo
from ..core.image import upload_to_s3
from ..core.gemini import get_gemini_response_image, get_additional_gemini_response
from ..db.session import client
from ..db.forbidden_fishing import fobidden_fishing, haversine
router = APIRouter()

collection = "fishing"


@router.post("/check-fishing-zone",response_model=Return_CheckFishingZone)
async def check_fishing_zone(FishingZone: FishingZone):
    for i in fobidden_fishing:
        if haversine(FishingZone.latitude, FishingZone.langitude, i["lattitude"], i["longtitude"]) < 5:
            return_val = Return_CheckFishingZone(fishing_avaliability=False, fishing_description="이곳은 어획 불가능한 구역입니다.")
            return return_val
    return_val = Return_CheckFishingZone(fishing_avaliability=True, fishing_description="이곳은 어획 가능한 구역입니다.")
    return return_val

@router.post("/check-fish",response_model=Return_FishDescription)
async def check_fish(fish_image: UploadFile, device_id: Optional[str] = None):
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
        fish_questions = ""
        if isinstance(fish_info[3], list):
            fish_questions = fish_info[3]
        else:
            fish_questions = fish_info[3:]        

        # file_name = f"{uuid.uuid4()}_{fish_image.filename}"
        # upload_to_s3(file=fish_image.file, bucket_name="realthon", file_name=file_name) # fish_image.filename으로 저장    

        fish_info_dict = {
            "fish_name": fish_name,
            "fishing_avaliability": fishing_avaliability,
            "fish_description": fish_description,
            "fish_questions": fish_questions
        }
        print(fish_info_dict)
        result = client[collection].insert_one({"device_id": device_id, "image_query_result":fish_info_dict, "queries":[]})
        
        # Fish_Description 객체 생성
        fish_info = Return_FishDescription(
            fish_name=fish_name,
            fishing_avaliability=fishing_avaliability,
            fish_description=fish_description,
            fish_questions=fish_questions,
            db_id=str(result.inserted_id)
        )
        return fish_info
    except Exception as e:
        print(e)
        return {"error": "이미지를 처리하는 중에 오류가 발생했습니다."}
    
@router.post("/additional-fish-info",response_model=Return_AdditionalFishInfo)
async def additional_fish_info(before_prompt: str, current_prompt: str, db_id: str):
    try:
        response = get_additional_gemini_response(before_prompt, current_prompt)
        print(response)
        return_val = response.split("\n")
        print(return_val)

        additional_fish_info_res = [item for item in return_val[1:] if item != '']
        tmp_dic = {
            "question": current_prompt,
            "answer":{
            "additional_result": return_val[0],
            "additional_fish_info": additional_fish_info_res
            }
        }

        db_id = ObjectId(db_id)
        result = client[collection].update_one(
            {"_id": db_id},  # 필터
            {"$push": {"queries": tmp_dic}},  # 기존 데이터 유지하며 값 추가
            upsert=True  # 문서가 없으면 새로 생성
        )
        return Return_AdditionalFishInfo(additional_result=return_val[0], additional_fish_info=additional_fish_info_res)
    except Exception as e:
        print(e)
        return {"error": "이미지를 처리하는 중에 오류가 발생했습니다."}
    
@router.get("/get-history")
async def get_history(device_id: str):
    result = list(client[collection].find({"device_id": device_id}))
    for i in result:
        i["_id"] = str(i["_id"])    
    return result
