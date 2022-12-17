def ():
    '''returns CompositeByteBuf\n\n
    (final ByteBufAllocator alloc, final boolean direct, final int maxNumComponents)\n
    (final ByteBufAllocator alloc, final boolean direct, final int maxNumComponents, final ByteBuf... buffers)\n
    (final ByteBufAllocator alloc, final boolean direct, final int maxNumComponents, final Iterable<ByteBuf> buffers)\n
    '''
def addComponent():
    '''returns CompositeByteBuf\n\n
    addComponent(final ByteBuf buffer)\n
    addComponent(final int cIndex, final ByteBuf buffer)\n
    addComponent(final boolean increaseWriterIndex, final ByteBuf buffer)\n
    addComponent(final boolean increaseWriterIndex, final int cIndex, final ByteBuf buffer)\n
    '''
def addComponents():
    '''returns CompositeByteBuf\n\n
    addComponents(final ByteBuf... buffers)\n
    addComponents(final Iterable<ByteBuf> buffers)\n
    addComponents(final boolean increaseWriterIndex, final ByteBuf... buffers)\n
    addComponents(final boolean increaseWriterIndex, final Iterable<ByteBuf> buffers)\n
    addComponents(final int cIndex, final ByteBuf... buffers)\n
    addComponents(final int cIndex, final Iterable<ByteBuf> buffers)\n
    '''
def addFlattenedComponents():
    '''returns CompositeByteBuf\n\n
    addFlattenedComponents(final boolean increaseWriterIndex, ByteBuf buffer)\n
    '''
def removeComponent():
    '''returns CompositeByteBuf\n\n
    removeComponent(final int cIndex)\n
    '''
def removeComponents():
    '''returns CompositeByteBuf\n\n
    removeComponents(final int cIndex, final int numComponents)\n
    '''
def iterator():
    '''returns Iterator<ByteBuf>\n\n
    iterator()\n
    '''
def decompose():
    '''returns List<ByteBuf>\n\n
    decompose(final int offset, final int length)\n
    '''
def isDirect():
    '''returns boolean\n\n
    isDirect()\n
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
def capacity():
    '''returns CompositeByteBuf\n\n
    capacity()\n
    capacity(final int newCapacity)\n
    '''
def alloc():
    '''returns ByteBufAllocator\n\n
    alloc()\n
    '''
def order():
    '''returns ByteOrder\n\n
    order()\n
    '''
def numComponents():
    '''returns int\n\n
    numComponents()\n
    '''
def maxNumComponents():
    '''returns int\n\n
    maxNumComponents()\n
    '''
def toComponentIndex():
    '''returns int\n\n
    toComponentIndex(final int offset)\n
    '''
def toByteIndex():
    '''returns int\n\n
    toByteIndex(final int cIndex)\n
    '''
def getByte():
    '''returns byte\n\n
    getByte(final int index)\n
    '''
def getBytes():
    '''returns CompositeByteBuf\n\n
    getBytes(int index, final byte[] dst, int dstIndex, int length)\n
    getBytes(int index, final ByteBuffer dst)\n
    getBytes(int index, final ByteBuf dst, int dstIndex, int length)\n
    getBytes(final int index, final GatheringByteChannel out, final int length)\n
    getBytes(final int index, final FileChannel out, final long position, final int length)\n
    getBytes(int index, final OutputStream out, int length)\n
    getBytes(final int index, final ByteBuf dst)\n
    getBytes(final int index, final ByteBuf dst, final int length)\n
    getBytes(final int index, final byte[] dst)\n
    '''
def setByte():
    '''returns CompositeByteBuf\n\n
    setByte(final int index, final int value)\n
    '''
def setShort():
    '''returns CompositeByteBuf\n\n
    setShort(final int index, final int value)\n
    '''
def setMedium():
    '''returns CompositeByteBuf\n\n
    setMedium(final int index, final int value)\n
    '''
def setInt():
    '''returns CompositeByteBuf\n\n
    setInt(final int index, final int value)\n
    '''
def setLong():
    '''returns CompositeByteBuf\n\n
    setLong(final int index, final long value)\n
    '''
def setBytes():
    '''returns CompositeByteBuf\n\n
    setBytes(int index, final byte[] src, int srcIndex, int length)\n
    setBytes(int index, final ByteBuffer src)\n
    setBytes(int index, final ByteBuf src, int srcIndex, int length)\n
    setBytes(int index, final InputStream in, int length)\n
    setBytes(int index, final ScatteringByteChannel in, int length)\n
    setBytes(int index, final FileChannel in, final long position, int length)\n
    setBytes(final int index, final ByteBuf src)\n
    setBytes(final int index, final ByteBuf src, final int length)\n
    setBytes(final int index, final byte[] src)\n
    '''
def copy():
    '''returns ByteBuf\n\n
    copy(final int index, final int length)\n
    '''
def component():
    '''returns ByteBuf\n\n
    component(final int cIndex)\n
    '''
def componentAtOffset():
    '''returns ByteBuf\n\n
    componentAtOffset(final int offset)\n
    '''
def internalComponent():
    '''returns ByteBuf\n\n
    internalComponent(final int cIndex)\n
    '''
def internalComponentAtOffset():
    '''returns ByteBuf\n\n
    internalComponentAtOffset(final int offset)\n
    '''
def nioBufferCount():
    '''returns int\n\n
    nioBufferCount()\n
    '''
def internalNioBuffer():
    '''returns ByteBuffer\n\n
    internalNioBuffer(final int index, final int length)\n
    '''
def nioBuffer():
    '''returns ByteBuffer\n\n
    nioBuffer(final int index, final int length)\n
    '''
def nioBuffers():
    '''returns ByteBuffer[]\n\n
    nioBuffers(int index, int length)\n
    nioBuffers()\n
    '''
def consolidate():
    '''returns CompositeByteBuf\n\n
    consolidate()\n
    consolidate(final int cIndex, final int numComponents)\n
    '''
def discardReadComponents():
    '''returns CompositeByteBuf\n\n
    discardReadComponents()\n
    '''
def discardReadBytes():
    '''returns CompositeByteBuf\n\n
    discardReadBytes()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def readerIndex():
    '''returns CompositeByteBuf\n\n
    readerIndex(final int readerIndex)\n
    '''
