PNG_COLOR_GRAY = "int  0"
PNG_COLOR_RGB = "int  2"
PNG_COLOR_PALETTE = "int  3"
PNG_COLOR_GRAY_ALPHA = "int  4"
PNG_COLOR_RGB_ALPHA = "int  6"
PNG_FILTER_NONE = "int  0"
PNG_FILTER_SUB = "int  1"
PNG_FILTER_UP = "int  2"
PNG_FILTER_AVERAGE = "int  3"
PNG_FILTER_PAETH = "int  4"
def PNGRed():
    '''public PNGRed(final InputStream stream)
    public PNGRed(InputStream stream, PNGDecodeParam decodeParam)
    '''
def createComponentColorModel():
    '''public static ColorModel createComponentColorModel(final SampleModel sm)
    '''
def copyData():
    '''public WritableRaster copyData(final WritableRaster wr)
    '''
def getTile():
    '''public Raster getTile(final int tileX, final int tileY)
    '''
def PNGChunk():
    '''public PNGChunk(final int length, final int type, final byte[] data, final int crc)
    '''
def getLength():
    '''public int getLength()
    '''
def getType():
    '''public int getType()
    '''
def getTypeString():
    '''public String getTypeString()
    '''
def getData():
    '''public byte[] getData()
    '''
def getByte():
    '''public byte getByte(final int offset)
    '''
def getInt1():
    '''public int getInt1(final int offset)
    '''
def getInt2():
    '''public int getInt2(final int offset)
    '''
def getInt4():
    '''public int getInt4(final int offset)
    '''
def getString4():
    '''public String getString4(final int offset)
    '''
def isType():
    '''public boolean isType(final String typeName)
    '''
