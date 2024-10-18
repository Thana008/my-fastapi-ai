from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# โมเดลสำหรับรับข้อมูลจากการส่ง POST
class AnalyzeRequest(BaseModel):
    name: str
    age: int

# เส้นทางที่สร้าง API
@app.post("/analyze")
async def analyze(request: AnalyzeRequest):
    # ตัวอย่างผลลัพธ์จากการวิเคราะห์ (แทนที่ด้วยโมเดล AI จริงในอนาคต)
    analysis_result = f"{request.name} is {request.age} years old. Analysis complete."
    
    return {
        "data": {
            "name": request.name,
            "age": request.age,
            "analysis_result": analysis_result
        },
        "message": "Analysis successful"
    }
