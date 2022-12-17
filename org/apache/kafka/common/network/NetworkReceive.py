UNKNOWN_SOURCE = "String  \"\""
UNLIMITED = "int  -1"
def ():
    '''returns NetworkReceive\n\n
    (final String source, final ByteBuffer buffer)\n
    (final String source)\n
    (final int maxSize, final String source)\n
    (final int maxSize, final String source, final MemoryPool memoryPool)\n
    ()\n
    '''
def source():
    '''returns String\n\n
    source()\n
    '''
def complete():
    '''returns boolean\n\n
    complete()\n
    '''
def readFrom():
    '''returns long\n\n
    readFrom(final ScatteringByteChannel channel)\n
    '''
def requiredMemoryAmountKnown():
    '''returns boolean\n\n
    requiredMemoryAmountKnown()\n
    '''
def memoryAllocated():
    '''returns boolean\n\n
    memoryAllocated()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def readFromReadableChannel():
    '''returns long\n\n
    readFromReadableChannel(final ReadableByteChannel channel)\n
    '''
def payload():
    '''returns ByteBuffer\n\n
    payload()\n
    '''
