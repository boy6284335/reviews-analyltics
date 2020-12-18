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

count1 = 0
for d in data:
    if len(d) < 100:
        count1 += 1
    else:
        pass
print('總共有', count1, '筆資料長度小於100')

good = [d for d in data if 'good' in d]
print('總共有', len(good), '提到good')


# 文字計數
wc = {} # word_count
for d in data:
    words = d.split() # split()預設值就為空字串
    for word in words:
        if word in wc: # 字如果有出現在字典裡
            wc[word] += 1 
        else:
            wc[word] = 1 # 新增新的key進wc字典
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))

while True:
	word = input('請問你想查甚麼字: ')
	if word == 'q':
		break
	if word in wc:	
		print(word, '出現過的次數為', wc[word])
	else:
		print('留言中沒有出現過', word)
print('感謝您使用字典查詢功能~')

