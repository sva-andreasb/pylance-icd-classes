def ():
    '''returns BufferPool\n\n
    (final long memory, final int poolableSize, final Metrics metrics, final Time time, final String metricGrpName)\n
    '''
def allocate():
    '''returns ByteBuffer\n\n
    allocate(final int size, final long maxTimeToBlockMs)\n
    '''
def deallocate():
    '''returns None\n\n
    deallocate(final ByteBuffer buffer, final int size)\n
    deallocate(final ByteBuffer buffer)\n
    '''
def availableMemory():
    '''returns long\n\n
    availableMemory()\n
    '''
def unallocatedMemory():
    '''returns long\n\n
    unallocatedMemory()\n
    '''
def queued():
    '''returns int\n\n
    queued()\n
    '''
def poolableSize():
    '''returns int\n\n
    poolableSize()\n
    '''
def totalMemory():
    '''returns long\n\n
    totalMemory()\n
    '''
