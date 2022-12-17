AR_NOVOWEL = "int  1"
AR_COMPOSEDTASHKEEL = "int  4"
AR_LIG = "int  8"
DIGITS_EN2AN = "int  32"
DIGITS_AN2EN = "int  64"
DIGITS_EN2AN_INIT_LR = "int  96"
DIGITS_EN2AN_INIT_AL = "int  128"
DIGIT_TYPE_AN = "int  0"
DIGIT_TYPE_AN_EXTENDED = "int  256"
GLOBAL_SPACE_CHAR_RATIO = "float  0.0f"
NO_MORE_TEXT = "int  1"
NO_MORE_COLUMN = "int  2"
def ():
    '''returns ColumnText\n\n
    (final PdfContentByte canvas)\n
    '''
def setACopy():
    '''returns ColumnText\n\n
    setACopy(final ColumnText org)\n
    '''
def addText():
    '''returns None\n\n
    addText(final Phrase phrase)\n
    addText(final Chunk chunk)\n
    '''
def setText():
    '''returns None\n\n
    setText(final Phrase phrase)\n
    '''
def addElement():
    '''returns None\n\n
    addElement(Element element)\n
    '''
def setColumns():
    '''returns None\n\n
    setColumns(final float[] leftLine, final float[] rightLine)\n
    '''
def setSimpleColumn():
    '''returns None\n\n
    setSimpleColumn(final Phrase phrase, final float llx, final float lly, final float urx, final float ury, final float leading, final int alignment)\n
    setSimpleColumn(final float llx, final float lly, final float urx, final float ury, final float leading, final int alignment)\n
    setSimpleColumn(final float llx, final float lly, final float urx, final float ury)\n
    '''
def setLeading():
    '''returns None\n\n
    setLeading(final float leading)\n
    setLeading(final float fixedLeading, final float multipliedLeading)\n
    '''
def getLeading():
    '''returns float\n\n
    getLeading()\n
    '''
def getMultipliedLeading():
    '''returns float\n\n
    getMultipliedLeading()\n
    '''
def setYLine():
    '''returns None\n\n
    setYLine(final float yLine)\n
    '''
def getYLine():
    '''returns float\n\n
    getYLine()\n
    '''
def setAlignment():
    '''returns None\n\n
    setAlignment(final int alignment)\n
    '''
def getAlignment():
    '''returns int\n\n
    getAlignment()\n
    '''
def setIndent():
    '''returns None\n\n
    setIndent(final float indent)\n
    '''
def getIndent():
    '''returns float\n\n
    getIndent()\n
    '''
def setFollowingIndent():
    '''returns None\n\n
    setFollowingIndent(final float indent)\n
    '''
def getFollowingIndent():
    '''returns float\n\n
    getFollowingIndent()\n
    '''
def setRightIndent():
    '''returns None\n\n
    setRightIndent(final float indent)\n
    '''
def getRightIndent():
    '''returns float\n\n
    getRightIndent()\n
    '''
def go():
    '''returns int\n\n
    go()\n
    go(final boolean simulate)\n
    '''
def getExtraParagraphSpace():
    '''returns float\n\n
    getExtraParagraphSpace()\n
    '''
def setExtraParagraphSpace():
    '''returns None\n\n
    setExtraParagraphSpace(final float extraParagraphSpace)\n
    '''
def clearChunks():
    '''returns None\n\n
    clearChunks()\n
    '''
def getSpaceCharRatio():
    '''returns float\n\n
    getSpaceCharRatio()\n
    '''
def setSpaceCharRatio():
    '''returns None\n\n
    setSpaceCharRatio(final float spaceCharRatio)\n
    '''
def setRunDirection():
    '''returns None\n\n
    setRunDirection(final int runDirection)\n
    '''
def getRunDirection():
    '''returns int\n\n
    getRunDirection()\n
    '''
def getLinesWritten():
    '''returns int\n\n
    getLinesWritten()\n
    '''
def getArabicOptions():
    '''returns int\n\n
    getArabicOptions()\n
    '''
def setArabicOptions():
    '''returns None\n\n
    setArabicOptions(final int arabicOptions)\n
    '''
def getDescender():
    '''returns float\n\n
    getDescender()\n
    '''
def getCanvas():
    '''returns PdfContentByte\n\n
    getCanvas()\n
    '''
def setCanvas():
    '''returns None\n\n
    setCanvas(final PdfContentByte canvas)\n
    '''
def zeroHeightElement():
    '''returns boolean\n\n
    zeroHeightElement()\n
    '''
def isUseAscender():
    '''returns boolean\n\n
    isUseAscender()\n
    '''
def setUseAscender():
    '''returns None\n\n
    setUseAscender(final boolean use)\n
    '''
