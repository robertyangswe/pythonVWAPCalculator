FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY vwap_calculator.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "vwap_calculator.py"]
