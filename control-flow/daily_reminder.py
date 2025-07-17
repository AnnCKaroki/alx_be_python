task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ").lower()

reminder_message = [f"'{task}' is a "]

match priority:
    case "high":
        reminder_message.append("high priority task ")
    case "medium":
        reminder_message.append("medium priority task ")
    case "low":
        reminder_message.append("low priority task ")
    case _:
        reminder_message.append("task of unknown priority")
        print("Error: Invalid priority entered")

if time_bound == "yes":
    reminder_message.append("that requires immediate attention today!")
elif time_bound == "no" and priority == "low":
    reminder_message.append(". Consider completing it when you have free time.")
elif time_bound != "no":
    print("Invalid time bound input!")

print('Reminder ', ''.join(reminder_message))
