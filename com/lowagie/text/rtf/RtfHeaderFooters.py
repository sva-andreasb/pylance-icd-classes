ALL_PAGES = "int  0"
LEFT_PAGES = "int  1"
RIGHT_PAGES = "int  2"
FIRST_PAGE = "int  3"
def ():
    '''returns RtfHeaderFooters\n\n
    ()\n
    (final Phrase before, final Phrase after)\n
    (final Phrase before, final boolean numbered)\n
    '''
def set():
    '''returns None\n\n
    set(final int type, final HeaderFooter hf)\n
    '''
def get():
    '''returns HeaderFooter\n\n
    get(final int type)\n
    '''
