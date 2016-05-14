def validateUserInput(rawUserInput):
    try: 
        validUserInput = float(rawUserInput)
        return validUserInput
    except: 
        print("Data must be entered as a number!")
        rawUserInput = input("Please enter number: ")
        return validateUserInput(rawUserInput)

def calculateWeeklyPay(weeklyHours, hourlyWage):
    if weeklyHours > 40:
        overtimeWage = hourlyWage * 1.5
        overtimeAmount = (weeklyHours - 40) * overtimeWage 
        weeklyHours = 40
    else: 
        overtimeAmount = 0
    weeklyPay = weeklyHours * hourlyWage + overtimeAmount 
    return weeklyPay

def main(): 
    print("Weekly Wage Calculator")
    rawUserHours = input("Enter work hours: ")
    validUserHours = validateUserInput(rawUserHours)
    rawUserWage = input("Enter pay rate: ") 
    validUserWage = validateUserInput(rawUserWage)
    screenOutput = calculateWeeklyPay(validUserHours, validUserWage)
    screenOutput = str(screenOutput)
    print("Weekly pay is $" + screenOutput)

main()