MAGIC = "int  407708164"
LZ4_MAX_HEADER_LENGTH = "int  19"
LZ4_FRAME_INCOMPRESSIBLE_MASK = "int  Integer.MIN_VALUE"
CLOSED_STREAM = "String  The stream is already closed""
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
pass
def useBrokenFlagDescriptorChecksum():
'''public boolean useBrokenFlagDescriptorChecksum()
'''
pass
def write():
'''public void write(final int b)
public void write(final byte[] b, int off, int len)
'''
pass
def flush():
'''public void flush()
'''
pass
def close():
'''public void close()
'''
pass
def FLG():
'''public FLG()
public FLG(final boolean blockChecksum)
'''
pass
def fromByte():
'''public static FLG fromByte(final byte flg)
public static BD fromByte(final byte bd)
'''
pass
def toByte():
'''public byte toByte()
public byte toByte()
'''
pass
def isContentChecksumSet():
'''public boolean isContentChecksumSet()
'''
pass
def isContentSizeSet():
'''public boolean isContentSizeSet()
'''
pass
def isBlockChecksumSet():
'''public boolean isBlockChecksumSet()
'''
pass
def isBlockIndependenceSet():
'''public boolean isBlockIndependenceSet()
'''
pass
def getVersion():
'''public int getVersion()
'''
pass
def BD():
'''public BD()
public BD(final int blockSizeValue)
'''
pass
def getBlockMaximumSize():
'''public int getBlockMaximumSize()
'''
pass
