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
'''public PNGEncodeParam()
'''
pass
def getDefaultEncodeParam():
'''public static PNGEncodeParam getDefaultEncodeParam(final RenderedImage im)
'''
pass
def getBitDepth():
'''public int getBitDepth()
'''
pass
def unsetBitDepth():
'''public void unsetBitDepth()
'''
pass
def setInterlacing():
'''public void setInterlacing(final boolean useInterlacing)
'''
pass
def getInterlacing():
'''public boolean getInterlacing()
'''
pass
def unsetBackground():
'''public void unsetBackground()
public void unsetBackground()
public void unsetBackground()
public void unsetBackground()
'''
pass
def isBackgroundSet():
'''public boolean isBackgroundSet()
public boolean isBackgroundSet()
public boolean isBackgroundSet()
public boolean isBackgroundSet()
'''
pass
def setChromaticity():
'''public void setChromaticity(final float[] chromaticity)
public void setChromaticity(final float whitePointX, final float whitePointY, final float redX, final float redY, final float greenX, final float greenY, final float blueX, final float blueY)
'''
pass
def getChromaticity():
'''public float[] getChromaticity()
'''
pass
def unsetChromaticity():
'''public void unsetChromaticity()
'''
pass
def isChromaticitySet():
'''public boolean isChromaticitySet()
'''
pass
def setGamma():
'''public void setGamma(final float gamma)
'''
pass
def getGamma():
'''public float getGamma()
'''
pass
def unsetGamma():
'''public void unsetGamma()
'''
pass
def isGammaSet():
'''public boolean isGammaSet()
'''
pass
def setPaletteHistogram():
'''public void setPaletteHistogram(final int[] paletteHistogram)
'''
pass
def getPaletteHistogram():
'''public int[] getPaletteHistogram()
'''
pass
def unsetPaletteHistogram():
'''public void unsetPaletteHistogram()
'''
pass
def isPaletteHistogramSet():
'''public boolean isPaletteHistogramSet()
'''
pass
def setICCProfileData():
'''public void setICCProfileData(final byte[] iccProfileData)
'''
pass
def getICCProfileData():
'''public byte[] getICCProfileData()
'''
pass
def unsetICCProfileData():
'''public void unsetICCProfileData()
'''
pass
def isICCProfileDataSet():
'''public boolean isICCProfileDataSet()
'''
pass
def setPhysicalDimension():
'''public void setPhysicalDimension(final int[] physicalDimension)
public void setPhysicalDimension(final int xPixelsPerUnit, final int yPixelsPerUnit, final int unitSpecifier)
'''
pass
def getPhysicalDimension():
'''public int[] getPhysicalDimension()
'''
pass
def unsetPhysicalDimension():
'''public void unsetPhysicalDimension()
'''
pass
def isPhysicalDimensionSet():
'''public boolean isPhysicalDimensionSet()
'''
pass
def setSuggestedPalette():
'''public void setSuggestedPalette(final PNGSuggestedPaletteEntry[] palette)
'''
pass
def getSuggestedPalette():
'''public PNGSuggestedPaletteEntry[] getSuggestedPalette()
'''
pass
def unsetSuggestedPalette():
'''public void unsetSuggestedPalette()
'''
pass
def isSuggestedPaletteSet():
'''public boolean isSuggestedPaletteSet()
'''
pass
def setSignificantBits():
'''public void setSignificantBits(final int[] significantBits)
'''
pass
def getSignificantBits():
'''public int[] getSignificantBits()
'''
pass
def unsetSignificantBits():
'''public void unsetSignificantBits()
'''
pass
def isSignificantBitsSet():
'''public boolean isSignificantBitsSet()
'''
pass
def setSRGBIntent():
'''public void setSRGBIntent(final int srgbIntent)
'''
pass
def getSRGBIntent():
'''public int getSRGBIntent()
'''
pass
def unsetSRGBIntent():
'''public void unsetSRGBIntent()
'''
pass
def isSRGBIntentSet():
'''public boolean isSRGBIntentSet()
'''
pass
def setText():
'''public void setText(final String[] text)
'''
pass
def getText():
'''public String[] getText()
'''
pass
def unsetText():
'''public void unsetText()
'''
pass
def isTextSet():
'''public boolean isTextSet()
'''
pass
def setModificationTime():
'''public void setModificationTime(final Date modificationTime)
'''
pass
def getModificationTime():
'''public Date getModificationTime()
'''
pass
def unsetModificationTime():
'''public void unsetModificationTime()
'''
pass
def isModificationTimeSet():
'''public boolean isModificationTimeSet()
'''
pass
def unsetTransparency():
'''public void unsetTransparency()
'''
pass
def isTransparencySet():
'''public boolean isTransparencySet()
'''
pass
def setCompressedText():
'''public void setCompressedText(final String[] text)
'''
pass
def getCompressedText():
'''public String[] getCompressedText()
'''
pass
def unsetCompressedText():
'''public void unsetCompressedText()
'''
pass
def isCompressedTextSet():
'''public boolean isCompressedTextSet()
'''
pass
def addPrivateChunk():
'''public synchronized void addPrivateChunk(final String type, final byte[] data)
'''
pass
def getNumPrivateChunks():
'''public synchronized int getNumPrivateChunks()
'''
pass
def getPrivateChunkType():
'''public synchronized String getPrivateChunkType(final int index)
'''
pass
def getPrivateChunkData():
'''public synchronized byte[] getPrivateChunkData(final int index)
'''
pass
def removeUnsafeToCopyPrivateChunks():
'''public synchronized void removeUnsafeToCopyPrivateChunks()
'''
pass
def removeAllPrivateChunks():
'''public synchronized void removeAllPrivateChunks()
'''
pass
def paethPredictor():
'''public static int paethPredictor(final int a, final int b, final int c)
'''
pass
def filterRow():
'''public int filterRow(final byte[] currRow, final byte[] prevRow, final byte[][] scratchRows, final int bytesPerRow, final int bytesPerPixel)
'''
pass
def setBitDepth():
'''public void setBitDepth(final int bitDepth)
public void setBitDepth(final int bitDepth)
public void setBitDepth(final int bitDepth)
'''
pass
def setPalette():
'''public void setPalette(final int[] rgb)
'''
pass
def getPalette():
'''public int[] getPalette()
'''
pass
def unsetPalette():
'''public void unsetPalette()
'''
pass
def isPaletteSet():
'''public boolean isPaletteSet()
'''
pass
def setBackgroundPaletteIndex():
'''public void setBackgroundPaletteIndex(final int index)
'''
pass
def getBackgroundPaletteIndex():
'''public int getBackgroundPaletteIndex()
'''
pass
def setPaletteTransparency():
'''public void setPaletteTransparency(final byte[] alpha)
'''
pass
def getPaletteTransparency():
'''public byte[] getPaletteTransparency()
'''
pass
def setBackgroundGray():
'''public void setBackgroundGray(final int gray)
'''
pass
def getBackgroundGray():
'''public int getBackgroundGray()
'''
pass
def setTransparentGray():
'''public void setTransparentGray(final int transparentGray)
'''
pass
def getTransparentGray():
'''public int getTransparentGray()
'''
pass
def setBitShift():
'''public void setBitShift(final int bitShift)
'''
pass
def getBitShift():
'''public int getBitShift()
'''
pass
def unsetBitShift():
'''public void unsetBitShift()
'''
pass
def isBitShiftSet():
'''public boolean isBitShiftSet()
'''
pass
def isBitDepthSet():
'''public boolean isBitDepthSet()
'''
pass
def setBackgroundRGB():
'''public void setBackgroundRGB(final int[] rgb)
'''
pass
def getBackgroundRGB():
'''public int[] getBackgroundRGB()
'''
pass
def setTransparentRGB():
'''public void setTransparentRGB(final int[] transparentRGB)
'''
pass
def getTransparentRGB():
'''public int[] getTransparentRGB()
'''
pass
