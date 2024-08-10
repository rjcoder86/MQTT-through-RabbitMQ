from fastapi import FastAPI
import uvicorn
from mongo_connector import MongoConnector
app = FastAPI()


@app.get('/get')
async def status_count(start_time, end_time ):
    connector = MongoConnector()
    connector.connect()
    data = connector.get_data(start_time, end_time)
    return data


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)