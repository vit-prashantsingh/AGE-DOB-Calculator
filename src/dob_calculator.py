#Defining a function which does the calculation of the age of the user on the basis of the given data
def dob_calculation_student_data(year_now, month_now, day_now, age_year, age_month, age_day):
    dob_year = str((year_now - age_year))
    dob_month = str((month_now - age_month))
    dob_day = str((day_now - age_day))
    print(f"You were born on: {dob_day}/{dob_month}/{dob_year}")