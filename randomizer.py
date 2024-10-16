import json
import random
from datetime import datetime, timedelta

# Given data from usd_rate.json
usd_rate_data = {
    "base": "USD",
    "date": "2024-10-16",
    "rates": {
        "USD": 1,
        "AED": 3.67,
        "AFN": 67.15,
        "ALL": 90.55,
        "AMD": 387.35,
        "ANG": 1.79,
        "AOA": 915.82,
        "ARS": 980.58,
        "AUD": 1.49,
        "AWG": 1.79,
        "AZN": 1.7,
        "BAM": 1.8,
        "BBD": 2,
        "BDT": 119.5,
        "BGN": 1.8
    }
}

# Prepare the time series data
start_date = datetime.strptime(usd_rate_data["date"], "%Y-%m-%d")
time_series_data = {
    "base": usd_rate_data["base"],
    "rates": {}
}

# Generate daily rates for 3 months
for i in range(90):  # 90 days for 3 months
    current_date = start_date + timedelta(days=i)
    date_key = current_date.strftime("%Y-%m-%d")

    # Create a new rates dictionary for the current date
    daily_rates = {}
    for currency, rate in usd_rate_data["rates"].items():
        # Introduce random variations
        if currency in ["USD", "AED", "AUD"]:  # Small fluctuations
            variation = random.uniform(-0.05, 0.05)  # ±5 cents
        elif currency in ["ARS", "BDT", "AOA"]:  # Larger fluctuations
            variation = random.uniform(-0.1, 0.1)  # ±10 cents
        else:  # Drastic fluctuations for others
            variation = random.uniform(-0.5, 0.5)  # ±50 cents
        
        # Ensure rates do not go below zero
        new_rate = max(0, round(rate + variation, 2))
        daily_rates[currency] = new_rate

    time_series_data["rates"][date_key] = daily_rates

# Save the time series data to a JSON file
output_file = 'usd_rate_time_series_fluctuated.json'
with open(output_file, 'w') as json_file:
    json.dump(time_series_data, json_file, indent=4)

print(f"Time series data with fluctuations saved to {output_file}")