INTENT_PERCEPTUAL = "int  0"
INTENT_RELATIVE = "int  1"
INTENT_SATURATION = "int  2"
INTENT_ABSOLUTE = "int  3"
PNG_FILTER_NONE = "int  0"
PNG_FILTER_SUB = "int  1"
PNG_FILTER_UP = "int  2"
PNG_FILTER_AVERAGE = "int  3"
PNG_FILTER_PAETH = "int  4"
def ():
    '''returns PNGEncodeParam\n\n
    ()\n
    '''
def getBitDepth():
    '''returns int\n\n
    getBitDepth()\n
    '''
def unsetBitDepth():
    '''returns None\n\n
    unsetBitDepth()\n
    '''
def setInterlacing():
    '''returns None\n\n
    setInterlacing(final boolean useInterlacing)\n
    '''
def getInterlacing():
    '''returns boolean\n\n
    getInterlacing()\n
    '''
def unsetBackground():
    '''returns None\n\n
    unsetBackground()\n
    unsetBackground()\n
    unsetBackground()\n
    unsetBackground()\n
    '''
def isBackgroundSet():
    '''returns boolean\n\n
    isBackgroundSet()\n
    isBackgroundSet()\n
    isBackgroundSet()\n
    isBackgroundSet()\n
    '''
def setChromaticity():
    '''returns None\n\n
    setChromaticity(final float[] chromaticity)\n
    setChromaticity(final float whitePointX, final float whitePointY, final float redX, final float redY, final float greenX, final float greenY, final float blueX, final float blueY)\n
    '''
def getChromaticity():
    '''returns float[]\n\n
    getChromaticity()\n
    '''
def unsetChromaticity():
    '''returns None\n\n
    unsetChromaticity()\n
    '''
def isChromaticitySet():
    '''returns boolean\n\n
    isChromaticitySet()\n
    '''
def setGamma():
    '''returns None\n\n
    setGamma(final float gamma)\n
    '''
def getGamma():
    '''returns float\n\n
    getGamma()\n
    '''
def unsetGamma():
    '''returns None\n\n
    unsetGamma()\n
    '''
def isGammaSet():
    '''returns boolean\n\n
    isGammaSet()\n
    '''
def setPaletteHistogram():
    '''returns None\n\n
    setPaletteHistogram(final int[] paletteHistogram)\n
    '''
def getPaletteHistogram():
    '''returns int[]\n\n
    getPaletteHistogram()\n
    '''
def unsetPaletteHistogram():
    '''returns None\n\n
    unsetPaletteHistogram()\n
    '''
def isPaletteHistogramSet():
    '''returns boolean\n\n
    isPaletteHistogramSet()\n
    '''
def setICCProfileData():
    '''returns None\n\n
    setICCProfileData(final byte[] iccProfileData)\n
    '''
def getICCProfileData():
    '''returns byte[]\n\n
    getICCProfileData()\n
    '''
def unsetICCProfileData():
    '''returns None\n\n
    unsetICCProfileData()\n
    '''
def isICCProfileDataSet():
    '''returns boolean\n\n
    isICCProfileDataSet()\n
    '''
def setPhysicalDimension():
    '''returns None\n\n
    setPhysicalDimension(final int[] physicalDimension)\n
    setPhysicalDimension(final int xPixelsPerUnit, final int yPixelsPerUnit, final int unitSpecifier)\n
    '''
def getPhysicalDimension():
    '''returns int[]\n\n
    getPhysicalDimension()\n
    '''
def unsetPhysicalDimension():
    '''returns None\n\n
    unsetPhysicalDimension()\n
    '''
def isPhysicalDimensionSet():
    '''returns boolean\n\n
    isPhysicalDimensionSet()\n
    '''
def setSuggestedPalette():
    '''returns None\n\n
    setSuggestedPalette(final PNGSuggestedPaletteEntry[] palette)\n
    '''
def getSuggestedPalette():
    '''returns PNGSuggestedPaletteEntry[]\n\n
    getSuggestedPalette()\n
    '''
def unsetSuggestedPalette():
    '''returns None\n\n
    unsetSuggestedPalette()\n
    '''
def isSuggestedPaletteSet():
    '''returns boolean\n\n
    isSuggestedPaletteSet()\n
    '''
def setSignificantBits():
    '''returns None\n\n
    setSignificantBits(final int[] significantBits)\n
    '''
def getSignificantBits():
    '''returns int[]\n\n
    getSignificantBits()\n
    '''
def unsetSignificantBits():
    '''returns None\n\n
    unsetSignificantBits()\n
    '''
