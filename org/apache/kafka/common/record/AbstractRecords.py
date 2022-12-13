def AbstractRecords():
    '''public AbstractRecords()
    '''
def iterator():
    '''public Iterator<Record> iterator()
    '''
def hasMatchingMagic():
    '''public boolean hasMatchingMagic(final byte magic)
    '''
def hasCompatibleMagic():
    '''public boolean hasCompatibleMagic(final byte magic)
    '''
def records():
    '''public Iterable<Record> records()
    '''
def estimateSizeInBytes():
    '''public static int estimateSizeInBytes(final byte magic, final long baseOffset, final CompressionType compressionType, final Iterable<Record> records)
    public static int estimateSizeInBytes(final byte magic, final CompressionType compressionType, final Iterable<SimpleRecord> records)
    '''
def estimateSizeInBytesUpperBound():
    '''public static int estimateSizeInBytesUpperBound(final byte magic, final CompressionType compressionType, final byte[] key, final byte[] value, final Header[] headers)
    public static int estimateSizeInBytesUpperBound(final byte magic, final CompressionType compressionType, final ByteBuffer key, final ByteBuffer value, final Header[] headers)
    '''
def recordBatchHeaderSizeInBytes():
    '''public static int recordBatchHeaderSizeInBytes(final byte magic, final CompressionType compressionType)
    '''
