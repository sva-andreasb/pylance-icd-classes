def makeLinear_sRGBCM():
    '''    public static ColorModel makeLinear_sRGBCM(final boolean premult)
    '''
def makeLinearBufferedImage():
    '''    public static BufferedImage makeLinearBufferedImage(final int width, final int height, final boolean premult)
    '''
def convertToLsRGB():
    '''    public static CachableRed convertToLsRGB(final CachableRed src)
    '''
def convertTosRGB():
    '''    public static CachableRed convertTosRGB(final CachableRed src)
    '''
def wrap():
    '''    public static CachableRed wrap(final RenderedImage ri)
    '''
def copyData_INT_PACK():
    '''    public static void copyData_INT_PACK(final Raster src, final WritableRaster dst)
    '''
def copyData_FALLBACK():
    '''    public static void copyData_FALLBACK(final Raster src, final WritableRaster dst)
    '''
def copyData():
    '''    public static void copyData(final Raster src, final WritableRaster dst)
    public static void copyData(final BufferedImage src, final BufferedImage dst)
    public static void copyData(final BufferedImage src, final Rectangle srcRect, final BufferedImage dst, final Point destP)
    '''
def copyRaster():
    '''    public static WritableRaster copyRaster(final Raster ras)
    public static WritableRaster copyRaster(final Raster ras, final int minX, final int minY)
    '''
def makeRasterWritable():
    '''    public static WritableRaster makeRasterWritable(final Raster ras)
    public static WritableRaster makeRasterWritable(final Raster ras, final int minX, final int minY)
    '''
def coerceColorModel():
    '''    public static ColorModel coerceColorModel(final ColorModel cm, final boolean newAlphaPreMult)
    '''
def coerceData():
    '''    public static ColorModel coerceData(final WritableRaster wr, final ColorModel cm, final boolean newAlphaPreMult)
    '''
def multiplyAlpha():
    '''    public static void multiplyAlpha(final WritableRaster wr)
    '''
def divideAlpha():
    '''    public static void divideAlpha(final WritableRaster wr)
    '''
def copyBand():
    '''    public static void copyBand(final Raster src, final int srcBand, final WritableRaster dst, final int dstBand)
    public static void copyBand(final Raster src, Rectangle sR, final int sBand, final WritableRaster dst, Rectangle dR, final int dBand)
    '''
def is_INT_PACK_Data():
    '''    public static boolean is_INT_PACK_Data(final SampleModel sm, final boolean requireAlpha)
    '''
def is_BYTE_COMP_Data():
    '''    public static boolean is_BYTE_COMP_Data(final SampleModel sm)
    '''
def getAlphaRaster():
    '''    public static Raster getAlphaRaster(final RenderedImage image)
    '''
