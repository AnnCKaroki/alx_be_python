from datetime import datetime, timedelta

current_date = datetime.now()

def display_current_datetime():
    return current_date

display_current_datetime()

def calculate_future_age():
    future_date = int(input("Enter the number of days to add to the current date:"))
    calculate_future_date = current_date + timedelta(days= future_date)
    calculate_future_date = calculate_future_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Future date: {calculate_future_date}")

calculate_future_age()
