import sys
from age_calculator import age_calculation_student_data
from dob_calculator import dob_calculation_student_data

print('''
    ====================================================
                        AGE/DOB CALCULATOR
    ====================================================

    1. Calculate Age
    2. Calculate Birth Year
    3. Exit
    
    ''')
user_input = int(input("What do you want to do? "))

if user_input == 3:
    sys.exit
elif user_input == 2:
    print('''
        ====================================================
                         DOB CALCULATOR
        ====================================================
        ''')
    year_now  = int(input("Enter  present year:")) #Asking for input for ongoing year.
    month_now = int(input("Enter present month:")) #Asking for input for ongoing month.
    day_now = int(input("Enter present Day:")) #Asking for input for ongoing day.
    age_year = int(input("How old are you? (year): "))
    age_month = int(input("How old are you? (month): "))
    age_day = int(input("How old are you? (day): "))
    dob_calculation_student_data(year_now, month_now, day_now, age_year, age_month, age_day)

elif user_input == 1:
    print('''
        ====================================================
                          AGE CALCULATOR
        ====================================================
    ''')
    year_now  = int(input("Enter  present year:")) #Asking for input for ongoing year.
    month_now = int(input("Enter present month:")) #Asking for input for ongoing month.
    day_now = int(input("Enter present Day:")) #Asking for input for ongoing day.
    year_birth  = int(input("Enter your birth year:")) #Asking for input for birth year.
    month_birth = int(input("Enter your birth Month:")) #Asking for input for birth month.
    day_birth = int(input("Enter your Birth Day:")) #Asking for input for birth day.
    age_calculation_student_data(year_now , month_now , day_now , year_birth ,month_birth , day_birth)
