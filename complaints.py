from fastapi import APIRouter
from schemas.complaint_schema import ComplaintCreate

router = APIRouter()

complaints = []


@router.get("/complaints")
def get_complaints():
    return{
        "status": "success", "complaints": complaints
    }
@router.post("/complaints")
def create_complaint(data:ComplaintCreate):
    complaints.append(data.dict())
    return {
        "message": "Complaint created successfully", "complaint": data
    }