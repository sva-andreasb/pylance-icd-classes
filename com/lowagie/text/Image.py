DEFAULT = "int  0"
RIGHT = "int  2"
LEFT = "int  0"
MIDDLE = "int  1"
TEXTWRAP = "int  4"
UNDERLYING = "int  8"
AX = "int  0"
AY = "int  1"
BX = "int  2"
BY = "int  3"
CX = "int  4"
CY = "int  5"
DX = "int  6"
DY = "int  7"
ORIGINAL_NONE = "int  0"
ORIGINAL_JPEG = "int  1"
ORIGINAL_PNG = "int  2"
ORIGINAL_GIF = "int  3"
ORIGINAL_BMP = "int  4"
ORIGINAL_TIFF = "int  5"
ORIGINAL_WMF = "int  6"
ORIGINAL_PS = "int  7"
def Image():
    '''public Image(final URL url)
    '''
def getInstance():
    '''public static Image getInstance(final Image image)
    public static Image getInstance(final URL url)
    public static Image getInstance(final byte[] imgb)
    public static Image getInstance(final java.awt.Image image, final Color color, final boolean forceBW)
    public static Image getInstance(final java.awt.Image image, final Color color)
    public static Image getInstance(final String filename)
    public static Image getInstance(final int width, final int height, final int components, final int bpc, final byte[] data)
    public static Image getInstance(final PdfTemplate template)
    public static Image getInstance(final int width, final int height, final boolean reverseBits, final int typeCCITT, final int parameters, final byte[] data)
    public static Image getInstance(final int width, final int height, final boolean reverseBits, final int typeCCITT, final int parameters, final byte[] data, final int[] transparency)
    public static Image getInstance(final int width, final int height, final int components, final int bpc, final byte[] data, final int[] transparency)
    public static Image getInstance(final Properties attributes)
    '''
def setAlignment():
    '''public void setAlignment(final int alignment)
    '''
def setAlt():
    '''public void setAlt(final String alt)
    '''
def setAbsolutePosition():
    '''public void setAbsolutePosition(final float absoluteX, final float absoluteY)
    '''
def scaleAbsolute():
    '''public void scaleAbsolute(final float newWidth, final float newHeight)
    '''
def scaleAbsoluteWidth():
    '''public void scaleAbsoluteWidth(final float newWidth)
    '''
def scaleAbsoluteHeight():
    '''public void scaleAbsoluteHeight(final float newHeight)
    '''
def scalePercent():
    '''public void scalePercent(final float percent)
    public void scalePercent(final float percentX, final float percentY)
    '''
def scaleToFit():
    '''public void scaleToFit(final float fitWidth, final float fitHeight)
    '''
def setRotation():
    '''public void setRotation(final float r)
    '''
def setRotationDegrees():
    '''public void setRotationDegrees(final float deg)
    '''
def setAnnotation():
    '''public void setAnnotation(final Annotation annotation)
    '''
def annotation():
    '''public Annotation annotation()
    '''
def bpc():
    '''public int bpc()
    '''
def rawData():
    '''public byte[] rawData()
    '''
def templateData():
    '''public PdfTemplate templateData()
    '''
def setTemplateData():
    '''public void setTemplateData(final PdfTemplate template)
    '''
def hasAbsolutePosition():
    '''public boolean hasAbsolutePosition()
    '''
def hasAbsoluteX():
    '''public boolean hasAbsoluteX()
    '''
def absoluteX():
    '''public float absoluteX()
    '''
def absoluteY():
    '''public float absoluteY()
    '''
def type():
    '''public int type()
    '''
def isJpeg():
    '''public boolean isJpeg()
    '''
def isImgRaw():
    '''public boolean isImgRaw()
    '''
def isImgTemplate():
    '''public boolean isImgTemplate()
    '''
def url():
    '''public URL url()
    '''
def alignment():
    '''public int alignment()
    '''
def alt():
    '''public String alt()
    '''
def scaledWidth():
    '''public float scaledWidth()
    '''
def scaledHeight():
    '''public float scaledHeight()
    '''
def colorspace():
    '''public int colorspace()
    '''
def matrix():
    '''public float[] matrix()
    '''
