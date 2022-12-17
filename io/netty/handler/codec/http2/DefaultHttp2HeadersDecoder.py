def ():
    '''returns DefaultHttp2HeadersDecoder\n\n
    ()\n
    (final boolean validateHeaders)\n
    (final boolean validateHeaders, final long maxHeaderListSize)\n
    (final boolean validateHeaders, final long maxHeaderListSize, @Deprecated final int initialHuffmanDecodeCapacity)\n
    '''
def maxHeaderTableSize():
    '''returns long\n\n
    maxHeaderTableSize(final long max)\n
    maxHeaderTableSize()\n
    '''
def maxHeaderListSize():
    '''returns long\n\n
    maxHeaderListSize(final long max, final long goAwayMax)\n
    maxHeaderListSize()\n
    '''
def maxHeaderListSizeGoAway():
    '''returns long\n\n
    maxHeaderListSizeGoAway()\n
    '''
def configuration():
    '''returns Configuration\n\n
    configuration()\n
    '''
def decodeHeaders():
    '''returns Http2Headers\n\n
    decodeHeaders(final int streamId, final ByteBuf headerBlock)\n
    '''
