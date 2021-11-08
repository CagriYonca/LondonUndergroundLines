from fastapi import FastAPI
from typing import Optional
from server.routes.station import router as StationRouter

app = FastAPI()
app.include_router(StationRouter, prefix="/station", tags=["Station"])


@app.get("/", tags=["Root"])
async def root():
    return {"message": "Hello World"}

@app.get("/lines")
def get_lines():
    return get_data_from_db("line")

@app.get("/stations")
def get_stations(line_id: Optional[int] = None):
    if line_id is not None:
        return get_data_from_db("station", line_id=line_id)
    else:
        return get_data_from_db("station")