def DuplicatedByteBuf():
'''public DuplicatedByteBuf(final ByteBuf buffer)
'''
pass
def unwrap():
'''public ByteBuf unwrap()
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
def isDirect():
'''public boolean isDirect()
'''
pass
def capacity():
'''public int capacity()
public ByteBuf capacity(final int newCapacity)
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
def getByte():
'''public byte getByte(final int index)
'''
pass
def getShort():
'''public short getShort(final int index)
'''
pass
def getShortLE():
'''public short getShortLE(final int index)
'''
pass
def getUnsignedMedium():
'''public int getUnsignedMedium(final int index)
'''
pass
def getUnsignedMediumLE():
'''public int getUnsignedMediumLE(final int index)
'''
pass
def getInt():
'''public int getInt(final int index)
'''
pass
def getIntLE():
'''public int getIntLE(final int index)
'''
pass
def getLong():
'''public long getLong(final int index)
'''
pass
def getLongLE():
'''public long getLongLE(final int index)
'''
pass
def copy():
'''public ByteBuf copy(final int index, final int length)
'''
pass
def slice():
'''public ByteBuf slice(final int index, final int length)
'''
pass
def getBytes():
'''public ByteBuf getBytes(final int index, final ByteBuf dst, final int dstIndex, final int length)
public ByteBuf getBytes(final int index, final byte[] dst, final int dstIndex, final int length)
public ByteBuf getBytes(final int index, final ByteBuffer dst)
public ByteBuf getBytes(final int index, final OutputStream out, final int length)
public int getBytes(final int index, final GatheringByteChannel out, final int length)
public int getBytes(final int index, final FileChannel out, final long position, final int length)
'''
pass
def setByte():
'''public ByteBuf setByte(final int index, final int value)
'''
pass
def setShort():
'''public ByteBuf setShort(final int index, final int value)
'''
pass
def setShortLE():
'''public ByteBuf setShortLE(final int index, final int value)
'''
pass
def setMedium():
'''public ByteBuf setMedium(final int index, final int value)
'''
pass
def setMediumLE():
'''public ByteBuf setMediumLE(final int index, final int value)
'''
pass
def setInt():
'''public ByteBuf setInt(final int index, final int value)
'''
pass
def setIntLE():
'''public ByteBuf setIntLE(final int index, final int value)
'''
pass
def setLong():
'''public ByteBuf setLong(final int index, final long value)
'''
pass
def setLongLE():
'''public ByteBuf setLongLE(final int index, final long value)
'''
pass
def setBytes():
'''public ByteBuf setBytes(final int index, final byte[] src, final int srcIndex, final int length)
public ByteBuf setBytes(final int index, final ByteBuf src, final int srcIndex, final int length)
public ByteBuf setBytes(final int index, final ByteBuffer src)
public int setBytes(final int index, final InputStream in, final int length)
public int setBytes(final int index, final ScatteringByteChannel in, final int length)
public int setBytes(final int index, final FileChannel in, final long position, final int length)
'''
pass
def nioBufferCount():
'''public int nioBufferCount()
'''
pass
def nioBuffers():
'''public ByteBuffer[] nioBuffers(final int index, final int length)
'''
pass
def forEachByte():
'''public int forEachByte(final int index, final int length, final ByteProcessor processor)
'''
pass
def forEachByteDesc():
'''public int forEachByteDesc(final int index, final int length, final ByteProcessor processor)
'''
pass
