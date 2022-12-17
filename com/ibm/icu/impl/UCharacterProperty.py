LATIN_CAPITAL_LETTER_I_WITH_DOT_ABOVE_ = "char  '\u0130'"
LATIN_SMALL_LETTER_DOTLESS_I_ = "char  '\u0131'"
LATIN_SMALL_LETTER_I_ = "char  'i'"
TYPE_MASK = "int  31"
SRC_NONE = "int  0"
SRC_CHAR = "int  1"
SRC_PROPSVEC = "int  2"
SRC_NAMES = "int  3"
SRC_CASE = "int  4"
SRC_BIDI = "int  5"
SRC_CHAR_AND_PROPSVEC = "int  6"
SRC_CASE_AND_NORM = "int  7"
SRC_NFC = "int  8"
SRC_NFKC = "int  9"
SRC_NFKC_CF = "int  10"
SRC_NFC_CANON_ITER = "int  11"
SRC_COUNT = "int  12"
def setIndexData():
    '''returns None\n\n
    setIndexData(final CharTrie.FriendAgent friendagent)\n
    '''
def getAdditional():
    '''returns int\n\n
    getAdditional(final int codepoint, final int column)\n
    '''
def getAge():
    '''returns VersionInfo\n\n
    getAge(final int codepoint)\n
    '''
def hasBinaryProperty():
    '''returns boolean\n\n
    hasBinaryProperty(int c, final int which)\n
    '''
def getMaxValues():
    '''returns int\n\n
    getMaxValues(final int column)\n
    '''
def addPropertyStarts():
    '''returns UnicodeSet\n\n
    addPropertyStarts(final UnicodeSet set)\n
    '''
def upropsvec_addPropertyStarts():
    '''returns None\n\n
    upropsvec_addPropertyStarts(final UnicodeSet set)\n
    '''
def ():
    '''returns BinaryProperties\n\n
    (final int column, final int mask)\n
    '''
