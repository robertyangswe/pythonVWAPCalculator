# Stock VWAP Calculator for RSU

This project calculates the Volume Weighted Average Price (VWAP) for a stock over a specified time period. The analysis is broken down by month to provide detailed insights into price trends.

## Features

- Calculates VWAP for a stock from 2020 to 2025
- Monthly breakdown of VWAP values
- Dockerized application for easy deployment
- Error handling for periods with no available data

## Project Structure

- `vwap_calculator.py`: Main script that calculates VWAP
- `requirements.txt`: Python dependencies
- `Dockerfile`: Container configuration

## Requirements

- Python 3.9+
- yfinance library
- Docker (optional)

## Installation

### Local Setup
```bash
pip install -r requirements.txt
```

### Docker Setup
```bash
docker build -t vwap-calculator .
docker run vwap-calculator
```

## Output Format

The script outputs VWAP values in the following format:
```
=== YYYY ===
January: $XX.XX
February: $XX.XX
...
```

## Notes

- Future dates (2025+) will show "No data available" as they don't exist yet
- The script handles missing data gracefully
- VWAP is calculated using the formula: Σ(Price × Volume) / Σ(Volume)

## Development

This project was generated using [Cursor](https://cursor.sh), an AI-powered code editor that helps developers write, understand, and modify code more efficiently.
