def iterator():
    '''public Iterator<MutableRecordBatch> iterator()
    '''
def sizeInBytes():
    '''public int sizeInBytes()
    '''
def writeTo():
    '''public long writeTo(final GatheringByteChannel channel, final long position, final int length)
    '''
def writeFullyTo():
    '''public int writeFullyTo(final GatheringByteChannel channel)
    '''
def validBytes():
    '''public int validBytes()
    '''
def downConvert():
    '''public ConvertedRecords<MemoryRecords> downConvert(final byte toMagic, final long firstOffset, final Time time)
    '''
def filterTo():
    '''public FilterResult filterTo(final TopicPartition partition, final RecordFilter filter, final ByteBuffer destinationBuffer, final int maxRecordBatchSize, final BufferSupplier decompressionBufferSupplier)
    '''
def buffer():
    '''public ByteBuffer buffer()
    '''
def batches():
    '''public Iterable<MutableRecordBatch> batches()
    '''
def toString():
    '''public String toString()
    '''
def equals():
    '''public boolean equals(final Object o)
    '''
def hashCode():
    '''public int hashCode()
    '''
def readableRecords():
    '''public static MemoryRecords readableRecords(final ByteBuffer buffer)
    '''
def builder():
    '''public static MemoryRecordsBuilder builder(final ByteBuffer buffer, final CompressionType compressionType, final TimestampType timestampType, final long baseOffset)
    public static MemoryRecordsBuilder builder(final ByteBuffer buffer, final byte magic, final CompressionType compressionType, final TimestampType timestampType, final long baseOffset, final long logAppendTime)
    public static MemoryRecordsBuilder builder(final ByteBuffer buffer, final byte magic, final CompressionType compressionType, final TimestampType timestampType, final long baseOffset)
    public static MemoryRecordsBuilder builder(final ByteBuffer buffer, final byte magic, final CompressionType compressionType, final TimestampType timestampType, final long baseOffset, final long logAppendTime, final int partitionLeaderEpoch)
    public static MemoryRecordsBuilder builder(final ByteBuffer buffer, final CompressionType compressionType, final long baseOffset, final long producerId, final short producerEpoch, final int baseSequence, final boolean isTransactional)
    public static MemoryRecordsBuilder builder(final ByteBuffer buffer, final byte magic, final CompressionType compressionType, final TimestampType timestampType, final long baseOffset, final long logAppendTime, final long producerId, final short producerEpoch, final int baseSequence)
    public static MemoryRecordsBuilder builder(final ByteBuffer buffer, final byte magic, final CompressionType compressionType, final TimestampType timestampType, final long baseOffset, final long logAppendTime, final long producerId, final short producerEpoch, final int baseSequence, final boolean isTransactional, final int partitionLeaderEpoch)
    public static MemoryRecordsBuilder builder(final ByteBuffer buffer, final byte magic, final CompressionType compressionType, final TimestampType timestampType, final long baseOffset, final long logAppendTime, final long producerId, final short producerEpoch, final int baseSequence, final boolean isTransactional, final boolean isControlBatch, final int partitionLeaderEpoch)
    '''
def idempotentBuilder():
    '''public static MemoryRecordsBuilder idempotentBuilder(final ByteBuffer buffer, final CompressionType compressionType, final long baseOffset, final long producerId, final short producerEpoch, final int baseSequence)
    '''
def withRecords():
    '''public static MemoryRecords withRecords(final CompressionType compressionType, final SimpleRecord... records)
    public static MemoryRecords withRecords(final CompressionType compressionType, final int partitionLeaderEpoch, final SimpleRecord... records)
    public static MemoryRecords withRecords(final byte magic, final CompressionType compressionType, final SimpleRecord... records)
    public static MemoryRecords withRecords(final long initialOffset, final CompressionType compressionType, final SimpleRecord... records)
    public static MemoryRecords withRecords(final long initialOffset, final CompressionType compressionType, final Integer partitionLeaderEpoch, final SimpleRecord... records)
    public static MemoryRecords withRecords(final byte magic, final long initialOffset, final CompressionType compressionType, final TimestampType timestampType, final SimpleRecord... records)
    public static MemoryRecords withRecords(final byte magic, final long initialOffset, final CompressionType compressionType, final TimestampType timestampType, final long producerId, final short producerEpoch, final int baseSequence, final int partitionLeaderEpoch, final boolean isTransactional, final SimpleRecord... records)
    '''
def withIdempotentRecords():
    '''public static MemoryRecords withIdempotentRecords(final CompressionType compressionType, final long producerId, final short producerEpoch, final int baseSequence, final SimpleRecord... records)
    public static MemoryRecords withIdempotentRecords(final byte magic, final long initialOffset, final CompressionType compressionType, final long producerId, final short producerEpoch, final int baseSequence, final int partitionLeaderEpoch, final SimpleRecord... records)
    public static MemoryRecords withIdempotentRecords(final long initialOffset, final CompressionType compressionType, final long producerId, final short producerEpoch, final int baseSequence, final int partitionLeaderEpoch, final SimpleRecord... records)
    '''
def withTransactionalRecords():
    '''public static MemoryRecords withTransactionalRecords(final CompressionType compressionType, final long producerId, final short producerEpoch, final int baseSequence, final SimpleRecord... records)
    public static MemoryRecords withTransactionalRecords(final byte magic, final long initialOffset, final CompressionType compressionType, final long producerId, final short producerEpoch, final int baseSequence, final int partitionLeaderEpoch, final SimpleRecord... records)
    public static MemoryRecords withTransactionalRecords(final long initialOffset, final CompressionType compressionType, final long producerId, final short producerEpoch, final int baseSequence, final int partitionLeaderEpoch, final SimpleRecord... records)
    '''
def withEndTransactionMarker():
    '''public static MemoryRecords withEndTransactionMarker(final long producerId, final short producerEpoch, final EndTransactionMarker marker)
    public static MemoryRecords withEndTransactionMarker(final long timestamp, final long producerId, final short producerEpoch, final EndTransactionMarker marker)
    public static MemoryRecords withEndTransactionMarker(final long initialOffset, final long timestamp, final int partitionLeaderEpoch, final long producerId, final short producerEpoch, final EndTransactionMarker marker)
    '''
def writeEndTransactionalMarker():
    '''public static void writeEndTransactionalMarker(final ByteBuffer buffer, final long initialOffset, final long timestamp, final int partitionLeaderEpoch, final long producerId, final short producerEpoch, final EndTransactionMarker marker)
    '''
def FilterResult():
    '''public FilterResult(final ByteBuffer output, final int messagesRead, final int bytesRead, final int messagesRetained, final int bytesRetained, final long maxOffset, final long maxTimestamp, final long shallowOffsetOfMaxTimestamp)
    '''
