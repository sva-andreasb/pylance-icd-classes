def lastOffset():
    '''    public long lastOffset()
    public long lastOffset()
    '''
def isValid():
    '''    public boolean isValid()
    '''
def ensureValid():
    '''    public void ensureValid()
    '''
def keySize():
    '''    public int keySize()
    '''
def hasKey():
    '''    public boolean hasKey()
    '''
def key():
    '''    public ByteBuffer key()
    '''
def valueSize():
    '''    public int valueSize()
    '''
def hasValue():
    '''    public boolean hasValue()
    '''
def value():
    '''    public ByteBuffer value()
    '''
def headers():
    '''    public Header[] headers()
    '''
def hasMagic():
    '''    public boolean hasMagic(final byte magic)
    '''
def hasTimestampType():
    '''    public boolean hasTimestampType(final TimestampType timestampType)
    '''
def checksumOrNull():
    '''    public Long checksumOrNull()
    '''
def checksum():
    '''    public long checksum()
    '''
def maxTimestamp():
    '''    public long maxTimestamp()
    '''
def timestamp():
    '''    public long timestamp()
    '''
def timestampType():
    '''    public TimestampType timestampType()
    '''
def baseOffset():
    '''    public long baseOffset()
    public long baseOffset()
    '''
def magic():
    '''    public byte magic()
    '''
def compressionType():
    '''    public CompressionType compressionType()
    '''
def sizeInBytes():
    '''    public int sizeInBytes()
    '''
def countOrNull():
    '''    public Integer countOrNull()
    public Integer countOrNull()
    '''
def toString():
    '''    public String toString()
    '''
def writeTo():
    '''    public void writeTo(final ByteBuffer buffer)
    public void writeTo(final ByteBufferOutputStream outputStream)
    '''
def producerId():
    '''    public long producerId()
    public long producerId()
    '''
def producerEpoch():
    '''    public short producerEpoch()
    public short producerEpoch()
    '''
def hasProducerId():
    '''    public boolean hasProducerId()
    '''
def sequence():
    '''    public int sequence()
    '''
def baseSequence():
    '''    public int baseSequence()
    public int baseSequence()
    '''
def lastSequence():
    '''    public int lastSequence()
    public int lastSequence()
    '''
def isTransactional():
    '''    public boolean isTransactional()
    public boolean isTransactional()
    '''
def partitionLeaderEpoch():
    '''    public int partitionLeaderEpoch()
    public int partitionLeaderEpoch()
    '''
def isControlBatch():
    '''    public boolean isControlBatch()
    public boolean isControlBatch()
    '''
def iterator():
    '''    public Iterator<Record> iterator()
    '''
def close():
    '''    public void close()
    public void close()
    '''
def hasNext():
    '''    public boolean hasNext()
    '''
def next():
    '''    public Record next()
    '''
def remove():
    '''    public void remove()
    '''
def streamingIterator():
    '''    public CloseableIterator<Record> streamingIterator(final BufferSupplier bufferSupplier)
    '''
def nextBatch():
    '''    public AbstractLegacyRecordBatch nextBatch()
    '''
def offset():
    '''    public long offset()
    public long offset()
    '''
def outerRecord():
    '''    public LegacyRecord outerRecord()
    public LegacyRecord outerRecord()
    '''
def equals():
    '''    public boolean equals(final Object o)
    public boolean equals(final Object o)
    '''
def hashCode():
    '''    public int hashCode()
    public int hashCode()
    '''
def setLastOffset():
    '''    public void setLastOffset(final long offset)
    '''
def setMaxTimestamp():
    '''    public void setMaxTimestamp(final TimestampType timestampType, final long timestamp)
    '''
def setPartitionLeaderEpoch():
    '''    public void setPartitionLeaderEpoch(final int epoch)
    '''
