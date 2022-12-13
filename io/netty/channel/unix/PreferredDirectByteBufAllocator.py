def updateAllocator():
'''public void updateAllocator(final ByteBufAllocator allocator)
'''
pass
def buffer():
'''public ByteBuf buffer()
public ByteBuf buffer(final int initialCapacity)
public ByteBuf buffer(final int initialCapacity, final int maxCapacity)
'''
pass
def ioBuffer():
'''public ByteBuf ioBuffer()
public ByteBuf ioBuffer(final int initialCapacity)
public ByteBuf ioBuffer(final int initialCapacity, final int maxCapacity)
'''
pass
def heapBuffer():
'''public ByteBuf heapBuffer()
public ByteBuf heapBuffer(final int initialCapacity)
public ByteBuf heapBuffer(final int initialCapacity, final int maxCapacity)
'''
pass
def directBuffer():
'''public ByteBuf directBuffer()
public ByteBuf directBuffer(final int initialCapacity)
public ByteBuf directBuffer(final int initialCapacity, final int maxCapacity)
'''
pass
def compositeBuffer():
'''public CompositeByteBuf compositeBuffer()
public CompositeByteBuf compositeBuffer(final int maxNumComponents)
'''
pass
def compositeHeapBuffer():
'''public CompositeByteBuf compositeHeapBuffer()
public CompositeByteBuf compositeHeapBuffer(final int maxNumComponents)
'''
pass
def compositeDirectBuffer():
'''public CompositeByteBuf compositeDirectBuffer()
public CompositeByteBuf compositeDirectBuffer(final int maxNumComponents)
'''
pass
def isDirectBufferPooled():
'''public boolean isDirectBufferPooled()
'''
pass
def calculateNewCapacity():
'''public int calculateNewCapacity(final int minNewCapacity, final int maxCapacity)
'''
pass
