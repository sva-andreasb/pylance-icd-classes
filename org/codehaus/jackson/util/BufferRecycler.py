DEFAULT_WRITE_CONCAT_BUFFER_LEN = "int  2000"
def BufferRecycler():
'''public BufferRecycler()
'''
pass
def allocByteBuffer():
'''public final byte[] allocByteBuffer(final ByteBufferType type)
'''
pass
def releaseByteBuffer():
'''public final void releaseByteBuffer(final ByteBufferType type, final byte[] buffer)
'''
pass
def allocCharBuffer():
'''public final char[] allocCharBuffer(final CharBufferType type)
public final char[] allocCharBuffer(final CharBufferType type, int minSize)
'''
pass
def releaseCharBuffer():
'''public final void releaseCharBuffer(final CharBufferType type, final char[] buffer)
'''
pass
