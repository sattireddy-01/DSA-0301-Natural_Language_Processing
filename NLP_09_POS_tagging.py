import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import RegexpTagger

patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),   
    (r'.*es$', 'VBZ'),   
    (r'.*ly$', 'RB'),    
    (r'.*ion$', 'NN'),   
    (r'.*ment$', 'NN'),  
    (r'.*ful$', 'JJ'),   
    (r'.*ness$', 'NN'),  
    (r'.*ous$', 'JJ'),   
    (r'.*s$', 'NNS'),    
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  
    (r'.*', 'NN')        
]

regexp_tagger = RegexpTagger(patterns)

text = input("Enter text: ")

tokens = word_tokenize(text)

pos_tags = regexp_tagger.tag(tokens)

print("Word  →  POS Tag")
for word, tag in pos_tags:
    print(f"{word:10}  →  {tag}")
