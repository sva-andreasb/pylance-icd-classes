FWD = "int  32"
BACK = "int  16"
UTF16 = "int  8"
CONTAINED = "int  2"
NOT_CONTAINED = "int  1"
ALL = "int  63"
FWD_UTF16_CONTAINED = "int  42"
FWD_UTF16_NOT_CONTAINED = "int  41"
BACK_UTF16_CONTAINED = "int  26"
BACK_UTF16_NOT_CONTAINED = "int  25"
def ():
    '''returns OffsetList\n\n
    (final UnicodeSet set, final ArrayList<String> setStrings, final int which)\n
    (final UnicodeSetStringSpan otherStringSpan, final ArrayList<String> newParentSetStrings)\n
    ()\n
    '''
def needsStringSpanUTF16():
    '''returns boolean\n\n
    needsStringSpanUTF16()\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final int c)\n
    '''
def setMaxLength():
    '''returns None\n\n
    setMaxLength(final int maxLength)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def shift():
    '''returns None\n\n
    shift(final int delta)\n
    '''
def addOffset():
    '''returns None\n\n
    addOffset(final int offset)\n
    '''
def containsOffset():
    '''returns boolean\n\n
    containsOffset(final int offset)\n
    '''
def popMinimum():
    '''returns int\n\n
    popMinimum()\n
    '''
