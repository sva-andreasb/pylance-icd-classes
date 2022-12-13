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
def ColumnText():
    '''public ColumnText(final PdfContentByte canvas)
    '''
def duplicate():
    '''public static ColumnText duplicate(final ColumnText org)
    '''
def setACopy():
    '''public ColumnText setACopy(final ColumnText org)
    '''
def addText():
    '''public void addText(final Phrase phrase)
    public void addText(final Chunk chunk)
    '''
def setText():
    '''public void setText(final Phrase phrase)
    '''
def addElement():
    '''public void addElement(Element element)
    '''
def setColumns():
    '''public void setColumns(final float[] leftLine, final float[] rightLine)
    '''
def setSimpleColumn():
    '''public void setSimpleColumn(final Phrase phrase, final float llx, final float lly, final float urx, final float ury, final float leading, final int alignment)
    public void setSimpleColumn(final float llx, final float lly, final float urx, final float ury, final float leading, final int alignment)
    public void setSimpleColumn(final float llx, final float lly, final float urx, final float ury)
    '''
def setLeading():
    '''public void setLeading(final float leading)
    public void setLeading(final float fixedLeading, final float multipliedLeading)
    '''
def getLeading():
    '''public float getLeading()
    '''
def getMultipliedLeading():
    '''public float getMultipliedLeading()
    '''
def setYLine():
    '''public void setYLine(final float yLine)
    '''
def getYLine():
    '''public float getYLine()
    '''
def setAlignment():
    '''public void setAlignment(final int alignment)
    '''
def getAlignment():
    '''public int getAlignment()
    '''
def setIndent():
    '''public void setIndent(final float indent)
    '''
def getIndent():
    '''public float getIndent()
    '''
def setFollowingIndent():
    '''public void setFollowingIndent(final float indent)
    '''
def getFollowingIndent():
    '''public float getFollowingIndent()
    '''
def setRightIndent():
    '''public void setRightIndent(final float indent)
    '''
def getRightIndent():
    '''public float getRightIndent()
    '''
def go():
    '''public int go()
    public int go(final boolean simulate)
    '''
def getExtraParagraphSpace():
    '''public float getExtraParagraphSpace()
    '''
def setExtraParagraphSpace():
    '''public void setExtraParagraphSpace(final float extraParagraphSpace)
    '''
def clearChunks():
    '''public void clearChunks()
    '''
def getSpaceCharRatio():
    '''public float getSpaceCharRatio()
    '''
def setSpaceCharRatio():
    '''public void setSpaceCharRatio(final float spaceCharRatio)
    '''
def setRunDirection():
    '''public void setRunDirection(final int runDirection)
    '''
def getRunDirection():
    '''public int getRunDirection()
    '''
def getLinesWritten():
    '''public int getLinesWritten()
    '''
def getArabicOptions():
    '''public int getArabicOptions()
    '''
def setArabicOptions():
    '''public void setArabicOptions(final int arabicOptions)
    '''
def getDescender():
    '''public float getDescender()
    '''
def getWidth():
    '''public static float getWidth(final Phrase phrase, final int runDirection, final int arabicOptions)
    public static float getWidth(final Phrase phrase)
    '''
def showTextAligned():
    '''public static void showTextAligned(final PdfContentByte canvas, int alignment, final Phrase phrase, final float x, final float y, final float rotation, final int runDirection, final int arabicOptions)
    public static void showTextAligned(final PdfContentByte canvas, final int alignment, final Phrase phrase, final float x, final float y, final float rotation)
    '''
def getCanvas():
    '''public PdfContentByte getCanvas()
    '''
def setCanvas():
    '''public void setCanvas(final PdfContentByte canvas)
    '''
def zeroHeightElement():
    '''public boolean zeroHeightElement()
    '''
def isUseAscender():
    '''public boolean isUseAscender()
    '''
def setUseAscender():
    '''public void setUseAscender(final boolean use)
    '''
