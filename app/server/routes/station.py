from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    retrieve_station,
    retrieve_stations
)

from server.models.station import (
    ErrorResponseModel,
    ResponseModel,
    StationSchema,
    UpdateStationModel
)

router = APIRouter()

@router.get("/")
async def get_stations():
    stations = await retrieve_stations()
    if stations:
        return ResponseModel(stations, "")
    return retrieve_stations()