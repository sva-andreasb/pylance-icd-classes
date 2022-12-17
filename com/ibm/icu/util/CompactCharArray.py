UNICODECOUNT = "int  65536"
BLOCKSHIFT = "int  5"
def ():
    '''returns CompactCharArray\n\n
    ()\n
    (final char defaultValue)\n
    (final char[] indexArray, final char[] newValues)\n
    (final String indexArray, final String valueArray)\n
    '''
def elementAt():
    '''returns char\n\n
    elementAt(final char index)\n
    '''
def setElementAt():
    '''returns None\n\n
    setElementAt(final char index, final char value)\n
    setElementAt(final char start, final char end, final char value)\n
    '''
def compact():
    '''returns None\n\n
    compact()\n
    compact(final boolean exhaustive)\n
    '''
def getIndexArray():
    '''returns char[]\n\n
    getIndexArray()\n
    '''
def getValueArray():
    '''returns char[]\n\n
    getValueArray()\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
