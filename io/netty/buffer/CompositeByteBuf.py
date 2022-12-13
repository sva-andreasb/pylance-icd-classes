def CompositeByteBuf():
    '''    public CompositeByteBuf(final ByteBufAllocator alloc, final boolean direct, final int maxNumComponents)
    public CompositeByteBuf(final ByteBufAllocator alloc, final boolean direct, final int maxNumComponents, final ByteBuf... buffers)
    public CompositeByteBuf(final ByteBufAllocator alloc, final boolean direct, final int maxNumComponents, final Iterable<ByteBuf> buffers)
    '''
def addComponent():
    '''    public CompositeByteBuf addComponent(final ByteBuf buffer)
    public CompositeByteBuf addComponent(final int cIndex, final ByteBuf buffer)
    public CompositeByteBuf addComponent(final boolean increaseWriterIndex, final ByteBuf buffer)
    public CompositeByteBuf addComponent(final boolean increaseWriterIndex, final int cIndex, final ByteBuf buffer)
    '''
def addComponents():
    '''    public CompositeByteBuf addComponents(final ByteBuf... buffers)
    public CompositeByteBuf addComponents(final Iterable<ByteBuf> buffers)
    public CompositeByteBuf addComponents(final boolean increaseWriterIndex, final ByteBuf... buffers)
    public CompositeByteBuf addComponents(final boolean increaseWriterIndex, final Iterable<ByteBuf> buffers)
    public CompositeByteBuf addComponents(final int cIndex, final ByteBuf... buffers)
    public CompositeByteBuf addComponents(final int cIndex, final Iterable<ByteBuf> buffers)
    '''
def addFlattenedComponents():
    '''    public CompositeByteBuf addFlattenedComponents(final boolean increaseWriterIndex, ByteBuf buffer)
    '''
def removeComponent():
    '''    public CompositeByteBuf removeComponent(final int cIndex)
    '''
def removeComponents():
    '''    public CompositeByteBuf removeComponents(final int cIndex, final int numComponents)
    '''
def iterator():
    '''    public Iterator<ByteBuf> iterator()
    '''
def decompose():
    '''    public List<ByteBuf> decompose(final int offset, final int length)
    '''
