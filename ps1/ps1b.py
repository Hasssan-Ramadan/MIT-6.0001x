annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input(
    "Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(
    input("Enter the semi­annual raise, as a decimal: "))

current_savings = 0.0
portion_down_payment = .25*total_cost
number_of_months = 0

while current_savings <= portion_down_payment:
    current_savings += portion_saved * \
        (annual_salary/12) + current_savings*(0.04/12)
    number_of_months += 1
    if number_of_months % 6 == 0:
        annual_salary += semi_annual_raise*annual_salary

print("Number of months: ", number_of_months)
