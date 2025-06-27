import calendar

print("List of Months:\n")

for month_num in range(1, 13):
    print(f"{month_num}: {calendar.month_name[month_num]}")
