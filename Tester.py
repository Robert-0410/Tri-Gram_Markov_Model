# Reads input files, connects to Markov.py to generate the output story


from Markov import MarkovModel, choose_random_word


# Split sentences by period and returns a list with all the sentences
def read_strip_lowercase_lines(file_name: str):
    lines = list()
    novel = open(file_name, 'r')
    chapter = 'CHAPTER'

    # skip over title and arthur
    for i in range(4):
        novel.readline()

    for next_line in novel:
        # strip whitespace
        one = next_line.rstrip('\n')
        two = one.lstrip(' ')
        if two == '':
            continue
        if chapter in two:
            novel.readline()
            continue
        final1 = two.lower()
        lines.append(final1)

    novel.close()
    return lines


# updates list so that each index is an entire sentence
def make_lines_based_on_periods(the_list: list):
    output_sentences = list()
    s_d = '.'
    ex = '!'
    ques = '?'
    sentence_list = list()
    for line in the_list:
        # split line into list of words
        current = line.split()
        # iterate through the line into list and append words to a sentence list stopping with '.!?'
        for word in current:
            sentence_list.append(word)
            if s_d in word or ex in word or ques in word:
                # make sentence_list to a str and append to the output list
                sentence = " ".join(sentence_list)
                output_sentences.append(sentence)
                # clear the sentence_list
                sentence_list.clear()
    return output_sentences


# removes all punctuations from the sentences
def clean_punctuation(the_list: list):
    output = list()
    for line in the_list:
        current = remove_punctuation(line)
        output.append(current)
    return output


# removes punctuation from an input sentence
# inspired by: https://www.geeksforgeeks.org/removing-punctuations-given-string/
def remove_punctuation(sentence: str):
    # Regular expression
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for x in sentence.lower():
        if x in punctuations:
            sentence = sentence.replace(x, "")
    return sentence


# Current entry point for the program
def prepare_sentences(file_name: str):
    initial_list = read_strip_lowercase_lines(file_name)  # TODO pass string with file name
    intermediate_sentences = make_lines_based_on_periods(initial_list)
    output = clean_punctuation(intermediate_sentences)
    return output


# main entry point for the program
def run():
    # Collect data
    novel1 = prepare_sentences("houn.txt")
    novel2 = prepare_sentences("sign.txt")
    novel3 = prepare_sentences("stud.txt")
    novel4 = prepare_sentences("vall.txt")

    # Train AI
    writer = MarkovModel()
    writer.train_markov_model(novel1)
    writer.train_markov_model(novel2)
    writer.train_markov_model(novel3)
    writer.train_markov_model(novel4)

    # Write story to file
    starting_word = choose_random_word(writer.raw_sentences)
    writer.build_new_story(starting_word)

    print(writer.story)
    print(len(writer.story))

    #for key in writer.hash_table:
     #   print("The key: ", key, ": ", end=" ")
      #  print(writer.hash_table.get(key).to_string())

# running the program, the proceeding block of code may be held in write_me_a_story_myAI()
#  sentences = prepare_sentences()
#  print(sentences)
run()
