LAST_OFFSET_DELTA_OFFSET = "int  23"
RECORDS_COUNT_OFFSET = "int  57"
RECORD_BATCH_OVERHEAD = "int  61"
def magic():
    '''public byte magic()
    '''
def ensureValid():
    '''public void ensureValid()
    '''
def firstTimestamp():
    '''public long firstTimestamp()
    '''
def maxTimestamp():
    '''public long maxTimestamp()
    '''
def timestampType():
    '''public TimestampType timestampType()
    '''
def baseOffset():
    '''public long baseOffset()
    public long baseOffset()
    '''
def lastOffset():
    '''public long lastOffset()
    public long lastOffset()
    '''
def producerId():
    '''public long producerId()
    public long producerId()
    '''
def producerEpoch():
    '''public short producerEpoch()
    public short producerEpoch()
    '''
def baseSequence():
    '''public int baseSequence()
    public int baseSequence()
    '''
def lastSequence():
    '''public int lastSequence()
    public int lastSequence()
    '''
def compressionType():
    '''public CompressionType compressionType()
    '''
def sizeInBytes():
    '''public int sizeInBytes()
    public static int sizeInBytes(final long baseOffset, final Iterable<Record> records)
    public static int sizeInBytes(final Iterable<SimpleRecord> records)
    '''
def countOrNull():
    '''public Integer countOrNull()
    public Integer countOrNull()
    '''
def writeTo():
    '''public void writeTo(final ByteBuffer buffer)
    public void writeTo(final ByteBufferOutputStream outputStream)
    '''
def isTransactional():
    '''public boolean isTransactional()
    public boolean isTransactional()
    '''
def isControlBatch():
    '''public boolean isControlBatch()
    public boolean isControlBatch()
    '''
def partitionLeaderEpoch():
    '''public int partitionLeaderEpoch()
    public int partitionLeaderEpoch()
    '''
def close():
    '''public void close()
    public void close()
    '''
def iterator():
    '''public Iterator<Record> iterator()
    '''
def streamingIterator():
    '''public CloseableIterator<Record> streamingIterator(final BufferSupplier bufferSupplier)
    '''
def setLastOffset():
    '''public void setLastOffset(final long offset)
    '''
def setMaxTimestamp():
    '''public void setMaxTimestamp(final TimestampType timestampType, final long maxTimestamp)
    '''
def setPartitionLeaderEpoch():
    '''public void setPartitionLeaderEpoch(final int epoch)
    '''
def checksum():
    '''public long checksum()
    public long checksum()
    '''
def isValid():
    '''public boolean isValid()
    '''
def equals():
    '''public boolean equals(final Object o)
    '''
def hashCode():
    '''public int hashCode()
    '''
def writeEmptyHeader():
    '''public static void writeEmptyHeader(final ByteBuffer buffer, final byte magic, final long producerId, final short producerEpoch, final int baseSequence, final long baseOffset, final long lastOffset, final int partitionLeaderEpoch, final TimestampType timestampType, final long timestamp, final boolean isTransactional, final boolean isControlRecord)
    '''
def toString():
    '''public String toString()
    '''
def RecordIterator():
    '''public RecordIterator()
    '''
def hasNext():
    '''public boolean hasNext()
    '''
def next():
    '''public Record next()
    '''
def remove():
    '''public void remove()
    '''
