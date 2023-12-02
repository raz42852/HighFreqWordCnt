import sys

def WordListFile(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        data = data.replace("\n"," ")
        words = data.split(' ')
        return words
    except TypeError:
        print("Only integers are allowed")

def ListToCntDict(words):
    dict_words = {}
    for word in words:
        if word in dict_words:
            dict_words[word] += 1
        else:
            dict_words[word] = 1
    return dict_words

def SortedByFrequent(dict_cnt):
    return list(sorted(dict_cnt, key=lambda x: dict_cnt[x], reverse=True))

def PrintHighFreqWords(list_sorted):
    global dict_cnt
    try:
        for x in range(int(sys.argv[1])):
            print(x + 1, "- word '", list_sorted[x], "'", dict_cnt[list_sorted[x]], "times")
    except IndexError:
        print("You have only", len(dict_cnt), "words in the file and not", sys.argv[1])
    except ValueError:
        print("Only integers are allowed")

if __name__ == '__main__':
    file_path = input("Enter the file path : ")
    words_list = WordListFile(file_path)
    dict_cnt = ListToCntDict(words_list)
    list_sorted = SortedByFrequent(dict_cnt)
    PrintHighFreqWords(list_sorted)