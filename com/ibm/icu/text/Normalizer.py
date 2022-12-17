UNICODE_3_2 = "int  32"
DONE = "int  -1"
IGNORE_HANGUL = "int  1"
FOLD_CASE_DEFAULT = "int  0"
INPUT_IS_FCD = "int  131072"
COMPARE_IGNORE_CASE = "int  65536"
COMPARE_CODE_POINT_ORDER = "int  32768"
FOLD_CASE_EXCLUDE_SPECIAL_I = "int  1"
COMPARE_NORM_OPTIONS_SHIFT = "int  20"
def ():
    '''returns CharsAppendable\n\n
    (final String str, final Mode mode, final int opt)\n
    (final CharacterIterator iter, final Mode mode, final int opt)\n
    (final UCharacterIterator iter, final Mode mode, final int options)\n
    (final char[] dest, final int destStart, final int destLimit)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def current():
    '''returns int\n\n
    current()\n
    '''
def next():
    '''returns int\n\n
    next()\n
    '''
def previous():
    '''returns int\n\n
    previous()\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def setIndexOnly():
    '''returns None\n\n
    setIndexOnly(final int index)\n
    '''
def setIndex():
    '''returns int\n\n
    setIndex(final int index)\n
    '''
def getBeginIndex():
    '''returns int\n\n
    getBeginIndex()\n
    '''
def getEndIndex():
    '''returns int\n\n
    getEndIndex()\n
    '''
def first():
    '''returns int\n\n
    first()\n
    '''
def last():
    '''returns int\n\n
    last()\n
    '''
def getIndex():
    '''returns int\n\n
    getIndex()\n
    '''
def startIndex():
    '''returns int\n\n
    startIndex()\n
    '''
def endIndex():
    '''returns int\n\n
    endIndex()\n
    '''
def setMode():
    '''returns None\n\n
    setMode(final Mode newMode)\n
    '''
def getMode():
    '''returns Mode\n\n
    getMode()\n
    '''
def setOption():
    '''returns None\n\n
    setOption(final int option, final boolean value)\n
    '''
def getOption():
    '''returns int\n\n
    getOption(final int option)\n
    '''
def getText():
    '''returns String\n\n
    getText(final char[] fillIn)\n
    getText()\n
    '''
def getLength():
    '''returns int\n\n
    getLength()\n
    '''
def setText():
    '''returns None\n\n
    setText(final StringBuffer newText)\n
    setText(final char[] newText)\n
    setText(final String newText)\n
    setText(final CharacterIterator newText)\n
    setText(final UCharacterIterator newText)\n
    '''
def length():
    '''returns int\n\n
    length()\n
    '''
def append():
    '''returns Appendable\n\n
    append(final char c)\n
    append(final CharSequence s)\n
    append(final CharSequence s, int sStart, final int sLimit)\n
    '''
