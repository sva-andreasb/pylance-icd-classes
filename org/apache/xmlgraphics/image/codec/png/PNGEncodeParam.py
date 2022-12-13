INTENT_PERCEPTUAL = "int  0"
INTENT_RELATIVE = "int  1"
INTENT_SATURATION = "int  2"
INTENT_ABSOLUTE = "int  3"
PNG_FILTER_NONE = "int  0"
PNG_FILTER_SUB = "int  1"
PNG_FILTER_UP = "int  2"
PNG_FILTER_AVERAGE = "int  3"
PNG_FILTER_PAETH = "int  4"
def PNGEncodeParam():
    '''    public PNGEncodeParam()
    '''
def getDefaultEncodeParam():
    '''    public static PNGEncodeParam getDefaultEncodeParam(final RenderedImage im)
    '''
def getBitDepth():
    '''    public int getBitDepth()
    '''
def unsetBitDepth():
    '''    public void unsetBitDepth()
    '''
def setInterlacing():
    '''    public void setInterlacing(final boolean useInterlacing)
    '''
def getInterlacing():
    '''    public boolean getInterlacing()
    '''
def unsetBackground():
    '''    public void unsetBackground()
    public void unsetBackground()
    public void unsetBackground()
    public void unsetBackground()
    '''
def isBackgroundSet():
    '''    public boolean isBackgroundSet()
    public boolean isBackgroundSet()
    public boolean isBackgroundSet()
    public boolean isBackgroundSet()
    '''
def setChromaticity():
    '''    public void setChromaticity(final float[] chromaticity)
    public void setChromaticity(final float whitePointX, final float whitePointY, final float redX, final float redY, final float greenX, final float greenY, final float blueX, final float blueY)
    '''
def getChromaticity():
    '''    public float[] getChromaticity()
    '''
def unsetChromaticity():
    '''    public void unsetChromaticity()
    '''
def isChromaticitySet():
    '''    public boolean isChromaticitySet()
    '''
def setGamma():
    '''    public void setGamma(final float gamma)
    '''
def getGamma():
    '''    public float getGamma()
    '''
def unsetGamma():
    '''    public void unsetGamma()
    '''
def isGammaSet():
    '''    public boolean isGammaSet()
    '''
def setPaletteHistogram():
    '''    public void setPaletteHistogram(final int[] paletteHistogram)
    '''
def getPaletteHistogram():
    '''    public int[] getPaletteHistogram()
    '''
def unsetPaletteHistogram():
    '''    public void unsetPaletteHistogram()
    '''
def isPaletteHistogramSet():
    '''    public boolean isPaletteHistogramSet()
    '''
def setICCProfileData():
    '''    public void setICCProfileData(final byte[] iccProfileData)
    '''
def getICCProfileData():
    '''    public byte[] getICCProfileData()
    '''
def unsetICCProfileData():
    '''    public void unsetICCProfileData()
    '''
def isICCProfileDataSet():
    '''    public boolean isICCProfileDataSet()
    '''
def setPhysicalDimension():
    '''    public void setPhysicalDimension(final int[] physicalDimension)
    public void setPhysicalDimension(final int xPixelsPerUnit, final int yPixelsPerUnit, final int unitSpecifier)
    '''
def getPhysicalDimension():
    '''    public int[] getPhysicalDimension()
    '''
def unsetPhysicalDimension():
    '''    public void unsetPhysicalDimension()
    '''
def isPhysicalDimensionSet():
    '''    public boolean isPhysicalDimensionSet()
    '''
def setSuggestedPalette():
    '''    public void setSuggestedPalette(final PNGSuggestedPaletteEntry[] palette)
    '''
def getSuggestedPalette():
    '''    public PNGSuggestedPaletteEntry[] getSuggestedPalette()
    '''
def unsetSuggestedPalette():
    '''    public void unsetSuggestedPalette()
    '''
def isSuggestedPaletteSet():
    '''    public boolean isSuggestedPaletteSet()
    '''
def setSignificantBits():
    '''    public void setSignificantBits(final int[] significantBits)
    '''
def getSignificantBits():
    '''    public int[] getSignificantBits()
    '''
def unsetSignificantBits():
    '''    public void unsetSignificantBits()
    '''
def isSignificantBitsSet():
    '''    public boolean isSignificantBitsSet()
    '''
