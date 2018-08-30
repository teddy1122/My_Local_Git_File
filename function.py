def xxx(x,n = 2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s
	
print(xxx(4,3))

def product(*numbers):
	result = 1
	for x in numbers:
		result = result * x
	return result
print('product(5) =',product(5))
print('product(5,6) =',product(5,6))
print('product(5,6,7) =',product(5,6,7))
print('product(5,6,7,9) =',product(5,6,7,9))