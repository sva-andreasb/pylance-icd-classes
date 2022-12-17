def ():
    '''returns BasicHttpResponse\n\n
    (final StatusLine statusline, final ReasonPhraseCatalog catalog, final Locale locale)\n
    (final StatusLine statusline)\n
    (final ProtocolVersion ver, final int code, final String reason)\n
    '''
def getProtocolVersion():
    '''returns ProtocolVersion\n\n
    getProtocolVersion()\n
    '''
def getStatusLine():
    '''returns StatusLine\n\n
    getStatusLine()\n
    '''
def getEntity():
    '''returns HttpEntity\n\n
    getEntity()\n
    '''
def getLocale():
    '''returns Locale\n\n
    getLocale()\n
    '''
def setStatusLine():
    '''returns None\n\n
    setStatusLine(final StatusLine statusline)\n
    setStatusLine(final ProtocolVersion ver, final int code)\n
    setStatusLine(final ProtocolVersion ver, final int code, final String reason)\n
    '''
def setStatusCode():
    '''returns None\n\n
    setStatusCode(final int code)\n
    '''
def setReasonPhrase():
    '''returns None\n\n
    setReasonPhrase(final String reason)\n
    '''
def setEntity():
    '''returns None\n\n
    setEntity(final HttpEntity entity)\n
    '''
def setLocale():
    '''returns None\n\n
    setLocale(final Locale locale)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
