def updateAllocator():
    '''returns None\n\n
    updateAllocator(final ByteBufAllocator allocator)\n
    '''
def buffer():
    '''returns ByteBuf\n\n
    buffer()\n
    buffer(final int initialCapacity)\n
    buffer(final int initialCapacity, final int maxCapacity)\n
    '''
def ioBuffer():
    '''returns ByteBuf\n\n
    ioBuffer()\n
    ioBuffer(final int initialCapacity)\n
    ioBuffer(final int initialCapacity, final int maxCapacity)\n
    '''
def heapBuffer():
    '''returns ByteBuf\n\n
    heapBuffer()\n
    heapBuffer(final int initialCapacity)\n
    heapBuffer(final int initialCapacity, final int maxCapacity)\n
    '''
def directBuffer():
    '''returns ByteBuf\n\n
    directBuffer()\n
    directBuffer(final int initialCapacity)\n
    directBuffer(final int initialCapacity, final int maxCapacity)\n
    '''
def compositeBuffer():
    '''returns CompositeByteBuf\n\n
    compositeBuffer()\n
    compositeBuffer(final int maxNumComponents)\n
    '''
def compositeHeapBuffer():
    '''returns CompositeByteBuf\n\n
    compositeHeapBuffer()\n
    compositeHeapBuffer(final int maxNumComponents)\n
    '''
def compositeDirectBuffer():
    '''returns CompositeByteBuf\n\n
    compositeDirectBuffer()\n
    compositeDirectBuffer(final int maxNumComponents)\n
    '''
def isDirectBufferPooled():
    '''returns boolean\n\n
    isDirectBufferPooled()\n
    '''
def calculateNewCapacity():
    '''returns int\n\n
    calculateNewCapacity(final int minNewCapacity, final int maxCapacity)\n
    '''
