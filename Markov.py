# Implements the hash table/linked structure

# Node representation of a word
# where p1 is W_i-1
#       p2 is W_i
class Word:
    def __init__(self, word):
        self.word = word
        self.next_word1 = None  # other word that comes after the key/hashed
        self.next_word2 = None  # proceeding in a sentence
        self.is_i = False  # determines if 3rd word or position 2

    def add_word2(self, word2):
        self.next_word2 = word2
        self.next_word2.is_i = True


class LinkedWords:
    def __init__(self, word: Word):
        self.head = word


# Tri-Gram Markov Model that helps AI create a new story
class MarkovModel:
    def __init__(self):
        dictionary = dict()


# ---------------Code below is for testing and experimenting-------------------------


# TODO implement the data structure
s1 = "this is a test sentence from a document"
s2 = "an other sentence my friend"
s3 = "an other of you will also have to leave"
s4 = "this quarter has been rough"
s5 = "but its almost over and i will graduate"

test_list = [s1, s2, s3, s4, s5]
# TODO function that uses the below function to create the hash table, should take in a list of sentences
# takes a sentence and hashes TODO: prevents sentence under size 3
the_dictionary = dict()
for sentence in test_list:
    s_to_list = sentence.split()
    for i in range(len(s_to_list) - 2):  # minus 2 prevents index out of bounce
        current_word = s_to_list[i]
        # if key exist, update the linked list
        if current_word in the_dictionary:
            current = the_dictionary.get(current_word)
            next_word = s_to_list[i + 1]
            if next_word == current.head.word:
                next_word2 = s_to_list[i + 2]
                # need to add next_word2 as link or increase count of occurrence
                if next_word2 == current.head.next_word2.word:
                    print("increase count")
                else:
                    print("move to next p2")
            else:
                print("move to next p1")  # TODO might have to do function that finds nodes or doesnt

        # if it does not exist, add as key and update linked list
        else:
            w_1 = Word(s_to_list[i + 1])
            w_1.add_word2(Word(s_to_list[i + 2]))
            the_dictionary[current_word] = LinkedWords(w_1)

