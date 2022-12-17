def ():
    '''returns ClosedXMLStreamReader\n\n
    ()\n
    ()\n
    (final Properties properties)\n
    (final XMLStreamReader fStreamReader)\n
    (final XMLStreamReader xmlStreamReader)\n
    ()\n
    '''
def createXMLStreamReader():
    '''returns XMLStreamReader\n\n
    createXMLStreamReader(final Reader reader)\n
    createXMLStreamReader(final Source source)\n
    createXMLStreamReader(final InputStream inputStream)\n
    createXMLStreamReader(final InputStream inputStream, final String s)\n
    createXMLStreamReader(final String s, final InputStream inputStream)\n
    createXMLStreamReader(final String s, final Reader reader)\n
    '''
def createXMLEventReader():
    '''returns XMLEventReader\n\n
    createXMLEventReader(final Reader reader)\n
    createXMLEventReader(final String s, final Reader reader)\n
    createXMLEventReader(final XMLStreamReader xmlStreamReader)\n
    createXMLEventReader(final Source source)\n
    createXMLEventReader(final InputStream inputStream)\n
    createXMLEventReader(final InputStream inputStream, final String s)\n
    createXMLEventReader(final String s, final InputStream inputStream)\n
    '''
def createFilteredReader():
    '''returns XMLEventReader\n\n
    createFilteredReader(final XMLStreamReader xmlStreamReader, final StreamFilter streamFilter)\n
    createFilteredReader(final XMLEventReader xmlEventReader, final EventFilter eventFilter)\n
    '''
def getXMLResolver():
    '''returns XMLResolver\n\n
    getXMLResolver()\n
    '''
def setXMLResolver():
    '''returns None\n\n
    setXMLResolver(final XMLResolver resolver)\n
    '''
def getXMLReporter():
    '''returns XMLReporter\n\n
    getXMLReporter()\n
    '''
def setXMLReporter():
    '''returns None\n\n
    setXMLReporter(final XMLReporter reporter)\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final String anObject, final Object o)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String s)\n
    getProperty(final String s)\n
    getProperty(final String s)\n
    getProperty(final String s)\n
    getProperty(final String s)\n
    '''
def isPropertySupported():
    '''returns boolean\n\n
    isPropertySupported(final String anObject)\n
    '''
def setEventAllocator():
    '''returns None\n\n
    setEventAllocator(final XMLEventAllocator allocator)\n
    '''
def getEventAllocator():
    '''returns XMLEventAllocator\n\n
    getEventAllocator()\n
    '''
def insertFilter():
    '''returns None\n\n
    insertFilter(final XMLStreamReader fStreamReader)\n
    '''
def next():
    '''returns int\n\n
    next()\n
    next()\n
    next()\n
    next()\n
    '''
def require():
    '''returns None\n\n
    require(final int n, final String s, final String s2)\n
    require(final int value, final String s, final String s2)\n
    require(final int value, final String s, final String s2)\n
    require(final int n, final String s, final String s2)\n
    '''
def getElementText():
    '''returns String\n\n
    getElementText()\n
    getElementText()\n
    getElementText()\n
    getElementText()\n
    '''
def nextTag():
    '''returns int\n\n
    nextTag()\n
    nextTag()\n
    nextTag()\n
    nextTag()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    hasNext()\n
    hasNext()\n
    hasNext()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    close()\n
    close()\n
    close()\n
    '''
def getNamespaceURI():
    '''returns String\n\n
    getNamespaceURI(final String s)\n
    getNamespaceURI(final int n)\n
    getNamespaceURI()\n
    getNamespaceURI(final String s)\n
    getNamespaceURI(final int n)\n
    getNamespaceURI()\n
    getNamespaceURI(final String s)\n
    getNamespaceURI(final int n)\n
    getNamespaceURI()\n
    getNamespaceURI(final String s)\n
    getNamespaceURI(final int n)\n
    getNamespaceURI()\n
    '''
def isStartElement():
    '''returns boolean\n\n
    isStartElement()\n
    isStartElement()\n
    isStartElement()\n
    isStartElement()\n
    '''
def isEndElement():
    '''returns boolean\n\n
    isEndElement()\n
    isEndElement()\n
    isEndElement()\n
    isEndElement()\n
    '''
def isCharacters():
    '''returns boolean\n\n
    isCharacters()\n
    isCharacters()\n
    isCharacters()\n
    isCharacters()\n
    '''
def isWhiteSpace():
    '''returns boolean\n\n
    isWhiteSpace()\n
    isWhiteSpace()\n
    isWhiteSpace()\n
    isWhiteSpace()\n
    '''
def getAttributeValue():
    '''returns String\n\n
    getAttributeValue(final String s, final String s2)\n
    getAttributeValue(final int n)\n
    getAttributeValue(final String s, final String s2)\n
    getAttributeValue(final int n)\n
    getAttributeValue(final String s, final String s2)\n
    getAttributeValue(final int n)\n
    getAttributeValue(final String s, final String s2)\n
    getAttributeValue(final int n)\n
    '''
def getAttributeCount():
    '''returns int\n\n
    getAttributeCount()\n
    getAttributeCount()\n
    getAttributeCount()\n
    getAttributeCount()\n
    '''
