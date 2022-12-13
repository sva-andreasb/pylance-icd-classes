def BasicLineParser():
'''public BasicLineParser(final ProtocolVersion proto)
public BasicLineParser()
'''
pass
def parseProtocolVersion():
'''public static ProtocolVersion parseProtocolVersion(final String value, final LineParser parser)
public ProtocolVersion parseProtocolVersion(final CharArrayBuffer buffer, final ParserCursor cursor)
'''
pass
def hasProtocolVersion():
'''public boolean hasProtocolVersion(final CharArrayBuffer buffer, final ParserCursor cursor)
'''
pass
def parseRequestLine():
'''public static RequestLine parseRequestLine(final String value, final LineParser parser)
public RequestLine parseRequestLine(final CharArrayBuffer buffer, final ParserCursor cursor)
'''
pass
def parseStatusLine():
'''public static StatusLine parseStatusLine(final String value, final LineParser parser)
public StatusLine parseStatusLine(final CharArrayBuffer buffer, final ParserCursor cursor)
'''
pass
def parseHeader():
'''public static Header parseHeader(final String value, final LineParser parser)
public Header parseHeader(final CharArrayBuffer buffer)
'''
pass
