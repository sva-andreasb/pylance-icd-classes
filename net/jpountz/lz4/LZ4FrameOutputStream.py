def LZ4FrameOutputStream():
    '''    public LZ4FrameOutputStream(final OutputStream out, final BLOCKSIZE blockSize, final FLG.Bits... bits)
    public LZ4FrameOutputStream(final OutputStream out, final BLOCKSIZE blockSize, final long knownSize, final FLG.Bits... bits)
    public LZ4FrameOutputStream(final OutputStream out, final BLOCKSIZE blockSize)
    public LZ4FrameOutputStream(final OutputStream out)
    '''
def write():
    '''    public void write(final int b)
    public void write(final byte[] b, int off, int len)
    '''
def flush():
    '''    public void flush()
    '''
def close():
    '''    public void close()
    '''
def getIndicator():
    '''    public int getIndicator()
    '''
def valueOf():
    '''    public static BLOCKSIZE valueOf(final int indicator)
    '''
def FLG():
    '''    public FLG(final int version, final Bits... bits)
    '''
def fromByte():
    '''    public static FLG fromByte(final byte flg)
    public static BD fromByte(final byte bd)
    '''
def toByte():
    '''    public byte toByte()
    public byte toByte()
    '''
def isEnabled():
    '''    public boolean isEnabled(final Bits bit)
    public boolean isEnabled(final FLG.Bits bit)
    '''
def getVersion():
    '''    public int getVersion()
    '''
def getBlockMaximumSize():
    '''    public int getBlockMaximumSize()
    '''
def FrameInfo():
    '''    public FrameInfo(final FLG flg, final BD bd)
    '''
def getFLG():
    '''    public FLG getFLG()
    '''
def getBD():
    '''    public BD getBD()
    '''
def updateStreamHash():
    '''    public void updateStreamHash(final byte[] buff, final int off, final int len)
    '''
def currentStreamHash():
    '''    public int currentStreamHash()
    '''
def finish():
    '''    public void finish()
    '''
def isFinished():
    '''    public boolean isFinished()
    '''
