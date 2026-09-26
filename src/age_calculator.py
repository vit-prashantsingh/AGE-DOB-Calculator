#Defining a function which does the calculation of the age of the user on the basis of the given data
def age_calculation_student_data(year_now , month_now , day_now , year_birth ,month_birth , day_birth):
    age_now_years = str((year_now - year_birth))
    age_now_months = str((month_now - month_birth))
    age_now_days = str((day_now - day_birth))
    print ("Your currently "+age_now_years+"years,"+age_now_months+"months and "+age_now_days+"days old ")