import math
hourlyWage = float(input("Enter the wage: "))
regularHours = float(input("Enter the regular hours:"))
overtimeHours = float(input("Enter the overtime hours:"))
overtimePay = overtimeHours * (1.5 * hourlyWage)
regularPay = hourlyWage * regularHours
totalPay = overtimePay + regularPay

print("The total weekly pay is", totalPay)
