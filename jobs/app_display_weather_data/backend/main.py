from typing import Union, List
from datetime import datetime

from pydantic import BaseModel
import pandas as pd
import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_FNAME = 'weatherstats_winnipeg_forecast_daily.csv'


class Item(BaseModel):
    date_time_local: Union[str, None] = None
    unixtime: Union[str, None] = None
    period_index: Union[str, None] = None
    period_string: Union[str, None] = None
    cloudprecip: Union[str, None] = None
    snowlevel: Union[str, None] = None
    visibility_wind: Union[str, None] = None
    visibility_other: Union[str, None] = None
    precipitation: Union[str, None] = None
    winds: Union[str, None] = None
    temperatures: Union[str, None] = None
    windchill: Union[str, None] = None
    humidex: Union[str, None] = None
    uv: Union[str, None] = None


@app.post("/")
async def post_weather(items: Union[Item, List[Item]]):
    if isinstance(items, Item):
        items_as_dicts = [items.dict()]
    else:
        items_as_dicts = [item.dict() for item in items]
    df_new = pd.DataFrame(items_as_dicts)
    # Question doesn't say anything about allowing duplicates or not
    # df_existing = pd.read_csv(DB_FNAME)
    # df = pd.concat([df_existing, df_new]).drop_duplicates().reset_index(drop=True)
    df_new.to_csv(DB_FNAME, mode='a', index=False, header=False)
    return "added new data to db"


@app.get("/")
async def get_weather(start_date=None, start_time=None):
    df = pd.read_csv(DB_FNAME)
    df = df.fillna('')
    df.date_time_local = pd.to_datetime(df.date_time_local)
    if not start_date:
        return
    start = datetime.strptime(start_date, '%m/%d/%Y')
    df['day'] = df.date_time_local.dt.floor('D')
    df['hour'] = df.date_time_local.dt.floor('H')
    if start_time:
        start = start.replace(hour=int(start_time))
        df2 = df.loc[df.hour == start]
    else:
        df2 = df.loc[df.day == start]
    df3 = df2.drop(['day', 'hour'], axis=1).sort_values(['date_time_local', 'period_index'])
    return df3.to_dict('records')


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
