import nltk
from nltk import CFG

grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | N
    VP -> V NP | V
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog' | 'mat'
    V -> 'sits' | 'barks'
""")

rd_parser = nltk.RecursiveDescentParser(grammar)

sentence = "the cat sits".split()

print("Parsing Tree(s):")
for tree in rd_parser.parse(sentence):
    print(tree)
    tree.pretty_print()
