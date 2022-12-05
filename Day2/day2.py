scoreDictPlayer2 = {'A':{'X':4,'Y':8,'Z':3}, 'B': {'X':1,'Y':5,'Z':9}, 'C': {'X':7,'Y':2,'Z':6}}
scoreDictPart2 = {'A':{'X':3,'Y':4,'Z':8}, 'B': {'X':1,'Y':5,'Z':9}, 'C': {'X':2,'Y':6,'Z':7}}
with open('input.txt','r') as file:
	score = 0
	score2 = 0
	for line in file:
		them,you = line.strip().split(' ')
		print(them,you)
		score += scoreDictPlayer2[them][you]
		score2 += scoreDictPart2[them][you]
	print(score)
	print(score2)
