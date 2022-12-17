def ():
    '''returns HttpChunkedInput\n\n
    (final ChunkedInput<ByteBuf> input)\n
    (final ChunkedInput<ByteBuf> input, final LastHttpContent lastHttpContent)\n
    '''
def isEndOfInput():
    '''returns boolean\n\n
    isEndOfInput()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def readChunk():
    '''returns HttpContent\n\n
    readChunk(final ChannelHandlerContext ctx)\n
    readChunk(final ByteBufAllocator allocator)\n
    '''
def length():
    '''returns long\n\n
    length()\n
    '''
def progress():
    '''returns long\n\n
    progress()\n
    '''
