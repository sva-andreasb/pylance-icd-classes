TIFF_COMPRESSION_LZW = "int  0"
TIFF_COMPRESSION_CCITT4 = "int  1"
TIFF_COMPRESSION_CCITT3 = "int  2"
TIFF_COMPRESSION_NONE = "int  4"
PAGE_COORDINATE_TYPE_CROP_BOX = "int  1"
PAGE_COORDINATE_TYPE_MEDIA_BOX = "int  0"
COLOR_DEPTH_DEFAULT = "int  0"
COLOR_DEPTH_FORMAT_1_BPP = "int  3"
COLOR_DEPTH_FORMAT_4_BPP = "int  2"
COLOR_DEPTH_FORMAT_8_BPP = "int  1"
SHAPE_TYPE_NONE = "int  0"
SHAPE_TYPE_PORTRAIT = "int  2"
SHAPE_TYPE_LANDSCAPE = "int  1"
def ToTiffOptions():
    '''public ToTiffOptions()
    public ToTiffOptions(final boolean multipage)
    public ToTiffOptions(final boolean multipage, final int compression)
    '''
def isMultipage():
    '''public boolean isMultipage()
    '''
def setMultipage():
    '''public void setMultipage(final boolean multipage)
    '''
def getShape():
    '''public int getShape()
    '''
def setShape():
    '''public void setShape(final int shape)
    '''
def getDepth():
    '''public int getDepth()
    '''
def setDepth():
    '''public void setDepth(final int depth)
    '''
def getCoordinateType():
    '''public int getCoordinateType()
    '''
def setCoordinateType():
    '''public void setCoordinateType(final int coordinateType)
    '''
def getCompression():
    '''public int getCompression()
    '''
def setCompression():
    '''public void setCompression(final int compression)
    '''
def getBrightness():
    '''public float getBrightness()
    '''
def setBrightness():
    '''public void setBrightness(final float brightness)
    '''
def isSkipBlankPages():
    '''public boolean isSkipBlankPages()
    '''
def setSkipBlankPages():
    '''public void setSkipBlankPages(final boolean skipBlankPages)
    '''
