AND = "int  0"
OR = "int  1"
NOT = "int  2"
EQUALITY_MATCH = "int  3"
SUBSTRINGS = "int  4"
GREATER_OR_EQUAL = "int  5"
LESS_OR_EQUAL = "int  6"
PRESENT = "int  7"
APPROX_MATCH = "int  8"
EXTENSIBLE_MATCH = "int  9"
INITIAL = "int  0"
ANY = "int  1"
FINAL = "int  2"
def ():
    '''returns FilterIterator\n\n
    (final String s)\n
    ()\n
    (final String filter)\n
    (final ASN1Tagged root)\n
    '''
def startSubstrings():
    '''returns None\n\n
    startSubstrings(final String s)\n
    '''
def addSubstring():
    '''returns None\n\n
    addSubstring(final int n, final byte[] array)\n
    '''
def endSubstrings():
    '''returns None\n\n
    endSubstrings()\n
    '''
def addAttributeValueAssertion():
    '''returns None\n\n
    addAttributeValueAssertion(final int n, final String s, final byte[] array)\n
    '''
def addPresent():
    '''returns None\n\n
    addPresent(final String s)\n
    '''
def addExtensibleMatch():
    '''returns None\n\n
    addExtensibleMatch(final String s, final String s2, final byte[] array, final boolean b)\n
    '''
def startNestedFilter():
    '''returns None\n\n
    startNestedFilter(final int n)\n
    '''
def endNestedFilter():
    '''returns None\n\n
    endNestedFilter(final int n)\n
    '''
def getFilterIterator():
    '''returns Iterator\n\n
    getFilterIterator()\n
    '''
def filterToString():
    '''returns String\n\n
    filterToString()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns Object\n\n
    next()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
