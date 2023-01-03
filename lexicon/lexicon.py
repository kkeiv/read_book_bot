from lexicon.lexicon_ru import LEXICON_RU
from lexicon.lexicon_en import LEXICON_EN

# @brief get text based on language settings
def get_text(param : str) -> str:

    # TODO: select dictionary based on language
    lang : str = 'RU'
    ret : str = ""

    # form text based on language settings
    # in case of key is absent in the dictionary - print param`s name
    if lang == 'RU':
        ret = LEXICON_RU.get(param, param)
    elif lang == 'EN':
        ret = LEXICON_EN.get(param, param)
    else:   # by default in English
        ret = LEXICON_EN.get(param, param)

    return ret