def skip():
    '''public static void skip(final InputStream is, int size)
    '''
def toURL():
    '''public static URL toURL(final String filename)
    '''
def getTransparency():
    '''public int[] getTransparency()
    '''
def setTransparency():
    '''public void setTransparency(final int[] transparency)
    '''
def isTag():
    '''public static boolean isTag(final String tag)
    '''
def plainWidth():
    '''public float plainWidth()
    '''
def plainHeight():
    '''public float plainHeight()
    '''
def getMySerialId():
    '''public Long getMySerialId()
    '''
def getDpiX():
    '''public int getDpiX()
    '''
def getDpiY():
    '''public int getDpiY()
    '''
def setDpi():
    '''public void setDpi(final int dpiX, final int dpiY)
    '''
def isMaskCandidate():
    '''public boolean isMaskCandidate()
    '''
def makeMask():
    '''public void makeMask()
    '''
def setImageMask():
    '''public void setImageMask(final Image mask)
    '''
def getImageMask():
    '''public Image getImageMask()
    '''
def isMask():
    '''public boolean isMask()
    '''
def setInvertMask():
    '''public void setInvertMask(final boolean invert)
    '''
def isInvertMask():
    '''public boolean isInvertMask()
    '''
def isInverted():
    '''public boolean isInverted()
    '''
def setInverted():
    '''public void setInverted(final boolean invert)
    '''
def isInterpolation():
    '''public boolean isInterpolation()
    '''
def setInterpolation():
    '''public void setInterpolation(final boolean interpolation)
    '''
def setMarkupAttribute():
    '''public void setMarkupAttribute(final String name, final String value)
    '''
def setMarkupAttributes():
    '''public void setMarkupAttributes(final Properties markupAttributes)
    '''
def getMarkupAttribute():
    '''public String getMarkupAttribute(final String name)
    '''
def getMarkupAttributeNames():
    '''public Set getMarkupAttributeNames()
    '''
def getMarkupAttributes():
    '''public Properties getMarkupAttributes()
    '''
def tagICC():
    '''public void tagICC(final ICC_Profile profile)
    '''
def hasICCProfile():
    '''public boolean hasICCProfile()
    '''
def getICCProfile():
    '''public ICC_Profile getICCProfile()
    '''
def isDeflated():
    '''public boolean isDeflated()
    '''
def setDeflated():
    '''public void setDeflated(final boolean deflated)
    '''
def getAdditional():
    '''public PdfDictionary getAdditional()
    '''
def setAdditional():
    '''public void setAdditional(final PdfDictionary additional)
    '''
def isSmask():
    '''public boolean isSmask()
    '''
def setSmask():
    '''public void setSmask(final boolean smask)
    '''
def getXYRatio():
    '''public float getXYRatio()
    '''
def setXYRatio():
    '''public void setXYRatio(final float XYRatio)
    '''
def indentationLeft():
    '''public float indentationLeft()
    '''
def indentationRight():
    '''public float indentationRight()
    '''
def setIndentationLeft():
    '''public void setIndentationLeft(final float f)
    '''
def setIndentationRight():
    '''public void setIndentationRight(final float f)
    '''
def getOriginalType():
    '''public int getOriginalType()
    '''
def setOriginalType():
    '''public void setOriginalType(final int originalType)
    '''
def getOriginalData():
    '''public byte[] getOriginalData()
    '''
def setOriginalData():
    '''public void setOriginalData(final byte[] originalData)
    '''
def setUrl():
    '''public void setUrl(final URL url)
    '''
def setSpacingBefore():
    '''public void setSpacingBefore(final float spacing)
    '''
def setSpacingAfter():
    '''public void setSpacingAfter(final float spacing)
    '''
def spacingBefore():
    '''public float spacingBefore()
    '''
def spacingAfter():
    '''public float spacingAfter()
    '''
def getWidthPercentage():
    '''public float getWidthPercentage()
    '''
def setWidthPercentage():
    '''public void setWidthPercentage(final float widthPercentage)
    '''
def getLayer():
    '''public PdfOCG getLayer()
    '''
def setLayer():
    '''public void setLayer(final PdfOCG layer)
    '''
