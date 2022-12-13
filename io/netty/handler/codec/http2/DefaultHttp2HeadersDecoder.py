def DefaultHttp2HeadersDecoder():
    '''public DefaultHttp2HeadersDecoder()
    public DefaultHttp2HeadersDecoder(final boolean validateHeaders)
    public DefaultHttp2HeadersDecoder(final boolean validateHeaders, final long maxHeaderListSize)
    public DefaultHttp2HeadersDecoder(final boolean validateHeaders, final long maxHeaderListSize, @Deprecated final int initialHuffmanDecodeCapacity)
    '''
def maxHeaderTableSize():
    '''public void maxHeaderTableSize(final long max)
    public long maxHeaderTableSize()
    '''
def maxHeaderListSize():
    '''public void maxHeaderListSize(final long max, final long goAwayMax)
    public long maxHeaderListSize()
    '''
def maxHeaderListSizeGoAway():
    '''public long maxHeaderListSizeGoAway()
    '''
def configuration():
    '''public Configuration configuration()
    '''
def decodeHeaders():
    '''public Http2Headers decodeHeaders(final int streamId, final ByteBuf headerBlock)
    '''
