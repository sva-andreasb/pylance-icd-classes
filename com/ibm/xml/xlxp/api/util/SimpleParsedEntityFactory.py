REQUIRE_IANA_ENCODING_NAMES = "boolean  false"
def ():
    '''returns SimpleParsedEntityFactory\n\n
    (final DataBufferFactory fBufferFactory)\n
    '''
def setBufferLength():
    '''returns None\n\n
    setBufferLength(final int bufferLength)\n
    '''
def reset():
    '''returns None\n\n
    reset(final boolean b)\n
    '''
def createParsedEntity():
    '''returns ParsedEntity\n\n
    createParsedEntity(final InputStream inputStream, final String s)\n
    '''
def createParsedEntityFromXMLString():
    '''returns ParsedEntity\n\n
    createParsedEntityFromXMLString(final XMLString content, final String baseURI)\n
    '''
def releaseParsedEntity():
    '''returns None\n\n
    releaseParsedEntity(final ParsedEntity parsedEntity)\n
    '''
def releaseRewindableInputStream():
    '''returns None\n\n
    releaseRewindableInputStream(final RewindableInputStream rewindableInputStream)\n
    '''
