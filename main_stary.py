import calculator
import speed
import calculations.calculator

# distance = float(input("Please enter distance of your travel:"))
# time = float(input("Please enter time of your travel:"))
#
# avg_speed = speed.speed_count(distance, time)

# a = float(input("Please enter a of triangle:"))
# b = float(input("Please enter b of triangle:"))
#
# c = speed.triangle_calc(a,b)

invested_capital = int(input("Please enter quote to investment:"))
percentage = int(input("Please enter percentage:"))
duration_in_years = int(input("Please enter duration in years:"))

qote_with_profit = calculator.invest_calc(invested_capital,percentage,duration_in_years)

print(f"Your profit is {qote_with_profit:.2f}")
