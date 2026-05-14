import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text=state_union.raw("2006-GWBush.txt")
sample_text=state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer=PunktSentenceTokenizer(sample_text)
print(custom_sent_tokenizer)

tokenized=custom_sent_tokenizer.tokenize(sample_text)


def process_content():
        for i in tokenized:
            words=nltk.word_tokenize(i)
            tagged=nltk.pos_tag(words)
            chunkGram="""Chunk:{<RB.?>*<VB.?>*<NNP><NN>?}"""
            chunkParser=nltk.RegexpParser(chunkGram)
            chunked=chunkParser.parse(tagged)
            # chunked.draw()
            print(chunked)
            
process_content()