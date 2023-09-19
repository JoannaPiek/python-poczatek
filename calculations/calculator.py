import math


def invest_calc(start_valu,percentage,duration):
    end_value = math.pow((start_valu*(1 + (percentage/100))), duration)
    print(f"You will earn {end_value:.2f}")
    return end_value