def isDirect():
    '''    public boolean isDirect()
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
def capacity():
    '''    public int capacity()
    public CompositeByteBuf capacity(final int newCapacity)
    '''
def alloc():
    '''    public ByteBufAllocator alloc()
    '''
def order():
    '''    public ByteOrder order()
    '''
def numComponents():
    '''    public int numComponents()
    '''
def maxNumComponents():
    '''    public int maxNumComponents()
    '''
def toComponentIndex():
    '''    public int toComponentIndex(final int offset)
    '''
def toByteIndex():
    '''    public int toByteIndex(final int cIndex)
    '''
def getByte():
    '''    public byte getByte(final int index)
    '''
def getBytes():
    '''    public CompositeByteBuf getBytes(int index, final byte[] dst, int dstIndex, int length)
    public CompositeByteBuf getBytes(int index, final ByteBuffer dst)
    public CompositeByteBuf getBytes(int index, final ByteBuf dst, int dstIndex, int length)
    public int getBytes(final int index, final GatheringByteChannel out, final int length)
    public int getBytes(final int index, final FileChannel out, final long position, final int length)
    public CompositeByteBuf getBytes(int index, final OutputStream out, int length)
    public CompositeByteBuf getBytes(final int index, final ByteBuf dst)
    public CompositeByteBuf getBytes(final int index, final ByteBuf dst, final int length)
    public CompositeByteBuf getBytes(final int index, final byte[] dst)
    '''
def setByte():
    '''    public CompositeByteBuf setByte(final int index, final int value)
    '''
def setShort():
    '''    public CompositeByteBuf setShort(final int index, final int value)
    '''
def setMedium():
    '''    public CompositeByteBuf setMedium(final int index, final int value)
    '''
def setInt():
    '''    public CompositeByteBuf setInt(final int index, final int value)
    '''
def setLong():
    '''    public CompositeByteBuf setLong(final int index, final long value)
    '''
def setBytes():
    '''    public CompositeByteBuf setBytes(int index, final byte[] src, int srcIndex, int length)
    public CompositeByteBuf setBytes(int index, final ByteBuffer src)
    public CompositeByteBuf setBytes(int index, final ByteBuf src, int srcIndex, int length)
    public int setBytes(int index, final InputStream in, int length)
    public int setBytes(int index, final ScatteringByteChannel in, int length)
    public int setBytes(int index, final FileChannel in, final long position, int length)
    public CompositeByteBuf setBytes(final int index, final ByteBuf src)
    public CompositeByteBuf setBytes(final int index, final ByteBuf src, final int length)
    public CompositeByteBuf setBytes(final int index, final byte[] src)
    '''
def copy():
    '''    public ByteBuf copy(final int index, final int length)
    '''
def component():
    '''    public ByteBuf component(final int cIndex)
    '''
def componentAtOffset():
    '''    public ByteBuf componentAtOffset(final int offset)
    '''
def internalComponent():
    '''    public ByteBuf internalComponent(final int cIndex)
    '''
def internalComponentAtOffset():
    '''    public ByteBuf internalComponentAtOffset(final int offset)
    '''
def nioBufferCount():
    '''    public int nioBufferCount()
    '''
def internalNioBuffer():
    '''    public ByteBuffer internalNioBuffer(final int index, final int length)
    '''
def nioBuffer():
    '''    public ByteBuffer nioBuffer(final int index, final int length)
    '''
def nioBuffers():
    '''    public ByteBuffer[] nioBuffers(int index, int length)
    public ByteBuffer[] nioBuffers()
    '''
def consolidate():
    '''    public CompositeByteBuf consolidate()
    public CompositeByteBuf consolidate(final int cIndex, final int numComponents)
    '''
def discardReadComponents():
    '''    public CompositeByteBuf discardReadComponents()
    '''
def discardReadBytes():
    '''    public CompositeByteBuf discardReadBytes()
    '''
def toString():
    '''    public String toString()
    '''
def readerIndex():
    '''    public CompositeByteBuf readerIndex(final int readerIndex)
    '''
def writerIndex():
    '''    public CompositeByteBuf writerIndex(final int writerIndex)
    '''
def setIndex():
    '''    public CompositeByteBuf setIndex(final int readerIndex, final int writerIndex)
    '''
def clear():
    '''    public CompositeByteBuf clear()
    '''
def markReaderIndex():
    '''    public CompositeByteBuf markReaderIndex()
    '''
def resetReaderIndex():
    '''    public CompositeByteBuf resetReaderIndex()
    '''
def markWriterIndex():
    '''    public CompositeByteBuf markWriterIndex()
    '''
def resetWriterIndex():
    '''    public CompositeByteBuf resetWriterIndex()
    '''
def ensureWritable():
    '''    public CompositeByteBuf ensureWritable(final int minWritableBytes)
    '''
def setBoolean():
    '''    public CompositeByteBuf setBoolean(final int index, final boolean value)
    '''
def setChar():
    '''    public CompositeByteBuf setChar(final int index, final int value)
    '''
def setFloat():
    '''    public CompositeByteBuf setFloat(final int index, final float value)
    '''
def setDouble():
    '''    public CompositeByteBuf setDouble(final int index, final double value)
    '''
def setZero():
    '''    public CompositeByteBuf setZero(final int index, final int length)
    '''
def readBytes():
    '''    public CompositeByteBuf readBytes(final ByteBuf dst)
    public CompositeByteBuf readBytes(final ByteBuf dst, final int length)
    public CompositeByteBuf readBytes(final ByteBuf dst, final int dstIndex, final int length)
    public CompositeByteBuf readBytes(final byte[] dst)
    public CompositeByteBuf readBytes(final byte[] dst, final int dstIndex, final int length)
    public CompositeByteBuf readBytes(final ByteBuffer dst)
    public CompositeByteBuf readBytes(final OutputStream out, final int length)
    '''
def skipBytes():
    '''    public CompositeByteBuf skipBytes(final int length)
    '''
def writeBoolean():
    '''    public CompositeByteBuf writeBoolean(final boolean value)
    '''
def writeByte():
    '''    public CompositeByteBuf writeByte(final int value)
    '''
def writeShort():
    '''    public CompositeByteBuf writeShort(final int value)
    '''
def writeMedium():
    '''    public CompositeByteBuf writeMedium(final int value)
    '''
def writeInt():
    '''    public CompositeByteBuf writeInt(final int value)
    '''
def writeLong():
    '''    public CompositeByteBuf writeLong(final long value)
    '''
def writeChar():
    '''    public CompositeByteBuf writeChar(final int value)
    '''
def writeFloat():
    '''    public CompositeByteBuf writeFloat(final float value)
    '''
def writeDouble():
    '''    public CompositeByteBuf writeDouble(final double value)
    '''
def writeBytes():
    '''    public CompositeByteBuf writeBytes(final ByteBuf src)
    public CompositeByteBuf writeBytes(final ByteBuf src, final int length)
    public CompositeByteBuf writeBytes(final ByteBuf src, final int srcIndex, final int length)
    public CompositeByteBuf writeBytes(final byte[] src)
    public CompositeByteBuf writeBytes(final byte[] src, final int srcIndex, final int length)
    public CompositeByteBuf writeBytes(final ByteBuffer src)
    '''
def writeZero():
    '''    public CompositeByteBuf writeZero(final int length)
    '''
def retain():
    '''    public CompositeByteBuf retain(final int increment)
    public CompositeByteBuf retain()
    '''
def touch():
    '''    public CompositeByteBuf touch()
    public CompositeByteBuf touch(final Object hint)
    '''
def discardSomeReadBytes():
    '''    public CompositeByteBuf discardSomeReadBytes()
    '''
def unwrap():
    '''    public ByteBuf unwrap()
    '''
def wrap():
    '''    public ByteBuf wrap(final byte[] bytes)
    public ByteBuf wrap(final ByteBuffer bytes)
    '''
def isEmpty():
    '''    public boolean isEmpty(final byte[] bytes)
    public boolean isEmpty(final ByteBuffer bytes)
    '''
def hasNext():
    '''    public boolean hasNext()
    '''
def next():
    '''    public ByteBuf next()
    '''
def remove():
    '''    public void remove()
    '''
