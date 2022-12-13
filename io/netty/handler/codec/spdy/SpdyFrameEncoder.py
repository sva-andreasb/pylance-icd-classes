def SpdyFrameEncoder():
    '''public SpdyFrameEncoder(final SpdyVersion spdyVersion)
    '''
def encodeDataFrame():
    '''public ByteBuf encodeDataFrame(final ByteBufAllocator allocator, final int streamId, final boolean last, final ByteBuf data)
    '''
def encodeSynStreamFrame():
    '''public ByteBuf encodeSynStreamFrame(final ByteBufAllocator allocator, final int streamId, final int associatedToStreamId, final byte priority, final boolean last, final boolean unidirectional, final ByteBuf headerBlock)
    '''
def encodeSynReplyFrame():
    '''public ByteBuf encodeSynReplyFrame(final ByteBufAllocator allocator, final int streamId, final boolean last, final ByteBuf headerBlock)
    '''
def encodeRstStreamFrame():
    '''public ByteBuf encodeRstStreamFrame(final ByteBufAllocator allocator, final int streamId, final int statusCode)
    '''
def encodeSettingsFrame():
    '''public ByteBuf encodeSettingsFrame(final ByteBufAllocator allocator, final SpdySettingsFrame spdySettingsFrame)
    '''
def encodePingFrame():
    '''public ByteBuf encodePingFrame(final ByteBufAllocator allocator, final int id)
    '''
def encodeGoAwayFrame():
    '''public ByteBuf encodeGoAwayFrame(final ByteBufAllocator allocator, final int lastGoodStreamId, final int statusCode)
    '''
def encodeHeadersFrame():
    '''public ByteBuf encodeHeadersFrame(final ByteBufAllocator allocator, final int streamId, final boolean last, final ByteBuf headerBlock)
    '''
def encodeWindowUpdateFrame():
    '''public ByteBuf encodeWindowUpdateFrame(final ByteBufAllocator allocator, final int streamId, final int deltaWindowSize)
    '''
