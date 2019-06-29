import pprint,json
with open('rawquestion.txt', 'r') as file:
	text = file.read()
	a=text.split("#----------------------------------------#")
# print(a)

finalQuetionList = []
for rawQuestion in a[2:]:
	dict_={}
	rawQuestion = rawQuestion.strip()
	temp = rawQuestion.split('\n')
	q = ''
	if len(rawQuestion) != 0:
		if temp[1] == 'Level 1':
			level = 'easy'
		elif temp[1] == 'Level 2':
			level = 'medium'
		elif temp[1] == 'Level 3':
			level = 'hard'	
	for i in temp[4:]:
		if i=='Hints:':
			break
		q+=(i)
	dict_['id'] = len(finalQuetionList)+1
	dict_['challenge'] = q
	dict_['level'] = level


	if dict_['challenge'] != '':
		finalQuetionList.append(dict_)

# pprint.pprint(finalQuetionList)

with open('challenges2.json', 'w') as file:
	temp= json.dumps(finalQuetionList)
	file.write(temp)
	file.close()