from datetime import datetime, date

date_of_birth = input("enter date of birth (DD-MM-YYYY): ")

print(date_of_birth)

dob = datetime.strptime(date_of_birth, "%d-%m-%Y").date()

print(dob)

today_date = date.today()

print(today_date)

age = today_date - dob

age_in_days = age.days

print(f"Your age in days: {age_in_days}")