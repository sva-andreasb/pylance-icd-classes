def lastOffset():
    '''returns long\n\n
    lastOffset()\n
    lastOffset()\n
    '''
def isValid():
    '''returns boolean\n\n
    isValid()\n
    '''
def ensureValid():
    '''returns None\n\n
    ensureValid()\n
    '''
def keySize():
    '''returns int\n\n
    keySize()\n
    '''
def hasKey():
    '''returns boolean\n\n
    hasKey()\n
    '''
def key():
    '''returns ByteBuffer\n\n
    key()\n
    '''
def valueSize():
    '''returns int\n\n
    valueSize()\n
    '''
def hasValue():
    '''returns boolean\n\n
    hasValue()\n
    '''
def value():
    '''returns ByteBuffer\n\n
    value()\n
    '''
def headers():
    '''returns Header[]\n\n
    headers()\n
    '''
def hasMagic():
    '''returns boolean\n\n
    hasMagic(final byte magic)\n
    '''
def hasTimestampType():
    '''returns boolean\n\n
    hasTimestampType(final TimestampType timestampType)\n
    '''
def checksumOrNull():
    '''returns Long\n\n
    checksumOrNull()\n
    '''
def checksum():
    '''returns long\n\n
    checksum()\n
    '''
def maxTimestamp():
    '''returns long\n\n
    maxTimestamp()\n
    '''
def timestamp():
    '''returns long\n\n
    timestamp()\n
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
def magic():
    '''returns byte\n\n
    magic()\n
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
def toString():
    '''returns String\n\n
    toString()\n
    '''
def writeTo():
    '''returns None\n\n
    writeTo(final ByteBuffer buffer)\n
    writeTo(final ByteBufferOutputStream outputStream)\n
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
def hasProducerId():
    '''returns boolean\n\n
    hasProducerId()\n
    '''
def sequence():
    '''returns int\n\n
    sequence()\n
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
def isTransactional():
    '''returns boolean\n\n
    isTransactional()\n
    isTransactional()\n
    '''
def partitionLeaderEpoch():
    '''returns int\n\n
    partitionLeaderEpoch()\n
    partitionLeaderEpoch()\n
    '''
def isControlBatch():
    '''returns boolean\n\n
    isControlBatch()\n
    isControlBatch()\n
    '''
def iterator():
    '''returns Iterator<Record>\n\n
    iterator()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    close()\n
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
def streamingIterator():
    '''returns CloseableIterator<Record>\n\n
    streamingIterator(final BufferSupplier bufferSupplier)\n
    '''
def nextBatch():
    '''returns AbstractLegacyRecordBatch\n\n
    nextBatch()\n
    '''
def offset():
    '''returns long\n\n
    offset()\n
    offset()\n
    '''
def outerRecord():
    '''returns LegacyRecord\n\n
    outerRecord()\n
    outerRecord()\n
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
def setLastOffset():
    '''returns None\n\n
    setLastOffset(final long offset)\n
    '''
def setMaxTimestamp():
    '''returns None\n\n
    setMaxTimestamp(final TimestampType timestampType, final long timestamp)\n
    '''
def setPartitionLeaderEpoch():
    '''returns None\n\n
    setPartitionLeaderEpoch(final int epoch)\n
    '''
