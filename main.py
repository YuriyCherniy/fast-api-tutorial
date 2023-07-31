from datetime import date

from fastapi import FastAPI, Query, Depends
from pydantic import BaseModel


app = FastAPI()


class HotelSearchArgs():
    def __init__(
        self,
        locations: str,
        date_from: date,
        date_to: date,
        has_spa: bool|None = None,
        stars: int|None = Query(None, lt=5, gt=1)
    ):
        locations = self.locations
        date_from = self.date_from
        date_to = self.date_to
        has_spa = self.has_spa
        stars = self.stars


@app.get('/hotels')
def get_hotels(
    search_args: HotelSearchArgs = Depends()
):
    return search_args


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post('/bookings')
def add_booking(booking: SBooking):
    pass