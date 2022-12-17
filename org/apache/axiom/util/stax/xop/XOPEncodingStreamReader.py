def ():
    '''returns NamespaceContextWrapper\n\n
    (final XMLStreamReader parent, final ContentIDGenerator contentIDGenerator, final OptimizationPolicy optimizationPolicy)\n
    (final NamespaceContext parent)\n
    '''
def next():
    '''returns int\n\n
    next()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def nextTag():
    '''returns int\n\n
    nextTag()\n
    '''
def require():
    '''returns None\n\n
    require(final int type, final String namespaceURI, final String localName)\n
    '''
def getLocation():
    '''returns Location\n\n
    getLocation()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String name)\n
    '''
def getEncoding():
    '''returns String\n\n
    getEncoding()\n
    '''
def getCharacterEncodingScheme():
    '''returns String\n\n
    getCharacterEncodingScheme()\n
    '''
def getVersion():
    '''returns String\n\n
    getVersion()\n
    '''
def isStandalone():
    '''returns boolean\n\n
    isStandalone()\n
    '''
def standaloneSet():
    '''returns boolean\n\n
    standaloneSet()\n
    '''
def getPIData():
    '''returns String\n\n
    getPIData()\n
    '''
def getPITarget():
    '''returns String\n\n
    getPITarget()\n
    '''
def getAttributeCount():
    '''returns int\n\n
    getAttributeCount()\n
    '''
def getAttributeLocalName():
    '''returns String\n\n
    getAttributeLocalName(final int index)\n
    '''
def getAttributeName():
    '''returns QName\n\n
    getAttributeName(final int index)\n
    '''
def getAttributeNamespace():
    '''returns String\n\n
    getAttributeNamespace(final int index)\n
    '''
def getAttributePrefix():
    '''returns String\n\n
    getAttributePrefix(final int index)\n
    '''
def getAttributeType():
    '''returns String\n\n
    getAttributeType(final int index)\n
    '''
def getAttributeValue():
    '''returns String\n\n
    getAttributeValue(final int index)\n
    getAttributeValue(final String namespaceURI, final String localName)\n
    '''
def isAttributeSpecified():
    '''returns boolean\n\n
    isAttributeSpecified(final int index)\n
    '''
def getElementText():
    '''returns String\n\n
    getElementText()\n
    '''
def getEventType():
    '''returns int\n\n
    getEventType()\n
    '''
def getNamespaceURI():
    '''returns String\n\n
    getNamespaceURI()\n
    getNamespaceURI(final String prefix)\n
    getNamespaceURI(final int index)\n
    getNamespaceURI(final String prefix)\n
    '''
def getLocalName():
    '''returns String\n\n
    getLocalName()\n
    '''
def getPrefix():
    '''returns String\n\n
    getPrefix()\n
    getPrefix(final String namespaceURI)\n
    '''
def getName():
    '''returns QName\n\n
    getName()\n
    '''
def getNamespaceContext():
    '''returns NamespaceContext\n\n
    getNamespaceContext()\n
    '''
def getNamespaceCount():
    '''returns int\n\n
    getNamespaceCount()\n
    '''
def getNamespacePrefix():
    '''returns String\n\n
    getNamespacePrefix(final int index)\n
    '''
def getText():
    '''returns String\n\n
    getText()\n
    '''
def getTextStart():
    '''returns int\n\n
    getTextStart()\n
    '''
def getTextLength():
    '''returns int\n\n
    getTextLength()\n
    '''
def getTextCharacters():
    '''returns int\n\n
    getTextCharacters()\n
    getTextCharacters(final int sourceStart, final char[] target, final int targetStart, final int length)\n
    '''
def hasName():
    '''returns boolean\n\n
    hasName()\n
    '''
def hasText():
    '''returns boolean\n\n
    hasText()\n
    '''
def isCharacters():
    '''returns boolean\n\n
    isCharacters()\n
    '''
def isWhiteSpace():
    '''returns boolean\n\n
    isWhiteSpace()\n
    '''
def isStartElement():
    '''returns boolean\n\n
    isStartElement()\n
    '''
def isEndElement():
    '''returns boolean\n\n
    isEndElement()\n
    '''
def getPrefixes():
    '''returns Iterator\n\n
    getPrefixes(final String namespaceURI)\n
    '''
