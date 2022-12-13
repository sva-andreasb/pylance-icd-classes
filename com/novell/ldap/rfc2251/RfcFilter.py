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
pass
def startSubstrings():
'''public void startSubstrings(final String s)
'''
pass
def addSubstring():
'''public void addSubstring(final int n, final byte[] array)
'''
pass
def endSubstrings():
'''public void endSubstrings()
'''
pass
def addAttributeValueAssertion():
'''public void addAttributeValueAssertion(final int n, final String s, final byte[] array)
'''
pass
def addPresent():
'''public void addPresent(final String s)
'''
pass
def addExtensibleMatch():
'''public void addExtensibleMatch(final String s, final String s2, final byte[] array, final boolean b)
'''
pass
def startNestedFilter():
'''public void startNestedFilter(final int n)
'''
pass
def endNestedFilter():
'''public void endNestedFilter(final int n)
'''
pass
def getFilterIterator():
'''public Iterator getFilterIterator()
'''
pass
def filterToString():
'''public String filterToString()
'''
pass
def FilterTokenizer():
'''public FilterTokenizer(final String filter)
'''
pass
def getLeftParen():
'''public final void getLeftParen()
'''
pass
def getRightParen():
'''public final void getRightParen()
'''
pass
def getOpOrAttr():
'''public final int getOpOrAttr()
'''
pass
def getFilterType():
'''public final int getFilterType()
'''
pass
def getValue():
'''public final String getValue()
'''
pass
def getAttr():
'''public final String getAttr()
'''
pass
def peekChar():
'''public final char peekChar()
'''
pass
def FilterIterator():
'''public FilterIterator(final ASN1Tagged root)
'''
pass
def hasNext():
'''public boolean hasNext()
'''
pass
def next():
'''public Object next()
'''
pass
def remove():
'''public void remove()
'''
pass
