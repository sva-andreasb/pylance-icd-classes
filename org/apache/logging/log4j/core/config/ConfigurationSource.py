def ():
    '''returns ConfigurationSource\n\n
    (final InputStream stream, final File file)\n
    (final InputStream stream, final URL url)\n
    (final InputStream stream, final URL url, final long lastModified)\n
    (final InputStream stream)\n
    (final Source source, final byte[] data, final long lastModified)\n
    '''
def getFile():
    '''returns File\n\n
    getFile()\n
    '''
def getURL():
    '''returns URL\n\n
    getURL()\n
    '''
def setSource():
    '''returns None\n\n
    setSource(final Source source)\n
    '''
def setData():
    '''returns None\n\n
    setData(final byte[] data)\n
    '''
def setModifiedMillis():
    '''returns None\n\n
    setModifiedMillis(final long modifiedMillis)\n
    '''
def getURI():
    '''returns URI\n\n
    getURI()\n
    '''
def getLastModified():
    '''returns long\n\n
    getLastModified()\n
    '''
def getLocation():
    '''returns String\n\n
    getLocation()\n
    '''
def getInputStream():
    '''returns InputStream\n\n
    getInputStream()\n
    '''
def resetInputStream():
    '''returns ConfigurationSource\n\n
    resetInputStream()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