def setSRGBIntent():
    '''    public void setSRGBIntent(final int srgbIntent)
    '''
def getSRGBIntent():
    '''    public int getSRGBIntent()
    '''
def unsetSRGBIntent():
    '''    public void unsetSRGBIntent()
    '''
def isSRGBIntentSet():
    '''    public boolean isSRGBIntentSet()
    '''
def setText():
    '''    public void setText(final String[] text)
    '''
def getText():
    '''    public String[] getText()
    '''
def unsetText():
    '''    public void unsetText()
    '''
def isTextSet():
    '''    public boolean isTextSet()
    '''
def setModificationTime():
    '''    public void setModificationTime(final Date modificationTime)
    '''
def getModificationTime():
    '''    public Date getModificationTime()
    '''
def unsetModificationTime():
    '''    public void unsetModificationTime()
    '''
def isModificationTimeSet():
    '''    public boolean isModificationTimeSet()
    '''
def unsetTransparency():
    '''    public void unsetTransparency()
    '''
def isTransparencySet():
    '''    public boolean isTransparencySet()
    '''
def setCompressedText():
    '''    public void setCompressedText(final String[] text)
    '''
def getCompressedText():
    '''    public String[] getCompressedText()
    '''
def unsetCompressedText():
    '''    public void unsetCompressedText()
    '''
def isCompressedTextSet():
    '''    public boolean isCompressedTextSet()
    '''
def addPrivateChunk():
    '''    public synchronized void addPrivateChunk(final String type, final byte[] data)
    '''
def getNumPrivateChunks():
    '''    public synchronized int getNumPrivateChunks()
    '''
def getPrivateChunkType():
    '''    public synchronized String getPrivateChunkType(final int index)
    '''
def getPrivateChunkData():
    '''    public synchronized byte[] getPrivateChunkData(final int index)
    '''
def removeUnsafeToCopyPrivateChunks():
    '''    public synchronized void removeUnsafeToCopyPrivateChunks()
    '''
def removeAllPrivateChunks():
    '''    public synchronized void removeAllPrivateChunks()
    '''
def paethPredictor():
    '''    public static int paethPredictor(final int a, final int b, final int c)
    '''
def filterRow():
    '''    public int filterRow(final byte[] currRow, final byte[] prevRow, final byte[][] scratchRows, final int bytesPerRow, final int bytesPerPixel)
    '''
def setBitDepth():
    '''    public void setBitDepth(final int bitDepth)
    public void setBitDepth(final int bitDepth)
    public void setBitDepth(final int bitDepth)
    '''
def setPalette():
    '''    public void setPalette(final int[] rgb)
    '''
def getPalette():
    '''    public int[] getPalette()
    '''
def unsetPalette():
    '''    public void unsetPalette()
    '''
def isPaletteSet():
    '''    public boolean isPaletteSet()
    '''
def setBackgroundPaletteIndex():
    '''    public void setBackgroundPaletteIndex(final int index)
    '''
def getBackgroundPaletteIndex():
    '''    public int getBackgroundPaletteIndex()
    '''
def setPaletteTransparency():
    '''    public void setPaletteTransparency(final byte[] alpha)
    '''
def getPaletteTransparency():
    '''    public byte[] getPaletteTransparency()
    '''
def setBackgroundGray():
    '''    public void setBackgroundGray(final int gray)
    '''
def getBackgroundGray():
    '''    public int getBackgroundGray()
    '''
def setTransparentGray():
    '''    public void setTransparentGray(final int transparentGray)
    '''
def getTransparentGray():
    '''    public int getTransparentGray()
    '''
def setBitShift():
    '''    public void setBitShift(final int bitShift)
    '''
def getBitShift():
    '''    public int getBitShift()
    '''
def unsetBitShift():
    '''    public void unsetBitShift()
    '''
def isBitShiftSet():
    '''    public boolean isBitShiftSet()
    '''
def isBitDepthSet():
    '''    public boolean isBitDepthSet()
    '''
def setBackgroundRGB():
    '''    public void setBackgroundRGB(final int[] rgb)
    '''
def getBackgroundRGB():
    '''    public int[] getBackgroundRGB()
    '''
def setTransparentRGB():
    '''    public void setTransparentRGB(final int[] transparentRGB)
    '''
def getTransparentRGB():
    '''    public int[] getTransparentRGB()
    '''
