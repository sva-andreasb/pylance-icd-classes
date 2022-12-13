def BasicHttpResponse():
'''public BasicHttpResponse(final StatusLine statusline, final ReasonPhraseCatalog catalog, final Locale locale)
public BasicHttpResponse(final StatusLine statusline)
public BasicHttpResponse(final ProtocolVersion ver, final int code, final String reason)
'''
pass
def getProtocolVersion():
'''public ProtocolVersion getProtocolVersion()
'''
pass
def getStatusLine():
'''public StatusLine getStatusLine()
'''
pass
def getEntity():
'''public HttpEntity getEntity()
'''
pass
def getLocale():
'''public Locale getLocale()
'''
pass
def setStatusLine():
'''public void setStatusLine(final StatusLine statusline)
public void setStatusLine(final ProtocolVersion ver, final int code)
public void setStatusLine(final ProtocolVersion ver, final int code, final String reason)
'''
pass
def setStatusCode():
'''public void setStatusCode(final int code)
'''
pass
def setReasonPhrase():
'''public void setReasonPhrase(final String reason)
'''
pass
def setEntity():
'''public void setEntity(final HttpEntity entity)
'''
pass
def setLocale():
'''public void setLocale(final Locale locale)
'''
pass
def toString():
'''public String toString()
'''
pass
