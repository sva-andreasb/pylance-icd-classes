def BasicLineParser():
    '''    public BasicLineParser(final ProtocolVersion proto)
    public BasicLineParser()
    '''
def parseProtocolVersion():
    '''    public static ProtocolVersion parseProtocolVersion(final String value, final LineParser parser)
    public ProtocolVersion parseProtocolVersion(final CharArrayBuffer buffer, final ParserCursor cursor)
    '''
def hasProtocolVersion():
    '''    public boolean hasProtocolVersion(final CharArrayBuffer buffer, final ParserCursor cursor)
    '''
def parseRequestLine():
    '''    public static RequestLine parseRequestLine(final String value, final LineParser parser)
    public RequestLine parseRequestLine(final CharArrayBuffer buffer, final ParserCursor cursor)
    '''
def parseStatusLine():
    '''    public static StatusLine parseStatusLine(final String value, final LineParser parser)
    public StatusLine parseStatusLine(final CharArrayBuffer buffer, final ParserCursor cursor)
    '''
def parseHeader():
    '''    public static Header parseHeader(final String value, final LineParser parser)
    public Header parseHeader(final CharArrayBuffer buffer)
    '''
