# Reads input files, connects to Markov.py to generate the output story


# Split sentences by period and returns a list with all the sentences
def split_by_period():
    delimiters = '.!?'
    lines = list()
    novel = open('houn.txt', 'r')
    chapter = 'CHAPTER'

    # skip over title and arthur
    for i in range(4):
        novel.readline()

    for next_line in novel:
        one = next_line.rstrip('\n')
        two = one.lstrip(' ')
        if two == '':
            continue
        if chapter in two:
            novel.readline()
            continue
        final = remove_punctuation(two)  # TODO might have too do this step when I figure out how to split by period
        lines.append(final)

    novel.close()
    print(lines)
    # TODO clean and lowercase all into the list


# removes punctuation from an input sentence
# inspired by: https://www.geeksforgeeks.org/removing-punctuations-given-string/
def remove_punctuation(sentence: str):
    # Regular expression
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for x in sentence.lower():
        if x in punctuations:
            sentence = sentence.replace(x, "")
    return sentence


split_by_period()
