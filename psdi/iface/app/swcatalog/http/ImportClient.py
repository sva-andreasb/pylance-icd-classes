def ():
    '''returns ImportClient\n\n
    (final String urlSpec)\n
    (final String host, final int port)\n
    '''
def getURLEncodedString():
    '''returns String\n\n
    getURLEncodedString(final Map<String, String> requestProps)\n
    '''
def getGUID():
    '''returns String\n\n
    getGUID()\n
    '''
def getStatus():
    '''returns String\n\n
    getStatus(final String guid)\n
    '''
def logProperties():
    '''returns None\n\n
    logProperties(final Properties props)\n
    '''
def pollStatus():
    '''returns None\n\n
    pollStatus(final String guid, final int seconds, final int timeout)\n
    '''
def getCanonical():
    '''returns None\n\n
    getCanonical(final String filename, final String sourceDir)\n
    '''
def send():
    '''returns InputStream\n\n
    send(final String url)\n
    send(final String url2, final String url1)\n
    '''
def getBaseUrl():
    '''returns String\n\n
    getBaseUrl()\n
    '''
def verify():
    '''returns boolean\n\n
    verify(final String arg0, final SSLSession arg1)\n
    '''
