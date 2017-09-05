#!/usr/bin/env python3

from sys import argv
from itertools import product

DEBUG = 0

def debug(s):
	if DEBUG == 1:
		print(s)

actions = { 'addition'  :'+', \
            'substract' :'-', \
            'product'   :'*', \
            'division'  :'/', \
            'exchange'  :'X', \
            'append'    :'A', \
            'alter_sign':'S', \
            'shift_left':'L'
			}

def usage():
	print("Usage: "+argv[0]+" <source> <target> <steps> <op_1> [<op_2> ... <op_n>]")
	usage = {}
	usage['addition  '] = "Adds one number. Example: +2"
	usage['substract '] = "Substracts one number. Example: -5"
	usage['product   '] = "Multiplies by one number. Examples: *6 , *-2"
	usage['division  '] = "Divides by one number. Examples: /4 , /-3"
	usage['exchange  '] = "Replaces the occurrences of some number x for some other y. Examples: X-12:3, X6:-9"
	usage['append    '] = "Appends a number to another. Example: A5"
	usage['alter_sign'] = "Is equivalent to multiply by -1. Usage: S"
	usage['shift_left'] = "Removes the last digit: Usage: L"
	print("  Operations available:")
	for k in usage.keys():
		print('\t'+k,':',usage[k])
	exit(1)

def addOptionNode(l,op):
	debug("Adding op "+op)
	id = op[0]
	if id == actions['addition']:
		l.append((lambda x: x + int(op.split(id)[1]),op))
	elif id == actions['product']:
		l.append((lambda x: x * int(op.split(id)[1]),op))
	elif id == actions['division']:
		l.append((lambda x: x / int(op.split(id)[1]),op))
	elif id == actions['substract']:
		l.append((lambda x: x - int(op.split(id)[1]),op))
	elif id == actions['append']:
		l.append((lambda x: x * 10 + int(op.split(id)[1]),op))
	elif id == actions['alter_sign']:
		l.append((lambda x: -x,'+/-'))
	elif id == actions['exchange']:
		l.append((lambda x: int(str(x).replace(str(int(op[1:].split(':')[0])),\
		str(int(op[1:].split(':')[1])))),\
		op[1:].split(':')[0]+'->'+op[1:].split(':')[1]))
	elif id == actions['shift_left']:
		l.append((lambda x: -((-x - -x%10) // 10) if x < 0 \
		else (x - x%10) // 10,'<<'))
	else:
		print("Unrecognized operation:", op)
		raise Exception()


def evaluation(source, stack):
	evaluated = source
	for op in stack:
		evaluated = op[0](evaluated)
	debug("evaluation of source "+str(source)+ " with stack "\
	+ str([op[1] for op in stack]) + " was " + str(evaluated))
	return evaluated

def printHeader():
    print("Source: " + str(source) + " Target: " + str(target)\
    + " Steps: " + str(steps))

def collect_operations(opts):
	for arg in argv[4:]:
		addOptionNode(opts,arg)

def find_one_solution(opts):
	for chain in product(opts,repeat=steps):
		try:
			if evaluation(source,chain) == target:
				return chain
		except:
			debug("exception catched during evaluation: "+str(source)+" "+\
			str([op[1] for op in chain]))
	return None

if __name__ == "__main__":
	if len(argv) < 5:
		usage()
	try:
		source, target, steps = [int(a) for a in argv[1:4]]
		operations = []
		collect_operations(operations)
	except:
		usage()
	printHeader()
	found = find_one_solution(operations)
	if found is not None:
		print("--- Target found ---")
		print([op[1] for op in found])
	else:
		print("No solution was found")
