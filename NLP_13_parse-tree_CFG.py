import nltk
from nltk import CFG
from nltk.parse import RecursiveDescentParser

grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | N
    VP -> V NP | V
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog' | 'mat'
    V -> 'sits' | 'barks'
""")

parser = RecursiveDescentParser(grammar)

sentence = "the cat sits".split()

print("Parse Tree(s):")
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
