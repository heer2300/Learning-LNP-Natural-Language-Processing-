import spacy
from sympy.codegen import Print
from sympy.printing.tree import print_node

nlp = spacy.load('en_core_web_sm')

with open("wiki_us.txt") as f:
    tt = f.read()

#print(tt)

doc = nlp(tt)

print(doc)
print(len(tt))

print(len(doc))

for token in tt[0:10]:
    print(token)
print("-------------------------------------------/n")
for token in doc[0:10]:
    print(token)

for sent in doc.sents:
    print(sent)

sent1 = list(doc.sents)[0]
# print(sent1)


i=1
for sent in list(doc.sents)[0:10]:
    print(i,sent)
    i+=1

for token in doc[:10]:
    print(token)


token1 = sent1[2]
print(token1)

print(token1.left_edge)
print(token1.right_edge)


for ent in doc.ents:
    print(ent.text, ent.label_)
