def ():
    '''returns InternalEntityMonitor\n\n
    ()\n
    (final SymbolTable symbolTable)\n
    (final SymbolTable symbolTable, final XMLGrammarPool xmlGrammarPool)\n
    (final SymbolTable symbolTable, final XMLGrammarPool xmlGrammarPool, final XMLComponentManager xmlComponentManager)\n
    ()\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String s)\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final String s, final Object o)\n
    '''
def resolveEntity():
    '''returns XMLInputSource\n\n
    resolveEntity(final XMLResourceIdentifier xmlResourceIdentifier)\n
    '''
def setEntityResolver():
    '''returns None\n\n
    setEntityResolver(final XMLEntityResolver fEntityResolver)\n
    '''
def getEntityResolver():
    '''returns XMLEntityResolver\n\n
    getEntityResolver()\n
    '''
def read():
    '''returns int\n\n
    read()\n
    read(final char[] cbuf, final int off, final int len)\n
    read()\n
    read(final byte[] b, final int off, final int len)\n
    '''
def startDTD():
    '''returns None\n\n
    startDTD(final XMLLocator xmlLocator, final Augmentations augmentations)\n
    '''
def startParameterEntity():
    '''returns None\n\n
    startParameterEntity(final String s, final XMLResourceIdentifier xmlResourceIdentifier, final String s2, final Augmentations augmentations)\n
    '''
def textDecl():
    '''returns None\n\n
    textDecl(final String s, final String s2, final Augmentations augmentations)\n
    '''
def endParameterEntity():
    '''returns None\n\n
    endParameterEntity(final String s, final Augmentations augmentations)\n
    '''
def startExternalSubset():
    '''returns None\n\n
    startExternalSubset(final XMLResourceIdentifier xmlResourceIdentifier, final Augmentations augmentations)\n
    '''
def endExternalSubset():
    '''returns None\n\n
    endExternalSubset(final Augmentations augmentations)\n
    '''
def comment():
    '''returns None\n\n
    comment(final XMLString xmlString, final Augmentations augmentations)\n
    '''
def processingInstruction():
    '''returns None\n\n
    processingInstruction(final String s, final XMLString xmlString, final Augmentations augmentations)\n
    '''
def elementDecl():
    '''returns None\n\n
    elementDecl(final String s, final String s2, final Augmentations augmentations)\n
    '''
def startAttlist():
    '''returns None\n\n
    startAttlist(final String s, final Augmentations augmentations)\n
    '''
def attributeDecl():
    '''returns None\n\n
    attributeDecl(final String s, final String s2, final String s3, final String[] array, final String s4, final XMLString xmlString, final XMLString xmlString2, final Augmentations augmentations)\n
    '''
def endAttlist():
    '''returns None\n\n
    endAttlist(final Augmentations augmentations)\n
    '''
def internalEntityDecl():
    '''returns None\n\n
    internalEntityDecl(final String s, final XMLString xmlString, final XMLString xmlString2, final Augmentations augmentations)\n
    '''
def externalEntityDecl():
    '''returns None\n\n
    externalEntityDecl(final String s, final XMLResourceIdentifier xmlResourceIdentifier, final Augmentations augmentations)\n
    '''
def unparsedEntityDecl():
    '''returns None\n\n
    unparsedEntityDecl(final String s, final XMLResourceIdentifier xmlResourceIdentifier, final String s2, final Augmentations augmentations)\n
    '''
def notationDecl():
    '''returns None\n\n
    notationDecl(final String s, final XMLResourceIdentifier xmlResourceIdentifier, final Augmentations augmentations)\n
    '''
def startConditional():
    '''returns None\n\n
    startConditional(final short n, final Augmentations augmentations)\n
    '''
def ignoredCharacters():
    '''returns None\n\n
    ignoredCharacters(final XMLString xmlString, final Augmentations augmentations)\n
    '''
def endConditional():
    '''returns None\n\n
    endConditional(final Augmentations augmentations)\n
    '''
def endDTD():
    '''returns None\n\n
    endDTD(final Augmentations augmentations)\n
    '''
def setDTDSource():
    '''returns None\n\n
    setDTDSource(final XMLDTDSource fdtdSource)\n
    '''
def getDTDSource():
    '''returns XMLDTDSource\n\n
    getDTDSource()\n
    '''
def setDTDHandler():
    '''returns None\n\n
    setDTDHandler(final XMLDTDHandler fdtdHandler)\n
    '''
def getDTDHandler():
    '''returns XMLDTDHandler\n\n
    getDTDHandler()\n
    '''
