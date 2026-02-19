# CS361 (Group 17) - Small Pool Microservice: Deadline Checker

**What does this microservice do?**

This microservice allows the user to provide a date, and returns the the number of days between the current date and the provided date. It will return a positive number if the provided date is in the future, and a negative number if the provided date is in the past.

**How do I request data from this microservice?**

To request data from this microservice, you will need to make an `HTTP GET request` to the `/deadline_checker` endpoint. You must pass the `event_date` as a string in the form of `YYYY-MM-DD` as a query parameter.

_Example call:_ `GET http://127.0.0.1:8000/deadline_checker?event_date=2026-04-01`

**How will I receive data from this microservice?**

The microservice will return a `JSON object`. The object will have one name/value pair. The name/value pair will be `days_remaining` which is an integer representing the difference, in days, between the provided date and the current date.

_Example response (valid date, date is in the future)_:

Status code: `200`
```yaml
{
"days_remaining": 14
}
```

_Example response (valid date, date is in the past)_:

Status code: `200`
```yaml
{
"days_remaining": -3
}
```

_Example response (invalid date)_:

Status code: `400`
```yaml
{
"detail": "Invalid date format. Please use YYYY-MM-DD."
}
```
**UML Sequence Diagram**

<img width="585" height="395" alt="image" src="https://github.com/user-attachments/assets/249aef57-f88f-432f-8825-7f385ab33e06" />
