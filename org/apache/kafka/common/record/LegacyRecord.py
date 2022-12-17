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
def ():
    '''returns LegacyRecord\n\n
    (final ByteBuffer buffer)\n
    (final ByteBuffer buffer, final Long wrapperRecordTimestamp, final TimestampType wrapperRecordTimestampType)\n
    '''
def computeChecksum():
    '''returns long\n\n
    computeChecksum()\n
    '''
def checksum():
    '''returns long\n\n
    checksum()\n
    '''
def isValid():
    '''returns boolean\n\n
    isValid()\n
    '''
def wrapperRecordTimestamp():
    '''returns Long\n\n
    wrapperRecordTimestamp()\n
    '''
def wrapperRecordTimestampType():
    '''returns TimestampType\n\n
    wrapperRecordTimestampType()\n
    '''
def ensureValid():
    '''returns None\n\n
    ensureValid()\n
    '''
def sizeInBytes():
    '''returns int\n\n
    sizeInBytes()\n
    '''
def keySize():
    '''returns int\n\n
    keySize()\n
    '''
def hasKey():
    '''returns boolean\n\n
    hasKey()\n
    '''
def valueSize():
    '''returns int\n\n
    valueSize()\n
    '''
def hasNullValue():
    '''returns boolean\n\n
    hasNullValue()\n
    '''
def magic():
    '''returns byte\n\n
    magic()\n
    '''
def attributes():
    '''returns byte\n\n
    attributes()\n
    '''
def timestamp():
    '''returns long\n\n
    timestamp()\n
    '''
def timestampType():
    '''returns TimestampType\n\n
    timestampType()\n
    '''
def compressionType():
    '''returns CompressionType\n\n
    compressionType()\n
    '''
def value():
    '''returns ByteBuffer\n\n
    value()\n
    '''
def key():
    '''returns ByteBuffer\n\n
    key()\n
    '''
def buffer():
    '''returns ByteBuffer\n\n
    buffer()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
