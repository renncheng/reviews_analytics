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
sum_length = 0
for d in data:
	sum_length += len(d)
print('Total length of the messages is', sum_length)
print('The average length of the messages is', sum_length/len(data))

