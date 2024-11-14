from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional, Dict

app = FastAPI()

class Wage(BaseModel):
    salary: Optional[float] = Field(..., description="The base salary amount")
    bonus: Optional[float] = Field(..., description="The bonus amount")
    taxes: Optional[float] = Field(..., description="The tax amount to be subtracted")

@app.post("/calculate_wage")
async def calculate_wage(wage: Wage):
    """required_fields = {"salary", "bonus", "taxes"}
    missing_fields = required_fields - wage
    if missing_fields:
        missing_field = ", ".join(missing_fields)
        return {"error": f"3 fields expected (salary, bonus, taxes). You forgot: {missing_field}."}

    for key, value in wage.items():
        if not isinstance(value, (int, float)):
            return {"error": "expected numbers, got strings."}"""

    total_compensation = wage.salary + wage.bonus - wage.taxes
    return {"result": total_compensation}
