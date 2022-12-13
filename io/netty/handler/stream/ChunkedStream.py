def ChunkedStream():
    '''public ChunkedStream(final InputStream in)
    public ChunkedStream(final InputStream in, final int chunkSize)
    '''
def transferredBytes():
    '''public long transferredBytes()
    '''
def isEndOfInput():
    '''public boolean isEndOfInput()
    '''
def close():
    '''public void close()
    '''
def readChunk():
    '''public ByteBuf readChunk(final ChannelHandlerContext ctx)
    public ByteBuf readChunk(final ByteBufAllocator allocator)
    '''
def length():
    '''public long length()
    '''
def progress():
    '''public long progress()
    '''
