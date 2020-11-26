words = []
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		for word in line:
			words.append(word)
		
print("檔案讀取完了，總共有", len(data), "筆資料")
print("每筆留言的平均長度為", len(words)/len(data))