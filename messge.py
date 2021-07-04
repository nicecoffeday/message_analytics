data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count %10000 == 0:
			print(len(data))
print('Finshed, It have', len(data), 'message')

print(data[0])	

wc = {} # word_count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1
for word in wc:
	if wc[word] > 100:
		print(word, wc[word])

while True:
	word = input('What do you want:')
	if word == 'q':
		break
	if word in wc:
		print(word, 'times', wc[word])
	else:
		print('none')
print('think your welcom')















# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)
# print('It have', len(new), 'message lend less than 100')
# print(new[0])
# print(new[1])

# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(a)
# # print('It have', len(good), 'message mention good')