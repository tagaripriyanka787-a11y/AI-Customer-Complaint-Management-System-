from pydantic import BaseModel
class ComplaintCreate(BaseModel):
    name:str
    email:str
    complaint:str
    
