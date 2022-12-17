def ():
    '''returns UnpooledHeapByteBuf\n\n
    (final ByteBufAllocator alloc, final int initialCapacity, final int maxCapacity)\n
    '''
def alloc():
    '''returns ByteBufAllocator\n\n
    alloc()\n
    '''
def order():
    '''returns ByteOrder\n\n
    order()\n
    '''
def isDirect():
    '''returns boolean\n\n
    isDirect()\n
    '''
def capacity():
    '''returns ByteBuf\n\n
    capacity()\n
    capacity(final int newCapacity)\n
    '''
def hasArray():
    '''returns boolean\n\n
    hasArray()\n
    '''
def array():
    '''returns byte[]\n\n
    array()\n
    '''
def arrayOffset():
    '''returns int\n\n
    arrayOffset()\n
    '''
def hasMemoryAddress():
    '''returns boolean\n\n
    hasMemoryAddress()\n
    '''
def memoryAddress():
    '''returns long\n\n
    memoryAddress()\n
    '''
def getBytes():
    '''returns int\n\n
    getBytes(final int index, final ByteBuf dst, final int dstIndex, final int length)\n
    getBytes(final int index, final byte[] dst, final int dstIndex, final int length)\n
    getBytes(final int index, final ByteBuffer dst)\n
    getBytes(final int index, final OutputStream out, final int length)\n
    getBytes(final int index, final GatheringByteChannel out, final int length)\n
    getBytes(final int index, final FileChannel out, final long position, final int length)\n
    '''
def readBytes():
    '''returns int\n\n
    readBytes(final GatheringByteChannel out, final int length)\n
    readBytes(final FileChannel out, final long position, final int length)\n
    '''
def setBytes():
    '''returns int\n\n
    setBytes(final int index, final ByteBuf src, final int srcIndex, final int length)\n
    setBytes(final int index, final byte[] src, final int srcIndex, final int length)\n
    setBytes(final int index, final ByteBuffer src)\n
    setBytes(final int index, final InputStream in, final int length)\n
    setBytes(final int index, final ScatteringByteChannel in, final int length)\n
    setBytes(final int index, final FileChannel in, final long position, final int length)\n
    '''
def nioBufferCount():
    '''returns int\n\n
    nioBufferCount()\n
    '''
def nioBuffer():
    '''returns ByteBuffer\n\n
    nioBuffer(final int index, final int length)\n
    '''
def nioBuffers():
    '''returns ByteBuffer[]\n\n
    nioBuffers(final int index, final int length)\n
    '''
def internalNioBuffer():
    '''returns ByteBuffer\n\n
    internalNioBuffer(final int index, final int length)\n
    '''
def getByte():
    '''returns byte\n\n
    getByte(final int index)\n
    '''
def getShort():
    '''returns short\n\n
    getShort(final int index)\n
    '''
def getShortLE():
    '''returns short\n\n
    getShortLE(final int index)\n
    '''
def getUnsignedMedium():
    '''returns int\n\n
    getUnsignedMedium(final int index)\n
    '''
def getUnsignedMediumLE():
    '''returns int\n\n
    getUnsignedMediumLE(final int index)\n
    '''
def getInt():
    '''returns int\n\n
    getInt(final int index)\n
    '''
def getIntLE():
    '''returns int\n\n
    getIntLE(final int index)\n
    '''
def getLong():
    '''returns long\n\n
    getLong(final int index)\n
    '''
def getLongLE():
    '''returns long\n\n
    getLongLE(final int index)\n
    '''
def setByte():
    '''returns ByteBuf\n\n
    setByte(final int index, final int value)\n
    '''
def setShort():
    '''returns ByteBuf\n\n
    setShort(final int index, final int value)\n
    '''
def setShortLE():
    '''returns ByteBuf\n\n
    setShortLE(final int index, final int value)\n
    '''
def setMedium():
    '''returns ByteBuf\n\n
    setMedium(final int index, final int value)\n
    '''
def setMediumLE():
    '''returns ByteBuf\n\n
    setMediumLE(final int index, final int value)\n
    '''
def setInt():
    '''returns ByteBuf\n\n
    setInt(final int index, final int value)\n
    '''
def setIntLE():
    '''returns ByteBuf\n\n
    setIntLE(final int index, final int value)\n
    '''
def setLong():
    '''returns ByteBuf\n\n
    setLong(final int index, final long value)\n
    '''
def setLongLE():
    '''returns ByteBuf\n\n
    setLongLE(final int index, final long value)\n
    '''
def copy():
    '''returns ByteBuf\n\n
    copy(final int index, final int length)\n
    '''
def unwrap():
    '''returns ByteBuf\n\n
    unwrap()\n
    '''
