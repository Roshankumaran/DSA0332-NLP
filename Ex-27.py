import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser
grammar = PCFG.fromstring("""
S -> S '+' S [0.3]
S -> S '*' S [0.3]
S -> 'id' [0.4]
""")
sentence = ['id', '+', 'id', '*', 'id']
parser = ViterbiParser(grammar)
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
