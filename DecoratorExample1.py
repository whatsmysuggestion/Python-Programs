def decorator(*args, **kwargs):
	print("Inside decorator")
	def inner(fun):
		print("Inside inner function")
		print("I like", kwargs['like'])
		return fun
	return inner

@decorator(like = "testing")
def func():
	print("Inside")

func()
