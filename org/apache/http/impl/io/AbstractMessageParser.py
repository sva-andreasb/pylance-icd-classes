def AbstractMessageParser():
'''public AbstractMessageParser(final SessionInputBuffer buffer, final LineParser parser, final HttpParams params)
public AbstractMessageParser(final SessionInputBuffer buffer, final LineParser lineParser, final MessageConstraints constraints)
'''
pass
def parseHeaders():
'''public static Header[] parseHeaders(final SessionInputBuffer inbuffer, final int maxHeaderCount, final int maxLineLen, final LineParser parser)
public static Header[] parseHeaders(final SessionInputBuffer inbuffer, final int maxHeaderCount, final int maxLineLen, final LineParser parser, final List<CharArrayBuffer> headerLines)
'''
pass
def parse():
'''public T parse()
'''
pass
