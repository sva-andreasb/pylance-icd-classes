LAST_OFFSET_DELTA_OFFSET = "int  23"
RECORDS_COUNT_OFFSET = "int  57"
RECORD_BATCH_OVERHEAD = "int  61"
def magic():
    '''returns byte\n\n
    magic()\n
    '''
def ensureValid():
    '''returns None\n\n
    ensureValid()\n
    '''
def firstTimestamp():
    '''returns long\n\n
    firstTimestamp()\n
    '''
def maxTimestamp():
    '''returns long\n\n
    maxTimestamp()\n
    '''
def timestampType():
    '''returns TimestampType\n\n
    timestampType()\n
    '''
def baseOffset():
    '''returns long\n\n
    baseOffset()\n
    baseOffset()\n
    '''
def lastOffset():
    '''returns long\n\n
    lastOffset()\n
    lastOffset()\n
    '''
def producerId():
    '''returns long\n\n
    producerId()\n
    producerId()\n
    '''
def producerEpoch():
    '''returns short\n\n
    producerEpoch()\n
    producerEpoch()\n
    '''
def baseSequence():
    '''returns int\n\n
    baseSequence()\n
    baseSequence()\n
    '''
def lastSequence():
    '''returns int\n\n
    lastSequence()\n
    lastSequence()\n
    '''
def compressionType():
    '''returns CompressionType\n\n
    compressionType()\n
    '''
def sizeInBytes():
    '''returns int\n\n
    sizeInBytes()\n
    '''
def countOrNull():
    '''returns Integer\n\n
    countOrNull()\n
    countOrNull()\n
    '''
def writeTo():
    '''returns None\n\n
    writeTo(final ByteBuffer buffer)\n
    writeTo(final ByteBufferOutputStream outputStream)\n
    '''
def isTransactional():
    '''returns boolean\n\n
    isTransactional()\n
    isTransactional()\n
    '''
def isControlBatch():
    '''returns boolean\n\n
    isControlBatch()\n
    isControlBatch()\n
    '''
def partitionLeaderEpoch():
    '''returns int\n\n
    partitionLeaderEpoch()\n
    partitionLeaderEpoch()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    close()\n
    '''
def iterator():
    '''returns Iterator<Record>\n\n
    iterator()\n
    '''
def streamingIterator():
    '''returns CloseableIterator<Record>\n\n
    streamingIterator(final BufferSupplier bufferSupplier)\n
    '''
def setLastOffset():
    '''returns None\n\n
    setLastOffset(final long offset)\n
    '''
def setMaxTimestamp():
    '''returns None\n\n
    setMaxTimestamp(final TimestampType timestampType, final long maxTimestamp)\n
    '''
def setPartitionLeaderEpoch():
    '''returns None\n\n
    setPartitionLeaderEpoch(final int epoch)\n
    '''
def checksum():
    '''returns long\n\n
    checksum()\n
    checksum()\n
    '''
def isValid():
    '''returns boolean\n\n
    isValid()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def ():
    '''returns RecordIterator\n\n
    ()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns Record\n\n
    next()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
