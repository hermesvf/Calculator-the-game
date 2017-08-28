from sys import argv

DEBUG = 0
EXPLORED = 0

def debug(s):
	if DEBUG == 1:
		print(s)

opts = []
actions = { '+':'addition', \
            '-':'substract',\
            '*':'product',  \
            '/':'division', \
            'X':'exchange', \
            'A':'append',   \
            'S':'alter_sign'\
            }

# Format: +5 -5 *5 /5 X144->50 A5 S

source, target, steps = [int(a) for a in argv[1:4]]
def addOptionNode(l,op):
	debug("Adding op "+op)
	id = op[0]
	if id == '+':
		l.append((lambda x: x + int(op.split(id)[1]),op))
	elif id == '*':
		l.append((lambda x: x * int(op.split(id)[1]),op))
	elif id == '/':
		l.append((lambda x: x / int(op.split(id)[1]),op))
	elif id == '-':
		l.append((lambda x: x - int(op.split(id)[1]),op))
	elif id == 'A':
		l.append((lambda x: x * 10 + int(op.split(id)[1]),op))
	elif id == 'S':
		l.append((lambda x: -x,'+/-'))
	elif id == 'X':
		l.append((lambda x: int(str(x).replace(op[1:].split('->')[0],\
		op[1:].split('->')[1])),op[1:]))


def evaluation(source, stack):
    evaluated = source
    for op in stack:
        evaluated = op[0](evaluated)
    debug("evaluation of source "+str(source)+ " with stack "\
     + str([op[1] for op in stack]) + " was " + str(evaluated))
    return evaluated

def searchInDepth(stack):
    global EXPLORED
    if len(stack) == steps:
        EXPLORED += 1
        debug("Stack completed")
        if evaluation(source,stack) == target:
            debug("*** TARGET FOUND ***")
            return stack
    else:
        if len(stack) < steps:
            for op in opts:
                stack.append(op)
                debug("+ stacking op " + op[1])
                ret = searchInDepth(stack)
                if ret is not None:
                	return ret
                debug("- unstacking op" + op[1])
                stack.pop()
def printHeader():
    print("Source: " + str(source) + " Target: " + str(target)\
    + " Steps: " + str(steps))

def main():
    printHeader()
    for arg in argv[4:]:
        addOptionNode(opts,arg)
    operations = searchInDepth([])
    if operations is not None:
        print([o[1] for o in operations])
        print ("solution found after", EXPLORED,"branches explored")
    else:
        print("No solution was found")

if __name__ == "__main__":
	main()
