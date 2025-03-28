import pandas as pd
import numpy as np

# Generate synthetic data
data = {
    "distance_km": np.random.uniform(1, 50, 500),
    "start_lat": np.random.uniform(-1.9, 1.5, 500),
    "start_lon": np.random.uniform(29.0, 30.0, 500),
    "end_lat": np.random.uniform(-1.9, 1.5, 500),
    "end_lon": np.random.uniform(29.0, 30.0, 500),
    "weather": np.random.choice(["Sunny", "Rainy", "Cloudy"], 500),
    "temperature": np.random.uniform(15, 35, 500),
    "traffic_level": np.random.choice(["Low", "Medium", "High"], 500),
    "day_of_week": np.random.choice(["Weekday", "Weekend"], 500),
    "hour_of_day": np.random.randint(0, 24, 500),
    "journey_duration_min": np.random.randint(10, 120, 500),
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV file
df.to_csv("journey_data.csv", index=False)

print("CSV file 'journey_data.csv' has been created successfully.")