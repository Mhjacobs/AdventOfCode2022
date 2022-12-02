

def getElves():
	elves = [0]
	i = 0
	with open('input.txt', 'r') as file:
		for line in file:
			if line == '\n':
				i += 1
				elves.append(0)
			else:
				elves[i]+= int(line)
	
	elves.sort(reverse=True)
	print('q1:',elves[0])
	print('q2:',sum(elves[0:3]))
			




getElves()



