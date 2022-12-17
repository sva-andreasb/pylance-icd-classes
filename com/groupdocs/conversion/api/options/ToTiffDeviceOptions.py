FORM_PRESENTATION_MODE_EDITOR = "int  1"
FORM_PRESENTATION_MODE_PRODUCTION = "int  0"
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
def ():
    '''returns ToTiffDeviceOptions\n\n
    ()\n
    (final boolean multipage)\n
    '''
def isMultipage():
    '''returns boolean\n\n
    isMultipage()\n
    '''
def setMultipage():
    '''returns None\n\n
    setMultipage(final boolean multipage)\n
    '''
def getFormPresentationMode():
    '''returns int\n\n
    getFormPresentationMode()\n
    '''
def setFormPresentationMode():
    '''returns None\n\n
    setFormPresentationMode(final int formPresentationMode)\n
    '''
def isUseNewImagingEngine():
    '''returns boolean\n\n
    isUseNewImagingEngine()\n
    '''
def setUseNewImagingEngine():
    '''returns None\n\n
    setUseNewImagingEngine(final boolean useNewImagingEngine)\n
    '''
def isSystemFontsNativeRendering():
    '''returns boolean\n\n
    isSystemFontsNativeRendering()\n
    '''
def setSystemFontsNativeRendering():
    '''returns None\n\n
    setSystemFontsNativeRendering(final boolean systemFontsNativeRendering)\n
    '''
def isBarcodeOptimization():
    '''returns boolean\n\n
    isBarcodeOptimization()\n
    '''
def setBarcodeOptimization():
    '''returns None\n\n
    setBarcodeOptimization(final boolean barcodeOptimization)\n
    '''
def getShape():
    '''returns int\n\n
    getShape()\n
    '''
def setShape():
    '''returns None\n\n
    setShape(final int shape)\n
    '''
def isSkipBlankPages():
    '''returns boolean\n\n
    isSkipBlankPages()\n
    '''
def setSkipBlankPages():
    '''returns None\n\n
    setSkipBlankPages(final boolean skipBlankPages)\n
    '''
def getBrightness():
    '''returns float\n\n
    getBrightness()\n
    '''
def setBrightness():
    '''returns None\n\n
    setBrightness(final float brightness)\n
    '''
def getCompression():
    '''returns int\n\n
    getCompression()\n
    '''
def setCompression():
    '''returns None\n\n
    setCompression(final int compression)\n
    '''
def getCoordinateType():
    '''returns int\n\n
    getCoordinateType()\n
    '''
def setCoordinateType():
    '''returns None\n\n
    setCoordinateType(final int coordinateType)\n
    '''
def getDepth():
    '''returns int\n\n
    getDepth()\n
    '''
def setDepth():
    '''returns None\n\n
    setDepth(final int depth)\n
    '''
