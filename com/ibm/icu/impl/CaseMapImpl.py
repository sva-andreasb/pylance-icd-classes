TITLECASE_WHOLE_STRING = "int  32"
TITLECASE_SENTENCES = "int  64"
TITLECASE_ADJUST_TO_CASED = "int  1024"
OMIT_UNCHANGED_TEXT = "int  16384"
def ():
    '''returns StringContextIterator\n\n
    (final CharSequence src)\n
    (final CharSequence src, final int cpStart, final int cpLimit)\n
    '''
def setLimit():
    '''returns None\n\n
    setLimit(final int lim)\n
    '''
def moveToLimit():
    '''returns None\n\n
    moveToLimit()\n
    '''
def nextCaseMapCP():
    '''returns int\n\n
    nextCaseMapCP()\n
    '''
def setCPStartAndLimit():
    '''returns None\n\n
    setCPStartAndLimit(final int s, final int l)\n
    '''
def getCPStart():
    '''returns int\n\n
    getCPStart()\n
    '''
def getCPLimit():
    '''returns int\n\n
    getCPLimit()\n
    '''
def getCPLength():
    '''returns int\n\n
    getCPLength()\n
    '''
def reset():
    '''returns None\n\n
    reset(final int direction)\n
    '''
def next():
    '''returns int\n\n
    next()\n
    next(final int n)\n
    next()\n
    '''
def first():
    '''returns int\n\n
    first()\n
    '''
def last():
    '''returns int\n\n
    last()\n
    '''
def previous():
    '''returns int\n\n
    previous()\n
    '''
def following():
    '''returns int\n\n
    following(final int offset)\n
    '''
def current():
    '''returns int\n\n
    current()\n
    '''
def getText():
    '''returns CharacterIterator\n\n
    getText()\n
    '''
def setText():
    '''returns None\n\n
    setText(final CharacterIterator newText)\n
    setText(final CharSequence newText)\n
    setText(final String newText)\n
    '''
