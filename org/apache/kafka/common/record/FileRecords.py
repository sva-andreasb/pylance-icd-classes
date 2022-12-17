def ():
    '''returns TimestampAndOffset\n\n
    (final File file, final FileChannel channel, final int start, final int end, final boolean isSlice)\n
    (final long offset, final int position, final int size)\n
    (final long timestamp, final long offset)\n
    '''
def sizeInBytes():
    '''returns int\n\n
    sizeInBytes()\n
    '''
def file():
    '''returns File\n\n
    file()\n
    '''
def channel():
    '''returns FileChannel\n\n
    channel()\n
    '''
def readInto():
    '''returns ByteBuffer\n\n
    readInto(final ByteBuffer buffer, final int position)\n
    '''
def read():
    '''returns FileRecords\n\n
    read(final int position, final int size)\n
    '''
def append():
    '''returns int\n\n
    append(final MemoryRecords records)\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def closeHandlers():
    '''returns None\n\n
    closeHandlers()\n
    '''
def deleteIfExists():
    '''returns boolean\n\n
    deleteIfExists()\n
    '''
def trim():
    '''returns None\n\n
    trim()\n
    '''
def setFile():
    '''returns None\n\n
    setFile(final File file)\n
    '''
def renameTo():
    '''returns None\n\n
    renameTo(final File f)\n
    '''
def truncateTo():
    '''returns int\n\n
    truncateTo(final int targetSize)\n
    '''
def writeTo():
    '''returns long\n\n
    writeTo(final GatheringByteChannel destChannel, final long offset, final int length)\n
    '''
def searchForOffsetWithSize():
    '''returns LogOffsetPosition\n\n
    searchForOffsetWithSize(final long targetOffset, final int startingPosition)\n
    '''
def searchForTimestamp():
    '''returns TimestampAndOffset\n\n
    searchForTimestamp(final long targetTimestamp, final int startingPosition, final long startingOffset)\n
    '''
def largestTimestampAfter():
    '''returns TimestampAndOffset\n\n
    largestTimestampAfter(final int startingPosition)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    hashCode()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
