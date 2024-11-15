from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
import pandas as pd

app = FastAPI()

class StateBuilding(str, Enum):
    good_as_new = "GOOD_AS_NEW"
    requires_renovation  = "REQUIRES_RENOVATION"

class PropertyType(str, Enum):
    apartment = "APARTMENT"
    house = "HOUSE"

class EquippedKitchen(str, Enum):
    not_installed = "NOT_INSTALLED"
    semi_equipped = "SEMI_EQUIPPED"
    equipped = "EQUIPPED"
    hyper_equipped = "HYPER_EQUIPPED"

class EPC(str, Enum):
    a_plus_plus = "A++"
    a_plus = "A+"
    a = "A"
    b = "B"
    c = "C"
    d = "D"
    e = "E"
    f = "F"
    g = "G"

class Property(BaseModel):
    state_building: StateBuilding
    property_type: PropertyType
    zip_code: int
    construction_year: int
    nbr_bedrooms: int
    equipped_kitchen: EquippedKitchen
    fl_furnished: bool
    terrace_sqm: float
    garden_sqm: float
    fl_swimming_pool: bool
    epc: EPC

@app.post("/predict_price")
async def predict_price(property: Property):
    data = {
        "state_building": property.state_building,
        "property_type": property.property_type,
        "zip_code": property.zip_code,
        "construction_year": property.construction_year,
        "nbr_bedrooms": property.nbr_bedrooms,
        "equipped_kitchen": property.equipped_kitchen,
        "fl_furnished": property.fl_furnished,
        "terrace_sqm": property.terrace_sqm,
        "garden_sqm": property.garden_sqm,
        "fl_swimming_pool": property.fl_swimming_pool,
        "epc": property.epc
    }

    df = pd.DataFrame(data)

    return "Work in progress"
