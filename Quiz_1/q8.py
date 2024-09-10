import math

def probability_lower_bound(test_outcomes, deviation):
    card_D = len(test_outcomes)
    upper = 2*(math.e**(-2*card_D*(deviation**2)))
    return 1-upper

print(probability_lower_bound([True, False] * 500, 0.05))