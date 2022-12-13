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
pass
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
pass
def setAlignment():
'''public void setAlignment(final int alignment)
'''
pass
def setAlt():
'''public void setAlt(final String alt)
'''
pass
def setAbsolutePosition():
'''public void setAbsolutePosition(final float absoluteX, final float absoluteY)
'''
pass
def scaleAbsolute():
'''public void scaleAbsolute(final float newWidth, final float newHeight)
'''
pass
def scaleAbsoluteWidth():
'''public void scaleAbsoluteWidth(final float newWidth)
'''
pass
def scaleAbsoluteHeight():
'''public void scaleAbsoluteHeight(final float newHeight)
'''
pass
def scalePercent():
'''public void scalePercent(final float percent)
public void scalePercent(final float percentX, final float percentY)
'''
pass
def scaleToFit():
'''public void scaleToFit(final float fitWidth, final float fitHeight)
'''
pass
def setRotation():
'''public void setRotation(final float r)
'''
pass
def setRotationDegrees():
'''public void setRotationDegrees(final float deg)
'''
pass
def setAnnotation():
'''public void setAnnotation(final Annotation annotation)
'''
pass
def annotation():
'''public Annotation annotation()
'''
pass
def bpc():
'''public int bpc()
'''
pass
def rawData():
'''public byte[] rawData()
'''
pass
def templateData():
'''public PdfTemplate templateData()
'''
pass
def setTemplateData():
'''public void setTemplateData(final PdfTemplate template)
'''
pass
def hasAbsolutePosition():
'''public boolean hasAbsolutePosition()
'''
pass
def hasAbsoluteX():
'''public boolean hasAbsoluteX()
'''
pass
def absoluteX():
'''public float absoluteX()
'''
pass
def absoluteY():
'''public float absoluteY()
'''
pass
def type():
'''public int type()
'''
pass
def isJpeg():
'''public boolean isJpeg()
'''
pass
def isImgRaw():
'''public boolean isImgRaw()
'''
pass
def isImgTemplate():
'''public boolean isImgTemplate()
'''
pass
def url():
'''public URL url()
'''
pass
def alignment():
'''public int alignment()
'''
pass
def alt():
'''public String alt()
'''
pass
def scaledWidth():
'''public float scaledWidth()
'''
pass
def scaledHeight():
'''public float scaledHeight()
'''
pass
def colorspace():
'''public int colorspace()
'''
pass
def matrix():
'''public float[] matrix()
'''
pass
def skip():
'''public static void skip(final InputStream is, int size)
'''
pass
def toURL():
'''public static URL toURL(final String filename)
'''
pass
def getTransparency():
'''public int[] getTransparency()
'''
pass
def setTransparency():
'''public void setTransparency(final int[] transparency)
'''
pass
def isTag():
'''public static boolean isTag(final String tag)
'''
pass
def plainWidth():
'''public float plainWidth()
'''
pass
def plainHeight():
'''public float plainHeight()
'''
pass
def getMySerialId():
'''public Long getMySerialId()
'''
pass
def getDpiX():
'''public int getDpiX()
'''
pass
def getDpiY():
'''public int getDpiY()
'''
pass
def setDpi():
'''public void setDpi(final int dpiX, final int dpiY)
'''
pass
def isMaskCandidate():
'''public boolean isMaskCandidate()
'''
pass
def makeMask():
'''public void makeMask()
'''
pass
def setImageMask():
'''public void setImageMask(final Image mask)
'''
pass
def getImageMask():
'''public Image getImageMask()
'''
pass
def isMask():
'''public boolean isMask()
'''
pass
def setInvertMask():
'''public void setInvertMask(final boolean invert)
'''
pass
def isInvertMask():
'''public boolean isInvertMask()
'''
pass
def isInverted():
'''public boolean isInverted()
'''
pass
def setInverted():
'''public void setInverted(final boolean invert)
'''
pass
def isInterpolation():
'''public boolean isInterpolation()
'''
pass
def setInterpolation():
'''public void setInterpolation(final boolean interpolation)
'''
pass
def setMarkupAttribute():
'''public void setMarkupAttribute(final String name, final String value)
'''
pass
def setMarkupAttributes():
'''public void setMarkupAttributes(final Properties markupAttributes)
'''
pass
def getMarkupAttribute():
'''public String getMarkupAttribute(final String name)
'''
pass
def getMarkupAttributeNames():
'''public Set getMarkupAttributeNames()
'''
pass
def getMarkupAttributes():
'''public Properties getMarkupAttributes()
'''
pass
def tagICC():
'''public void tagICC(final ICC_Profile profile)
'''
pass
def hasICCProfile():
'''public boolean hasICCProfile()
'''
pass
def getICCProfile():
'''public ICC_Profile getICCProfile()
'''
pass
def isDeflated():
'''public boolean isDeflated()
'''
pass
def setDeflated():
'''public void setDeflated(final boolean deflated)
'''
pass
def getAdditional():
'''public PdfDictionary getAdditional()
'''
pass
def setAdditional():
'''public void setAdditional(final PdfDictionary additional)
'''
pass
def isSmask():
'''public boolean isSmask()
'''
pass
def setSmask():
'''public void setSmask(final boolean smask)
'''
pass
def getXYRatio():
'''public float getXYRatio()
'''
pass
def setXYRatio():
'''public void setXYRatio(final float XYRatio)
'''
pass
def indentationLeft():
'''public float indentationLeft()
'''
pass
def indentationRight():
'''public float indentationRight()
'''
pass
def setIndentationLeft():
'''public void setIndentationLeft(final float f)
'''
pass
def setIndentationRight():
'''public void setIndentationRight(final float f)
'''
pass
def getOriginalType():
'''public int getOriginalType()
'''
pass
def setOriginalType():
'''public void setOriginalType(final int originalType)
'''
pass
def getOriginalData():
'''public byte[] getOriginalData()
'''
pass
def setOriginalData():
'''public void setOriginalData(final byte[] originalData)
'''
pass
def setUrl():
'''public void setUrl(final URL url)
'''
pass
def setSpacingBefore():
'''public void setSpacingBefore(final float spacing)
'''
pass
def setSpacingAfter():
'''public void setSpacingAfter(final float spacing)
'''
pass
def spacingBefore():
'''public float spacingBefore()
'''
pass
def spacingAfter():
'''public float spacingAfter()
'''
pass
def getWidthPercentage():
'''public float getWidthPercentage()
'''
pass
def setWidthPercentage():
'''public void setWidthPercentage(final float widthPercentage)
'''
pass
def getLayer():
'''public PdfOCG getLayer()
'''
pass
def setLayer():
'''public void setLayer(final PdfOCG layer)
'''
pass
