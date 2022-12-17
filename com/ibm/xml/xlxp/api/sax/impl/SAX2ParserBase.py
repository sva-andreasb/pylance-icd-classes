def xmlDeclEvent():
    '''returns None\n\n
    xmlDeclEvent(final XMLString xmlString)\n
    '''
def startElementEvent():
    '''returns None\n\n
    startElementEvent(final QName qName, final NSDeclList fnsDecls, final AttrList fAttrs, final boolean b)\n
    '''
def endElementEvent():
    '''returns None\n\n
    endElementEvent(final QName qName, final NSDeclList fnsDecls)\n
    '''
def characters():
    '''returns None\n\n
    characters(final XMLString xmlString)\n
    '''
def whitespace():
    '''returns None\n\n
    whitespace(final XMLString xmlString)\n
    '''
def character():
    '''returns None\n\n
    character(final int n, final boolean b)\n
    '''
def processingInstruction():
    '''returns None\n\n
    processingInstruction(final XMLString xmlString, final XMLString xmlString2)\n
    '''
def skippedEntity():
    '''returns boolean\n\n
    skippedEntity(final XMLString xmlString)\n
    '''
def startEntity():
    '''returns None\n\n
    startEntity(final XMLString xmlString)\n
    '''
def endEntity():
    '''returns None\n\n
    endEntity(final XMLString xmlString)\n
    '''
def startCDATASection():
    '''returns None\n\n
    startCDATASection()\n
    '''
def endCDATASection():
    '''returns None\n\n
    endCDATASection()\n
    '''
def comment():
    '''returns None\n\n
    comment(final XMLString xmlString)\n
    '''
def reportWarning():
    '''returns None\n\n
    reportWarning(final String s, final int n, final int n2, final XMLString[] array)\n
    '''
def reportRecoverableError():
    '''returns None\n\n
    reportRecoverableError(final String s, final int n, final int n2, final XMLString[] array)\n
    '''
def reportFatalError():
    '''returns None\n\n
    reportFatalError(final String s, final int n, final int n2, final XMLString[] array)\n
    '''
def getLength():
    '''returns int\n\n
    getLength()\n
    '''
def getURI():
    '''returns String\n\n
    getURI(final int n)\n
    '''
def getLocalName():
    '''returns String\n\n
    getLocalName(final int n)\n
    '''
def getQName():
    '''returns String\n\n
    getQName(final int n)\n
    '''
def getType():
    '''returns String\n\n
    getType(final int n)\n
    getType(final String s, final String s2)\n
    getType(final String s)\n
    '''
def getValue():
    '''returns String\n\n
    getValue(int n)\n
    getValue(final String s, final String s2)\n
    getValue(final String s)\n
    '''
def getIndex():
    '''returns int\n\n
    getIndex(final String s, final String s2)\n
    getIndex(final String s)\n
    '''
def getPublicId():
    '''returns String\n\n
    getPublicId()\n
    '''
def getSystemId():
    '''returns String\n\n
    getSystemId()\n
    '''
def getLineNumber():
    '''returns int\n\n
    getLineNumber()\n
    '''
def getColumnNumber():
    '''returns int\n\n
    getColumnNumber()\n
    '''
def getFeature():
    '''returns boolean\n\n
    getFeature(final String s)\n
    '''
def setFeature():
    '''returns None\n\n
    setFeature(final String s, final boolean b)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String s)\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final String s, final Object o)\n
    '''
def setContentHandler():
    '''returns None\n\n
    setContentHandler(final ContentHandler fContentHandler)\n
    '''
def getContentHandler():
    '''returns ContentHandler\n\n
    getContentHandler()\n
    '''
def setErrorHandler():
    '''returns None\n\n
    setErrorHandler(final ErrorHandler fErrorHandler)\n
    '''
def getErrorHandler():
    '''returns ErrorHandler\n\n
    getErrorHandler()\n
    '''
def parse():
    '''returns None\n\n
    parse(final InputSource inputSource)\n
    parse(final String systemId)\n
    '''
