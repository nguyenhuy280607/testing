import random
i = 0
for i in range(10):
	print(i*random.randrange(10))
	if i == 10:
		print('lucky')
	else: 
		print('unlucky')