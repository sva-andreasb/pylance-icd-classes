MAX_BLOCK_SIZE = "int  65536"
DEFAULT_BLOCK_SIZE = "int  65536"
DEFAULT_MIN_COMPRESSION_RATIO = "double  0.85"
def SnappyFramedOutputStream():
'''public SnappyFramedOutputStream(final OutputStream outputStream)
public SnappyFramedOutputStream(final OutputStream out, final int n, final double n2)
public SnappyFramedOutputStream(final WritableByteChannel writableByteChannel)
public SnappyFramedOutputStream(final WritableByteChannel out, final int capacity, final double n)
'''
pass
def isOpen():
'''public boolean isOpen()
'''
pass
def write():
'''public void write(final int n)
public void write(final byte[] src, int offset, int i)
public int write(final ByteBuffer src)
'''
pass
def transferFrom():
'''public long transferFrom(final InputStream inputStream)
public long transferFrom(final ReadableByteChannel readableByteChannel)
'''
pass
def flush():
'''public final void flush()
'''
pass
def close():
'''public final void close()
'''
pass