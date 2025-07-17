task = input("Enter task description: ")
priority = input("Enter task priority (high, medium, low): ").lower()
time_bound = input("Is the task time bound (Yes, No)? ").lower()

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


if priority == "low" and time_bound == "no":
    starter = "Note:"
else:
    starter = "Reminder"



print(starter, ''.join(reminder_message))
