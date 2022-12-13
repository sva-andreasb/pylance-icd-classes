MAX_RECORD_OVERHEAD = "int  21"
def offset():
'''public long offset()
'''
pass
def sequence():
'''public int sequence()
'''
pass
def sizeInBytes():
'''public int sizeInBytes()
public static int sizeInBytes(final int offsetDelta, final long timestampDelta, final ByteBuffer key, final ByteBuffer value, final Header[] headers)
public static int sizeInBytes(final int offsetDelta, final long timestampDelta, final int keySize, final int valueSize, final Header[] headers)
'''
pass
def timestamp():
'''public long timestamp()
'''
pass
def attributes():
'''public byte attributes()
'''
pass
def checksumOrNull():
'''public Long checksumOrNull()
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
def valueSize():
'''public int valueSize()
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
def writeTo():
'''public static int writeTo(final DataOutputStream out, final int offsetDelta, final long timestampDelta, final ByteBuffer key, final ByteBuffer value, final Header[] headers)
'''
pass
def hasMagic():
'''public boolean hasMagic(final byte magic)
'''
pass
def isCompressed():
'''public boolean isCompressed()
'''
pass
def hasTimestampType():
'''public boolean hasTimestampType(final TimestampType timestampType)
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
def readFrom():
'''public static DefaultRecord readFrom(final DataInput input, final long baseOffset, final long baseTimestamp, final int baseSequence, final Long logAppendTime)
public static DefaultRecord readFrom(final ByteBuffer buffer, final long baseOffset, final long baseTimestamp, final int baseSequence, final Long logAppendTime)
'''
pass
def computePartialChecksum():
'''public static long computePartialChecksum(final long timestamp, final int serializedKeySize, final int serializedValueSize)
'''
pass
