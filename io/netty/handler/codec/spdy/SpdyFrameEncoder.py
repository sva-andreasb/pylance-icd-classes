def SpdyFrameEncoder():
'''public SpdyFrameEncoder(final SpdyVersion spdyVersion)
'''
pass
def encodeDataFrame():
'''public ByteBuf encodeDataFrame(final ByteBufAllocator allocator, final int streamId, final boolean last, final ByteBuf data)
'''
pass
def encodeSynStreamFrame():
'''public ByteBuf encodeSynStreamFrame(final ByteBufAllocator allocator, final int streamId, final int associatedToStreamId, final byte priority, final boolean last, final boolean unidirectional, final ByteBuf headerBlock)
'''
pass
def encodeSynReplyFrame():
'''public ByteBuf encodeSynReplyFrame(final ByteBufAllocator allocator, final int streamId, final boolean last, final ByteBuf headerBlock)
'''
pass
def encodeRstStreamFrame():
'''public ByteBuf encodeRstStreamFrame(final ByteBufAllocator allocator, final int streamId, final int statusCode)
'''
pass
def encodeSettingsFrame():
'''public ByteBuf encodeSettingsFrame(final ByteBufAllocator allocator, final SpdySettingsFrame spdySettingsFrame)
'''
pass
def encodePingFrame():
'''public ByteBuf encodePingFrame(final ByteBufAllocator allocator, final int id)
'''
pass
def encodeGoAwayFrame():
'''public ByteBuf encodeGoAwayFrame(final ByteBufAllocator allocator, final int lastGoodStreamId, final int statusCode)
'''
pass
def encodeHeadersFrame():
'''public ByteBuf encodeHeadersFrame(final ByteBufAllocator allocator, final int streamId, final boolean last, final ByteBuf headerBlock)
'''
pass
def encodeWindowUpdateFrame():
'''public ByteBuf encodeWindowUpdateFrame(final ByteBufAllocator allocator, final int streamId, final int deltaWindowSize)
'''
pass
