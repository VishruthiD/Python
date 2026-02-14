# Payroll Program

# Input from user
hours = float(input("Enter total hours worked: "))
rate = float(input("Enter hourly rate: "))

# Check condition
if hours <= 40:
    regular_pay = hours * rate
    print("Regular Pay:", regular_pay)
else:
    overtime_hours = hours - 40
    regular_pay = 40 * rate
    overtime_pay = overtime_hours * (rate * 1.5)   # 1.5 times regular rate
    total_pay = regular_pay + overtime_pay
    
    print("Regular Pay:", regular_pay)
    print("Overtime Hours:", overtime_hours)
    print("Overtime Pay:", overtime_pay)
    print("Total Pay:", total_pay)
