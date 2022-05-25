# Implements the hash table/linked structure

# Node representation of a word
# where p1 is W_i-1
#       p2 is W_i
class Node:
    def __init__(self, word: str):
        self.data = word
        self.next = None
        self.count = 0

    def __eq__(self, other):
        return self.data == other

    def count(self):
        self.count += 1

    def add_second_list(self):
        setattr(self, "linked_list", LinkedWords())


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

    def to_string(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next


# Tri-Gram Markov Model that helps a simple AI create a new story
class MarkovModel:
    def __init__(self):
        self.hash_table = dict()


# ---------------Code below is for testing and experimenting-------------------------


def test_sentences():
    s1 = "this is a test sentence from a document"
    s2 = "an other sentence my friend"
    s3 = "an other of you will also have to leave"
    s4 = "this quarter has an an been rough a rough sentence my ninja"
    s5 = "but its almost over and i will graduate"
    output = [s1, s2, s3, s4, s5]
    return output


test_list = test_sentences()

# TODO idea: function that uses the below function to create the hash table, should take in a list of sentences
# takes a sentence and hashes TODO: prevents sentence under size 3
table = dict()
for sentence in test_list:
    # TODO idea: can have a function doing this work when taking a sentence as input
    s_list = sentence.split()
    for i in range(len(s_list) - 2):  # minus 2 prevents index out of bounce
        current_key = s_list[i]
        word1 = s_list[i + 1]
        word2 = s_list[i + 2]
        # if key exist, update the linked list
        if current_key in table:
            # layer refers to the linked lists
            layer1 = table.get(current_key)
            response = layer1.search(word1)
            # word is found
            if response[0]:
                print(response[1].data, " was found")
            # word is not found
            else:
                layer1.add_node(Node(word1))

        # if key does not exist, add as key and start layer 1 linked list
        else:
            # TODO continue with layer 2
            layer1 = LinkedWords()
            node = Node(word1)
            layer1.add_node(node)
            table[current_key] = layer1

print("Table size: ", len(table))
for key in table:
    print("The key: ", key, ": ", end=" ")
    print(table.get(key).to_string())
