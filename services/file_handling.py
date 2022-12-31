BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

# prepare empty book
book: dict[int, str] = {}

# @brief get text for correspond page
def _get_part_text(text : str, start : int, size : int) -> tuple[str, int]:
    # list of end symbols
    ends = ',.!:;?'
    ret = ''

    # make a proposal for end position of page
    end = start + size - 1

    #delete cuted path (words or multysymbol)
    if end < len(text):                 # full size page
        # find laster "ends" symbols
        while text[end] not in ends:
            end -= 1
        # cut part for page (not clear)
        ret = text[start: end+1 :]
    else:                               # last page
        ret = text[start::]



    return ret, len(ret)

# @brief form dictionary of pages from file
def prepare_book (path : str) -> None:
    pass


# form pages from book
prepare_book(BOOK_PATH)