def isSignificantBitsSet():
    '''returns boolean\n\n
    isSignificantBitsSet()\n
    '''
def setSRGBIntent():
    '''returns None\n\n
    setSRGBIntent(final int srgbIntent)\n
    '''
def getSRGBIntent():
    '''returns int\n\n
    getSRGBIntent()\n
    '''
def unsetSRGBIntent():
    '''returns None\n\n
    unsetSRGBIntent()\n
    '''
def isSRGBIntentSet():
    '''returns boolean\n\n
    isSRGBIntentSet()\n
    '''
def setText():
    '''returns None\n\n
    setText(final String[] text)\n
    '''
def getText():
    '''returns String[]\n\n
    getText()\n
    '''
def unsetText():
    '''returns None\n\n
    unsetText()\n
    '''
def isTextSet():
    '''returns boolean\n\n
    isTextSet()\n
    '''
def setModificationTime():
    '''returns None\n\n
    setModificationTime(final Date modificationTime)\n
    '''
def getModificationTime():
    '''returns Date\n\n
    getModificationTime()\n
    '''
def unsetModificationTime():
    '''returns None\n\n
    unsetModificationTime()\n
    '''
def isModificationTimeSet():
    '''returns boolean\n\n
    isModificationTimeSet()\n
    '''
def unsetTransparency():
    '''returns None\n\n
    unsetTransparency()\n
    '''
def isTransparencySet():
    '''returns boolean\n\n
    isTransparencySet()\n
    '''
def setCompressedText():
    '''returns None\n\n
    setCompressedText(final String[] text)\n
    '''
def getCompressedText():
    '''returns String[]\n\n
    getCompressedText()\n
    '''
def unsetCompressedText():
    '''returns None\n\n
    unsetCompressedText()\n
    '''
def isCompressedTextSet():
    '''returns boolean\n\n
    isCompressedTextSet()\n
    '''
def filterRow():
    '''returns int\n\n
    filterRow(final byte[] currRow, final byte[] prevRow, final byte[][] scratchRows, final int bytesPerRow, final int bytesPerPixel)\n
    '''
def setBitDepth():
    '''returns None\n\n
    setBitDepth(final int bitDepth)\n
    setBitDepth(final int bitDepth)\n
    setBitDepth(final int bitDepth)\n
    '''
def setPalette():
    '''returns None\n\n
    setPalette(final int[] rgb)\n
    '''
def getPalette():
    '''returns int[]\n\n
    getPalette()\n
    '''
def unsetPalette():
    '''returns None\n\n
    unsetPalette()\n
    '''
def isPaletteSet():
    '''returns boolean\n\n
    isPaletteSet()\n
    '''
def setBackgroundPaletteIndex():
    '''returns None\n\n
    setBackgroundPaletteIndex(final int index)\n
    '''
def getBackgroundPaletteIndex():
    '''returns int\n\n
    getBackgroundPaletteIndex()\n
    '''
def setPaletteTransparency():
    '''returns None\n\n
    setPaletteTransparency(final byte[] alpha)\n
    '''
def getPaletteTransparency():
    '''returns byte[]\n\n
    getPaletteTransparency()\n
    '''
def setBackgroundGray():
    '''returns None\n\n
    setBackgroundGray(final int gray)\n
    '''
def getBackgroundGray():
    '''returns int\n\n
    getBackgroundGray()\n
    '''
def setTransparentGray():
    '''returns None\n\n
    setTransparentGray(final int transparentGray)\n
    '''
def getTransparentGray():
    '''returns int\n\n
    getTransparentGray()\n
    '''
def setBitShift():
    '''returns None\n\n
    setBitShift(final int bitShift)\n
    '''
def getBitShift():
    '''returns int\n\n
    getBitShift()\n
    '''
def unsetBitShift():
    '''returns None\n\n
    unsetBitShift()\n
    '''
def isBitShiftSet():
    '''returns boolean\n\n
    isBitShiftSet()\n
    '''
def isBitDepthSet():
    '''returns boolean\n\n
    isBitDepthSet()\n
    '''
def setBackgroundRGB():
    '''returns None\n\n
    setBackgroundRGB(final int[] rgb)\n
    '''
def getBackgroundRGB():
    '''returns int[]\n\n
    getBackgroundRGB()\n
    '''
def setTransparentRGB():
    '''returns None\n\n
    setTransparentRGB(final int[] transparentRGB)\n
    '''
def getTransparentRGB():
    '''returns int[]\n\n
    getTransparentRGB()\n
    '''
