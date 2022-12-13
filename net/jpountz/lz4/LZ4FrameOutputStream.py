def LZ4FrameOutputStream():
'''public LZ4FrameOutputStream(final OutputStream out, final BLOCKSIZE blockSize, final FLG.Bits... bits)
public LZ4FrameOutputStream(final OutputStream out, final BLOCKSIZE blockSize, final long knownSize, final FLG.Bits... bits)
public LZ4FrameOutputStream(final OutputStream out, final BLOCKSIZE blockSize)
public LZ4FrameOutputStream(final OutputStream out)
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
def getIndicator():
'''public int getIndicator()
'''
pass
def valueOf():
'''public static BLOCKSIZE valueOf(final int indicator)
'''
pass
def FLG():
'''public FLG(final int version, final Bits... bits)
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
def isEnabled():
'''public boolean isEnabled(final Bits bit)
public boolean isEnabled(final FLG.Bits bit)
'''
pass
def getVersion():
'''public int getVersion()
'''
pass
def getBlockMaximumSize():
'''public int getBlockMaximumSize()
'''
pass
def FrameInfo():
'''public FrameInfo(final FLG flg, final BD bd)
'''
pass
def getFLG():
'''public FLG getFLG()
'''
pass
def getBD():
'''public BD getBD()
'''
pass
def updateStreamHash():
'''public void updateStreamHash(final byte[] buff, final int off, final int len)
'''
pass
def currentStreamHash():
'''public int currentStreamHash()
'''
pass
def finish():
'''public void finish()
'''
pass
def isFinished():
'''public boolean isFinished()
'''
pass
