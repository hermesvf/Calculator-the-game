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

# Format: +5 -5 *5 /5 X144->50 A5 S L

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
		l.append((lambda x: int(str(x).replace(op[1:].split('->')[0],\
		op[1:].split('->')[1])),op[1:]))
	elif id == actions['shift_left']:
		l.append((lambda x: -((-x - -x%10) // 10) if x < 0 \
		else (x - x%10) // 10,'<<'))


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
		if evaluation(source,chain) == target:
			return chain
	return None

if __name__ == "__main__":
	source, target, steps = [int(a) for a in argv[1:4]]
	operations = []
	printHeader()
	collect_operations(operations)
	found = find_one_solution(operations)
	if found is not None:
		print("--- Target found ---")
		print([op[1] for op in found])
	else:
		print("No solution was found")
