def iterator():
    '''returns Iterator<MutableRecordBatch>\n\n
    iterator()\n
    '''
def sizeInBytes():
    '''returns int\n\n
    sizeInBytes()\n
    '''
def writeTo():
    '''returns long\n\n
    writeTo(final GatheringByteChannel channel, final long position, final int length)\n
    '''
def writeFullyTo():
    '''returns int\n\n
    writeFullyTo(final GatheringByteChannel channel)\n
    '''
def validBytes():
    '''returns int\n\n
    validBytes()\n
    '''
def downConvert():
    '''returns ConvertedRecords<MemoryRecords>\n\n
    downConvert(final byte toMagic, final long firstOffset, final Time time)\n
    '''
def filterTo():
    '''returns FilterResult\n\n
    filterTo(final TopicPartition partition, final RecordFilter filter, final ByteBuffer destinationBuffer, final int maxRecordBatchSize, final BufferSupplier decompressionBufferSupplier)\n
    '''
def buffer():
    '''returns ByteBuffer\n\n
    buffer()\n
    '''
def batches():
    '''returns Iterable<MutableRecordBatch>\n\n
    batches()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def ():
    '''returns FilterResult\n\n
    (final ByteBuffer output, final int messagesRead, final int bytesRead, final int messagesRetained, final int bytesRetained, final long maxOffset, final long maxTimestamp, final long shallowOffsetOfMaxTimestamp)\n
    '''
