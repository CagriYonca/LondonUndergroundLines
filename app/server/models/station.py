from typing import Optional
from pydantic import BaseModel, Field

class StationSchema(BaseModel):
    fid: int = Field(...)
    objectid: int = Field(...)
    name: str = Field(...)
    easting: int = Field(...)
    northing: int = Field(...)
    lines: str = Field(...)
    network: str = Field(...)
    zone: int = Field(...)
    x: float = Field(...)
    y: float = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fid": 0,
                "objectid": 78,
                "name": "Temple",
                "easting": 530959,
                "northing": 180803,
                "lines": "District, Circle",
                "network": "London Underground",
                "zone": 1,
                "x": -0.112643564,
                "y": 51.5104742
            }
        }

class UpdateStationModel(BaseModel):
    fid: Optional[int]
    objectid: Optional[int]
    name: Optional[str]
    easting: Optional[int]
    northing: Optional[int]
    lines: Optional[str]
    network: Optional[str]
    zone: Optional[int]
    x: Optional[float]
    y: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "fid": 1,
                "objectid": 80,
                "name": "Temple",
                "easting": 400000,
                "northing": 100000,
                "lines": "District, Circle",
                "network": "London Underground",
                "zone": 1,
                "x": -0.112643564,
                "y": 51.5104742
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "message": message,
        "code": 200
    }

def ErrorResponseModel(message):
    return {
        "error": error,
        "code": code,
        "message": message
    }