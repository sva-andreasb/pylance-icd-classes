CRC_OFFSET = "int  0"
CRC_LENGTH = "int  4"
MAGIC_OFFSET = "int  4"
MAGIC_LENGTH = "int  1"
ATTRIBUTES_OFFSET = "int  5"
ATTRIBUTES_LENGTH = "int  1"
TIMESTAMP_OFFSET = "int  6"
TIMESTAMP_LENGTH = "int  8"
KEY_SIZE_OFFSET_V0 = "int  6"
KEY_SIZE_OFFSET_V1 = "int  14"
KEY_SIZE_LENGTH = "int  4"
KEY_OFFSET_V0 = "int  10"
KEY_OFFSET_V1 = "int  18"
VALUE_SIZE_LENGTH = "int  4"
HEADER_SIZE_V0 = "int  6"
HEADER_SIZE_V1 = "int  14"
RECORD_OVERHEAD_V0 = "int  14"
RECORD_OVERHEAD_V1 = "int  22"
NO_TIMESTAMP = "long  -1L"
def LegacyRecord():
'''public LegacyRecord(final ByteBuffer buffer)
public LegacyRecord(final ByteBuffer buffer, final Long wrapperRecordTimestamp, final TimestampType wrapperRecordTimestampType)
'''
pass
def computeChecksum():
'''public long computeChecksum()
public static long computeChecksum(final byte magic, final byte attributes, final long timestamp, final byte[] key, final byte[] value)
'''
pass
def checksum():
'''public long checksum()
'''
pass
def isValid():
'''public boolean isValid()
'''
pass
def wrapperRecordTimestamp():
'''public Long wrapperRecordTimestamp()
'''
pass
def wrapperRecordTimestampType():
'''public TimestampType wrapperRecordTimestampType()
'''
pass
def ensureValid():
'''public void ensureValid()
'''
pass
def sizeInBytes():
'''public int sizeInBytes()
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
def valueSize():
'''public int valueSize()
'''
pass
def hasNullValue():
'''public boolean hasNullValue()
'''
pass
def magic():
'''public byte magic()
'''
pass
def attributes():
'''public byte attributes()
'''
pass
def timestamp():
'''public long timestamp()
'''
pass
def timestampType():
'''public TimestampType timestampType()
public static TimestampType timestampType(final byte magic, final TimestampType wrapperRecordTimestampType, final byte attributes)
'''
pass
def compressionType():
'''public CompressionType compressionType()
'''
pass
def value():
'''public ByteBuffer value()
'''
pass
def key():
'''public ByteBuffer key()
'''
pass
def buffer():
'''public ByteBuffer buffer()
'''
pass
def toString():
'''public String toString()
'''
pass
def equals():
'''public boolean equals(final Object other)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def create():
'''public static LegacyRecord create(final byte magic, final long timestamp, final byte[] key, final byte[] value, final CompressionType compressionType, final TimestampType timestampType)
public static LegacyRecord create(final byte magic, final long timestamp, final byte[] key, final byte[] value)
'''
pass
def writeCompressedRecordHeader():
'''public static void writeCompressedRecordHeader(final ByteBuffer buffer, final byte magic, final int recordSize, final long timestamp, final CompressionType compressionType, final TimestampType timestampType)
'''
pass
def write():
'''public static long write(final DataOutputStream out, final byte magic, final long timestamp, final byte[] key, final byte[] value, final CompressionType compressionType, final TimestampType timestampType)
public static long write(final DataOutputStream out, final byte magic, final long timestamp, final ByteBuffer key, final ByteBuffer value, final CompressionType compressionType, final TimestampType timestampType)
public static void write(final DataOutputStream out, final byte magic, final long crc, final byte attributes, final long timestamp, final byte[] key, final byte[] value)
'''
pass
def recordSize():
'''public static int recordSize(final byte magic, final int keySize, final int valueSize)
'''
pass
def computeAttributes():
'''public static byte computeAttributes(final byte magic, final CompressionType type, final TimestampType timestampType)
'''
pass
