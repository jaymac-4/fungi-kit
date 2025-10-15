# Import the matplotlib library so we can make graphs
import matplotlib.pyplot as plt

# Import pandas to help read and work with data stored in tables (like spreadsheets)
import pandas as pd

# Read the data from a CSV file (a text file where each line has values separated by commas)
# The 'r' before the string just means "read this exactly as it is"
data = pd.read_csv(r"C:\data.csv")

# Remove the first 200 rows and the last 100 rows from the data
# This might be done to get rid of messy or unwanted data at the start and end
data = data.iloc[200:-100]

# Make sure the chosen columns are numbers, not text.
# If something can't be turned into a number, it's replaced with NaN (a missing value)
for col in ["timestamp", "A0", "A1", "A2", "A3"]: 
    data[col] = pd.to_numeric(data[col], errors="coerce")

# Drop (remove) any rows that have missing values in these columns
data = data.dropna(subset=["timestamp", "A0", "A1", "A2", "A3"])

# Plot each of the sensor readings (A0–A3) over time
plt.plot(data["timestamp"], data["A0"], label="A0")
plt.plot(data["timestamp"], data["A1"], label="A1")
plt.plot(data["timestamp"], data["A2"], label="A2")
plt.plot(data["timestamp"], data["A3"], label="A3")

# Label the x-axis (horizontal) and y-axis (vertical)
plt.xlabel("Time")
plt.ylabel("Value (V)")

# Give the graph a title
plt.title("TITLE")

# Show a small box that explains which line is which
plt.legend()

# Display the graph on the screen
plt.show()
