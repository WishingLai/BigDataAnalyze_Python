#####################################
#           A1035537賴煒勛          #
#           2018/3/5  lab_1_p2      #
#####################################

import matplotlib.pyplot as plt
import operator

##Open file
file = open("word.txt", "r", encoding="utf8")

book = dict()
names = []
symbol = "\"\'?!,.*[]#:-"      ##Symbol that need to replace

##逐行讀取直到檔案尾
for line0 in file:
    for element in symbol:           ##Replace symbol from every word
        line0 = line0.replace(element,'')
    line0 = line0.lower()
    words = line0.split()            ##split every line
    for word in words:               ##Search the list "words"
        book[word] = book.get(word,0) + 1

"""""
sorted_book = sorted(book.items(), key=operator.itemgetter(1))
for a in range(10):
    print(sorted_book[a][0],sorted_book[a][1])
"""""

#sort
value_count = sorted(book.items(), key=lambda d: d[1],reverse=True)

#plot
R = 10
plt.title("Word_Count",color="r")
plt.xlabel("word",color="r")
plt.ylabel("number",color="r")
#in matplotlib,the output will be sorted by category, hence alphabetically...this is a bug#plt.bar([value_count[i][0] for i in range(10)], [value_count[i][1] for i in range(10)],color = 'r')
plt.bar(range(R), [value_count[i][1] for i in range(10)], align='center')
plt.xticks(range(R), [value_count[i][0] for i in range(10)])
plt.show()


"""""

for line in file:
    ##line = line.rstrip()
    ##items = line.strip().split(' ')
    words = line.split()
    print('Words:',words)

    ##print(items)
    ##['a','a','a']

    for word in words:
        book[word] = book.get(word,0) + 1

"""""

"""
    for word in items:
        print(word)
        for word in names:
            if word not in book:
                book[word] = 1
            else:
                book[word] = book[word] + 1
"""


##print(book)
file.close()