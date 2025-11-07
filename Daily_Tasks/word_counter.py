# Word Counter
# Description: Take a text input and count words, characters, sentences, and paragraphs.


import re
def word_counter(text):
    chars=len(text)
    words=re.findall(r"\w+",text)
    sentence=re.findall(r"[.?!]+",text)
    paragraph=[p for p in text.split("\n")]

    return {
        "characters":chars,
        "words":len(words),
        "sentences":len(sentence),
        "paragraphs":len(paragraph)
    }

print(word_counter("hai hello how. All is right?\n yeah I'm doing great"))