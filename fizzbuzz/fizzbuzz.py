#!usr/bin/env python

def FizzBuzz(numero):

	if not numero % 3 and not numero % 5:
		return 'fizzbuzz'

	if not numero % 5:
		return 'buzz'

	if not numero % 3:
		return 'fizz'
	
	return numero