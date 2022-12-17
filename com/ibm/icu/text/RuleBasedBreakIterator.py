WORD_NONE = "int  0"
WORD_NONE_LIMIT = "int  100"
WORD_NUMBER = "int  100"
WORD_NUMBER_LIMIT = "int  200"
WORD_LETTER = "int  200"
WORD_LETTER_LIMIT = "int  300"
WORD_KANA = "int  300"
WORD_KANA_LIMIT = "int  400"
WORD_IDEO = "int  400"
WORD_IDEO_LIMIT = "int  500"
def ():
    '''returns RuleBasedBreakIterator\n\n
    ()\n
    (final String rules)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object that)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def dump():
    '''returns None\n\n
    dump()\n
    '''
def first():
    '''returns int\n\n
    first()\n
    '''
def last():
    '''returns int\n\n
    last()\n
    '''
def next():
    '''returns int\n\n
    next(int n)\n
    next()\n
    '''
def previous():
    '''returns int\n\n
    previous()\n
    '''
def following():
    '''returns int\n\n
    following(final int offset)\n
    '''
def preceding():
    '''returns int\n\n
    preceding(final int offset)\n
    '''
def isBoundary():
    '''returns boolean\n\n
    isBoundary(final int offset)\n
    '''
def current():
    '''returns int\n\n
    current()\n
    '''
def getRuleStatus():
    '''returns int\n\n
    getRuleStatus()\n
    '''
def getRuleStatusVec():
    '''returns int\n\n
    getRuleStatusVec(final int[] fillInArray)\n
    '''
def getText():
    '''returns CharacterIterator\n\n
    getText()\n
    '''
def setText():
    '''returns None\n\n
    setText(final CharacterIterator newText)\n
    '''
