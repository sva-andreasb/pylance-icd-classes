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
def ():
    '''returns Image\n\n
    (final URL url)\n
    '''
def setAlignment():
    '''returns None\n\n
    setAlignment(final int alignment)\n
    '''
def setAlt():
    '''returns None\n\n
    setAlt(final String alt)\n
    '''
def setAbsolutePosition():
    '''returns None\n\n
    setAbsolutePosition(final float absoluteX, final float absoluteY)\n
    '''
def scaleAbsolute():
    '''returns None\n\n
    scaleAbsolute(final float newWidth, final float newHeight)\n
    '''
def scaleAbsoluteWidth():
    '''returns None\n\n
    scaleAbsoluteWidth(final float newWidth)\n
    '''
def scaleAbsoluteHeight():
    '''returns None\n\n
    scaleAbsoluteHeight(final float newHeight)\n
    '''
def scalePercent():
    '''returns None\n\n
    scalePercent(final float percent)\n
    scalePercent(final float percentX, final float percentY)\n
    '''
def scaleToFit():
    '''returns None\n\n
    scaleToFit(final float fitWidth, final float fitHeight)\n
    '''
def setRotation():
    '''returns None\n\n
    setRotation(final float r)\n
    '''
def setRotationDegrees():
    '''returns None\n\n
    setRotationDegrees(final float deg)\n
    '''
def setAnnotation():
    '''returns None\n\n
    setAnnotation(final Annotation annotation)\n
    '''
def annotation():
    '''returns Annotation\n\n
    annotation()\n
    '''
def bpc():
    '''returns int\n\n
    bpc()\n
    '''
def rawData():
    '''returns byte[]\n\n
    rawData()\n
    '''
def templateData():
    '''returns PdfTemplate\n\n
    templateData()\n
    '''
def setTemplateData():
    '''returns None\n\n
    setTemplateData(final PdfTemplate template)\n
    '''
def hasAbsolutePosition():
    '''returns boolean\n\n
    hasAbsolutePosition()\n
    '''
def hasAbsoluteX():
    '''returns boolean\n\n
    hasAbsoluteX()\n
    '''
def absoluteX():
    '''returns float\n\n
    absoluteX()\n
    '''
def absoluteY():
    '''returns float\n\n
    absoluteY()\n
    '''
def type():
    '''returns int\n\n
    type()\n
    '''
def isJpeg():
    '''returns boolean\n\n
    isJpeg()\n
    '''
def isImgRaw():
    '''returns boolean\n\n
    isImgRaw()\n
    '''
def isImgTemplate():
    '''returns boolean\n\n
    isImgTemplate()\n
    '''
def url():
    '''returns URL\n\n
    url()\n
    '''
def alignment():
    '''returns int\n\n
    alignment()\n
    '''
def alt():
    '''returns String\n\n
    alt()\n
    '''
def scaledWidth():
    '''returns float\n\n
    scaledWidth()\n
    '''
def scaledHeight():
    '''returns float\n\n
    scaledHeight()\n
    '''
def colorspace():
    '''returns int\n\n
    colorspace()\n
    '''
def matrix():
    '''returns float[]\n\n
    matrix()\n
    '''
def getTransparency():
    '''returns int[]\n\n
    getTransparency()\n
    '''
def setTransparency():
    '''returns None\n\n
    setTransparency(final int[] transparency)\n
    '''
def plainWidth():
    '''returns float\n\n
    plainWidth()\n
    '''
def plainHeight():
    '''returns float\n\n
    plainHeight()\n
    '''
def getMySerialId():
    '''returns Long\n\n
    getMySerialId()\n
    '''
def getDpiX():
    '''returns int\n\n
    getDpiX()\n
    '''
def getDpiY():
    '''returns int\n\n
    getDpiY()\n
    '''
def setDpi():
    '''returns None\n\n
    setDpi(final int dpiX, final int dpiY)\n
    '''
def isMaskCandidate():
    '''returns boolean\n\n
    isMaskCandidate()\n
    '''
def makeMask():
    '''returns None\n\n
    makeMask()\n
    '''
def setImageMask():
    '''returns None\n\n
    setImageMask(final Image mask)\n
    '''
