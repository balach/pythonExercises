'''
	A simple method to return the sum of, the area of a regular polygon and its perimeter squared; limited to four decimal places.
	Hello.
	This is my first attempt at the polysum. Comments added for the sake of this exercise.
	Please do provide your feedback.
	I can be found on twitter.com/balatsch or facebook.com/balach
	Thank you.
'''
#Import math module for Tan and Pi
import math

#Method signature: takes two arguments, n is the number of sides of the polygon, and s is length of each side
def polysum(n,s):
	#calculate perimeter
	perimeter = n*s

	#calculate area according to the formula described in problem statement
	area = (0.25*n*(s**2))/math.tan(math.pi/n)

	#calculate sum
	sum = perimeter**2 + area

	#return sum by first using format to reduce it to max four decimal places (format returns a string), then cast it back to float	
	return float("{:.4f}".format(sum))

#test polysum works with a few example calls
print "Polysum of a polygon with three sides, each with length 4: " + str(polysum(3,4))
print "Polysum of a polygon with six sides, each with length 9: " + str(polysum(6,9))
print "Polysum of a polygon with ten sides, each with length 2: " + str(polysum(10,2))