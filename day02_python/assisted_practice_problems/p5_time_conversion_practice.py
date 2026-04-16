total_seconds = int(input("Enter the total seconds:"))

total_hours = total_seconds // 3600
total_minutes = (total_seconds % 3600) // 60
total_seconds = total_seconds % 60 % 3600

print(f"The total seconds give are:{total_seconds}\n" +
      f"Time duration of 3800 seconds in HH:MM:SS format is: {total_hours: 02d}:{total_minutes:02d}:{total_seconds:02d}")
