def GenericUrl():
    '''public GenericUrl()
    public GenericUrl(final String encodedUrl)
    public GenericUrl(final URI uri)
    public GenericUrl(final URL url)
    '''
def hashCode():
    '''public int hashCode()
    '''
def equals():
    '''public boolean equals(final Object obj)
    '''
def toString():
    '''public String toString()
    '''
def clone():
    '''public GenericUrl clone()
    '''
def set():
    '''public GenericUrl set(final String fieldName, final Object value)
    '''
def getScheme():
    '''public final String getScheme()
    '''
def setScheme():
    '''public final void setScheme(final String scheme)
    '''
def getHost():
    '''public String getHost()
    '''
def setHost():
    '''public final void setHost(final String host)
    '''
def getUserInfo():
    '''public final String getUserInfo()
    '''
def setUserInfo():
    '''public final void setUserInfo(final String userInfo)
    '''
def getPort():
    '''public int getPort()
    '''
def setPort():
    '''public final void setPort(final int port)
    '''
def getPathParts():
    '''public List<String> getPathParts()
    '''
def setPathParts():
    '''public void setPathParts(final List<String> pathParts)
    '''
def getFragment():
    '''public String getFragment()
    '''
def setFragment():
    '''public final void setFragment(final String fragment)
    '''
def build():
    '''public final String build()
    '''
def buildAuthority():
    '''public final String buildAuthority()
    '''
def buildRelativeUrl():
    '''public final String buildRelativeUrl()
    '''
def toURI():
    '''public final URI toURI()
    '''
def toURL():
    '''public final URL toURL()
    public final URL toURL(final String relativeUrl)
    '''
def getFirst():
    '''public Object getFirst(final String name)
    '''
def getAll():
    '''public Collection<Object> getAll(final String name)
    '''
def getRawPath():
    '''public String getRawPath()
    '''
def setRawPath():
    '''public void setRawPath(final String encodedPath)
    '''
def appendRawPath():
    '''public void appendRawPath(final String encodedPath)
    '''
def toPathParts():
    '''public static List<String> toPathParts(final String encodedPath)
    '''
