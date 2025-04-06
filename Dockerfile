FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY vwap_calculator.py .

# Install uv and set up virtual environment
RUN pip install uv && \
    uv venv && \
    . .venv/bin/activate && \
    uv pip install --no-cache-dir -r requirements.txt

# Use the virtual environment's Python
CMD [".venv/bin/python", "vwap_calculator.py"]
