LAST_OFFSET_DELTA_OFFSET = "int  23"
RECORDS_COUNT_OFFSET = "int  57"
RECORD_BATCH_OVERHEAD = "int  61"
def magic():
'''public byte magic()
'''
pass
def ensureValid():
'''public void ensureValid()
'''
pass
def firstTimestamp():
'''public long firstTimestamp()
'''
pass
def maxTimestamp():
'''public long maxTimestamp()
'''
pass
def timestampType():
'''public TimestampType timestampType()
'''
pass
def baseOffset():
'''public long baseOffset()
public long baseOffset()
'''
pass
def lastOffset():
'''public long lastOffset()
public long lastOffset()
'''
pass
def producerId():
'''public long producerId()
public long producerId()
'''
pass
def producerEpoch():
'''public short producerEpoch()
public short producerEpoch()
'''
pass
def baseSequence():
'''public int baseSequence()
public int baseSequence()
'''
pass
def lastSequence():
'''public int lastSequence()
public int lastSequence()
'''
pass
def compressionType():
'''public CompressionType compressionType()
'''
pass
def sizeInBytes():
'''public int sizeInBytes()
public static int sizeInBytes(final long baseOffset, final Iterable<Record> records)
public static int sizeInBytes(final Iterable<SimpleRecord> records)
'''
pass
def countOrNull():
'''public Integer countOrNull()
public Integer countOrNull()
'''
pass
def writeTo():
'''public void writeTo(final ByteBuffer buffer)
public void writeTo(final ByteBufferOutputStream outputStream)
'''
pass
def isTransactional():
'''public boolean isTransactional()
public boolean isTransactional()
'''
pass
def isControlBatch():
'''public boolean isControlBatch()
public boolean isControlBatch()
'''
pass
def partitionLeaderEpoch():
'''public int partitionLeaderEpoch()
public int partitionLeaderEpoch()
'''
pass
def close():
'''public void close()
public void close()
'''
pass
def iterator():
'''public Iterator<Record> iterator()
'''
pass
def streamingIterator():
'''public CloseableIterator<Record> streamingIterator(final BufferSupplier bufferSupplier)
'''
pass
def setLastOffset():
'''public void setLastOffset(final long offset)
'''
pass
def setMaxTimestamp():
'''public void setMaxTimestamp(final TimestampType timestampType, final long maxTimestamp)
'''
pass
def setPartitionLeaderEpoch():
'''public void setPartitionLeaderEpoch(final int epoch)
'''
pass
def checksum():
'''public long checksum()
public long checksum()
'''
pass
def isValid():
'''public boolean isValid()
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
def writeEmptyHeader():
'''public static void writeEmptyHeader(final ByteBuffer buffer, final byte magic, final long producerId, final short producerEpoch, final int baseSequence, final long baseOffset, final long lastOffset, final int partitionLeaderEpoch, final TimestampType timestampType, final long timestamp, final boolean isTransactional, final boolean isControlRecord)
'''
pass
def toString():
'''public String toString()
'''
pass
def RecordIterator():
'''public RecordIterator()
'''
pass
def hasNext():
'''public boolean hasNext()
'''
pass
def next():
'''public Record next()
'''
pass
def remove():
'''public void remove()
'''
pass
