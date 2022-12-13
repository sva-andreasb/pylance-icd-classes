def makeLinear_sRGBCM():
'''public static ColorModel makeLinear_sRGBCM(final boolean premult)
'''
pass
def makeLinearBufferedImage():
'''public static BufferedImage makeLinearBufferedImage(final int width, final int height, final boolean premult)
'''
pass
def convertToLsRGB():
'''public static CachableRed convertToLsRGB(final CachableRed src)
'''
pass
def convertTosRGB():
'''public static CachableRed convertTosRGB(final CachableRed src)
'''
pass
def wrap():
'''public static CachableRed wrap(final RenderedImage ri)
'''
pass
def copyData_INT_PACK():
'''public static void copyData_INT_PACK(final Raster src, final WritableRaster dst)
'''
pass
def copyData_FALLBACK():
'''public static void copyData_FALLBACK(final Raster src, final WritableRaster dst)
'''
pass
def copyData():
'''public static void copyData(final Raster src, final WritableRaster dst)
public static void copyData(final BufferedImage src, final BufferedImage dst)
public static void copyData(final BufferedImage src, final Rectangle srcRect, final BufferedImage dst, final Point destP)
'''
pass
def copyRaster():
'''public static WritableRaster copyRaster(final Raster ras)
public static WritableRaster copyRaster(final Raster ras, final int minX, final int minY)
'''
pass
def makeRasterWritable():
'''public static WritableRaster makeRasterWritable(final Raster ras)
public static WritableRaster makeRasterWritable(final Raster ras, final int minX, final int minY)
'''
pass
def coerceColorModel():
'''public static ColorModel coerceColorModel(final ColorModel cm, final boolean newAlphaPreMult)
'''
pass
def coerceData():
'''public static ColorModel coerceData(final WritableRaster wr, final ColorModel cm, final boolean newAlphaPreMult)
'''
pass
def multiplyAlpha():
'''public static void multiplyAlpha(final WritableRaster wr)
'''
pass
def divideAlpha():
'''public static void divideAlpha(final WritableRaster wr)
'''
pass
def copyBand():
'''public static void copyBand(final Raster src, final int srcBand, final WritableRaster dst, final int dstBand)
public static void copyBand(final Raster src, Rectangle sR, final int sBand, final WritableRaster dst, Rectangle dR, final int dBand)
'''
pass
def is_INT_PACK_Data():
'''public static boolean is_INT_PACK_Data(final SampleModel sm, final boolean requireAlpha)
'''
pass
def is_BYTE_COMP_Data():
'''public static boolean is_BYTE_COMP_Data(final SampleModel sm)
'''
pass
def getAlphaRaster():
'''public static Raster getAlphaRaster(final RenderedImage image)
'''
pass
