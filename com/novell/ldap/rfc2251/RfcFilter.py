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
def RfcFilter():
    '''public RfcFilter(final String s)
    public RfcFilter()
    '''
def startSubstrings():
    '''public void startSubstrings(final String s)
    '''
def addSubstring():
    '''public void addSubstring(final int n, final byte[] array)
    '''
def endSubstrings():
    '''public void endSubstrings()
    '''
def addAttributeValueAssertion():
    '''public void addAttributeValueAssertion(final int n, final String s, final byte[] array)
    '''
def addPresent():
    '''public void addPresent(final String s)
    '''
def addExtensibleMatch():
    '''public void addExtensibleMatch(final String s, final String s2, final byte[] array, final boolean b)
    '''
def startNestedFilter():
    '''public void startNestedFilter(final int n)
    '''
def endNestedFilter():
    '''public void endNestedFilter(final int n)
    '''
def getFilterIterator():
    '''public Iterator getFilterIterator()
    '''
def filterToString():
    '''public String filterToString()
    '''
def FilterTokenizer():
    '''public FilterTokenizer(final String filter)
    '''
def getLeftParen():
    '''public final void getLeftParen()
    '''
def getRightParen():
    '''public final void getRightParen()
    '''
def getOpOrAttr():
    '''public final int getOpOrAttr()
    '''
def getFilterType():
    '''public final int getFilterType()
    '''
def getValue():
    '''public final String getValue()
    '''
def getAttr():
    '''public final String getAttr()
    '''
def peekChar():
    '''public final char peekChar()
    '''
def FilterIterator():
    '''public FilterIterator(final ASN1Tagged root)
    '''
def hasNext():
    '''public boolean hasNext()
    '''
def next():
    '''public Object next()
    '''
def remove():
    '''public void remove()
    '''
