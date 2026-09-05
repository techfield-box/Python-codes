# 6.1 Payroll System

class Employee:
    def __init__(self, name, hourly_rate):
        self.name = name
        self.hourly_rate = float(hourly_rate)

    def calculate_weekly_salary(self, hours_worked):
        hours = float(hours_worked)

        if hours > 40:
            regular_pay = 40 * self.hourly_rate
            overtime_hours = hours - 40
            overtime_pay = overtime_hours * (self.hourly_rate * 1.5)
            return regular_pay + overtime_pay
        else:
            return hours * self.hourly_rate


# --- User Input Section ---
print("--- Payroll System Input ---")
name_input = input("Enter employee name: ")
rate_input = input("Enter hourly rate: ₹ ")
hours_input = input("Enter hours worked this week: ")


# Create the object and run the calculation
emp = Employee(name_input, rate_input)
total_salary = emp.calculate_weekly_salary(hours_input)


# Display result
print("-" * 30)
print(f"Weekly Salary for {emp.name}")
print(f"Total Amount: ₹{total_salary:.2f}")