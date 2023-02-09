import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
# it is interesting that the similarity level not only related to animal and also seems have higher similarity rate which monkey like banana but cat don't.

nlp = spacy.load('en_core_web_md')

word1 = nlp("car")
word2 = nlp("toyota")
word3 = nlp("wheel")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
# this is my example trying to use car related keyword and it seems the similarity rating is very close to what i have been thinking.

# from example.py change en_core_web_md to en_core_web_sm, I found that the similarity rate overall getting lower.
# and there are similarity previously zero, however it become one after changed, it is a totally opposite result, there must be something in the logic and reflect quite a different result as a whole.