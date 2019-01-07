import cmath
import numpy as np

def quad_form(coef_a, coef_b, coef_c):

	sqrt_numerator = cmath.sqrt(coef_b**2 -4*coef_a*coef_c)
	denominator = 2*coef_a

	x_add =(-coef_b+sqrt_numerator)/denominator
	x_sub =(-coef_b-sqrt_numerator)/denominator

	x_values = [x_add, x_sub]
	x_values = np.sort(x_values)
	x_values = tuple(x_values)
	
	return x_values
