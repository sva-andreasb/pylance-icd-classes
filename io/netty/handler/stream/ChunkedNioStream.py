def ():
    '''returns ChunkedNioStream\n\n
    (final ReadableByteChannel in)\n
    (final ReadableByteChannel in, final int chunkSize)\n
    '''
def transferredBytes():
    '''returns long\n\n
    transferredBytes()\n
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
    '''returns ByteBuf\n\n
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
