def PNGChunk():
    '''    public PNGChunk(final int length, final int type, final byte[] data, final int crc)
    '''
def getLength():
    '''    public int getLength()
    '''
def getType():
    '''    public int getType()
    '''
def getTypeString():
    '''    public String getTypeString()
    '''
def getData():
    '''    public byte[] getData()
    '''
def getByte():
    '''    public byte getByte(final int offset)
    '''
def getInt1():
    '''    public int getInt1(final int offset)
    '''
def getInt2():
    '''    public int getInt2(final int offset)
    '''
def getInt4():
    '''    public int getInt4(final int offset)
    '''
def getString4():
    '''    public String getString4(final int offset)
    '''
def isType():
    '''    public boolean isType(final String typeName)
    '''
def readChunk():
    '''    public static PNGChunk readChunk(final DataInputStream distream)
    '''
def getChunkType():
    '''    public static String getChunkType(final DataInputStream distream)
    '''
def skipChunk():
    '''    public static boolean skipChunk(final DataInputStream distream)
    '''
