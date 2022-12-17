def ():
    '''returns FloatDoubleColorModel\n\n
    (final ColorSpace colorSpace, final boolean hasAlpha, final boolean isAlphaPremultiplied, final int transparency, final int transferType)\n
    '''
def getRed():
    '''returns int\n\n
    getRed(final int pixel)\n
    getRed(final Object inData)\n
    '''
def getGreen():
    '''returns int\n\n
    getGreen(final int pixel)\n
    getGreen(final Object inData)\n
    '''
def getBlue():
    '''returns int\n\n
    getBlue(final int pixel)\n
    getBlue(final Object inData)\n
    '''
def getAlpha():
    '''returns int\n\n
    getAlpha(final int pixel)\n
    getAlpha(final Object inData)\n
    '''
def getRGB():
    '''returns int\n\n
    getRGB(final int pixel)\n
    getRGB(final Object inData)\n
    '''
def getDataElements():
    '''returns Object\n\n
    getDataElements(final int rgb, final Object pixel)\n
    getDataElements(final int[] components, final int offset, final Object obj)\n
    '''
def getComponents():
    '''returns int[]\n\n
    getComponents(final int pixel, final int[] components, final int offset)\n
    getComponents(final Object pixel, final int[] components, final int offset)\n
    '''
def getDataElement():
    '''returns int\n\n
    getDataElement(final int[] components, final int offset)\n
    '''
def coerceData():
    '''returns ColorModel\n\n
    coerceData(final WritableRaster raster, final boolean isAlphaPremultiplied)\n
    '''
def isCompatibleRaster():
    '''returns boolean\n\n
    isCompatibleRaster(final Raster raster)\n
    '''
def createCompatibleWritableRaster():
    '''returns WritableRaster\n\n
    createCompatibleWritableRaster(final int w, final int h)\n
    '''
def createCompatibleSampleModel():
    '''returns SampleModel\n\n
    createCompatibleSampleModel(final int w, final int h)\n
    '''
def isCompatibleSampleModel():
    '''returns boolean\n\n
    isCompatibleSampleModel(final SampleModel sm)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
