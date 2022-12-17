COPY_MASK = "int  128"
UNCOPIED = "int  0"
COPIED = "int  128"
DATATYPE_MASK = "int  127"
BINARY_MASK = "int  256"
NONBINARY = "int  0"
BINARY = "int  256"
TAG_BYTE_UNCOPIED = "int  0"
TAG_USHORT_UNCOPIED = "int  1"
TAG_SHORT_UNCOPIED = "int  2"
TAG_INT_UNCOPIED = "int  3"
TAG_FLOAT_UNCOPIED = "int  4"
TAG_DOUBLE_UNCOPIED = "int  5"
TAG_BYTE_COPIED = "int  128"
TAG_USHORT_COPIED = "int  129"
TAG_SHORT_COPIED = "int  130"
TAG_INT_COPIED = "int  131"
TAG_FLOAT_COPIED = "int  132"
TAG_DOUBLE_COPIED = "int  133"
def run():
    '''returns Object\n\n
    run()\n
    '''
def ():
    '''returns MediaLibAccessor\n\n
    (final Raster raster, final Rectangle rect, final int formatTag, final boolean preferPacked)\n
    (final Raster raster, final Rectangle rect, final int formatTag)\n
    '''
def isBinary():
    '''returns boolean\n\n
    isBinary()\n
    '''
def getMediaLibImages():
    '''returns mediaLibImage[]\n\n
    getMediaLibImages()\n
    '''
def getDataType():
    '''returns int\n\n
    getDataType()\n
    '''
def isDataCopy():
    '''returns boolean\n\n
    isDataCopy()\n
    '''
def getBandOffsets():
    '''returns int[]\n\n
    getBandOffsets()\n
    '''
def getIntParameters():
    '''returns int[]\n\n
    getIntParameters(final int band, final int[] params)\n
    '''
def getIntArrayParameters():
    '''returns int[][]\n\n
    getIntArrayParameters(final int band, final int[][] params)\n
    '''
def getDoubleParameters():
    '''returns double[]\n\n
    getDoubleParameters(final int band, final double[] params)\n
    '''
def copyDataToRaster():
    '''returns None\n\n
    copyDataToRaster()\n
    '''
def clampDataArrays():
    '''returns None\n\n
    clampDataArrays()\n
    '''
