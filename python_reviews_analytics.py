# python reviews-analytics


data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		count += 1
		data.append(line)
		if count % 10000 == 0:
			print('Count= ', count)
print('Loading successfully! There are', len(data), 'messages !!!')
#print('--------')
#print(data[0])
#print('--------')
#print(data[1])
#print('--------')
#print(data[2])

w_c = {}
for d in data:
	words = d.split()
	for word in words:
		if word in w_c:
			w_c[word] += 1 # Count number
		else:
			w_c[word] = 1 # Add a key in dictionary
for word in w_c:
	if w_c[word] > 100:
		print(word, w_c[word])
print('總共有', len(w_c), '個字')

while True:
	word = input('What word you want to search?')
	if word == 'q':
		break
	if word in w_c:
		print(word, '出現的次數為：', w_c[word])
	else:
		print('This word didnot exist.')
print('Thanks for using.')


sum_length = 0
for d in data:
	sum_length += len(d)
print('Total length of the messages is', sum_length)
print('The average length of the messages is', sum_length/len(data))

new = []
good = []
bad = []
for e in data:
	if len(e) < 100:
		new.append(e)
	if 'good' in e:
		good.append(e)
	if 'bad' in e:
		bad.append(e)
print('There are', len(new), 'messages length samller than 100. ')
print('Ther are', len(good), 'messages mentioned "good"')
print('Ther are', len(bad), 'messages mentioned "bad"')

# list comprehension!!!!
#good = [d for d in data if 'good' in d]
