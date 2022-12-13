def CompositeByteBuf():
'''public CompositeByteBuf(final ByteBufAllocator alloc, final boolean direct, final int maxNumComponents)
public CompositeByteBuf(final ByteBufAllocator alloc, final boolean direct, final int maxNumComponents, final ByteBuf... buffers)
public CompositeByteBuf(final ByteBufAllocator alloc, final boolean direct, final int maxNumComponents, final Iterable<ByteBuf> buffers)
'''
pass
def addComponent():
'''public CompositeByteBuf addComponent(final ByteBuf buffer)
public CompositeByteBuf addComponent(final int cIndex, final ByteBuf buffer)
public CompositeByteBuf addComponent(final boolean increaseWriterIndex, final ByteBuf buffer)
public CompositeByteBuf addComponent(final boolean increaseWriterIndex, final int cIndex, final ByteBuf buffer)
'''
pass
def addComponents():
'''public CompositeByteBuf addComponents(final ByteBuf... buffers)
public CompositeByteBuf addComponents(final Iterable<ByteBuf> buffers)
public CompositeByteBuf addComponents(final boolean increaseWriterIndex, final ByteBuf... buffers)
public CompositeByteBuf addComponents(final boolean increaseWriterIndex, final Iterable<ByteBuf> buffers)
public CompositeByteBuf addComponents(final int cIndex, final ByteBuf... buffers)
public CompositeByteBuf addComponents(final int cIndex, final Iterable<ByteBuf> buffers)
'''
pass
def addFlattenedComponents():
'''public CompositeByteBuf addFlattenedComponents(final boolean increaseWriterIndex, ByteBuf buffer)
'''
pass
def removeComponent():
'''public CompositeByteBuf removeComponent(final int cIndex)
'''
pass
def removeComponents():
'''public CompositeByteBuf removeComponents(final int cIndex, final int numComponents)
'''
pass
def iterator():
'''public Iterator<ByteBuf> iterator()
'''
pass
def decompose():
'''public List<ByteBuf> decompose(final int offset, final int length)
'''
pass
def isDirect():
'''public boolean isDirect()
'''
pass
def hasArray():
'''public boolean hasArray()
'''
pass
def array():
'''public byte[] array()
'''
pass
def arrayOffset():
'''public int arrayOffset()
'''
pass
def hasMemoryAddress():
'''public boolean hasMemoryAddress()
'''
pass
def memoryAddress():
'''public long memoryAddress()
'''
pass
def capacity():
'''public int capacity()
public CompositeByteBuf capacity(final int newCapacity)
'''
pass
def alloc():
'''public ByteBufAllocator alloc()
'''
pass
def order():
'''public ByteOrder order()
'''
pass
def numComponents():
'''public int numComponents()
'''
pass
def maxNumComponents():
'''public int maxNumComponents()
'''
pass
def toComponentIndex():
'''public int toComponentIndex(final int offset)
'''
pass
def toByteIndex():
'''public int toByteIndex(final int cIndex)
'''
pass
def getByte():
'''public byte getByte(final int index)
'''
pass
def getBytes():
'''public CompositeByteBuf getBytes(int index, final byte[] dst, int dstIndex, int length)
public CompositeByteBuf getBytes(int index, final ByteBuffer dst)
public CompositeByteBuf getBytes(int index, final ByteBuf dst, int dstIndex, int length)
public int getBytes(final int index, final GatheringByteChannel out, final int length)
public int getBytes(final int index, final FileChannel out, final long position, final int length)
public CompositeByteBuf getBytes(int index, final OutputStream out, int length)
public CompositeByteBuf getBytes(final int index, final ByteBuf dst)
public CompositeByteBuf getBytes(final int index, final ByteBuf dst, final int length)
public CompositeByteBuf getBytes(final int index, final byte[] dst)
'''
pass
def setByte():
'''public CompositeByteBuf setByte(final int index, final int value)
'''
pass
def setShort():
'''public CompositeByteBuf setShort(final int index, final int value)
'''
pass
def setMedium():
'''public CompositeByteBuf setMedium(final int index, final int value)
'''
pass
def setInt():
'''public CompositeByteBuf setInt(final int index, final int value)
'''
pass
def setLong():
'''public CompositeByteBuf setLong(final int index, final long value)
'''
pass
def setBytes():
'''public CompositeByteBuf setBytes(int index, final byte[] src, int srcIndex, int length)
public CompositeByteBuf setBytes(int index, final ByteBuffer src)
public CompositeByteBuf setBytes(int index, final ByteBuf src, int srcIndex, int length)
public int setBytes(int index, final InputStream in, int length)
public int setBytes(int index, final ScatteringByteChannel in, int length)
public int setBytes(int index, final FileChannel in, final long position, int length)
public CompositeByteBuf setBytes(final int index, final ByteBuf src)
public CompositeByteBuf setBytes(final int index, final ByteBuf src, final int length)
public CompositeByteBuf setBytes(final int index, final byte[] src)
'''
pass
def copy():
'''public ByteBuf copy(final int index, final int length)
'''
pass
def component():
'''public ByteBuf component(final int cIndex)
'''
pass
def componentAtOffset():
'''public ByteBuf componentAtOffset(final int offset)
'''
pass
def internalComponent():
'''public ByteBuf internalComponent(final int cIndex)
'''
pass
def internalComponentAtOffset():
'''public ByteBuf internalComponentAtOffset(final int offset)
'''
pass
def nioBufferCount():
'''public int nioBufferCount()
'''
pass
def internalNioBuffer():
'''public ByteBuffer internalNioBuffer(final int index, final int length)
'''
pass
def nioBuffer():
'''public ByteBuffer nioBuffer(final int index, final int length)
'''
pass
def nioBuffers():
'''public ByteBuffer[] nioBuffers(int index, int length)
public ByteBuffer[] nioBuffers()
'''
pass
def consolidate():
'''public CompositeByteBuf consolidate()
public CompositeByteBuf consolidate(final int cIndex, final int numComponents)
'''
pass
def discardReadComponents():
'''public CompositeByteBuf discardReadComponents()
'''
pass
def discardReadBytes():
'''public CompositeByteBuf discardReadBytes()
'''
pass
def toString():
'''public String toString()
'''
pass
def readerIndex():
'''public CompositeByteBuf readerIndex(final int readerIndex)
'''
pass
def writerIndex():
'''public CompositeByteBuf writerIndex(final int writerIndex)
'''
pass
def setIndex():
'''public CompositeByteBuf setIndex(final int readerIndex, final int writerIndex)
'''
pass
def clear():
'''public CompositeByteBuf clear()
'''
pass
def markReaderIndex():
'''public CompositeByteBuf markReaderIndex()
'''
pass
def resetReaderIndex():
'''public CompositeByteBuf resetReaderIndex()
'''
pass
def markWriterIndex():
'''public CompositeByteBuf markWriterIndex()
'''
pass
def resetWriterIndex():
'''public CompositeByteBuf resetWriterIndex()
'''
pass
def ensureWritable():
'''public CompositeByteBuf ensureWritable(final int minWritableBytes)
'''
pass
def setBoolean():
'''public CompositeByteBuf setBoolean(final int index, final boolean value)
'''
pass
def setChar():
'''public CompositeByteBuf setChar(final int index, final int value)
'''
pass
def setFloat():
'''public CompositeByteBuf setFloat(final int index, final float value)
'''
pass
def setDouble():
'''public CompositeByteBuf setDouble(final int index, final double value)
'''
pass
def setZero():
'''public CompositeByteBuf setZero(final int index, final int length)
'''
pass
def readBytes():
'''public CompositeByteBuf readBytes(final ByteBuf dst)
public CompositeByteBuf readBytes(final ByteBuf dst, final int length)
public CompositeByteBuf readBytes(final ByteBuf dst, final int dstIndex, final int length)
public CompositeByteBuf readBytes(final byte[] dst)
public CompositeByteBuf readBytes(final byte[] dst, final int dstIndex, final int length)
public CompositeByteBuf readBytes(final ByteBuffer dst)
public CompositeByteBuf readBytes(final OutputStream out, final int length)
'''
pass
def skipBytes():
'''public CompositeByteBuf skipBytes(final int length)
'''
pass
def writeBoolean():
'''public CompositeByteBuf writeBoolean(final boolean value)
'''
pass
def writeByte():
'''public CompositeByteBuf writeByte(final int value)
'''
pass
def writeShort():
'''public CompositeByteBuf writeShort(final int value)
'''
pass
def writeMedium():
'''public CompositeByteBuf writeMedium(final int value)
'''
pass
def writeInt():
'''public CompositeByteBuf writeInt(final int value)
'''
pass
def writeLong():
'''public CompositeByteBuf writeLong(final long value)
'''
pass
def writeChar():
'''public CompositeByteBuf writeChar(final int value)
'''
pass
def writeFloat():
'''public CompositeByteBuf writeFloat(final float value)
'''
pass
def writeDouble():
'''public CompositeByteBuf writeDouble(final double value)
'''
pass
def writeBytes():
'''public CompositeByteBuf writeBytes(final ByteBuf src)
public CompositeByteBuf writeBytes(final ByteBuf src, final int length)
public CompositeByteBuf writeBytes(final ByteBuf src, final int srcIndex, final int length)
public CompositeByteBuf writeBytes(final byte[] src)
public CompositeByteBuf writeBytes(final byte[] src, final int srcIndex, final int length)
public CompositeByteBuf writeBytes(final ByteBuffer src)
'''
pass
def writeZero():
'''public CompositeByteBuf writeZero(final int length)
'''
pass
def retain():
'''public CompositeByteBuf retain(final int increment)
public CompositeByteBuf retain()
'''
pass
def touch():
'''public CompositeByteBuf touch()
public CompositeByteBuf touch(final Object hint)
'''
pass
def discardSomeReadBytes():
'''public CompositeByteBuf discardSomeReadBytes()
'''
pass
def unwrap():
'''public ByteBuf unwrap()
'''
pass
def wrap():
'''public ByteBuf wrap(final byte[] bytes)
public ByteBuf wrap(final ByteBuffer bytes)
'''
pass
def isEmpty():
'''public boolean isEmpty(final byte[] bytes)
public boolean isEmpty(final ByteBuffer bytes)
'''
pass
def hasNext():
'''public boolean hasNext()
'''
pass
def next():
'''public ByteBuf next()
'''
pass
def remove():
'''public void remove()
'''
pass
