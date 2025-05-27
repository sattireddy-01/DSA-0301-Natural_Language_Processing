import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

# Define a Probabilistic Context-Free Grammar (PCFG)
pcfg_grammar = PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.5] | N [0.5]
    VP -> V NP [0.7] | V [0.3]
    Det -> 'the' [0.6] | 'a' [0.4]
    N -> 'cat' [0.5] | 'dog' [0.5]
    V -> 'sits' [0.6] | 'barks' [0.4]
""")

# Create a Viterbi parser (for PCFG)
parser = ViterbiParser(pcfg_grammar)

# Sentence to parse
sentence = "the cat sits".split()

# Parse and display parse tree with probabilities
print("PCFG Parsing Tree(s):")
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
