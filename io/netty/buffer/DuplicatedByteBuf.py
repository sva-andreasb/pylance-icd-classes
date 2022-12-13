def DuplicatedByteBuf():
    '''    public DuplicatedByteBuf(final ByteBuf buffer)
    '''
def unwrap():
    '''    public ByteBuf unwrap()
    '''
def alloc():
    '''    public ByteBufAllocator alloc()
    '''
def order():
    '''    public ByteOrder order()
    '''
def isDirect():
    '''    public boolean isDirect()
    '''
def capacity():
    '''    public int capacity()
    public ByteBuf capacity(final int newCapacity)
    '''
def hasArray():
    '''    public boolean hasArray()
    '''
def array():
    '''    public byte[] array()
    '''
def arrayOffset():
    '''    public int arrayOffset()
    '''
def hasMemoryAddress():
    '''    public boolean hasMemoryAddress()
    '''
def memoryAddress():
    '''    public long memoryAddress()
    '''
def getByte():
    '''    public byte getByte(final int index)
    '''
def getShort():
    '''    public short getShort(final int index)
    '''
def getShortLE():
    '''    public short getShortLE(final int index)
    '''
def getUnsignedMedium():
    '''    public int getUnsignedMedium(final int index)
    '''
def getUnsignedMediumLE():
    '''    public int getUnsignedMediumLE(final int index)
    '''
def getInt():
    '''    public int getInt(final int index)
    '''
def getIntLE():
    '''    public int getIntLE(final int index)
    '''
def getLong():
    '''    public long getLong(final int index)
    '''
def getLongLE():
    '''    public long getLongLE(final int index)
    '''
def copy():
    '''    public ByteBuf copy(final int index, final int length)
    '''
def slice():
    '''    public ByteBuf slice(final int index, final int length)
    '''
def getBytes():
    '''    public ByteBuf getBytes(final int index, final ByteBuf dst, final int dstIndex, final int length)
    public ByteBuf getBytes(final int index, final byte[] dst, final int dstIndex, final int length)
    public ByteBuf getBytes(final int index, final ByteBuffer dst)
    public ByteBuf getBytes(final int index, final OutputStream out, final int length)
    public int getBytes(final int index, final GatheringByteChannel out, final int length)
    public int getBytes(final int index, final FileChannel out, final long position, final int length)
    '''
def setByte():
    '''    public ByteBuf setByte(final int index, final int value)
    '''
def setShort():
    '''    public ByteBuf setShort(final int index, final int value)
    '''
def setShortLE():
    '''    public ByteBuf setShortLE(final int index, final int value)
    '''
def setMedium():
    '''    public ByteBuf setMedium(final int index, final int value)
    '''
def setMediumLE():
    '''    public ByteBuf setMediumLE(final int index, final int value)
    '''
def setInt():
    '''    public ByteBuf setInt(final int index, final int value)
    '''
def setIntLE():
    '''    public ByteBuf setIntLE(final int index, final int value)
    '''
def setLong():
    '''    public ByteBuf setLong(final int index, final long value)
    '''
def setLongLE():
    '''    public ByteBuf setLongLE(final int index, final long value)
    '''
def setBytes():
    '''    public ByteBuf setBytes(final int index, final byte[] src, final int srcIndex, final int length)
    public ByteBuf setBytes(final int index, final ByteBuf src, final int srcIndex, final int length)
    public ByteBuf setBytes(final int index, final ByteBuffer src)
    public int setBytes(final int index, final InputStream in, final int length)
    public int setBytes(final int index, final ScatteringByteChannel in, final int length)
    public int setBytes(final int index, final FileChannel in, final long position, final int length)
    '''
def nioBufferCount():
    '''    public int nioBufferCount()
    '''
def nioBuffers():
    '''    public ByteBuffer[] nioBuffers(final int index, final int length)
    '''
def forEachByte():
    '''    public int forEachByte(final int index, final int length, final ByteProcessor processor)
    '''
def forEachByteDesc():
    '''    public int forEachByteDesc(final int index, final int length, final ByteProcessor processor)
    '''
