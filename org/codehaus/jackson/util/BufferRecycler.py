DEFAULT_WRITE_CONCAT_BUFFER_LEN = "int  2000"
def BufferRecycler():
    '''    public BufferRecycler()
    '''
def allocByteBuffer():
    '''    public final byte[] allocByteBuffer(final ByteBufferType type)
    '''
def releaseByteBuffer():
    '''    public final void releaseByteBuffer(final ByteBufferType type, final byte[] buffer)
    '''
def allocCharBuffer():
    '''    public final char[] allocCharBuffer(final CharBufferType type)
    public final char[] allocCharBuffer(final CharBufferType type, int minSize)
    '''
def releaseCharBuffer():
    '''    public final void releaseCharBuffer(final CharBufferType type, final char[] buffer)
    '''
