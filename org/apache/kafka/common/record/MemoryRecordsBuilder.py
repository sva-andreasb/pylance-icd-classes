def ():
    '''returns RecordsInfo\n\n
    (final ByteBufferOutputStream bufferStream, final byte magic, final CompressionType compressionType, final TimestampType timestampType, final long baseOffset, final long logAppendTime, final long producerId, final short producerEpoch, final int baseSequence, final boolean isTransactional, final boolean isControlBatch, final int partitionLeaderEpoch, final int writeLimit)\n
    (final ByteBuffer buffer, final byte magic, final CompressionType compressionType, final TimestampType timestampType, final long baseOffset, final long logAppendTime, final long producerId, final short producerEpoch, final int baseSequence, final boolean isTransactional, final boolean isControlBatch, final int partitionLeaderEpoch, final int writeLimit)\n
    (final long maxTimestamp, final long shallowOffsetOfMaxTimestamp)\n
    '''
def buffer():
    '''returns ByteBuffer\n\n
    buffer()\n
    '''
def initialCapacity():
    '''returns int\n\n
    initialCapacity()\n
    '''
def compressionRatio():
    '''returns double\n\n
    compressionRatio()\n
    '''
def compressionType():
    '''returns CompressionType\n\n
    compressionType()\n
    '''
def isControlBatch():
    '''returns boolean\n\n
    isControlBatch()\n
    '''
def isTransactional():
    '''returns boolean\n\n
    isTransactional()\n
    '''
def build():
    '''returns MemoryRecords\n\n
    build()\n
    '''
def info():
    '''returns RecordsInfo\n\n
    info()\n
    '''
def numRecords():
    '''returns int\n\n
    numRecords()\n
    '''
def uncompressedBytesWritten():
    '''returns int\n\n
    uncompressedBytesWritten()\n
    '''
def setProducerState():
    '''returns None\n\n
    setProducerState(final long producerId, final short producerEpoch, final int baseSequence, final boolean isTransactional)\n
    '''
def overrideLastOffset():
    '''returns None\n\n
    overrideLastOffset(final long lastOffset)\n
    '''
def closeForRecordAppends():
    '''returns None\n\n
    closeForRecordAppends()\n
    '''
def abort():
    '''returns None\n\n
    abort()\n
    '''
def reopenAndRewriteProducerState():
    '''returns None\n\n
    reopenAndRewriteProducerState(final long producerId, final short producerEpoch, final int baseSequence, final boolean isTransactional)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def appendWithOffset():
    '''returns None\n\n
    appendWithOffset(final long offset, final long timestamp, final byte[] key, final byte[] value, final Header[] headers)\n
    appendWithOffset(final long offset, final long timestamp, final ByteBuffer key, final ByteBuffer value, final Header[] headers)\n
    appendWithOffset(final long offset, final long timestamp, final byte[] key, final byte[] value)\n
    appendWithOffset(final long offset, final long timestamp, final ByteBuffer key, final ByteBuffer value)\n
    appendWithOffset(final long offset, final SimpleRecord record)\n
    appendWithOffset(final long offset, final Record record)\n
    appendWithOffset(final long offset, final LegacyRecord record)\n
    '''
def append():
    '''returns None\n\n
    append(final long timestamp, final ByteBuffer key, final ByteBuffer value)\n
    append(final long timestamp, final ByteBuffer key, final ByteBuffer value, final Header[] headers)\n
    append(final long timestamp, final byte[] key, final byte[] value)\n
    append(final long timestamp, final byte[] key, final byte[] value, final Header[] headers)\n
    append(final SimpleRecord record)\n
    append(final Record record)\n
    append(final LegacyRecord record)\n
    '''
def appendEndTxnMarker():
    '''returns Long\n\n
    appendEndTxnMarker(final long timestamp, final EndTransactionMarker marker)\n
    '''
def appendUncheckedWithOffset():
    '''returns None\n\n
    appendUncheckedWithOffset(final long offset, final LegacyRecord record)\n
    '''
def setEstimatedCompressionRatio():
    '''returns None\n\n
    setEstimatedCompressionRatio(final float estimatedCompressionRatio)\n
    '''
def hasRoomFor():
    '''returns boolean\n\n
    hasRoomFor(final long timestamp, final byte[] key, final byte[] value, final Header[] headers)\n
    hasRoomFor(final long timestamp, final ByteBuffer key, final ByteBuffer value, final Header[] headers)\n
    '''
def isClosed():
    '''returns boolean\n\n
    isClosed()\n
    '''
def isFull():
    '''returns boolean\n\n
    isFull()\n
    '''
def estimatedSizeInBytes():
    '''returns int\n\n
    estimatedSizeInBytes()\n
    '''
def magic():
    '''returns byte\n\n
    magic()\n
    '''
def producerId():
    '''returns long\n\n
    producerId()\n
    '''
def producerEpoch():
    '''returns short\n\n
    producerEpoch()\n
    '''
def baseSequence():
    '''returns int\n\n
    baseSequence()\n
    '''
def write():
    '''returns None\n\n
    write(final int b)\n
    '''
