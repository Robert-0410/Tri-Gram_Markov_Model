import random


# Implements the hash table/linked structure

# Node representation of a word
# where p1 is W_i-1
#       p2 is W_i
class Node:
    # constructor
    def __init__(self, word: str):
        self.data = word
        self.next = None
        self.layer2 = None
        self.count = 0

    def __eq__(self, other):
        return self.data == other

    def count_word(self):
        self.count += 1

    def reset_count_to_zero(self):
        self.count = 0

    def add_layer2(self):
        setattr(self, "layer2", LinkedWords())


# LinkedList for the words in the Tri-gram
class LinkedWords:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, node: Node):
        # empty list case
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            current = self.tail
            self.tail = node
            current.next = node

    # Searches the linked list for specified Node
    def search(self, word: str):
        current = self.head
        while current is not None:
            if current == word:
                return [True, current]
            current = current.next
        return [False, None]

    # Searches for highest probable word in either the bi-gram or tri-gram
    def search_max(self):
        current = self.head
        max_count = 0
        output = None
        while current is not None:
            current_count = current.count
            if max_count < current_count:
                output = current
                max_count = current_count
            current = current.next
        output.reset_count_to_zero()
        return output

    def to_string(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            layer = current.layer2
            if layer is not None:
                layer.to_string()
            current = current.next


# Tri-Gram Markov Model that helps a simple AI create a new story
class MarkovModel:
    def __init__(self):
        self.hash_table = dict()
        self.raw_sentences = list()
        self.story = list()

    def process_sentence(self, sentence: str):
        s_list = sentence.split()
        for i in range(len(s_list) - 2):  # minus 2 prevents index out of bounce
            current_key = s_list[i]
            word1 = s_list[i + 1]
            word2 = s_list[i + 2]
            # if key exist, update the linked list
            if current_key in self.hash_table:
                # layer refers to the linked lists
                layer1 = self.hash_table.get(current_key)
                response = layer1.search(word1)
                # word is found, go into layer 2
                if response[0]:
                    layer1_node = response[1]
                    layer1_node.count_word()
                    #  print(response[1].data, " was found need to increment")
                    layer2 = layer1_node.layer2
                    response2 = layer2.search(word2)
                    # word2 is found in layer 2
                    if response2[0]:
                        response2[1].count_word()
                    # word2 not found in layer 2
                    else:
                        layer2_node = Node(word2)
                        layer2_node.count_word()
                        response[1].layer2.add_node(layer2_node)
                # word is not found
                else:
                    node = Node(word1)
                    node.count_word()
                    node.add_layer2()
                    layer2_node = Node(word2)
                    layer2_node.count_word()
                    node.layer2.add_node(layer2_node)
                    layer1.add_node(node)

            # if key does not exist, add as key and start layer 1 linked list
            else:
                layer1 = LinkedWords()
                node = Node(word1)
                node.count_word()
                node.add_layer2()
                # add W_i to layer 2
                layer2_node = Node(word2)
                layer2_node.count_word()
                node.layer2.add_node(layer2_node)
                layer1.add_node(node)
                self.hash_table[current_key] = layer1

    # trains AI to learn common words that can go together from the input data set
    def train_markov_model(self, sentences: list):
        self.raw_sentences.extend(sentences)
        for sentence in sentences:
            self.process_sentence(sentence)

    def build_new_sentence(self, word: str):
        bi_gram = self.hash_table.get(word)  # the key will come in from the method argument
        output_list = list()
        #  output_list.append(word)
        for i in range(2500):
            if bi_gram is None:
                continue
            max1 = bi_gram.search_max()
            tri_gram = max1.layer2
            max2 = tri_gram.search_max()
            output_list.append(max1.data)
            output_list.append(max2.data)

            if '.' in max2.data:
                word = choose_random_word(self.raw_sentences)
                while word is None or '.' in word:
                    word = choose_random_word(self.raw_sentences)
                bi_gram = self.hash_table.get(word)
            else:
                bi_gram = self.hash_table.get(max2.data)

        output = " ".join(output_list)
        self.story.append(output)

    # method that writes story to a file, appends the chosen first word to the beginning
    def write_down_story(self):
        file = open("Readme.txt", "w")
        words_lst = self.story[0].split()
        print(len(words_lst))
        amount = 0
        for word in words_lst:
            file.write(word)
            amount += 1
            if amount >= 12:
                file.write("\n")
                amount = 0
            else:
                file.write(" ")
        file.close()
        return 0

    # Builds the entire story consisting of 2000 words.
    def build_new_story(self, first_word):
        next_word = first_word
        self.build_new_sentence(next_word)


# function that picks a random word
def choose_random_word(sentences: list):
    limit = len(sentences) - 1
    random_index = random.randrange(0, limit)
    sentence = sentences.__getitem__(random_index)
    words = sentence.split()
    limit = len(words) - 1
    if limit == 0:
        return None
    else:
        random_index = random.randrange(0, limit)
    return words[random_index]
