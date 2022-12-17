COMPRESSION_NONE = "int  1"
COMPRESSION_PACKBITS = "int  32773"
COMPRESSION_GROUP3_1D = "int  2"
COMPRESSION_GROUP3_2D = "int  3"
COMPRESSION_GROUP4 = "int  4"
COMPRESSION_LZW = "int  5"
COMPRESSION_JPEG_TTN2 = "int  7"
COMPRESSION_DEFLATE = "int  32946"
def ():
    '''returns TIFFEncodeParam\n\n
    ()\n
    '''
def getCompression():
    '''returns int\n\n
    getCompression()\n
    '''
def setCompression():
    '''returns None\n\n
    setCompression(final int compression)\n
    '''
def getReverseFillOrder():
    '''returns boolean\n\n
    getReverseFillOrder()\n
    '''
def setReverseFillOrder():
    '''returns None\n\n
    setReverseFillOrder(final boolean reverseFillOrder)\n
    '''
def getT4Encode2D():
    '''returns boolean\n\n
    getT4Encode2D()\n
    '''
def setT4Encode2D():
    '''returns None\n\n
    setT4Encode2D(final boolean T4Encode2D)\n
    '''
def getT4PadEOLs():
    '''returns boolean\n\n
    getT4PadEOLs()\n
    '''
def setT4PadEOLs():
    '''returns None\n\n
    setT4PadEOLs(final boolean T4PadEOLs)\n
    '''
def getWriteTiled():
    '''returns boolean\n\n
    getWriteTiled()\n
    '''
def setWriteTiled():
    '''returns None\n\n
    setWriteTiled(final boolean writeTiled)\n
    '''
def setTileSize():
    '''returns None\n\n
    setTileSize(final int tileWidth, final int tileHeight)\n
    '''
def getTileWidth():
    '''returns int\n\n
    getTileWidth()\n
    '''
def getTileHeight():
    '''returns int\n\n
    getTileHeight()\n
    '''
def setDeflateLevel():
    '''returns None\n\n
    setDeflateLevel(final int deflateLevel)\n
    '''
def getDeflateLevel():
    '''returns int\n\n
    getDeflateLevel()\n
    '''
def setJPEGCompressRGBToYCbCr():
    '''returns None\n\n
    setJPEGCompressRGBToYCbCr(final boolean convertJPEGRGBToYCbCr)\n
    '''
def getJPEGCompressRGBToYCbCr():
    '''returns boolean\n\n
    getJPEGCompressRGBToYCbCr()\n
    '''
def setJPEGEncodeParam():
    '''returns None\n\n
    setJPEGEncodeParam(JPEGEncodeParam jpegEncodeParam)\n
    '''
def getJPEGEncodeParam():
    '''returns JPEGEncodeParam\n\n
    getJPEGEncodeParam()\n
    '''
def setExtraFields():
    '''returns None\n\n
    setExtraFields(final TIFFField[] extraFields)\n
    '''
def getExtraFields():
    '''returns TIFFField[]\n\n
    getExtraFields()\n
    '''
def setLittleEndian():
    '''returns None\n\n
    setLittleEndian(final boolean isLittleEndian)\n
    '''
def getLittleEndian():
    '''returns boolean\n\n
    getLittleEndian()\n
    '''
