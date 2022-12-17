def ():
    '''returns SpdyFrameEncoder\n\n
    (final SpdyVersion spdyVersion)\n
    '''
def encodeDataFrame():
    '''returns ByteBuf\n\n
    encodeDataFrame(final ByteBufAllocator allocator, final int streamId, final boolean last, final ByteBuf data)\n
    '''
def encodeSynStreamFrame():
    '''returns ByteBuf\n\n
    encodeSynStreamFrame(final ByteBufAllocator allocator, final int streamId, final int associatedToStreamId, final byte priority, final boolean last, final boolean unidirectional, final ByteBuf headerBlock)\n
    '''
def encodeSynReplyFrame():
    '''returns ByteBuf\n\n
    encodeSynReplyFrame(final ByteBufAllocator allocator, final int streamId, final boolean last, final ByteBuf headerBlock)\n
    '''
def encodeRstStreamFrame():
    '''returns ByteBuf\n\n
    encodeRstStreamFrame(final ByteBufAllocator allocator, final int streamId, final int statusCode)\n
    '''
def encodeSettingsFrame():
    '''returns ByteBuf\n\n
    encodeSettingsFrame(final ByteBufAllocator allocator, final SpdySettingsFrame spdySettingsFrame)\n
    '''
def encodePingFrame():
    '''returns ByteBuf\n\n
    encodePingFrame(final ByteBufAllocator allocator, final int id)\n
    '''
def encodeGoAwayFrame():
    '''returns ByteBuf\n\n
    encodeGoAwayFrame(final ByteBufAllocator allocator, final int lastGoodStreamId, final int statusCode)\n
    '''
def encodeHeadersFrame():
    '''returns ByteBuf\n\n
    encodeHeadersFrame(final ByteBufAllocator allocator, final int streamId, final boolean last, final ByteBuf headerBlock)\n
    '''
def encodeWindowUpdateFrame():
    '''returns ByteBuf\n\n
    encodeWindowUpdateFrame(final ByteBufAllocator allocator, final int streamId, final int deltaWindowSize)\n
    '''
