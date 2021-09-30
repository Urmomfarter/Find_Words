
'''
with open('unigram_freq.csv', 'r') as f:
    lines = f.readlines()

newlines = [line[0:line.find(',')] + '\n' for line in lines[1:106000+1]]

with open('frequent_words.txt', 'w+') as f:
    f.writelines(newlines)
#print([line[0:line.find(',')] + '\n' for line in lines[1:10+1]])
'''

#Find words that are in frequent but not in words

with open('unigram_freq.csv', 'r') as f:
    lines = f.readlines()
with open('revised.txt', 'r') as f:
    revised = f.readlines()
revised = [word[:-1] for word in revised]

############################################

oldlines = [line for line in lines[1:333333]]
newlines = [line[0:line.find(',')] for line in lines[1:333333]]
with open('by_pop2.txt','a+') as f:
    with open('notwords2.txt', 'a+') as f2:
        for i in range(0,10000000):
            word = newlines[i]
            if word in revised:
                f.write(word + '\n')
            else:
                f2.write(word + '\n')
                print(word)

quit()

for i in range(100000,200000,1000): # 1000*i+1000 max, 1000*i min
    oldlines = [line for line in lines[i:i+1000]]
    newlines = [line[0:line.find(',')] for line in lines[i:i+1000]]
    newlines.sort()
    finalwords = []
    letter = ''
    for word in newlines:
        if word in revised:
            finalwords += word + "\n"
            '''
            if not word[0] == letter:
                letter = word[0]
                print(letter)'''
    filename = 'a' + str(i) + '.txt'
    #print(filename)
    with open(filename, 'w+') as f:
        f.writelines(finalwords)
    print(str(i) + " Done")














