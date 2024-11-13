from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional, Dict

app = FastAPI()

@app.get("/multiply/{number}")
async def read_number(number: int):
    return {"double": number * 2}

class SalaryData(BaseModel):
    salary: Optional[float] = Field(..., description="The base salary amount")
    bonus: Optional[float] = Field(..., description="The bonus amount")
    taxes: Optional[float] = Field(..., description="The tax amount to be subtracted")

@app.post("/calculate_wage")
async def calculate_wage(data: Dict[str, Optional[float]]):
    required_fields = {"salary", "bonus", "taxes"}
    missing_fields = required_fields - data.keys()
    if missing_fields:
        missing_field = ", ".join(missing_fields)
        return {"error": f"3 fields expected (salary, bonus, taxes). You forgot: {missing_field}."}

    for key, value in data.items():
        if not isinstance(value, (int, float)):
            return {"error": "expected numbers, got strings."}

    total_compensation = data["salary"] + data["bonus"] - data["taxes"]
    return {"result": total_compensation}
