import datetime

current_date = datetime.datetime.now()

def display_current_datetime():
    return current_date

display_current_datetime()

def calculate_future_age():
    future_date = int(input("Enter number of days to add to the current date: "))
    new_date = current_date + datetime.timedelta(days= future_date)
    new_date = new_date.strftime("%Y-%m-%d")
    print(f"Future date: {new_date}")

calculate_future_age()
