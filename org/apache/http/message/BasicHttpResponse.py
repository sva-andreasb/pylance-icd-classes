def BasicHttpResponse():
    '''public BasicHttpResponse(final StatusLine statusline, final ReasonPhraseCatalog catalog, final Locale locale)
    public BasicHttpResponse(final StatusLine statusline)
    public BasicHttpResponse(final ProtocolVersion ver, final int code, final String reason)
    '''
def getProtocolVersion():
    '''public ProtocolVersion getProtocolVersion()
    '''
def getStatusLine():
    '''public StatusLine getStatusLine()
    '''
def getEntity():
    '''public HttpEntity getEntity()
    '''
def getLocale():
    '''public Locale getLocale()
    '''
def setStatusLine():
    '''public void setStatusLine(final StatusLine statusline)
    public void setStatusLine(final ProtocolVersion ver, final int code)
    public void setStatusLine(final ProtocolVersion ver, final int code, final String reason)
    '''
def setStatusCode():
    '''public void setStatusCode(final int code)
    '''
def setReasonPhrase():
    '''public void setReasonPhrase(final String reason)
    '''
def setEntity():
    '''public void setEntity(final HttpEntity entity)
    '''
def setLocale():
    '''public void setLocale(final Locale locale)
    '''
def toString():
    '''public String toString()
    '''
