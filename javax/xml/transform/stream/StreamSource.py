FEATURE = "String  \"http://javax.xml.transform.stream.StreamSource/feature\""
def ():
    '''returns StreamSource\n\n
    ()\n
    (final InputStream inputStream)\n
    (final InputStream inputStream, final String systemId)\n
    (final Reader reader)\n
    (final Reader reader, final String systemId)\n
    (final String systemId)\n
    (final File systemId)\n
    '''
def setInputStream():
    '''returns None\n\n
    setInputStream(final InputStream inputStream)\n
    '''
def getInputStream():
    '''returns InputStream\n\n
    getInputStream()\n
    '''
def setReader():
    '''returns None\n\n
    setReader(final Reader reader)\n
    '''
def getReader():
    '''returns Reader\n\n
    getReader()\n
    '''
def setPublicId():
    '''returns None\n\n
    setPublicId(final String publicId)\n
    '''
def getPublicId():
    '''returns String\n\n
    getPublicId()\n
    '''
def setSystemId():
    '''returns None\n\n
    setSystemId(final String systemId)\n
    setSystemId(final File file)\n
    '''
def getSystemId():
    '''returns String\n\n
    getSystemId()\n
    '''
