print ("Wage Calculator")
weeklyHours=input("Enter work hours: ")
hourlyWage=input("Enter pay rate: ")
weeklyPay=weeklyHours*hourlyWage
if weeklyHours>40:
	overtimeWage=hourlyWage*1.5
	overtimeAmount=(weeklyHours-40)*overtimeWage
	weeklyHours=40
	weeklyPay=weeklyHours*hourlyWage+overtimeAmount
weeklyPay=str(weeklyPay)
message="The weekly pay is $"
print (message+weeklyPay)