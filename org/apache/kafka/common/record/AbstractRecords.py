def AbstractRecords():
'''public AbstractRecords()
'''
pass
def iterator():
'''public Iterator<Record> iterator()
'''
pass
def hasMatchingMagic():
'''public boolean hasMatchingMagic(final byte magic)
'''
pass
def hasCompatibleMagic():
'''public boolean hasCompatibleMagic(final byte magic)
'''
pass
def records():
'''public Iterable<Record> records()
'''
pass
def estimateSizeInBytes():
'''public static int estimateSizeInBytes(final byte magic, final long baseOffset, final CompressionType compressionType, final Iterable<Record> records)
public static int estimateSizeInBytes(final byte magic, final CompressionType compressionType, final Iterable<SimpleRecord> records)
'''
pass
def estimateSizeInBytesUpperBound():
'''public static int estimateSizeInBytesUpperBound(final byte magic, final CompressionType compressionType, final byte[] key, final byte[] value, final Header[] headers)
public static int estimateSizeInBytesUpperBound(final byte magic, final CompressionType compressionType, final ByteBuffer key, final ByteBuffer value, final Header[] headers)
'''
pass
def recordBatchHeaderSizeInBytes():
'''public static int recordBatchHeaderSizeInBytes(final byte magic, final CompressionType compressionType)
'''
pass
