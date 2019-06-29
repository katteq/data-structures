#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
#
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
#
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
#
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# In[1]:


# Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.nodes = {}

    def insert(self, char):
        node = self.nodes.get(char)
        if node:
            return node

        node = TrieNode()
        self.nodes[char] = node
        return node

    def print_node(self, node):
        words = []
        for key in node.nodes:
            c = node.nodes[key]

            if c.is_end:
                words.append(key)
            new_words = self.print_node(c)
            for n in new_words:
                words.append(key + n)
        return words

    def suffixes(self):
        return self.print_node(self)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for p in word:
            current = current.insert(p)

        current.is_end = True

    def find(self, prefix):
        current = self.root
        for ch in prefix:
            if current.nodes[ch]:
                current = current.nodes[ch]
            else:
                return None
        return current


# # Finding Suffixes
#
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
#
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

# In[1]:


# Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.nodes = {}

    def insert(self, char):
        node = self.nodes.get(char)
        if node:
            return node

        node = TrieNode()
        self.nodes[char] = node
        return node

    def print_node(self, node):
        words = []
        for key in node.nodes:
            c = node.nodes[key]

            if c.is_end:
                words.append(key)
            new_words = self.print_node(c)
            for n in new_words:
                words.append(key + n)
        return words

    def suffixes(self):
        return self.print_node(self)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for p in word:
            current = current.insert(p)

        current.is_end = True

    def find(self, prefix):
        current = self.root
        for ch in prefix:
            current = current.nodes.get(ch)
            if not current:
                return None
        return current


# # Testing it all out
#
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# In[2]:


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


# In[3]:


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        print(prefixNode.suffixes())
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');


# In[ ]:




