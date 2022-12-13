def MemoryRecordsBuilder():
'''public MemoryRecordsBuilder(final ByteBufferOutputStream bufferStream, final byte magic, final CompressionType compressionType, final TimestampType timestampType, final long baseOffset, final long logAppendTime, final long producerId, final short producerEpoch, final int baseSequence, final boolean isTransactional, final boolean isControlBatch, final int partitionLeaderEpoch, final int writeLimit)
public MemoryRecordsBuilder(final ByteBuffer buffer, final byte magic, final CompressionType compressionType, final TimestampType timestampType, final long baseOffset, final long logAppendTime, final long producerId, final short producerEpoch, final int baseSequence, final boolean isTransactional, final boolean isControlBatch, final int partitionLeaderEpoch, final int writeLimit)
'''
pass
def buffer():
'''public ByteBuffer buffer()
'''
pass
def initialCapacity():
'''public int initialCapacity()
'''
pass
def compressionRatio():
'''public double compressionRatio()
'''
pass
def compressionType():
'''public CompressionType compressionType()
'''
pass
def isControlBatch():
'''public boolean isControlBatch()
'''
pass
def isTransactional():
'''public boolean isTransactional()
'''
pass
def build():
'''public MemoryRecords build()
'''
pass
def info():
'''public RecordsInfo info()
'''
pass
def numRecords():
'''public int numRecords()
'''
pass
def uncompressedBytesWritten():
'''public int uncompressedBytesWritten()
'''
pass
def setProducerState():
'''public void setProducerState(final long producerId, final short producerEpoch, final int baseSequence, final boolean isTransactional)
'''
pass
def overrideLastOffset():
'''public void overrideLastOffset(final long lastOffset)
'''
pass
def closeForRecordAppends():
'''public void closeForRecordAppends()
'''
pass
def abort():
'''public void abort()
'''
pass
def reopenAndRewriteProducerState():
'''public void reopenAndRewriteProducerState(final long producerId, final short producerEpoch, final int baseSequence, final boolean isTransactional)
'''
pass
def close():
'''public void close()
'''
pass
def appendWithOffset():
'''public Long appendWithOffset(final long offset, final long timestamp, final byte[] key, final byte[] value, final Header[] headers)
public Long appendWithOffset(final long offset, final long timestamp, final ByteBuffer key, final ByteBuffer value, final Header[] headers)
public Long appendWithOffset(final long offset, final long timestamp, final byte[] key, final byte[] value)
public Long appendWithOffset(final long offset, final long timestamp, final ByteBuffer key, final ByteBuffer value)
public Long appendWithOffset(final long offset, final SimpleRecord record)
public void appendWithOffset(final long offset, final Record record)
public void appendWithOffset(final long offset, final LegacyRecord record)
'''
pass
def append():
'''public Long append(final long timestamp, final ByteBuffer key, final ByteBuffer value)
public Long append(final long timestamp, final ByteBuffer key, final ByteBuffer value, final Header[] headers)
public Long append(final long timestamp, final byte[] key, final byte[] value)
public Long append(final long timestamp, final byte[] key, final byte[] value, final Header[] headers)
public Long append(final SimpleRecord record)
public void append(final Record record)
public void append(final LegacyRecord record)
'''
pass
def appendEndTxnMarker():
'''public Long appendEndTxnMarker(final long timestamp, final EndTransactionMarker marker)
'''
pass
def appendUncheckedWithOffset():
'''public void appendUncheckedWithOffset(final long offset, final LegacyRecord record)
'''
pass
def setEstimatedCompressionRatio():
'''public void setEstimatedCompressionRatio(final float estimatedCompressionRatio)
'''
pass
def hasRoomFor():
'''public boolean hasRoomFor(final long timestamp, final byte[] key, final byte[] value, final Header[] headers)
public boolean hasRoomFor(final long timestamp, final ByteBuffer key, final ByteBuffer value, final Header[] headers)
'''
pass
def isClosed():
'''public boolean isClosed()
'''
pass
def isFull():
'''public boolean isFull()
'''
pass
def estimatedSizeInBytes():
'''public int estimatedSizeInBytes()
'''
pass
def magic():
'''public byte magic()
'''
pass
def producerId():
'''public long producerId()
'''
pass
def producerEpoch():
'''public short producerEpoch()
'''
pass
def baseSequence():
'''public int baseSequence()
'''
pass
def write():
'''public void write(final int b)
'''
pass
def RecordsInfo():
'''public RecordsInfo(final long maxTimestamp, final long shallowOffsetOfMaxTimestamp)
'''
pass
