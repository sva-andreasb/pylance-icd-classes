def HttpURI():
    '''public HttpURI()
    public HttpURI(final boolean parsePartialAuth)
    public HttpURI(final String raw)
    public HttpURI(final byte[] raw, final int offset, final int length)
    public HttpURI(final URI uri)
    '''
def parse():
    '''public void parse(final String raw)
    public void parse(final byte[] raw, final int offset, final int length)
    '''
def parseConnect():
    '''public void parseConnect(final byte[] raw, final int offset, final int length)
    '''
def getScheme():
    '''public String getScheme()
    '''
def getAuthority():
    '''public String getAuthority()
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
def getDecodedPath():
    '''public String getDecodedPath()
    '''
def getPathAndParam():
    '''public String getPathAndParam()
    '''
def getCompletePath():
    '''public String getCompletePath()
    '''
def getParam():
    '''public String getParam()
    '''
def getQuery():
    '''public String getQuery()
    public String getQuery(final String encoding)
    '''
def hasQuery():
    '''public boolean hasQuery()
    '''
def getFragment():
    '''public String getFragment()
    '''
def decodeQueryTo():
    '''public void decodeQueryTo(final MultiMap parameters)
    public void decodeQueryTo(final MultiMap parameters, final String encoding)
    '''
def clear():
    '''public void clear()
    '''
def toString():
    '''public String toString()
    '''
def writeTo():
    '''public void writeTo(final Utf8StringBuilder buf)
    '''
