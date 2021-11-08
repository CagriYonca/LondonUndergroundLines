import motor.motor_asyncio

from bson.objectid import ObjectId
from decouple import config

MONGO_DETAILS = config('MONGO_DETAILS')

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.stations

station_collection = database.get_collection("stations_collection")


def station_helper(station) -> dict:
    return {
            "fid": str(station["fid"]),
            "objectid": str(station["objectid"]),
            "name": station["name"],
            "easting": station["easting"],
            "northing": station["northing"],
            "lines": station["lines"],
            "network": station["network"],
            "zone": station["zone"],
            "x": station["x"],
            "y": station["y"],
        }

station = {
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

async def retrieve_stations():
    stations = []
    async for station in station_collection.find():
        stations.append(station_helper(station))
    return stations

async def retrieve_station(id: str, data: dict) -> dict:
    station = await station_collection.find_one({"fid": ObjectId(id)})
    if station:
        return station_helper(station)

