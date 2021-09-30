
def revise(infile,outfile): #Filters out unwanted words. Excludes cwm and crwth
    vowels = 'aeiouy'
    string = '.,/;[]\\_=<>?:\"{}|+!@#$%^&*()' #no - or '
    with open(infile,"r") as f:
        all_lines = f.readlines()
    words = [word[:-1].lower() for word in all_lines]
    lines = ([word + "\n" for word in words if
              not any(['0123456789'[i] in word for i in range(10)]) #no numbers
              and not word == word.upper() #not all caps
              and not any([string[i] in word for i in range(len(string))]) #no symbol except - and '
              and any([i for i in vowels if i in word]) #at least 1 vowel
              ])
    with open(outfile,'w') as f:
        f.writelines(lines)
        
def cv_ratios(words, c_or_v): #c:v ratio or v:c ratio
    cons = "bcdfghjklmnpqrstvwxz" #y is a vowel
    vowels = "aeiouy"
    v_counts = [sum([word.count(vowel) for vowel in vowels]) for word in words]
    c_counts = [sum([word.count(con) for con in cons]) for word in words]
    if c_or_v == 'v':
        return [round(v_counts[i] / c_counts[i],3) if c_counts[i] else v_counts[i] for i in range(len(words))]
    elif c_or_v == 'c':
        return [round(c_counts[i] / v_counts[i],3) if v_counts[i] else c_counts[i] for i in range(len(words))]

def by_length(words, Length):
    words.sort(key=len, reverse=False)
    words_list = [words[i] for i in range(len(words)) if len(words[i]) == Length]
    length = len(words_list)
    return words_list

def words_from_letters(words, arr): # words contains only arr letters. Make sure lowercase.
    alf = 'abcdefghijklmnopqrstuvwxyz'
    letters = sorted(list(set(arr)))
    counts = [arr.count(letters[i]) for i in range(len(letters))]
    print(letters)
    print(counts)
    outWords = [word for word in words if
                not any([i for i in word if i not in letters])
                and not any([1 for i in range(len(letters)) if word.count(letters[i]) > counts[i]]
                )]
    outWords.sort()
    outWords.sort(key=len, reverse=True)
    return outWords

if __name__ == "__main__":
    #revise("words.txt","revised.txt")
    with open("by_pop.txt","r") as f:
        all_lines = f.readlines()[0:100000]
    words = [word[:-1].lower() for word in all_lines]
    outwords = words_from_letters(words, 'tenletters')
    print(outwords[:20])

