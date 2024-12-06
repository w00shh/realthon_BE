from pydantic import BaseModel, Field
from typing import List

class FishingZone(BaseModel):
    langitude: float
    latitude: float


class Return_CheckFishingZone(BaseModel):
    fishing_avaliability: bool = Field(..., example=True)
    fishing_description: str = Field(..., example="이곳은 어획 가능한 구역입니다.")


class Return_FishDescription(BaseModel):
    fish_name: str = Field(..., example="연어")
    fishing_avaliability: bool = Field(..., example=True)
    fish_description: str = Field(..., example="연어는 맛있어")
    fish_questions: List[str] = Field(..., example=["연어는 먹어도 되나요?", "연어는 무엇을 먹나요?"])