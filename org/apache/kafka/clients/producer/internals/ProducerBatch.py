def ():
    '''returns ProducerBatch\n\n
    (final TopicPartition tp, final MemoryRecordsBuilder recordsBuilder, final long now)\n
    (final TopicPartition tp, final MemoryRecordsBuilder recordsBuilder, final long now, final boolean isSplitBatch)\n
    '''
def tryAppend():
    '''returns FutureRecordMetadata\n\n
    tryAppend(final long timestamp, final byte[] key, final byte[] value, final Header[] headers, final Callback callback, final long now)\n
    '''
def abort():
    '''returns None\n\n
    abort(final RuntimeException exception)\n
    '''
def done():
    '''returns boolean\n\n
    done(final long baseOffset, final long logAppendTime, final RuntimeException exception)\n
    '''
def split():
    '''returns Deque<ProducerBatch>\n\n
    split(final int splitBatchSize)\n
    '''
def isCompressed():
    '''returns boolean\n\n
    isCompressed()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def inRetry():
    '''returns boolean\n\n
    inRetry()\n
    '''
def records():
    '''returns MemoryRecords\n\n
    records()\n
    '''
def estimatedSizeInBytes():
    '''returns int\n\n
    estimatedSizeInBytes()\n
    '''
def compressionRatio():
    '''returns double\n\n
    compressionRatio()\n
    '''
def isFull():
    '''returns boolean\n\n
    isFull()\n
    '''
def setProducerState():
    '''returns None\n\n
    setProducerState(final ProducerIdAndEpoch producerIdAndEpoch, final int baseSequence, final boolean isTransactional)\n
    '''
def resetProducerState():
    '''returns None\n\n
    resetProducerState(final ProducerIdAndEpoch producerIdAndEpoch, final int baseSequence, final boolean isTransactional)\n
    '''
def closeForRecordAppends():
    '''returns None\n\n
    closeForRecordAppends()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def abortRecordAppends():
    '''returns None\n\n
    abortRecordAppends()\n
    '''
def isClosed():
    '''returns boolean\n\n
    isClosed()\n
    '''
def buffer():
    '''returns ByteBuffer\n\n
    buffer()\n
    '''
def initialCapacity():
    '''returns int\n\n
    initialCapacity()\n
    '''
def isWritable():
    '''returns boolean\n\n
    isWritable()\n
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
def hasSequence():
    '''returns boolean\n\n
    hasSequence()\n
    '''
def isTransactional():
    '''returns boolean\n\n
    isTransactional()\n
    '''
def sequenceHasBeenReset():
    '''returns boolean\n\n
    sequenceHasBeenReset()\n
    '''
