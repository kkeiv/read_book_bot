BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 100 #1050

# list of end symbols
_ends = ',.!:;?'

# prepare empty book
book: dict[int, str] = {}

# @brief get text for correspond page
def _get_part_text(text : str, start : int, size : int) -> tuple[str, int]:
    ret : str = ''

    # make a proposal for end position of page
    new_page = start + size

    #delete cuted path (words or multysymbol)
    if new_page < len(text):                # not last page

        # if next page starts with "ends" symbol
        if text[new_page] in _ends:
            # find laster not "ends" symbol
            while text[new_page] in _ends:
                new_page -= 1

        # find laster "ends" symbol
        while text[new_page] not in _ends:
            new_page -= 1

        # cut part for page (not clear)
        ret = text[start: new_page+1]
    else:                                   # last page
        ret = text[start::]

    return ret, len(ret)

# @brief form dictionary of pages from file
def prepare_book (path : str) -> None:
    # read text from file
    with open(BOOK_PATH, mode="rt", encoding='UTF-8') as file:
        # initialize data
        book_text : str = file.read()
        page_num : int = 1
        curent_pos : int = 0
        text_last_position = len(book_text)

        # initialize buffer variables
        page_text : str = ""
        page_len : int = 0

        # form dictionary with pages
        while curent_pos < text_last_position:
            # read next page
            page_text, page_len = _get_part_text(book_text, curent_pos, PAGE_SIZE)

            # save page into dictionary
            book[page_num] = page_text.lstrip()

            # update variables
            page_num += 1
            curent_pos += page_len
    return

# form pages from book
prepare_book(BOOK_PATH)
