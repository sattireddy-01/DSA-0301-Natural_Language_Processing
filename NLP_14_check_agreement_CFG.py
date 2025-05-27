import nltk
from nltk import CFG

grammar = CFG.fromstring("""
    S -> NP_sg VP_sg | NP_pl VP_pl
    
    NP_sg -> Det_sg N_sg | Pronoun_sg
    NP_pl -> Det_pl N_pl | Pronoun_pl
    
    VP_sg -> V_sg | V_sg NP_sg
    VP_pl -> V_pl | V_pl NP_pl
    
    Det_sg -> 'the' | 'a'
    Det_pl -> 'the'
    
    N_sg -> 'dog' | 'cat'
    N_pl -> 'dogs' | 'cats'
    
    Pronoun_sg -> 'he' | 'she'
    Pronoun_pl -> 'they'
    
    V_sg -> 'runs' | 'jumps' | 'barks'
    V_pl -> 'run' | 'jump' | 'bark'
""")


parser = nltk.ChartParser(grammar)

sentences = [
    "the dog runs",      # ✅ Correct
    "the dogs run",      # ✅ Correct
    "the cat jump",      # ❌ Incorrect (should be 'jumps')
    "they barks",        # ❌ Incorrect (should be 'bark')
    "a big dogs run"     # ❌ Incorrect (should be 'dog' for singular)
]

def check_grammar(sentence):
    words = sentence.split()
    try:
        next(parser.parse(words))  
        return f"✅ '{sentence}' is grammatically correct!"
    except StopIteration:
        return f"❌ '{sentence}' is incorrect!"

for s in sentences:
    print(check_grammar(s))
