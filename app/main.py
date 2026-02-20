from fastapi import FastAPI, HTTPException, Query
from app.date_utils import calculate_days_difference
import uvicorn

app = FastAPI()

@app.get("/deadline_checker")
def deadline_checker(event_date: str = Query(...)):
    try:
        days = calculate_days_difference(event_date)
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Invalid date format. Please use YYYY-MM-DD."
        )

    return {"days_remaining": days}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
