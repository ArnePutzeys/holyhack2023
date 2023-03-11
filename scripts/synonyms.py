import requests
import deepl

# use free api to search for synonyms, perform some magic to extract the actual synonyms
def searchForSynonyms(word_to_search, timeout):
    url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'

    api_call = url + word_to_search

    # For if internet goes down
    try:
        response = requests.get(api_call, timeout=timeout)
    except Exception:
        return

    z = response.json()

    data = z[0]['meanings']

    # Extract the synonym fields
    synonyms = []
    for obj in data:
        synonyms.extend(obj['synonyms'])

    return synonyms


def deepLTranslate(to_translate, target_lang):
    # This key is linked to a fake credit card, so feel free to use all the free credit
    api_key = '65062874-51c5-9796-27a1-af89cd1b3c86:fx'

    # For if internet goes down
    try:
        translator = deepl.Translator(api_key)
    except Exception:
        return

    result = translator.translate_text(
        to_translate, target_lang=target_lang)

    return result

# There are no free api's available to find dutch synonyms, 
# so this function translates a dutch word into english, f
# inds synonyms and converts it back.
# Results are fairly odd, try "koud" -> "koperen aap"
def searchForSynonymsDutch(word_to_search, timeout):
    english_meaning = str(deepLTranslate(word_to_search, "EN-GB"))
    print("ENGLISH MEANING:", english_meaning)

    english_synonyms = searchForSynonyms(english_meaning, timeout)
    # First results seem to be the best, so keep these (see "koperen aap" remark) 
    if len(english_synonyms) > 3:
        english_synonyms = english_synonyms[0:3]
    # print("ENGLISH SYNONYMS", english_synonyms)

    nederlandse_synoniemen = []
    for synonym in english_synonyms:
        nederlandse_synoniemen.append(str(deepLTranslate(synonym, 'NL')))

    return nederlandse_synoniemen
