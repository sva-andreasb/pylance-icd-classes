MAX_RECORD_DATA_SIZE = "short  8224"
def ():
    '''returns SimpleHeaderInput\n\n
    (final InputStream in)\n
    (final InputStream in, final EncryptionInfo key, final int initialOffset)\n
    (final int sid, final int remainingByteCount)\n
    (final InputStream in)\n
    '''
def available():
    '''returns int\n\n
    available()\n
    available()\n
    '''
def read():
    '''returns int\n\n
    read(final byte[] b, final int off, final int len)\n
    '''
def getSid():
    '''returns short\n\n
    getSid()\n
    '''
def hasNextRecord():
    '''returns boolean\n\n
    hasNextRecord()\n
    '''
def nextRecord():
    '''returns None\n\n
    nextRecord()\n
    '''
def readByte():
    '''returns byte\n\n
    readByte()\n
    '''
def readShort():
    '''returns short\n\n
    readShort()\n
    '''
def readInt():
    '''returns int\n\n
    readInt()\n
    '''
def readLong():
    '''returns long\n\n
    readLong()\n
    '''
def readUByte():
    '''returns int\n\n
    readUByte()\n
    '''
def readUShort():
    '''returns int\n\n
    readUShort()\n
    '''
def readDouble():
    '''returns double\n\n
    readDouble()\n
    '''
def readPlain():
    '''returns None\n\n
    readPlain(final byte[] buf, final int off, final int len)\n
    '''
def readFully():
    '''returns None\n\n
    readFully(final byte[] buf)\n
    readFully(final byte[] buf, final int off, final int len)\n
    '''
def readString():
    '''returns String\n\n
    readString()\n
    '''
def readUnicodeLEString():
    '''returns String\n\n
    readUnicodeLEString(final int requestedLength)\n
    '''
def readCompressedUnicode():
    '''returns String\n\n
    readCompressedUnicode(final int requestedLength)\n
    '''
def readRemainder():
    '''returns byte[]\n\n
    readRemainder()\n
    '''
def readAllContinuedRemainder():
    '''returns byte[]\n\n
    readAllContinuedRemainder()\n
    '''
def remaining():
    '''returns int\n\n
    remaining()\n
    '''
def getNextSid():
    '''returns int\n\n
    getNextSid()\n
    '''
def mark():
    '''returns None\n\n
    mark(final int readlimit)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def readDataSize():
    '''returns int\n\n
    readDataSize()\n
    '''
def readRecordSID():
    '''returns int\n\n
    readRecordSID()\n
    '''
