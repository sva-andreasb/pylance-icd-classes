def MemoryRecordsBuilder():
    '''public MemoryRecordsBuilder(final ByteBufferOutputStream bufferStream, final byte magic, final CompressionType compressionType, final TimestampType timestampType, final long baseOffset, final long logAppendTime, final long producerId, final short producerEpoch, final int baseSequence, final boolean isTransactional, final boolean isControlBatch, final int partitionLeaderEpoch, final int writeLimit)
    public MemoryRecordsBuilder(final ByteBuffer buffer, final byte magic, final CompressionType compressionType, final TimestampType timestampType, final long baseOffset, final long logAppendTime, final long producerId, final short producerEpoch, final int baseSequence, final boolean isTransactional, final boolean isControlBatch, final int partitionLeaderEpoch, final int writeLimit)
    '''
def buffer():
    '''public ByteBuffer buffer()
    '''
def initialCapacity():
    '''public int initialCapacity()
    '''
def compressionRatio():
    '''public double compressionRatio()
    '''
def compressionType():
    '''public CompressionType compressionType()
    '''
def isControlBatch():
    '''public boolean isControlBatch()
    '''
def isTransactional():
    '''public boolean isTransactional()
    '''
def build():
    '''public MemoryRecords build()
    '''
def info():
    '''public RecordsInfo info()
    '''
def numRecords():
    '''public int numRecords()
    '''
def uncompressedBytesWritten():
    '''public int uncompressedBytesWritten()
    '''
def setProducerState():
    '''public void setProducerState(final long producerId, final short producerEpoch, final int baseSequence, final boolean isTransactional)
    '''
def overrideLastOffset():
    '''public void overrideLastOffset(final long lastOffset)
    '''
def closeForRecordAppends():
    '''public void closeForRecordAppends()
    '''
def abort():
    '''public void abort()
    '''
def reopenAndRewriteProducerState():
    '''public void reopenAndRewriteProducerState(final long producerId, final short producerEpoch, final int baseSequence, final boolean isTransactional)
    '''
def close():
    '''public void close()
    '''
def appendWithOffset():
    '''public Long appendWithOffset(final long offset, final long timestamp, final byte[] key, final byte[] value, final Header[] headers)
    public Long appendWithOffset(final long offset, final long timestamp, final ByteBuffer key, final ByteBuffer value, final Header[] headers)
    public Long appendWithOffset(final long offset, final long timestamp, final byte[] key, final byte[] value)
    public Long appendWithOffset(final long offset, final long timestamp, final ByteBuffer key, final ByteBuffer value)
    public Long appendWithOffset(final long offset, final SimpleRecord record)
    public void appendWithOffset(final long offset, final Record record)
    public void appendWithOffset(final long offset, final LegacyRecord record)
    '''
def append():
    '''public Long append(final long timestamp, final ByteBuffer key, final ByteBuffer value)
    public Long append(final long timestamp, final ByteBuffer key, final ByteBuffer value, final Header[] headers)
    public Long append(final long timestamp, final byte[] key, final byte[] value)
    public Long append(final long timestamp, final byte[] key, final byte[] value, final Header[] headers)
    public Long append(final SimpleRecord record)
    public void append(final Record record)
    public void append(final LegacyRecord record)
    '''
def appendEndTxnMarker():
    '''public Long appendEndTxnMarker(final long timestamp, final EndTransactionMarker marker)
    '''
def appendUncheckedWithOffset():
    '''public void appendUncheckedWithOffset(final long offset, final LegacyRecord record)
    '''
def setEstimatedCompressionRatio():
    '''public void setEstimatedCompressionRatio(final float estimatedCompressionRatio)
    '''
def hasRoomFor():
    '''public boolean hasRoomFor(final long timestamp, final byte[] key, final byte[] value, final Header[] headers)
    public boolean hasRoomFor(final long timestamp, final ByteBuffer key, final ByteBuffer value, final Header[] headers)
    '''
def isClosed():
    '''public boolean isClosed()
    '''
def isFull():
    '''public boolean isFull()
    '''
def estimatedSizeInBytes():
    '''public int estimatedSizeInBytes()
    '''
def magic():
    '''public byte magic()
    '''
def producerId():
    '''public long producerId()
    '''
def producerEpoch():
    '''public short producerEpoch()
    '''
def baseSequence():
    '''public int baseSequence()
    '''
def write():
    '''public void write(final int b)
    '''
def RecordsInfo():
    '''public RecordsInfo(final long maxTimestamp, final long shallowOffsetOfMaxTimestamp)
    '''
