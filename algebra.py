import cmath
import numpy as np

def quad_form(coef_a, coef_b, coef_c):

	sqrt_numerator = cmath.sqrt(coef_b**2 -4*coef_a*coef_c)
	denominator = 2*coef_a

	x_add =(-coef_b+sqrt_numerator)/denominator
	x_sub =(-coef_b-sqrt_numerator)/denominator

	unorg_values = [x_add, x_sub]
	for unorg_value in unorg_values:
		if unorg_value.imag == 0.0:
			x_values = [round(x_add.real,3) , round(x_sub.real, 3)]
		else:
			x_values = [x_add, x_sub]

	x_values = np.sort(x_values)
	x_values = set(x_values)
	
	if len(x_values) > 1:

		x_values = tuple(x_values)
	else:
		x_values = x_values.pop()
	
	return x_values

#print(quad_form(2,-4,-3))
#print(quad_form(3, 4, 3))
#print(quad_form(9,12,4))
