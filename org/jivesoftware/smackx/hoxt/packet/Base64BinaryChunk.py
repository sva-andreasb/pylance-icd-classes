ELEMENT_CHUNK = "String  \"chunk\""
ATTRIBUTE_STREAM_ID = "String  \"streamId\""
ATTRIBUTE_LAST = "String  \"last\""
ATTRIBUTE_NR = "String  \"nr\""
def Base64BinaryChunk():
    '''public Base64BinaryChunk(final String text, final String streamId, final int nr, final boolean last)
    public Base64BinaryChunk(final String text, final String streamId, final int nr)
    '''
def getStreamId():
    '''public String getStreamId()
    '''
def isLast():
    '''public boolean isLast()
    '''
def getText():
    '''public String getText()
    '''
def getNr():
    '''public int getNr()
    '''
def getElementName():
    '''public String getElementName()
    '''
def getNamespace():
    '''public String getNamespace()
    '''
def toXML():
    '''public XmlStringBuilder toXML(final String enclosingNamespace)
    '''
