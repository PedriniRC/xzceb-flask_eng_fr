'''
This provide the necessary credentials and set up the enviroment
'''

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

#Iniciate the language translation service
authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(URL)

#Translation from english to french
def english_to_french(english_text):
    """Function that translate english to french"""
    translation = language_translator.translate(
    text= english_text,
    model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

#Translation from french to english
def french_to_english(french_text):
    """Function that translate french to english"""
    translation = language_translator.translate(
    text= french_text,
    model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
