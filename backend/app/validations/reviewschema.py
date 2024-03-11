from pydantic import BaseModel


class ReviewCreate(BaseModel):
    name: str
    rating: int
    comment: str
    rating: int
