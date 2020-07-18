import nltk

sent_text = nltk.sent_tokenize("there's always a ridiculously long line for the red bean cakes I know it's weird") # this gives us a list of sentences
print(sent_text)
# now loop over each sentence and tokenize it separately
for sentence in sent_text:
    tokenized_text = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokenized_text)
    print(tagged)

# from nltk.corpus import gutenberg
# from pprint import pprint
# from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktTrainer



# print(dir(gutenberg))
# print(gutenberg.fileids())
 
# text = ""
# for file_id in gutenberg.fileids():
#     text += gutenberg.raw(file_id)
 
# print(len(text))


# trainer = PunktTrainer()
# trainer.INCLUDE_ALL_COLLOCS = True
# trainer.train(text)
 
# tokenizer = PunktSentenceTokenizer(trainer.get_params())
 
# # Test the tokenizer on a piece of text
# sentences = "Mr. James told me Dr. Brown is not available today. I will try tomorrow."
 
# print(tokenizer.tokenize(sentences))
# # ['Mr. James told me Dr.', 'Brown is not available today.', 'I will try tomorrow.']
 
# # View the learned abbreviations
# print(tokenizer._params.abbrev_types)
# # set([...])
 
# # Here's how to debug every split decision
# for decision in tokenizer.debug_decisions(sentences):
#     pprint(decision)
#     print( '=' * 30)

# tokenizer._params.abbrev_types.add('dr')
 
# print(tokenizer.tokenize(sentences))
# # ['Mr. James told me Dr. Brown is not available today.', 'I will try tomorrow.']
 
# for decision in tokenizer.debug_decisions(sentences):
#     pprint(decision)
#     print('=' * 30)