def writerIndex():
    '''returns CompositeByteBuf\n\n
    writerIndex(final int writerIndex)\n
    '''
def setIndex():
    '''returns CompositeByteBuf\n\n
    setIndex(final int readerIndex, final int writerIndex)\n
    '''
def clear():
    '''returns CompositeByteBuf\n\n
    clear()\n
    '''
def markReaderIndex():
    '''returns CompositeByteBuf\n\n
    markReaderIndex()\n
    '''
def resetReaderIndex():
    '''returns CompositeByteBuf\n\n
    resetReaderIndex()\n
    '''
def markWriterIndex():
    '''returns CompositeByteBuf\n\n
    markWriterIndex()\n
    '''
def resetWriterIndex():
    '''returns CompositeByteBuf\n\n
    resetWriterIndex()\n
    '''
def ensureWritable():
    '''returns CompositeByteBuf\n\n
    ensureWritable(final int minWritableBytes)\n
    '''
def setBoolean():
    '''returns CompositeByteBuf\n\n
    setBoolean(final int index, final boolean value)\n
    '''
def setChar():
    '''returns CompositeByteBuf\n\n
    setChar(final int index, final int value)\n
    '''
def setFloat():
    '''returns CompositeByteBuf\n\n
    setFloat(final int index, final float value)\n
    '''
def setDouble():
    '''returns CompositeByteBuf\n\n
    setDouble(final int index, final double value)\n
    '''
def setZero():
    '''returns CompositeByteBuf\n\n
    setZero(final int index, final int length)\n
    '''
def readBytes():
    '''returns CompositeByteBuf\n\n
    readBytes(final ByteBuf dst)\n
    readBytes(final ByteBuf dst, final int length)\n
    readBytes(final ByteBuf dst, final int dstIndex, final int length)\n
    readBytes(final byte[] dst)\n
    readBytes(final byte[] dst, final int dstIndex, final int length)\n
    readBytes(final ByteBuffer dst)\n
    readBytes(final OutputStream out, final int length)\n
    '''
def skipBytes():
    '''returns CompositeByteBuf\n\n
    skipBytes(final int length)\n
    '''
def writeBoolean():
    '''returns CompositeByteBuf\n\n
    writeBoolean(final boolean value)\n
    '''
def writeByte():
    '''returns CompositeByteBuf\n\n
    writeByte(final int value)\n
    '''
def writeShort():
    '''returns CompositeByteBuf\n\n
    writeShort(final int value)\n
    '''
def writeMedium():
    '''returns CompositeByteBuf\n\n
    writeMedium(final int value)\n
    '''
def writeInt():
    '''returns CompositeByteBuf\n\n
    writeInt(final int value)\n
    '''
def writeLong():
    '''returns CompositeByteBuf\n\n
    writeLong(final long value)\n
    '''
def writeChar():
    '''returns CompositeByteBuf\n\n
    writeChar(final int value)\n
    '''
def writeFloat():
    '''returns CompositeByteBuf\n\n
    writeFloat(final float value)\n
    '''
def writeDouble():
    '''returns CompositeByteBuf\n\n
    writeDouble(final double value)\n
    '''
def writeBytes():
    '''returns CompositeByteBuf\n\n
    writeBytes(final ByteBuf src)\n
    writeBytes(final ByteBuf src, final int length)\n
    writeBytes(final ByteBuf src, final int srcIndex, final int length)\n
    writeBytes(final byte[] src)\n
    writeBytes(final byte[] src, final int srcIndex, final int length)\n
    writeBytes(final ByteBuffer src)\n
    '''
def writeZero():
    '''returns CompositeByteBuf\n\n
    writeZero(final int length)\n
    '''
def retain():
    '''returns CompositeByteBuf\n\n
    retain(final int increment)\n
    retain()\n
    '''
def touch():
    '''returns CompositeByteBuf\n\n
    touch()\n
    touch(final Object hint)\n
    '''
def discardSomeReadBytes():
    '''returns CompositeByteBuf\n\n
    discardSomeReadBytes()\n
    '''
def unwrap():
    '''returns ByteBuf\n\n
    unwrap()\n
    '''
def wrap():
    '''returns ByteBuf\n\n
    wrap(final byte[] bytes)\n
    wrap(final ByteBuffer bytes)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty(final byte[] bytes)\n
    isEmpty(final ByteBuffer bytes)\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns ByteBuf\n\n
    next()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
