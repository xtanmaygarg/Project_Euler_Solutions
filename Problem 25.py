def fib(max_lenght):
	a, b = 1, 1
	term = 1
	while len(str(a)) < max_lenght:
		term += 1
		a, b = b, a + b
	return term
print(fib(1000))
