def getGlobalUserAgent():
    '''public static String getGlobalUserAgent()
    '''
def setGlobalUserAgent():
    '''public static void setGlobalUserAgent(final String userAgent)
    '''
def getHandler():
    '''public static synchronized ParsedURLProtocolHandler getHandler(final String protocol)
    '''
def registerHandler():
    '''public static synchronized void registerHandler(final ParsedURLProtocolHandler handler)
    '''
def checkGZIP():
    '''public static InputStream checkGZIP(final InputStream is)
    '''
def ParsedURL():
    '''public ParsedURL(final String urlStr)
    public ParsedURL(final URL url)
    public ParsedURL(final String baseStr, final String urlStr)
    public ParsedURL(final URL baseURL, final String urlStr)
    public ParsedURL(final ParsedURL baseURL, final String urlStr)
    '''
def toString():
    '''public String toString()
    '''
def getPostConnectionURL():
    '''public String getPostConnectionURL()
    '''
def equals():
    '''public boolean equals(final Object obj)
    '''
def hashCode():
    '''public int hashCode()
    '''
def complete():
    '''public boolean complete()
    '''
def getUserAgent():
    '''public String getUserAgent()
    '''
def setUserAgent():
    '''public void setUserAgent(final String userAgent)
    '''
def getProtocol():
    '''public String getProtocol()
    '''
def getHost():
    '''public String getHost()
    '''
def getPort():
    '''public int getPort()
    '''
def getPath():
    '''public String getPath()
    '''
def getRef():
    '''public String getRef()
    '''
def getPortStr():
    '''public String getPortStr()
    '''
def getContentType():
    '''public String getContentType()
    '''
def getContentTypeMediaType():
    '''public String getContentTypeMediaType()
    '''
def getContentTypeCharset():
    '''public String getContentTypeCharset()
    '''
def hasContentTypeParameter():
    '''public boolean hasContentTypeParameter(final String param)
    '''
def getContentEncoding():
    '''public String getContentEncoding()
    '''
def openStream():
    '''public InputStream openStream()
    public InputStream openStream(final String mimeType)
    public InputStream openStream(final String[] mimeTypes)
    public InputStream openStream(final Iterator mimeTypes)
    '''
def openStreamRaw():
    '''public InputStream openStreamRaw()
    public InputStream openStreamRaw(final String mimeType)
    public InputStream openStreamRaw(final String[] mimeTypes)
    public InputStream openStreamRaw(final Iterator mimeTypes)
    '''
def sameFile():
    '''public boolean sameFile(final ParsedURL other)
    '''
def parseURL():
    '''public static ParsedURLData parseURL(String urlStr)
    public static ParsedURLData parseURL(final String baseStr, final String urlStr)
    public static ParsedURLData parseURL(final ParsedURL baseURL, final String urlStr)
    '''
