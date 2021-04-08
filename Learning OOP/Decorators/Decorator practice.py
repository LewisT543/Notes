def decorator_function(origional_function):
	def wrapper_function():
		print(f'Wrapper executed this before {origional_function.__name__}.')
		return origional_function()
	return wrapper_function

@decorator_function
def display():
	print('display function ran')

display()