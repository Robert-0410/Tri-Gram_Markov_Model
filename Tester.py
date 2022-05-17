# Reads input files, connects to Markov.py to generate the output story

# TODO data structure that will hold words / phrases

# Split sentences by period and returns a list with all the sentences TODO skip over title, author, and chapters
def split_by_period():
    delimiters = '.!?'
    lines = list()
    novel = open('houn.txt', 'r')

    for i in range(15):  # TODO must parse entire file
        next_line = novel.readline().rstrip('\n')
        lines.append(next_line)

    novel.close()
    print(lines)
    return 0  # TODO temp return


# removes punctuation from an input sentence
# inspired by: https://www.geeksforgeeks.org/removing-punctuations-given-string/
def remove_punctuation(sentence: str):
    # Regular expression
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for x in sentence.lower():
        if x in punctuations:
            sentence = sentence.replace(x, "")
    return sentence


string = "Welcome???@@##$ to#$% Geeks%$^for$%^&Geeks. You going to learn today! Are you ready? YOu better be."
string2 = "welcome???@@##$ to#$% geeks%$^for$%^&geeks"
print(remove_punctuation(string))
print(remove_punctuation(string2))
split_by_period()
