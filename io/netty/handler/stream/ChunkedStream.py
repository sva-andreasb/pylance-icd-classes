def ChunkedStream():
'''public ChunkedStream(final InputStream in)
public ChunkedStream(final InputStream in, final int chunkSize)
'''
pass
def transferredBytes():
'''public long transferredBytes()
'''
pass
def isEndOfInput():
'''public boolean isEndOfInput()
'''
pass
def close():
'''public void close()
'''
pass
def readChunk():
'''public ByteBuf readChunk(final ChannelHandlerContext ctx)
public ByteBuf readChunk(final ByteBufAllocator allocator)
'''
pass
def length():
'''public long length()
'''
pass
def progress():
'''public long progress()
'''
pass
