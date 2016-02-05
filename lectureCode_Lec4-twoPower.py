# From Lecture 4, How Environments Separate Variable Bindings

def squareOut(x):
    return x*x

def twoPower(x,n):
	def square(x):
		print 'from square:' + str(x*x)
		return x*x
	while n > 1:
		x = square(x)
		n = n/2
	return x

x = 5
n = 1
print twoPower(2,8)
print x
print n

print 'square of 3:' + str(squareOut(3))
print 'square of 2:' + str(squareOut(2))