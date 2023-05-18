from fastapi import FastAPI

app = FastAPI()


@app.post("/calculate")
async def calculate(num1: float, num2: float, operator: str):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        return {"error": "Invalid operator"}

    return {"result": result}
