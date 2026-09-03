import spacy
import numpy as np

from sympy.codegen import Print
from sympy.printing.tree import print_node

nlp = spacy.load('en_core_web_md')

with open("wiki_us.txt",'r') as f:
    text = f.read()

doc = nlp(text)

sent1 = list(doc.sents)[0]
#print(sent1)


my_word = "contry"



#https://stackoverflow.com/questions/54717449/mapping-word-vector-to-the-most-similar-closest-word-using-spacy
your_word = "india"

ms = nlp.vocab.vectors.most_similar(
    np.asarray([nlp.vocab.vectors[nlp.vocab.strings[your_word]]]), n=100)
words = [nlp.vocab.strings[w] for w in ms[0][0]]
distances = ms[2]
print(words)


doc1 = nlp("i like eating good food")
doc2 = nlp("fast food is the best breakfast in the morning")
doc3 = nlp("i live in tokyo")
doc4 =nlp("friends it a good TV show ")
doc5 =nlp("i like orange ")
doc6 =nlp("i like apple")
print(doc1.similarity(doc2))
print(doc1.similarity(doc3))
print(doc4.similarity(doc3))
print(doc5.similarity(doc6))




# nlp = spacy.load("en_core_web_sm")
# 
# nlp.add_pipe("sentencizer")
# nlp.analyze_pipes()

