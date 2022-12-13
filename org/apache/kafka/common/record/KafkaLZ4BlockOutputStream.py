MAGIC = "int  407708164"
LZ4_MAX_HEADER_LENGTH = "int  19"
LZ4_FRAME_INCOMPRESSIBLE_MASK = "int  Integer.MIN_VALUE"
CLOSED_STREAM = "String  \"The stream is already closed\""
BLOCKSIZE_64KB = "int  4"
BLOCKSIZE_256KB = "int  5"
BLOCKSIZE_1MB = "int  6"
BLOCKSIZE_4MB = "int  7"
def KafkaLZ4BlockOutputStream():
    '''public KafkaLZ4BlockOutputStream(final OutputStream out, final int blockSize, final boolean blockChecksum, final boolean useBrokenFlagDescriptorChecksum)
    public KafkaLZ4BlockOutputStream(final OutputStream out, final int blockSize, final boolean blockChecksum)
    public KafkaLZ4BlockOutputStream(final OutputStream out, final int blockSize)
    public KafkaLZ4BlockOutputStream(final OutputStream out)
    public KafkaLZ4BlockOutputStream(final OutputStream out, final boolean useBrokenHC)
    '''
def useBrokenFlagDescriptorChecksum():
    '''public boolean useBrokenFlagDescriptorChecksum()
    '''
def write():
    '''public void write(final int b)
    public void write(final byte[] b, int off, int len)
    '''
def flush():
    '''public void flush()
    '''
def close():
    '''public void close()
    '''
def FLG():
    '''public FLG()
    public FLG(final boolean blockChecksum)
    '''
def fromByte():
    '''public static FLG fromByte(final byte flg)
    public static BD fromByte(final byte bd)
    '''
def toByte():
    '''public byte toByte()
    public byte toByte()
    '''
def isContentChecksumSet():
    '''public boolean isContentChecksumSet()
    '''
def isContentSizeSet():
    '''public boolean isContentSizeSet()
    '''
def isBlockChecksumSet():
    '''public boolean isBlockChecksumSet()
    '''
def isBlockIndependenceSet():
    '''public boolean isBlockIndependenceSet()
    '''
def getVersion():
    '''public int getVersion()
    '''
def BD():
    '''public BD()
    public BD(final int blockSizeValue)
    '''
def getBlockMaximumSize():
    '''public int getBlockMaximumSize()
    '''
