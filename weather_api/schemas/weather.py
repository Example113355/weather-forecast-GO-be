from ninja import Field, Schema
from ..utils.regex import EMAIL_PATTERN
from typing import List

class EmailSchema(Schema):
    email: str = Field(description="Email Address", min_length=1, max_length=255, pattern=EMAIL_PATTERN)

class EmailCodeSchema(Schema):
    email: str = Field(description="Email Address", min_length=1, max_length=255, pattern=EMAIL_PATTERN)
    code: str = Field(description="Code", min_length=6, max_length=6)
    locations: List[str] = Field(description="Location Name", min_items=1)

class EmailLocationSchema(Schema):
    email: str = Field(description="Email Address", min_length=1, max_length=255, pattern=EMAIL_PATTERN)
    location: List[str] = Field(description="Location Name", min_items=1)
