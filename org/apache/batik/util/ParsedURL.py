def getGlobalUserAgent():
'''public static String getGlobalUserAgent()
'''
pass
def setGlobalUserAgent():
'''public static void setGlobalUserAgent(final String userAgent)
'''
pass
def getHandler():
'''public static synchronized ParsedURLProtocolHandler getHandler(final String protocol)
'''
pass
def registerHandler():
'''public static synchronized void registerHandler(final ParsedURLProtocolHandler handler)
'''
pass
def checkGZIP():
'''public static InputStream checkGZIP(final InputStream is)
'''
pass
def ParsedURL():
'''public ParsedURL(final String urlStr)
public ParsedURL(final URL url)
public ParsedURL(final String baseStr, final String urlStr)
public ParsedURL(final URL baseURL, final String urlStr)
public ParsedURL(final ParsedURL baseURL, final String urlStr)
'''
pass
def toString():
'''public String toString()
'''
pass
def getPostConnectionURL():
'''public String getPostConnectionURL()
'''
pass
def equals():
'''public boolean equals(final Object obj)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def complete():
'''public boolean complete()
'''
pass
def getUserAgent():
'''public String getUserAgent()
'''
pass
def setUserAgent():
'''public void setUserAgent(final String userAgent)
'''
pass
def getProtocol():
'''public String getProtocol()
'''
pass
def getHost():
'''public String getHost()
'''
pass
def getPort():
'''public int getPort()
'''
pass
def getPath():
'''public String getPath()
'''
pass
def getRef():
'''public String getRef()
'''
pass
def getPortStr():
'''public String getPortStr()
'''
pass
def getContentType():
'''public String getContentType()
'''
pass
def getContentTypeMediaType():
'''public String getContentTypeMediaType()
'''
pass
def getContentTypeCharset():
'''public String getContentTypeCharset()
'''
pass
def hasContentTypeParameter():
'''public boolean hasContentTypeParameter(final String param)
'''
pass
def getContentEncoding():
'''public String getContentEncoding()
'''
pass
def openStream():
'''public InputStream openStream()
public InputStream openStream(final String mimeType)
public InputStream openStream(final String[] mimeTypes)
public InputStream openStream(final Iterator mimeTypes)
'''
pass
def openStreamRaw():
'''public InputStream openStreamRaw()
public InputStream openStreamRaw(final String mimeType)
public InputStream openStreamRaw(final String[] mimeTypes)
public InputStream openStreamRaw(final Iterator mimeTypes)
'''
pass
def sameFile():
'''public boolean sameFile(final ParsedURL other)
'''
pass
def parseURL():
'''public static ParsedURLData parseURL(String urlStr)
public static ParsedURLData parseURL(final String baseStr, final String urlStr)
public static ParsedURLData parseURL(final ParsedURL baseURL, final String urlStr)
'''
pass
