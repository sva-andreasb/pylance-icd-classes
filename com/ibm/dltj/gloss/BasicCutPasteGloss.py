DLT_CASE_CONV_NOCONV = "byte  0"
DLT_CASE_CONV_TOLOWER = "byte  1"
DLT_CASE_CONV_TOUPPER = "byte  2"
DLT_CASE_CONV_CAPITALIZE = "byte  3"
DLT_FUZZY_CASE_SS_IS_ONE_CHAR = "byte  1"
DLT_FUZZY_CASE_FIRST_CHAR_ONLY = "byte  2"
def read():
    '''returns None\n\n
    read(final DataInputStream dataInputStream, int capacity)\n
    '''
def write():
    '''returns None\n\n
    write(final DataOutputStream dataOutputStream, final GlossMapper glossMapper)\n
    '''
def getLemma():
    '''returns String\n\n
    getLemma(final CharacterIterator characterIterator, final int index, final int n, final StringBuffer sb)\n
    getLemma(final CharacterIterator characterIterator, final int n, final int n2)\n
    getLemma(final String text)\n
    '''
def toString():
    '''returns String\n\n
    toString(final String text)\n
    toString()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final BasicCutPasteGloss basicCutPasteGloss)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def getMinSourceLength():
    '''returns int\n\n
    getMinSourceLength()\n
    '''
def getConv():
    '''returns byte\n\n
    getConv()\n
    '''
def getCut():
    '''returns short\n\n
    getCut()\n
    '''
def getOptions():
    '''returns byte\n\n
    getOptions()\n
    '''
def process():
    '''returns None\n\n
    process(final CharacterIterator characterIterator, final byte b, final StringBuffer sb)\n
    process(final CharacterIterator characterIterator, final byte b, final StringBuffer sb)\n
    process(final CharacterIterator characterIterator, final byte b, final StringBuffer sb)\n
    '''
