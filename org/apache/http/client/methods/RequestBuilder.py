def setCharset():
    '''returns RequestBuilder\n\n
    setCharset(final Charset charset)\n
    '''
def getCharset():
    '''returns Charset\n\n
    getCharset()\n
    '''
def getMethod():
    '''returns String\n\n
    getMethod()\n
    getMethod()\n
    getMethod()\n
    '''
def getVersion():
    '''returns ProtocolVersion\n\n
    getVersion()\n
    '''
def setVersion():
    '''returns RequestBuilder\n\n
    setVersion(final ProtocolVersion version)\n
    '''
def getUri():
    '''returns URI\n\n
    getUri()\n
    '''
def setUri():
    '''returns RequestBuilder\n\n
    setUri(final URI uri)\n
    setUri(final String uri)\n
    '''
def getFirstHeader():
    '''returns Header\n\n
    getFirstHeader(final String name)\n
    '''
def getLastHeader():
    '''returns Header\n\n
    getLastHeader(final String name)\n
    '''
def getHeaders():
    '''returns Header[]\n\n
    getHeaders(final String name)\n
    '''
def addHeader():
    '''returns RequestBuilder\n\n
    addHeader(final Header header)\n
    addHeader(final String name, final String value)\n
    '''
def removeHeader():
    '''returns RequestBuilder\n\n
    removeHeader(final Header header)\n
    '''
def removeHeaders():
    '''returns RequestBuilder\n\n
    removeHeaders(final String name)\n
    '''
def setHeader():
    '''returns RequestBuilder\n\n
    setHeader(final Header header)\n
    setHeader(final String name, final String value)\n
    '''
def getEntity():
    '''returns HttpEntity\n\n
    getEntity()\n
    '''
def setEntity():
    '''returns RequestBuilder\n\n
    setEntity(final HttpEntity entity)\n
    '''
def getParameters():
    '''returns List<NameValuePair>\n\n
    getParameters()\n
    '''
def addParameter():
    '''returns RequestBuilder\n\n
    addParameter(final NameValuePair nvp)\n
    addParameter(final String name, final String value)\n
    '''
def addParameters():
    '''returns RequestBuilder\n\n
    addParameters(final NameValuePair... nvps)\n
    '''
def getConfig():
    '''returns RequestConfig\n\n
    getConfig()\n
    '''
def setConfig():
    '''returns RequestBuilder\n\n
    setConfig(final RequestConfig config)\n
    '''
def build():
    '''returns HttpUriRequest\n\n
    build()\n
    '''
