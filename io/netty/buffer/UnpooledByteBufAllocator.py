def ():
    '''returns UnpooledByteBufAllocator\n\n
    (final boolean preferDirect)\n
    (final boolean preferDirect, final boolean disableLeakDetector)\n
    (final boolean preferDirect, final boolean disableLeakDetector, final boolean tryNoCleaner)\n
    '''
def compositeHeapBuffer():
    '''returns CompositeByteBuf\n\n
    compositeHeapBuffer(final int maxNumComponents)\n
    '''
def compositeDirectBuffer():
    '''returns CompositeByteBuf\n\n
    compositeDirectBuffer(final int maxNumComponents)\n
    '''
def isDirectBufferPooled():
    '''returns boolean\n\n
    isDirectBufferPooled()\n
    '''
def metric():
    '''returns ByteBufAllocatorMetric\n\n
    metric()\n
    '''
def usedHeapMemory():
    '''returns long\n\n
    usedHeapMemory()\n
    '''
def usedDirectMemory():
    '''returns long\n\n
    usedDirectMemory()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
