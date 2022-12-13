MAX_RECORD_DATA_SIZE = "short  8224"
def RecordInputStream():
'''public RecordInputStream(final InputStream in)
public RecordInputStream(final InputStream in, final EncryptionInfo key, final int initialOffset)
'''
pass
def available():
'''public int available()
public int available()
'''
pass
def read():
'''public int read(final byte[] b, final int off, final int len)
'''
pass
def getSid():
'''public short getSid()
'''
pass
def hasNextRecord():
'''public boolean hasNextRecord()
'''
pass
def nextRecord():
'''public void nextRecord()
'''
pass
def readByte():
'''public byte readByte()
'''
pass
def readShort():
'''public short readShort()
'''
pass
def readInt():
'''public int readInt()
'''
pass
def readLong():
'''public long readLong()
'''
pass
def readUByte():
'''public int readUByte()
'''
pass
def readUShort():
'''public int readUShort()
'''
pass
def readDouble():
'''public double readDouble()
'''
pass
def readPlain():
'''public void readPlain(final byte[] buf, final int off, final int len)
'''
pass
def readFully():
'''public void readFully(final byte[] buf)
public void readFully(final byte[] buf, final int off, final int len)
'''
pass
def readString():
'''public String readString()
'''
pass
def readUnicodeLEString():
'''public String readUnicodeLEString(final int requestedLength)
'''
pass
def readCompressedUnicode():
'''public String readCompressedUnicode(final int requestedLength)
'''
pass
def readRemainder():
'''public byte[] readRemainder()
'''
pass
def readAllContinuedRemainder():
'''public byte[] readAllContinuedRemainder()
'''
pass
def remaining():
'''public int remaining()
'''
pass
def getNextSid():
'''public int getNextSid()
'''
pass
def mark():
'''public void mark(final int readlimit)
'''
pass
def reset():
'''public void reset()
'''
pass
def LeftoverDataException():
'''public LeftoverDataException(final int sid, final int remainingByteCount)
'''
pass
def SimpleHeaderInput():
'''public SimpleHeaderInput(final InputStream in)
'''
pass
def readDataSize():
'''public int readDataSize()
'''
pass
def readRecordSID():
'''public int readRecordSID()
'''
pass
