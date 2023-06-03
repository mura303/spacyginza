import spacy
nlp = spacy.load('ja_ginza')

doc1 = nlp('あなたのことが好きです')
doc2 = nlp('　好きだ')
doc3 = nlp('似る')

print(doc1.similarity(doc2))
print(doc1.similarity(doc3))
print(doc2.similarity(doc3))

