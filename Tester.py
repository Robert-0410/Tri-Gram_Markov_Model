# Reads input files, connects to Markov.py to generate the output story

# removes punctuation from an input sentence
# inspired by: https://www.geeksforgeeks.org/removing-punctuations-given-string/
def remove_punctuation(sentence: str):
    # Regular expression
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for x in sentence.lower():
        if x in punctuations:
            sentence = sentence.replace(x, "")
    return sentence


string = "Welcome???@@##$ to#$% Geeks%$^for$%^&Geeks"
print(remove_punctuation(string))