def getImageMask():
    '''returns Image\n\n
    getImageMask()\n
    '''
def isMask():
    '''returns boolean\n\n
    isMask()\n
    '''
def setInvertMask():
    '''returns None\n\n
    setInvertMask(final boolean invert)\n
    '''
def isInvertMask():
    '''returns boolean\n\n
    isInvertMask()\n
    '''
def isInverted():
    '''returns boolean\n\n
    isInverted()\n
    '''
def setInverted():
    '''returns None\n\n
    setInverted(final boolean invert)\n
    '''
def isInterpolation():
    '''returns boolean\n\n
    isInterpolation()\n
    '''
def setInterpolation():
    '''returns None\n\n
    setInterpolation(final boolean interpolation)\n
    '''
def setMarkupAttribute():
    '''returns None\n\n
    setMarkupAttribute(final String name, final String value)\n
    '''
def setMarkupAttributes():
    '''returns None\n\n
    setMarkupAttributes(final Properties markupAttributes)\n
    '''
def getMarkupAttribute():
    '''returns String\n\n
    getMarkupAttribute(final String name)\n
    '''
def getMarkupAttributeNames():
    '''returns Set\n\n
    getMarkupAttributeNames()\n
    '''
def getMarkupAttributes():
    '''returns Properties\n\n
    getMarkupAttributes()\n
    '''
def tagICC():
    '''returns None\n\n
    tagICC(final ICC_Profile profile)\n
    '''
def hasICCProfile():
    '''returns boolean\n\n
    hasICCProfile()\n
    '''
def getICCProfile():
    '''returns ICC_Profile\n\n
    getICCProfile()\n
    '''
def isDeflated():
    '''returns boolean\n\n
    isDeflated()\n
    '''
def setDeflated():
    '''returns None\n\n
    setDeflated(final boolean deflated)\n
    '''
def getAdditional():
    '''returns PdfDictionary\n\n
    getAdditional()\n
    '''
def setAdditional():
    '''returns None\n\n
    setAdditional(final PdfDictionary additional)\n
    '''
def isSmask():
    '''returns boolean\n\n
    isSmask()\n
    '''
def setSmask():
    '''returns None\n\n
    setSmask(final boolean smask)\n
    '''
def getXYRatio():
    '''returns float\n\n
    getXYRatio()\n
    '''
def setXYRatio():
    '''returns None\n\n
    setXYRatio(final float XYRatio)\n
    '''
def indentationLeft():
    '''returns float\n\n
    indentationLeft()\n
    '''
def indentationRight():
    '''returns float\n\n
    indentationRight()\n
    '''
def setIndentationLeft():
    '''returns None\n\n
    setIndentationLeft(final float f)\n
    '''
def setIndentationRight():
    '''returns None\n\n
    setIndentationRight(final float f)\n
    '''
def getOriginalType():
    '''returns int\n\n
    getOriginalType()\n
    '''
def setOriginalType():
    '''returns None\n\n
    setOriginalType(final int originalType)\n
    '''
def getOriginalData():
    '''returns byte[]\n\n
    getOriginalData()\n
    '''
def setOriginalData():
    '''returns None\n\n
    setOriginalData(final byte[] originalData)\n
    '''
def setUrl():
    '''returns None\n\n
    setUrl(final URL url)\n
    '''
def setSpacingBefore():
    '''returns None\n\n
    setSpacingBefore(final float spacing)\n
    '''
def setSpacingAfter():
    '''returns None\n\n
    setSpacingAfter(final float spacing)\n
    '''
def spacingBefore():
    '''returns float\n\n
    spacingBefore()\n
    '''
def spacingAfter():
    '''returns float\n\n
    spacingAfter()\n
    '''
def getWidthPercentage():
    '''returns float\n\n
    getWidthPercentage()\n
    '''
def setWidthPercentage():
    '''returns None\n\n
    setWidthPercentage(final float widthPercentage)\n
    '''
def getLayer():
    '''returns PdfOCG\n\n
    getLayer()\n
    '''
def setLayer():
    '''returns None\n\n
    setLayer(final PdfOCG layer)\n
    '''
