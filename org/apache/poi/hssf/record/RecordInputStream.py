MAX_RECORD_DATA_SIZE = "short  8224"
def RecordInputStream():
    '''    public RecordInputStream(final InputStream in)
    public RecordInputStream(final InputStream in, final EncryptionInfo key, final int initialOffset)
    '''
def available():
    '''    public int available()
    public int available()
    '''
def read():
    '''    public int read(final byte[] b, final int off, final int len)
    '''
def getSid():
    '''    public short getSid()
    '''
def hasNextRecord():
    '''    public boolean hasNextRecord()
    '''
def nextRecord():
    '''    public void nextRecord()
    '''
def readByte():
    '''    public byte readByte()
    '''
def readShort():
    '''    public short readShort()
    '''
def readInt():
    '''    public int readInt()
    '''
def readLong():
    '''    public long readLong()
    '''
def readUByte():
    '''    public int readUByte()
    '''
def readUShort():
    '''    public int readUShort()
    '''
def readDouble():
    '''    public double readDouble()
    '''
def readPlain():
    '''    public void readPlain(final byte[] buf, final int off, final int len)
    '''
def readFully():
    '''    public void readFully(final byte[] buf)
    public void readFully(final byte[] buf, final int off, final int len)
    '''
def readString():
    '''    public String readString()
    '''
def readUnicodeLEString():
    '''    public String readUnicodeLEString(final int requestedLength)
    '''
def readCompressedUnicode():
    '''    public String readCompressedUnicode(final int requestedLength)
    '''
def readRemainder():
    '''    public byte[] readRemainder()
    '''
def readAllContinuedRemainder():
    '''    public byte[] readAllContinuedRemainder()
    '''
def remaining():
    '''    public int remaining()
    '''
def getNextSid():
    '''    public int getNextSid()
    '''
def mark():
    '''    public void mark(final int readlimit)
    '''
def reset():
    '''    public void reset()
    '''
def LeftoverDataException():
    '''    public LeftoverDataException(final int sid, final int remainingByteCount)
    '''
def SimpleHeaderInput():
    '''    public SimpleHeaderInput(final InputStream in)
    '''
def readDataSize():
    '''    public int readDataSize()
    '''
def readRecordSID():
    '''    public int readRecordSID()
    '''
