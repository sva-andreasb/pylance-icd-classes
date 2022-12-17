ELEMENT_CHUNK = "String  \"chunk\""
ATTRIBUTE_STREAM_ID = "String  \"streamId\""
ATTRIBUTE_LAST = "String  \"last\""
ATTRIBUTE_NR = "String  \"nr\""
def ():
    '''returns Base64BinaryChunk\n\n
    (final String text, final String streamId, final int nr, final boolean last)\n
    (final String text, final String streamId, final int nr)\n
    '''
def getStreamId():
    '''returns String\n\n
    getStreamId()\n
    '''
def isLast():
    '''returns boolean\n\n
    isLast()\n
    '''
def getText():
    '''returns String\n\n
    getText()\n
    '''
def getNr():
    '''returns int\n\n
    getNr()\n
    '''
def getElementName():
    '''returns String\n\n
    getElementName()\n
    '''
def getNamespace():
    '''returns String\n\n
    getNamespace()\n
    '''
def toXML():
    '''returns XmlStringBuilder\n\n
    toXML(final String enclosingNamespace)\n
    '''
