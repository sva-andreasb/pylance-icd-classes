def ():
    '''returns StAXNamespaceContext\n\n
    (final InputSource inputSource, final XMLInputFactoryImpl.Properties properties)\n
    ()\n
    '''
def reset():
    '''returns None\n\n
    reset(final boolean b)\n
    '''
def dropBufferReferences():
    '''returns None\n\n
    dropBufferReferences()\n
    '''
def setDocumentEntity():
    '''returns None\n\n
    setDocumentEntity(final InputSource inputSource, final XMLInputFactoryImpl.Properties fProperties)\n
    '''
def resolveEntity():
    '''returns InputSource\n\n
    resolveEntity(final String s, final String s2)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String s)\n
    '''
def next():
    '''returns int\n\n
    next()\n
    '''
def require():
    '''returns None\n\n
    require(final int value, final String s, final String s2)\n
    '''
def getElementText():
    '''returns String\n\n
    getElementText()\n
    '''
def nextTag():
    '''returns int\n\n
    nextTag()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def getNamespaceURI():
    '''returns String\n\n
    getNamespaceURI(final String s)\n
    getNamespaceURI(final int n)\n
    getNamespaceURI()\n
    getNamespaceURI(final String s)\n
    '''
def isStartElement():
    '''returns boolean\n\n
    isStartElement()\n
    '''
def isEndElement():
    '''returns boolean\n\n
    isEndElement()\n
    '''
def isCharacters():
    '''returns boolean\n\n
    isCharacters()\n
    '''
def isWhiteSpace():
    '''returns boolean\n\n
    isWhiteSpace()\n
    '''
def getAttributeValue():
    '''returns XMLString\n\n
    getAttributeValue(final String s, final String s2)\n
    getAttributeValue(final int n)\n
    getAttributeValue(final int n, final int n2)\n
    '''
def getAttributeCount():
    '''returns int\n\n
    getAttributeCount()\n
    '''
def getAttributeName():
    '''returns QName\n\n
    getAttributeName(final int n)\n
    '''
def getAttributeNamespace():
    '''returns String\n\n
    getAttributeNamespace(final int n)\n
    '''
def getAttributeLocalName():
    '''returns String\n\n
    getAttributeLocalName(final int n)\n
    '''
def getAttributePrefix():
    '''returns String\n\n
    getAttributePrefix(final int n)\n
    '''
def getAttributeType():
    '''returns String\n\n
    getAttributeType(final int n)\n
    '''
def isAttributeSpecified():
    '''returns boolean\n\n
    isAttributeSpecified(final int n)\n
    '''
def getNamespaceCount():
    '''returns int\n\n
    getNamespaceCount()\n
    '''
def getNamespacePrefix():
    '''returns String\n\n
    getNamespacePrefix(final int n)\n
    '''
def getNamespaceContext():
    '''returns NamespaceContext\n\n
    getNamespaceContext()\n
    '''
def getEventType():
    '''returns int\n\n
    getEventType()\n
    '''
def getText():
    '''returns String\n\n
    getText()\n
    '''
def getTextCharacters():
    '''returns int\n\n
    getTextCharacters()\n
    getTextCharacters(final int n, final char[] array, final int n2, int n3)\n
    '''
def getTextStart():
    '''returns int\n\n
    getTextStart()\n
    '''
def getTextLength():
    '''returns int\n\n
    getTextLength()\n
    '''
def getEncoding():
    '''returns String\n\n
    getEncoding()\n
    '''
def hasText():
    '''returns boolean\n\n
    hasText()\n
    '''
def getLocation():
    '''returns Location\n\n
    getLocation()\n
    '''
def getName():
    '''returns QName\n\n
    getName()\n
    '''
def getLocalName():
    '''returns String\n\n
    getLocalName()\n
    '''
def hasName():
    '''returns boolean\n\n
    hasName()\n
    '''
def getPrefix():
    '''returns String\n\n
    getPrefix()\n
    getPrefix(final String s)\n
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
def getCharacterEncodingScheme():
    '''returns String\n\n
    getCharacterEncodingScheme()\n
    '''
def getPITarget():
    '''returns String\n\n
    getPITarget()\n
    '''
def getPIData():
    '''returns String\n\n
    getPIData()\n
    '''
def nsDeclList():
    '''returns NSDeclList\n\n
    nsDeclList()\n
    '''
def attrList():
    '''returns AttrList\n\n
    attrList()\n
    '''
def produceStartDocumentEvent():
    '''returns boolean\n\n
    produceStartDocumentEvent()\n
    '''
def produceEndDocumentEvent():
    '''returns boolean\n\n
    produceEndDocumentEvent()\n
    '''
def produceEmptyElementEvent():
    '''returns boolean\n\n
    produceEmptyElementEvent()\n
    '''
def produceStartElementEvent():
    '''returns boolean\n\n
    produceStartElementEvent()\n
    '''
def produceLeafElementEvent():
    '''returns boolean\n\n
    produceLeafElementEvent()\n
    '''
def produceEndElementEvent():
    '''returns boolean\n\n
    produceEndElementEvent(final com.ibm.xml.xlxp.scan.util.QName qName)\n
    '''
def produceCharactersEvent():
    '''returns boolean\n\n
    produceCharactersEvent()\n
    '''
def produceWhitespaceEvent():
    '''returns boolean\n\n
    produceWhitespaceEvent()\n
    '''
def produceStartCDATASectionEvent():
    '''returns boolean\n\n
    produceStartCDATASectionEvent()\n
    '''
def produceEndCDATASectionEvent():
    '''returns boolean\n\n
    produceEndCDATASectionEvent()\n
    '''
def produceCharacterEvent():
    '''returns boolean\n\n
    produceCharacterEvent(final int n)\n
    '''
def producePredefinedEntityEvent():
    '''returns boolean\n\n
    producePredefinedEntityEvent(final int n)\n
    '''
def produceProcessingInstructionEvent():
    '''returns boolean\n\n
    produceProcessingInstructionEvent()\n
    '''
def produceCommentEvent():
    '''returns boolean\n\n
    produceCommentEvent()\n
    '''
def produceWarningEvent():
    '''returns boolean\n\n
    produceWarningEvent(final String s, final int n)\n
    '''
def produceRecoverableErrorEvent():
    '''returns boolean\n\n
    produceRecoverableErrorEvent(final String s, final int n)\n
    '''
def produceFatalErrorEvent():
    '''returns boolean\n\n
    produceFatalErrorEvent(final String s, final int n)\n
    '''
def reportFatalError():
    '''returns boolean\n\n
    reportFatalError(final String s, final int n)\n
    '''
def produceDoctypeEvent():
    '''returns boolean\n\n
    produceDoctypeEvent(final boolean b)\n
    '''
def produceEntityReferenceEvent():
    '''returns boolean\n\n
    produceEntityReferenceEvent()\n
    '''
def getLineNumber():
    '''returns int\n\n
    getLineNumber()\n
    '''
def getColumnNumber():
    '''returns int\n\n
    getColumnNumber()\n
    '''
def getCharacterOffset():
    '''returns int\n\n
    getCharacterOffset()\n
    '''
def getPublicId():
    '''returns String\n\n
    getPublicId()\n
    '''
def getSystemId():
    '''returns String\n\n
    getSystemId()\n
    '''
def setNSContext():
    '''returns None\n\n
    setNSContext(final int fxlxpnsContext)\n
    '''
def getPrefixes():
    '''returns Iterator\n\n
    getPrefixes(final String s)\n
    '''
