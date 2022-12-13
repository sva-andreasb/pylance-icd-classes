def lastOffset():
'''public long lastOffset()
public long lastOffset()
'''
pass
def isValid():
'''public boolean isValid()
'''
pass
def ensureValid():
'''public void ensureValid()
'''
pass
def keySize():
'''public int keySize()
'''
pass
def hasKey():
'''public boolean hasKey()
'''
pass
def key():
'''public ByteBuffer key()
'''
pass
def valueSize():
'''public int valueSize()
'''
pass
def hasValue():
'''public boolean hasValue()
'''
pass
def value():
'''public ByteBuffer value()
'''
pass
def headers():
'''public Header[] headers()
'''
pass
def hasMagic():
'''public boolean hasMagic(final byte magic)
'''
pass
def hasTimestampType():
'''public boolean hasTimestampType(final TimestampType timestampType)
'''
pass
def checksumOrNull():
'''public Long checksumOrNull()
'''
pass
def checksum():
'''public long checksum()
'''
pass
def maxTimestamp():
'''public long maxTimestamp()
'''
pass
def timestamp():
'''public long timestamp()
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
def magic():
'''public byte magic()
'''
pass
def compressionType():
'''public CompressionType compressionType()
'''
pass
def sizeInBytes():
'''public int sizeInBytes()
'''
pass
def countOrNull():
'''public Integer countOrNull()
public Integer countOrNull()
'''
pass
def toString():
'''public String toString()
'''
pass
def writeTo():
'''public void writeTo(final ByteBuffer buffer)
public void writeTo(final ByteBufferOutputStream outputStream)
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
def hasProducerId():
'''public boolean hasProducerId()
'''
pass
def sequence():
'''public int sequence()
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
def isTransactional():
'''public boolean isTransactional()
public boolean isTransactional()
'''
pass
def partitionLeaderEpoch():
'''public int partitionLeaderEpoch()
public int partitionLeaderEpoch()
'''
pass
def isControlBatch():
'''public boolean isControlBatch()
public boolean isControlBatch()
'''
pass
def iterator():
'''public Iterator<Record> iterator()
'''
pass
def close():
'''public void close()
public void close()
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
def streamingIterator():
'''public CloseableIterator<Record> streamingIterator(final BufferSupplier bufferSupplier)
'''
pass
def nextBatch():
'''public AbstractLegacyRecordBatch nextBatch()
'''
pass
def offset():
'''public long offset()
public long offset()
'''
pass
def outerRecord():
'''public LegacyRecord outerRecord()
public LegacyRecord outerRecord()
'''
pass
def equals():
'''public boolean equals(final Object o)
public boolean equals(final Object o)
'''
pass
def hashCode():
'''public int hashCode()
public int hashCode()
'''
pass
def setLastOffset():
'''public void setLastOffset(final long offset)
'''
pass
def setMaxTimestamp():
'''public void setMaxTimestamp(final TimestampType timestampType, final long timestamp)
'''
pass
def setPartitionLeaderEpoch():
'''public void setPartitionLeaderEpoch(final int epoch)
'''
pass
