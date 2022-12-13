def iterator():
'''public Iterator<MutableRecordBatch> iterator()
'''
pass
def sizeInBytes():
'''public int sizeInBytes()
'''
pass
def writeTo():
'''public long writeTo(final GatheringByteChannel channel, final long position, final int length)
'''
pass
def writeFullyTo():
'''public int writeFullyTo(final GatheringByteChannel channel)
'''
pass
def validBytes():
'''public int validBytes()
'''
pass
def downConvert():
'''public ConvertedRecords<MemoryRecords> downConvert(final byte toMagic, final long firstOffset, final Time time)
'''
pass
def filterTo():
'''public FilterResult filterTo(final TopicPartition partition, final RecordFilter filter, final ByteBuffer destinationBuffer, final int maxRecordBatchSize, final BufferSupplier decompressionBufferSupplier)
'''
pass
def buffer():
'''public ByteBuffer buffer()
'''
pass
def batches():
'''public Iterable<MutableRecordBatch> batches()
'''
pass
def toString():
'''public String toString()
'''
pass
def equals():
'''public boolean equals(final Object o)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def readableRecords():
'''public static MemoryRecords readableRecords(final ByteBuffer buffer)
'''
pass
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
pass
def idempotentBuilder():
'''public static MemoryRecordsBuilder idempotentBuilder(final ByteBuffer buffer, final CompressionType compressionType, final long baseOffset, final long producerId, final short producerEpoch, final int baseSequence)
'''
pass
def withRecords():
'''public static MemoryRecords withRecords(final CompressionType compressionType, final SimpleRecord... records)
public static MemoryRecords withRecords(final CompressionType compressionType, final int partitionLeaderEpoch, final SimpleRecord... records)
public static MemoryRecords withRecords(final byte magic, final CompressionType compressionType, final SimpleRecord... records)
public static MemoryRecords withRecords(final long initialOffset, final CompressionType compressionType, final SimpleRecord... records)
public static MemoryRecords withRecords(final long initialOffset, final CompressionType compressionType, final Integer partitionLeaderEpoch, final SimpleRecord... records)
public static MemoryRecords withRecords(final byte magic, final long initialOffset, final CompressionType compressionType, final TimestampType timestampType, final SimpleRecord... records)
public static MemoryRecords withRecords(final byte magic, final long initialOffset, final CompressionType compressionType, final TimestampType timestampType, final long producerId, final short producerEpoch, final int baseSequence, final int partitionLeaderEpoch, final boolean isTransactional, final SimpleRecord... records)
'''
pass
def withIdempotentRecords():
'''public static MemoryRecords withIdempotentRecords(final CompressionType compressionType, final long producerId, final short producerEpoch, final int baseSequence, final SimpleRecord... records)
public static MemoryRecords withIdempotentRecords(final byte magic, final long initialOffset, final CompressionType compressionType, final long producerId, final short producerEpoch, final int baseSequence, final int partitionLeaderEpoch, final SimpleRecord... records)
public static MemoryRecords withIdempotentRecords(final long initialOffset, final CompressionType compressionType, final long producerId, final short producerEpoch, final int baseSequence, final int partitionLeaderEpoch, final SimpleRecord... records)
'''
pass
def withTransactionalRecords():
'''public static MemoryRecords withTransactionalRecords(final CompressionType compressionType, final long producerId, final short producerEpoch, final int baseSequence, final SimpleRecord... records)
public static MemoryRecords withTransactionalRecords(final byte magic, final long initialOffset, final CompressionType compressionType, final long producerId, final short producerEpoch, final int baseSequence, final int partitionLeaderEpoch, final SimpleRecord... records)
public static MemoryRecords withTransactionalRecords(final long initialOffset, final CompressionType compressionType, final long producerId, final short producerEpoch, final int baseSequence, final int partitionLeaderEpoch, final SimpleRecord... records)
'''
pass
def withEndTransactionMarker():
'''public static MemoryRecords withEndTransactionMarker(final long producerId, final short producerEpoch, final EndTransactionMarker marker)
public static MemoryRecords withEndTransactionMarker(final long timestamp, final long producerId, final short producerEpoch, final EndTransactionMarker marker)
public static MemoryRecords withEndTransactionMarker(final long initialOffset, final long timestamp, final int partitionLeaderEpoch, final long producerId, final short producerEpoch, final EndTransactionMarker marker)
'''
pass
def writeEndTransactionalMarker():
'''public static void writeEndTransactionalMarker(final ByteBuffer buffer, final long initialOffset, final long timestamp, final int partitionLeaderEpoch, final long producerId, final short producerEpoch, final EndTransactionMarker marker)
'''
pass
def FilterResult():
'''public FilterResult(final ByteBuffer output, final int messagesRead, final int bytesRead, final int messagesRetained, final int bytesRetained, final long maxOffset, final long maxTimestamp, final long shallowOffsetOfMaxTimestamp)
'''
pass
