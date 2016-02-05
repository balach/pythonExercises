#import lectureCode_circle
from lectureCode_circle import *
print area(3)
x=4
y=5
def doSomething(x):
	return x + y
print x
print y
print doSomething(1)

#import math
def polysummine(n,s):
	perimeter = n*s
	area = (0.25*n*(s**2))/math.tan(math.pi/n)
	sum = "{:.4f}".format(perimeter**2 + area)
	return float(sum)


def vowelito(testString):
	numOfVowels = 0
	for vowel in ['a','e','i','o','u']:
		numOfVowels += testString.count(vowel)
		print "found " + str(testString.count(vowel)) + " " + vowel
	return numOfVowels


z = vowelito('abcdefs')
print "total vowels found" + str(z)

z = vowelito('azcbobobegghakl')
print "total vowels found" + str(z)

z = vowelito('azcbobobegghaklazcbobobegghakl')
print "total vowels found" + str(z)
