from django.test import TestCase

# Create your tests here.

from googletrans import Translator
translator = Translator()
text='this is a test'
translation=translator.translate(text,dest='en')
print(translation.text)
