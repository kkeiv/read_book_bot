from lexicon_ru import LEXICON_RU
from lexicon_en import LEXICON_EN

# get text based on language settings
def get_text(param : str) -> str:

    # TODO: select dictionary based on language
    lang : str = 'RU'
    ret : str = ""

    if lang == 'RU':
        ret = LEXICON_RU.get(param, "NoRuPar")
        return ret

    ret = LEXICON_EN.get(param, "NoEnPar")
    return ret

