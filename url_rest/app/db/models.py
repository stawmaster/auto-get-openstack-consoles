from pydantic import BaseModel
from typing import Dict



class Request(BaseModel):
    template_id: int
    arguments: Dict