def getAttributeName():
    '''returns QName\n\n
    getAttributeName(final int n)\n
    getAttributeName(final int n)\n
    getAttributeName(final int n)\n
    getAttributeName(final int n)\n
    '''
def getAttributeNamespace():
    '''returns String\n\n
    getAttributeNamespace(final int n)\n
    getAttributeNamespace(final int n)\n
    getAttributeNamespace(final int n)\n
    getAttributeNamespace(final int n)\n
    '''
def getAttributeLocalName():
    '''returns String\n\n
    getAttributeLocalName(final int n)\n
    getAttributeLocalName(final int n)\n
    getAttributeLocalName(final int n)\n
    getAttributeLocalName(final int n)\n
    '''
def getAttributePrefix():
    '''returns String\n\n
    getAttributePrefix(final int n)\n
    getAttributePrefix(final int n)\n
    getAttributePrefix(final int n)\n
    getAttributePrefix(final int n)\n
    '''
def getAttributeType():
    '''returns String\n\n
    getAttributeType(final int n)\n
    getAttributeType(final int n)\n
    getAttributeType(final int n)\n
    getAttributeType(final int n)\n
    '''
def isAttributeSpecified():
    '''returns boolean\n\n
    isAttributeSpecified(final int n)\n
    isAttributeSpecified(final int n)\n
    isAttributeSpecified(final int n)\n
    isAttributeSpecified(final int n)\n
    '''
def getNamespaceCount():
    '''returns int\n\n
    getNamespaceCount()\n
    getNamespaceCount()\n
    getNamespaceCount()\n
    getNamespaceCount()\n
    '''
def getNamespacePrefix():
    '''returns String\n\n
    getNamespacePrefix(final int n)\n
    getNamespacePrefix(final int n)\n
    getNamespacePrefix(final int n)\n
    getNamespacePrefix(final int n)\n
    '''
def getNamespaceContext():
    '''returns NamespaceContext\n\n
    getNamespaceContext()\n
    getNamespaceContext()\n
    getNamespaceContext()\n
    getNamespaceContext()\n
    '''
def getEventType():
    '''returns int\n\n
    getEventType()\n
    getEventType()\n
    getEventType()\n
    getEventType()\n
    '''
def getText():
    '''returns String\n\n
    getText()\n
    getText()\n
    getText()\n
    getText()\n
    '''
def getTextCharacters():
    '''returns int\n\n
    getTextCharacters()\n
    getTextCharacters(final int n, final char[] array, final int n2, final int n3)\n
    getTextCharacters()\n
    getTextCharacters(final int n, final char[] array, final int n2, final int n3)\n
    getTextCharacters()\n
    getTextCharacters(final int value, final char[] array, final int value2, final int value3)\n
    getTextCharacters()\n
    getTextCharacters(final int n, final char[] array, final int n2, final int n3)\n
    '''
def getTextStart():
    '''returns int\n\n
    getTextStart()\n
    getTextStart()\n
    getTextStart()\n
    getTextStart()\n
    '''
def getTextLength():
    '''returns int\n\n
    getTextLength()\n
    getTextLength()\n
    getTextLength()\n
    getTextLength()\n
    '''
def getEncoding():
    '''returns String\n\n
    getEncoding()\n
    getEncoding()\n
    getEncoding()\n
    getEncoding()\n
    '''
def hasText():
    '''returns boolean\n\n
    hasText()\n
    hasText()\n
    hasText()\n
    hasText()\n
    '''
def getLocation():
    '''returns Location\n\n
    getLocation()\n
    getLocation()\n
    getLocation()\n
    getLocation()\n
    '''
def getName():
    '''returns QName\n\n
    getName()\n
    getName()\n
    getName()\n
    getName()\n
    '''
def getLocalName():
    '''returns String\n\n
    getLocalName()\n
    getLocalName()\n
    getLocalName()\n
    getLocalName()\n
    '''
def hasName():
    '''returns boolean\n\n
    hasName()\n
    hasName()\n
    hasName()\n
    hasName()\n
    '''
def getPrefix():
    '''returns String\n\n
    getPrefix()\n
    getPrefix()\n
    getPrefix()\n
    getPrefix()\n
    '''
def getVersion():
    '''returns String\n\n
    getVersion()\n
    getVersion()\n
    getVersion()\n
    getVersion()\n
    '''
def isStandalone():
    '''returns boolean\n\n
    isStandalone()\n
    isStandalone()\n
    isStandalone()\n
    isStandalone()\n
    '''
def standaloneSet():
    '''returns boolean\n\n
    standaloneSet()\n
    standaloneSet()\n
    standaloneSet()\n
    standaloneSet()\n
    '''
def getCharacterEncodingScheme():
    '''returns String\n\n
    getCharacterEncodingScheme()\n
    getCharacterEncodingScheme()\n
    getCharacterEncodingScheme()\n
    getCharacterEncodingScheme()\n
    '''
def getPITarget():
    '''returns String\n\n
    getPITarget()\n
    getPITarget()\n
    getPITarget()\n
    getPITarget()\n
    '''
def getPIData():
    '''returns String\n\n
    getPIData()\n
    getPIData()\n
    getPIData()\n
    getPIData()\n
    '''
def writeStAXProfile():
    '''returns None\n\n
    writeStAXProfile(final String s)\n
    '''
def writeReadableProfile():
    '''returns None\n\n
    writeReadableProfile(final String s)\n
    '''
