MAX_RECORD_OVERHEAD = "int  21"
def offset():
    '''public long offset()
    '''
def sequence():
    '''public int sequence()
    '''
def sizeInBytes():
    '''public int sizeInBytes()
    public static int sizeInBytes(final int offsetDelta, final long timestampDelta, final ByteBuffer key, final ByteBuffer value, final Header[] headers)
    public static int sizeInBytes(final int offsetDelta, final long timestampDelta, final int keySize, final int valueSize, final Header[] headers)
    '''
def timestamp():
    '''public long timestamp()
    '''
def attributes():
    '''public byte attributes()
    '''
def checksumOrNull():
    '''public Long checksumOrNull()
    '''
def isValid():
    '''public boolean isValid()
    '''
def ensureValid():
    '''public void ensureValid()
    '''
def keySize():
    '''public int keySize()
    '''
def valueSize():
    '''public int valueSize()
    '''
def hasKey():
    '''public boolean hasKey()
    '''
def key():
    '''public ByteBuffer key()
    '''
def hasValue():
    '''public boolean hasValue()
    '''
def value():
    '''public ByteBuffer value()
    '''
def headers():
    '''public Header[] headers()
    '''
def writeTo():
    '''public static int writeTo(final DataOutputStream out, final int offsetDelta, final long timestampDelta, final ByteBuffer key, final ByteBuffer value, final Header[] headers)
    '''
def hasMagic():
    '''public boolean hasMagic(final byte magic)
    '''
def isCompressed():
    '''public boolean isCompressed()
    '''
def hasTimestampType():
    '''public boolean hasTimestampType(final TimestampType timestampType)
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
def readFrom():
    '''public static DefaultRecord readFrom(final DataInput input, final long baseOffset, final long baseTimestamp, final int baseSequence, final Long logAppendTime)
    public static DefaultRecord readFrom(final ByteBuffer buffer, final long baseOffset, final long baseTimestamp, final int baseSequence, final Long logAppendTime)
    '''
def computePartialChecksum():
    '''public static long computePartialChecksum(final long timestamp, final int serializedKeySize, final int serializedValueSize)
    '''
