longest_word = "pneumonoultramicroscopicsilicovolcanoconiosis"
# for each_item in longest_word:
#     if each_item == 'o':
#         break
#     print(each_item)

# for num in range(1, 21):
#     print(num)
    
count = 0
for i in longest_word:
    if i == 'o':
        count += 1
        if count == 6:
            break
    print(i)
else:
    print('End')