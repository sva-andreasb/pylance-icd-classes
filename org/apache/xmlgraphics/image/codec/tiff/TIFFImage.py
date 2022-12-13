COMP_NONE = "int  1"
COMP_FAX_G3_1D = "int  2"
COMP_FAX_G3_2D = "int  3"
COMP_FAX_G4_2D = "int  4"
COMP_LZW = "int  5"
COMP_JPEG_OLD = "int  6"
COMP_JPEG_TTN2 = "int  7"
COMP_PACKBITS = "int  32773"
COMP_DEFLATE = "int  32946"
def TIFFImage():
    '''public TIFFImage(final SeekableStream stream, TIFFDecodeParam param, final int directory)
    '''
def getPrivateIFD():
    '''public TIFFDirectory getPrivateIFD(final long offset)
    '''
def copyData():
    '''public WritableRaster copyData(final WritableRaster wr)
    '''
def getTile():
    '''public synchronized Raster getTile(final int tileX, final int tileY)
    '''
