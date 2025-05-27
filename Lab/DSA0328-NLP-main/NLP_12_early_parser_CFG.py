import nltk
from nltk.parse import EarleyChartParser

grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N | N
    VP -> V NP | V
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog' | 'mat'
    V -> 'sits' | 'barks'
""")

earley_parser = EarleyChartParser(grammar)

sentence = "the dog barks".split()

print("Earley Parsing Tree(s):")
for tree in earley_parser.parse(sentence):
    print(tree)
    tree.pretty_print()
