import numpy as np

C_values = np.array([150E-12, 180E-12, 270E-12, 560E-12, 820E-12, 1E-9, 1.5E-9, 2E-9, 2.2E-9, 2.7E-9, 3.3E-9, 4.7E-9, 5.6E-9, 6.8E-9, 8.2E-9, 10E-9, 12E-9, 22E-9, 33E-9, 39E-9, 47E-9, 100E-9, 150E-9, 220E-9, 330E-9, 1E-6])
R_values = np.array([10.0, 100.0, 120.0, 150.0, 220.0, 330.0, 390.0, 560.0, 1E3, 1.2E3, 1.5E3, 1.8E3, 2.2E3, 2.7E3, 3E3, 3.3E3, 3.9E3, 4.7E3, 5.6E3, 6.2E3, 10E3, 12E3, 15E3, 20E3, 22E3, 27E3, 33E3, 39E3, 47E3, 56E3, 82E3, 100E3, 220E3, 300E3, 470E3, 820E3])

def to_unit(num, sf=3):
	"""Round a number to the specified significant figures (default is 3) and add the corresponding unit prefix.

	Args:
		var (float): number to be formatted.
		sf (int, optional): Significant figures. Defaults to 3.

	Returns:
		string: formatted number and unit prefix.
	"""
	units = ['', 'k', 'M', 'G', 'T', 'p', 'n', 'u', 'm']
	e_count = 0
	value, e_count = get_exp(num)

	if e_count > 4 or e_count < -4:
		return '{:.{}g}'.format(num, sf-1).rstrip('0').rstrip('.')
	else:
		return np.format_float_positional(value, precision=sf, unique=True, fractional=False, trim='-') + units[e_count]
	
def get_exp(num):
	"""Normalize a number to its engineering notation.

	Args:
		num (float): number to be normalized.

	Returns:
		float: normalized number.
		int: exponent of 1000 that num was divided by.
	"""
	e_count = 0
	value = num
	while e_count <= 4 and e_count >= -4:
		if 1 <= value < 1E3:
			break
		if value >= 1E3:
			value /= 1E3
			e_count += 1
		if value < 1:
			value *= 1E3
			e_count -= 1
	return value, e_count

def get_unit_prefix(num):
	prefix = ['', 'k', 'M', 'G', 'T', 'p', 'n', 'u', 'm']
	x, e_count = get_exp(num)

	if e_count > 4:
		unit_prefix = prefix[4]
	elif e_count < -4:
		unit_prefix = prefix[4]
	else:
		unit_prefix = prefix[e_count]

	return unit_prefix

def parallel(R1, R2):
	R = 1/(1/R1 + 1/R2)
	return R
