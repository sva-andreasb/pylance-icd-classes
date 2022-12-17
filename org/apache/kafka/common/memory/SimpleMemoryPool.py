def ():
    '''returns SimpleMemoryPool\n\n
    (final long sizeInBytes, final int maxSingleAllocationBytes, final boolean strict, final Sensor oomPeriodSensor)\n
    '''
def tryAllocate():
    '''returns ByteBuffer\n\n
    tryAllocate(final int sizeBytes)\n
    '''
def release():
    '''returns None\n\n
    release(final ByteBuffer previouslyAllocated)\n
    '''
def size():
    '''returns long\n\n
    size()\n
    '''
def availableMemory():
    '''returns long\n\n
    availableMemory()\n
    '''
def isOutOfMemory():
    '''returns boolean\n\n
    isOutOfMemory()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
