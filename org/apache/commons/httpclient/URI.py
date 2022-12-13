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
def isAbsoluteURI():
    '''public boolean isAbsoluteURI()
    '''
def isRelativeURI():
    '''public boolean isRelativeURI()
    '''
def isHierPart():
    '''public boolean isHierPart()
    '''
def isOpaquePart():
    '''public boolean isOpaquePart()
    '''
def isNetPath():
    '''public boolean isNetPath()
    '''
def isAbsPath():
    '''public boolean isAbsPath()
    '''
def isRelPath():
    '''public boolean isRelPath()
    '''
def hasAuthority():
    '''public boolean hasAuthority()
    '''
def isRegName():
    '''public boolean isRegName()
    '''
def isServer():
    '''public boolean isServer()
    '''
def hasUserinfo():
    '''public boolean hasUserinfo()
    '''
def isHostname():
    '''public boolean isHostname()
    '''
def isIPv4address():
    '''public boolean isIPv4address()
    '''
def isIPv6reference():
    '''public boolean isIPv6reference()
    '''
def hasQuery():
    '''public boolean hasQuery()
    '''
def hasFragment():
    '''public boolean hasFragment()
    '''
def setDefaultProtocolCharset():
    '''public static void setDefaultProtocolCharset(final String charset)
    '''
def getDefaultProtocolCharset():
    '''public static String getDefaultProtocolCharset()
    '''
def getProtocolCharset():
    '''public String getProtocolCharset()
    '''
def setDefaultDocumentCharset():
    '''public static void setDefaultDocumentCharset(final String charset)
    '''
def getDefaultDocumentCharset():
    '''public static String getDefaultDocumentCharset()
    '''
def getDefaultDocumentCharsetByLocale():
    '''public static String getDefaultDocumentCharsetByLocale()
    '''
def getDefaultDocumentCharsetByPlatform():
    '''public static String getDefaultDocumentCharsetByPlatform()
    '''
def getRawScheme():
    '''public char[] getRawScheme()
    '''
def getScheme():
    '''public String getScheme()
    '''
def setRawAuthority():
    '''public void setRawAuthority(final char[] escapedAuthority)
    '''
def setEscapedAuthority():
    '''public void setEscapedAuthority(final String escapedAuthority)
    '''
def getRawAuthority():
    '''public char[] getRawAuthority()
    '''
def getEscapedAuthority():
    '''public String getEscapedAuthority()
    '''
def getAuthority():
    '''public String getAuthority()
    '''
def getRawUserinfo():
    '''public char[] getRawUserinfo()
    '''
def getEscapedUserinfo():
    '''public String getEscapedUserinfo()
    '''
def getUserinfo():
    '''public String getUserinfo()
    '''
def getRawHost():
    '''public char[] getRawHost()
    '''
def getHost():
    '''public String getHost()
    '''
def getPort():
    '''public int getPort()
    '''
def setRawPath():
    '''public void setRawPath(char[] escapedPath)
    '''
def setEscapedPath():
    '''public void setEscapedPath(final String escapedPath)
    '''
def setPath():
    '''public void setPath(final String path)
    '''
def getRawCurrentHierPath():
    '''public char[] getRawCurrentHierPath()
    '''
def getEscapedCurrentHierPath():
    '''public String getEscapedCurrentHierPath()
    '''
def getCurrentHierPath():
    '''public String getCurrentHierPath()
    '''
def getRawAboveHierPath():
    '''public char[] getRawAboveHierPath()
    '''
def getEscapedAboveHierPath():
    '''public String getEscapedAboveHierPath()
    '''
def getAboveHierPath():
    '''public String getAboveHierPath()
    '''
def getRawPath():
    '''public char[] getRawPath()
    '''
def getEscapedPath():
    '''public String getEscapedPath()
    '''
def getPath():
    '''public String getPath()
    '''
def getRawName():
    '''public char[] getRawName()
    '''
def getEscapedName():
    '''public String getEscapedName()
    '''
def getName():
    '''public String getName()
    '''
def getRawPathQuery():
    '''public char[] getRawPathQuery()
    '''
def getEscapedPathQuery():
    '''public String getEscapedPathQuery()
    '''
def getPathQuery():
    '''public String getPathQuery()
    '''
def setRawQuery():
    '''public void setRawQuery(char[] escapedQuery)
    '''
def setEscapedQuery():
    '''public void setEscapedQuery(final String escapedQuery)
    '''
def setQuery():
    '''public void setQuery(final String query)
    '''
def getRawQuery():
    '''public char[] getRawQuery()
    '''
def getEscapedQuery():
    '''public String getEscapedQuery()
    '''
def getQuery():
    '''public String getQuery()
    '''
def setRawFragment():
    '''public void setRawFragment(final char[] escapedFragment)
    '''
def setEscapedFragment():
    '''public void setEscapedFragment(final String escapedFragment)
    '''
def setFragment():
    '''public void setFragment(final String fragment)
    '''
def getRawFragment():
    '''public char[] getRawFragment()
    '''
def getEscapedFragment():
    '''public String getEscapedFragment()
    '''
def getFragment():
    '''public String getFragment()
    '''
def normalize():
    '''public void normalize()
    '''
def equals():
    '''public boolean equals(final Object obj)
    '''
def hashCode():
    '''public int hashCode()
    '''
def compareTo():
    '''public int compareTo(final Object obj)
    '''
def clone():
    '''public synchronized Object clone()
    '''
def getRawURI():
    '''public char[] getRawURI()
    '''
def getEscapedURI():
    '''public String getEscapedURI()
    '''
def getURI():
    '''public String getURI()
    '''
def getRawURIReference():
    '''public char[] getRawURIReference()
    '''
def getEscapedURIReference():
    '''public String getEscapedURIReference()
    '''
def getURIReference():
    '''public String getURIReference()
    '''
def toString():
    '''public String toString()
    '''
def DefaultCharsetChanged():
    '''public DefaultCharsetChanged(final int reasonCode, final String reason)
    '''
def getReasonCode():
    '''public int getReasonCode()
    '''
def getReason():
    '''public String getReason()
    '''
def getCharset():
    '''public static String getCharset(final Locale locale)
    '''
