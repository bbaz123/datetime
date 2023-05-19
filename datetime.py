# Import the datetime module
import datetime

# Get the current date
today = datetime.date.today()

# Set the target date
target = datetime.date(2024, 1, 1)

# Calculate the difference between the two dates
delta = target - today

# Print the result
print(f"There are {delta.days} days until January 1, 2024")
