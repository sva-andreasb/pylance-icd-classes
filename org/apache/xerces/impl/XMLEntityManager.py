DEFAULT_BUFFER_SIZE = "int  2048"
DEFAULT_XMLDECL_BUFFER_SIZE = "int  64"
DEFAULT_INTERNAL_BUFFER_SIZE = "int  512"
def ():
    '''returns InternalEntity\n\n
    ()\n
    (final XMLEntityManager xmlEntityManager)\n
    (final InputStream fInputStream)\n
    (final String s, final XMLResourceIdentifier entityLocation, final InputStream stream, final Reader reader, final byte[] fByteBuffer, final String encoding, final boolean literal, final boolean mayReadChunks, final boolean isExternal)\n
    ()\n
    (final String name, final boolean inExternalSubset)\n
    (final boolean isExternal, final int n)\n
    (final int n, final int n2)\n
    (final int fPoolSize, final int fExternalBufferSize, final int fInternalBufferSize)\n
    (final int n)\n
    (final int fPoolSize, final int fBufferSize)\n
    ()\n
    (final String s, final XMLResourceIdentifier entityLocation, final String notation, final boolean b)\n
    ()\n
    (final String s, final String text, final boolean b)\n
    (final String s, final String s2, final boolean b, final int paramEntityRefs)\n
    '''
def setStandalone():
    '''returns None\n\n
    setStandalone(final boolean fStandalone)\n
    '''
def isStandalone():
    '''returns boolean\n\n
    isStandalone()\n
    '''
def setEntityHandler():
    '''returns None\n\n
    setEntityHandler(final XMLEntityHandler fEntityHandler)\n
    '''
def getCurrentResourceIdentifier():
    '''returns XMLResourceIdentifier\n\n
    getCurrentResourceIdentifier()\n
    '''
def getCurrentEntity():
    '''returns ScannedEntity\n\n
    getCurrentEntity()\n
    '''
def addInternalEntity():
    '''returns None\n\n
    addInternalEntity(final String s, final String s2, final int n)\n
    addInternalEntity(final String s, final String s2)\n
    '''
def getParamEntityRefCount():
    '''returns int\n\n
    getParamEntityRefCount(final String key)\n
    '''
def addExternalEntity():
    '''returns None\n\n
    addExternalEntity(final String s, final String s2, final String s3, String s4)\n
    '''
def isExternalEntity():
    '''returns boolean\n\n
    isExternalEntity(final String key)\n
    '''
def isEntityDeclInExternalSubset():
    '''returns boolean\n\n
    isEntityDeclInExternalSubset(final String key)\n
    isEntityDeclInExternalSubset()\n
    '''
def addUnparsedEntity():
    '''returns None\n\n
    addUnparsedEntity(final String s, final String s2, final String s3, final String s4, final String s5)\n
    '''
def isUnparsedEntity():
    '''returns boolean\n\n
    isUnparsedEntity(final String key)\n
    '''
def isDeclaredEntity():
    '''returns boolean\n\n
    isDeclaredEntity(final String key)\n
    '''
def resolveEntity():
    '''returns XMLInputSource\n\n
    resolveEntity(final XMLResourceIdentifier xmlResourceIdentifier)\n
    '''
def startEntity():
    '''returns None\n\n
    startEntity(final String str, final boolean b)\n
    startEntity(final String s, final XMLInputSource xmlInputSource, final boolean b, final boolean b2)\n
    '''
def startDocumentEntity():
    '''returns None\n\n
    startDocumentEntity(final XMLInputSource xmlInputSource)\n
    '''
def startDTDEntity():
    '''returns None\n\n
    startDTDEntity(final XMLInputSource xmlInputSource)\n
    '''
def startExternalSubset():
    '''returns None\n\n
    startExternalSubset()\n
    '''
def endExternalSubset():
    '''returns None\n\n
    endExternalSubset()\n
    '''
def setupCurrentEntity():
    '''returns String\n\n
    setupCurrentEntity(final String s, final XMLInputSource xmlInputSource, final boolean b, final boolean b2)\n
    '''
def setScannerVersion():
    '''returns None\n\n
    setScannerVersion(final short n)\n
    '''
def getEntityScanner():
    '''returns XMLEntityScanner\n\n
    getEntityScanner()\n
    '''
def closeReaders():
    '''returns None\n\n
    closeReaders()\n
    '''
def reset():
    '''returns None\n\n
    reset(final XMLComponentManager xmlComponentManager)\n
    reset()\n
    reset()\n
    '''
def getRecognizedFeatures():
    '''returns String[]\n\n
    getRecognizedFeatures()\n
    '''
def setFeature():
    '''returns None\n\n
    setFeature(final String s, final boolean fAllowJavaEncodings)\n
    '''
def getRecognizedProperties():
    '''returns String[]\n\n
    getRecognizedProperties()\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final String s, final Object o)\n
    '''
def getFeatureDefault():
    '''returns Boolean\n\n
    getFeatureDefault(final String anObject)\n
    '''
def getPropertyDefault():
    '''returns Object\n\n
    getPropertyDefault(final String anObject)\n
    '''
def run():
    '''returns Object\n\n
    run()\n
    '''
def setStartOffset():
    '''returns None\n\n
    setStartOffset(final int fStartOffset)\n
    '''
def rewind():
    '''returns None\n\n
    rewind()\n
    '''
def readAndBuffer():
    '''returns int\n\n
    readAndBuffer()\n
    '''
def read():
    '''returns int\n\n
    read()\n
    read(final byte[] b, final int off, int len)\n
    '''
def skip():
    '''returns long\n\n
    skip(long n)\n
    '''
def available():
    '''returns int\n\n
    available()\n
    '''
def mark():
    '''returns None\n\n
    mark(final int n)\n
    '''
def markSupported():
    '''returns boolean\n\n
    markSupported()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def setReader():
    '''returns None\n\n
    setReader(final InputStream inputStream, final String s, final Boolean b)\n
    '''
def getExpandedSystemId():
    '''returns String\n\n
    getExpandedSystemId()\n
    '''
def getLiteralSystemId():
    '''returns String\n\n
    getLiteralSystemId()\n
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
def getEncoding():
    '''returns String\n\n
    getEncoding()\n
    '''
def getXMLVersion():
    '''returns String\n\n
    getXMLVersion()\n
    '''
def isEncodingExternallySpecified():
    '''returns boolean\n\n
    isEncodingExternallySpecified()\n
    '''
def setEncodingExternallySpecified():
    '''returns None\n\n
    setEncodingExternallySpecified(final boolean externallySpecifiedEncoding)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    clear()\n
    clear()\n
    '''
def setValues():
    '''returns None\n\n
    setValues(final Entity entity)\n
    setValues(final Entity values)\n
    setValues(final ExternalEntity values)\n
    setValues(final Entity values)\n
    setValues(final InternalEntity values)\n
    '''
def getBuffer():
    '''returns byte[]\n\n
    getBuffer(final boolean b)\n
    getBuffer()\n
    '''
def returnBuffer():
    '''returns None\n\n
    returnBuffer(final CharacterBuffer characterBuffer)\n
    returnBuffer(final byte[] array)\n
    '''
def setExternalBufferSize():
    '''returns None\n\n
    setExternalBufferSize(final int fExternalBufferSize)\n
    '''
def setBufferSize():
    '''returns None\n\n
    setBufferSize(final int fBufferSize)\n
    '''
