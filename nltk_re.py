# regex for removing punctuation!
import re
# nltk preprocessing magic
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import spacy
import textacy
from spacy import displacy
import en_core_web_sm
# grabbing a part of speech function:
from part_of_speech import get_part_of_speech

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

nlp = spacy.load('en_core_web_sm')

text = "Hello Mary could you please openeds Chrome"
print("\nYour Text is:")
print(text)

cleaned = re.sub('\W+', ' ', text)
tokenized = word_tokenize(cleaned)

#stemmer = PorterStemmer()
#stemmed = [stemmer.stem(token) for token in tokenized]

#lemmatize
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(token, get_part_of_speech(token)) for token in tokenized]

#save the parts of speech 
posed = nltk.pos_tag(lemmatized)


#nouns and verbs phrase detection
nouns = []
verbs = []

for txt,pos in posed: 
    if pos == 'VB' or pos == 'VBD' or pos == 'VBG' or pos == 'VBN' or pos == 'VBP' or pos == 'VBZ' or pos == 'JJ':
        verbs.append(txt)
    elif pos == 'NN' or pos == 'NNS' or pos == 'NNP' or pos == 'NNPS':
        nouns.append(txt)

#Dependency Parsing
doc = nlp(text)

print('\n')
print ("{:<15} | {:<8} | {:<15} | {:<20}".format('Token','Relation','Head', 'Children'))
print ("-" * 70)

for token in doc:
  # Print the token, dependency nature, head and all dependents of the token
  print ("{:<15} | {:<8} | {:<15} | {:<20}"
         .format(str(token.text), str(token.dep_), str(token.head.text), str([child for child in token.children])))
  
 # Use displayCy to visualize the dependency 
displacy.render(doc, style='dep', options={'distance': 120})


#Save ROOT verb and subjects
subjects = []
for token in doc:
    if token.dep_ == 'ROOT':
        root_verb = token.text
    elif token.dep_ == 'nsubj':
        subjects.append(token.text)



#print("Stemmed text:")
#print(stemmed)
print("\nLemmatized text:")
print(lemmatized)
print("\nParts of speech:")
print(posed)
print("\nNouns:")
print(nouns)
print("\nVerbs:")
print(verbs)
print('\nSubjects:')
print(subjects)
print('\nRoot Verb: ['+ root_verb +']')



#POS: Part of speech with nltk
#NER: Named entity recognition with spacy
#Dependency grammar with spaCy

# POIOS 
# NA KANEI 
# TI 
