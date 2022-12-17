NAMESPACE = "String  \"urn:xmpp:markup:0\""
ELEMENT = "String  \"markup\""
ATTR_START = "String  \"start\""
ATTR_END = "String  \"end\""
def ():
    '''returns MarkupElement\n\n
    (final List<MarkupChildElement> childElements)\n
    '''
def getChildElements():
    '''returns List<MarkupChildElement>\n\n
    getChildElements()\n
    '''
def getNamespace():
    '''returns String\n\n
    getNamespace()\n
    '''
def getElementName():
    '''returns String\n\n
    getElementName()\n
    '''
def toXML():
    '''returns XmlStringBuilder\n\n
    toXML(final String enclosingNamespace)\n
    '''
def setDeleted():
    '''returns Builder\n\n
    setDeleted(final int start, final int end)\n
    '''
def setEmphasis():
    '''returns Builder\n\n
    setEmphasis(final int start, final int end)\n
    '''
def setCode():
    '''returns Builder\n\n
    setCode(final int start, final int end)\n
    '''
def addSpan():
    '''returns Builder\n\n
    addSpan(final int start, final int end, final Set<SpanElement.SpanStyle> styles)\n
    '''
def setBlockQuote():
    '''returns Builder\n\n
    setBlockQuote(final int start, final int end)\n
    '''
def setCodeBlock():
    '''returns Builder\n\n
    setCodeBlock(final int start, final int end)\n
    '''
def beginList():
    '''returns ListBuilder\n\n
    beginList()\n
    '''
def build():
    '''returns MarkupElement\n\n
    build()\n
    '''
def addEntry():
    '''returns ListBuilder\n\n
    addEntry(final int start, final int end)\n
    '''
def endList():
    '''returns Builder\n\n
    endList()\n
    '''
