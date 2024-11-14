from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class Wage(BaseModel):
    salary: Optional[float] = None
    bonus: Optional[float] = None
    taxes: Optional[float] = None

@app.post("/calculate_wage")
async def calculate_wage(wage: Wage):
    missing_fields = [field for field in ["salary", "bonus", "taxes"] if getattr(wage, field) is None]
    if missing_fields:
        missing_field = ", ".join(missing_fields)
        return {"error": f"3 fields expected (salary, bonus, taxes). You forgot: {missing_field}."}

    for key, value in wage.model_dump().items():
        if not isinstance(value, (int, float)):
            return {"error": "expected numbers, got strings."}

    total_compensation = wage.salary + wage.bonus - wage.taxes
    return {"wage": total_compensation}
