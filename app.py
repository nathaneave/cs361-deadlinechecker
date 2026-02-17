from fastapi import FastAPI, HTTPException
from datetime import date

app = FastAPI()

@app.get("/deadline_checker")
def root(event_date: str):
    #event_date should be in the format YYYY-MM-DD
    #try to convert the provided values a date object, if not return 400 error code
    try:
        target_date = date.fromisoformat(event_date)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format")
    
    today = date.today()
    difference = target_date - today

    #since difference is a time delta object, we need to get the number of days from it and return that
    return {"days_remaining": difference.days}
