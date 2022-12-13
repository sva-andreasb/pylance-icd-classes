def HttpURI():
'''public HttpURI()
public HttpURI(final boolean parsePartialAuth)
public HttpURI(final String raw)
public HttpURI(final byte[] raw, final int offset, final int length)
public HttpURI(final URI uri)
'''
pass
def parse():
'''public void parse(final String raw)
public void parse(final byte[] raw, final int offset, final int length)
'''
pass
def parseConnect():
'''public void parseConnect(final byte[] raw, final int offset, final int length)
'''
pass
def getScheme():
'''public String getScheme()
'''
pass
def getAuthority():
'''public String getAuthority()
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
def getDecodedPath():
'''public String getDecodedPath()
'''
pass
def getPathAndParam():
'''public String getPathAndParam()
'''
pass
def getCompletePath():
'''public String getCompletePath()
'''
pass
def getParam():
'''public String getParam()
'''
pass
def getQuery():
'''public String getQuery()
public String getQuery(final String encoding)
'''
pass
def hasQuery():
'''public boolean hasQuery()
'''
pass
def getFragment():
'''public String getFragment()
'''
pass
def decodeQueryTo():
'''public void decodeQueryTo(final MultiMap parameters)
public void decodeQueryTo(final MultiMap parameters, final String encoding)
'''
pass
def clear():
'''public void clear()
'''
pass
def toString():
'''public String toString()
'''
pass
def writeTo():
'''public void writeTo(final Utf8StringBuilder buf)
'''
pass
