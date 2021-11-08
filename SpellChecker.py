import numpy as np

# calculate the number of insertions, deletions, or substititions it would take to 
# make str1 and str2 the same string *edit distance*
def ED(str1, str2):
    if len(str1) > len(str2):
        str1, str2 = str2, str1

    distances = range(len(str1) + 1)
    for idx2, char2 in enumerate(str2):
        dist = [idx2+1]
        for idx1, char1 in enumerate(str1):
            if char1 == char2:
                dist.append(distances[idx1])
            else:
                dist.append(1 + min((distances[idx1], distances[idx1 + 1], dist[-1])))
        distances = dist
    return distances[-1]


# read the words from the text file to create the dictionary
dictionary = []
with open('dictionary.txt') as f:
    dictionary = f.read().splitlines()

def main():
    dist = []
    word = input("Enter a word: ")
    threshold = (len(word) - (len(word) * 0.70)) # 70% of the word has to match
    for entry in dictionary:
        d = ED(word, entry)
        dist.append(d)
    distances  = np.array([dist])
    indices = np.argpartition(distances, 5)
    matches = []
    for i in range(5):
        idx = ((indices[0])[i])
        val = distances[0][idx]
        if(val < threshold):
            matches.append(dictionary[idx])
    # print out the like words, if there are any
    if(len(matches) > 0):
        print("Top words you could've meant: ")
        for i in range(len(matches)):
            print(matches[i])
    else:
        print("There are no words that are close to what was entered!")

main()