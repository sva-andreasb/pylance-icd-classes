UNKNOWN = "int  0"
PROTOCOL_CHARSET = "int  1"
DOCUMENT_CHARSET = "int  2"
def URI():
'''public URI(final String s, final boolean escaped, final String charset)
public URI(final String s, final boolean escaped)
public URI(final char[] escaped, final String charset)
public URI(final char[] escaped)
public URI(final String original, final String charset)
public URI(final String original)
public URI(final String scheme, final String schemeSpecificPart, final String fragment)
public URI(final String scheme, final String authority, final String path, final String query, final String fragment)
public URI(final String scheme, final String userinfo, final String host, final int port)
public URI(final String scheme, final String userinfo, final String host, final int port, final String path)
public URI(final String scheme, final String userinfo, final String host, final int port, final String path, final String query)
public URI(final String scheme, final String userinfo, final String host, final int port, final String path, final String query, final String fragment)
public URI(final String scheme, final String host, final String path, final String fragment)
public URI(final URI base, final String relative)
public URI(final URI base, final String relative, final boolean escaped)
public URI(final URI base, final URI relative)
'''
pass
def isAbsoluteURI():
'''public boolean isAbsoluteURI()
'''
pass
def isRelativeURI():
'''public boolean isRelativeURI()
'''
pass
def isHierPart():
'''public boolean isHierPart()
'''
pass
def isOpaquePart():
'''public boolean isOpaquePart()
'''
pass
def isNetPath():
'''public boolean isNetPath()
'''
pass
def isAbsPath():
'''public boolean isAbsPath()
'''
pass
def isRelPath():
'''public boolean isRelPath()
'''
pass
def hasAuthority():
'''public boolean hasAuthority()
'''
pass
def isRegName():
'''public boolean isRegName()
'''
pass
def isServer():
'''public boolean isServer()
'''
pass
def hasUserinfo():
'''public boolean hasUserinfo()
'''
pass
def isHostname():
'''public boolean isHostname()
'''
pass
def isIPv4address():
'''public boolean isIPv4address()
'''
pass
def isIPv6reference():
'''public boolean isIPv6reference()
'''
pass
def hasQuery():
'''public boolean hasQuery()
'''
pass
def hasFragment():
'''public boolean hasFragment()
'''
pass
def setDefaultProtocolCharset():
'''public static void setDefaultProtocolCharset(final String charset)
'''
pass
def getDefaultProtocolCharset():
'''public static String getDefaultProtocolCharset()
'''
pass
def getProtocolCharset():
'''public String getProtocolCharset()
'''
pass
def setDefaultDocumentCharset():
'''public static void setDefaultDocumentCharset(final String charset)
'''
pass
def getDefaultDocumentCharset():
'''public static String getDefaultDocumentCharset()
'''
pass
def getDefaultDocumentCharsetByLocale():
'''public static String getDefaultDocumentCharsetByLocale()
'''
pass
def getDefaultDocumentCharsetByPlatform():
'''public static String getDefaultDocumentCharsetByPlatform()
'''
pass
def getRawScheme():
'''public char[] getRawScheme()
'''
pass
def getScheme():
'''public String getScheme()
'''
pass
def setRawAuthority():
'''public void setRawAuthority(final char[] escapedAuthority)
'''
pass
def setEscapedAuthority():
'''public void setEscapedAuthority(final String escapedAuthority)
'''
pass
def getRawAuthority():
'''public char[] getRawAuthority()
'''
pass
def getEscapedAuthority():
'''public String getEscapedAuthority()
'''
pass
def getAuthority():
'''public String getAuthority()
'''
pass
def getRawUserinfo():
'''public char[] getRawUserinfo()
'''
pass
def getEscapedUserinfo():
'''public String getEscapedUserinfo()
'''
pass
def getUserinfo():
'''public String getUserinfo()
'''
pass
def getRawHost():
'''public char[] getRawHost()
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
def setRawPath():
'''public void setRawPath(char[] escapedPath)
'''
pass
def setEscapedPath():
'''public void setEscapedPath(final String escapedPath)
'''
pass
def setPath():
'''public void setPath(final String path)
'''
pass
def getRawCurrentHierPath():
'''public char[] getRawCurrentHierPath()
'''
pass
def getEscapedCurrentHierPath():
'''public String getEscapedCurrentHierPath()
'''
pass
def getCurrentHierPath():
'''public String getCurrentHierPath()
'''
pass
def getRawAboveHierPath():
'''public char[] getRawAboveHierPath()
'''
pass
def getEscapedAboveHierPath():
'''public String getEscapedAboveHierPath()
'''
pass
def getAboveHierPath():
'''public String getAboveHierPath()
'''
pass
def getRawPath():
'''public char[] getRawPath()
'''
pass
def getEscapedPath():
'''public String getEscapedPath()
'''
pass
def getPath():
'''public String getPath()
'''
pass
def getRawName():
'''public char[] getRawName()
'''
pass
def getEscapedName():
'''public String getEscapedName()
'''
pass
def getName():
'''public String getName()
'''
pass
def getRawPathQuery():
'''public char[] getRawPathQuery()
'''
pass
def getEscapedPathQuery():
'''public String getEscapedPathQuery()
'''
pass
def getPathQuery():
'''public String getPathQuery()
'''
pass
def setRawQuery():
'''public void setRawQuery(char[] escapedQuery)
'''
pass
def setEscapedQuery():
'''public void setEscapedQuery(final String escapedQuery)
'''
pass
def setQuery():
'''public void setQuery(final String query)
'''
pass
def getRawQuery():
'''public char[] getRawQuery()
'''
pass
def getEscapedQuery():
'''public String getEscapedQuery()
'''
pass
def getQuery():
'''public String getQuery()
'''
pass
def setRawFragment():
'''public void setRawFragment(final char[] escapedFragment)
'''
pass
def setEscapedFragment():
'''public void setEscapedFragment(final String escapedFragment)
'''
pass
def setFragment():
'''public void setFragment(final String fragment)
'''
pass
def getRawFragment():
'''public char[] getRawFragment()
'''
pass
def getEscapedFragment():
'''public String getEscapedFragment()
'''
pass
def getFragment():
'''public String getFragment()
'''
pass
def normalize():
'''public void normalize()
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
def compareTo():
'''public int compareTo(final Object obj)
'''
pass
def clone():
'''public synchronized Object clone()
'''
pass
def getRawURI():
'''public char[] getRawURI()
'''
pass
def getEscapedURI():
'''public String getEscapedURI()
'''
pass
def getURI():
'''public String getURI()
'''
pass
def getRawURIReference():
'''public char[] getRawURIReference()
'''
pass
def getEscapedURIReference():
'''public String getEscapedURIReference()
'''
pass
def getURIReference():
'''public String getURIReference()
'''
pass
def toString():
'''public String toString()
'''
pass
def DefaultCharsetChanged():
'''public DefaultCharsetChanged(final int reasonCode, final String reason)
'''
pass
def getReasonCode():
'''public int getReasonCode()
'''
pass
def getReason():
'''public String getReason()
'''
pass
def getCharset():
'''public static String getCharset(final Locale locale)
'''
pass
