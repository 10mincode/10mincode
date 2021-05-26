# importing libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Input text - to summarize
text="""If an opaque object on the path of light becomes very small, light has a tendency to
bend around it and not walk in a straight line – an effect known as the diffraction of
light. Then the straight-line treatment of optics using rays fails. To explain phenomena
such as diffraction, light is thought of as a wave, the details of which you will study
in higher classes. Again, at the beginning of the 20th century, it became known that
the wave theory of light often becomes inadequate for treatment of the interaction of
light with matter, and light often behaves somewhat like a stream of particles. This
confusion about the true nature of light continued for some years till a modern
quantum theory of light emerged in which light is neither a ‘wave’ nor a ‘particle’ –
the new theory reconciles the particle properties of light with the wave nature."""
# Tokenizing the text
stopWords = set(stopwords.words("english"))
words = word_tokenize(text)

# Creating a frequency table to keep the
# score of each word

freqTable = dict()
for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1

# Creating a dictionary to keep the score
# of each sentence
sentences = sent_tokenize(text)
sentenceValue = dict()

for sentence in sentences:
    for word, freq in freqTable.items():
        if word in sentence.lower():
            if sentence in sentenceValue:
                sentenceValue[sentence] += freq
            else:
                sentenceValue[sentence] = freq

sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]

# Average value of a sentence from the original text

average = int(sumValues / len(sentenceValue))

# Storing sentences into our summary.
summary = ''
for sentence in sentences:
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2* average)):
        summary += " " + sentence
print(summary)

print()
print()
print(len(text))
print(len(summary))