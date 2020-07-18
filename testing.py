from translate import Translator

translator= Translator(to_lang="zh")
translation = translator.translate('hello')
other = ascii(translation)
print(other)
print(type(other))

translator= Translator(to_lang="hi")
translation = translator.translate('hello')
translation = translation.encode('utf-8')
print(translation.decode('utf-8'))
