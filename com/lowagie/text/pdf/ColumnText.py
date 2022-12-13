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
pass
def duplicate():
'''public static ColumnText duplicate(final ColumnText org)
'''
pass
def setACopy():
'''public ColumnText setACopy(final ColumnText org)
'''
pass
def addText():
'''public void addText(final Phrase phrase)
public void addText(final Chunk chunk)
'''
pass
def setText():
'''public void setText(final Phrase phrase)
'''
pass
def addElement():
'''public void addElement(Element element)
'''
pass
def setColumns():
'''public void setColumns(final float[] leftLine, final float[] rightLine)
'''
pass
def setSimpleColumn():
'''public void setSimpleColumn(final Phrase phrase, final float llx, final float lly, final float urx, final float ury, final float leading, final int alignment)
public void setSimpleColumn(final float llx, final float lly, final float urx, final float ury, final float leading, final int alignment)
public void setSimpleColumn(final float llx, final float lly, final float urx, final float ury)
'''
pass
def setLeading():
'''public void setLeading(final float leading)
public void setLeading(final float fixedLeading, final float multipliedLeading)
'''
pass
def getLeading():
'''public float getLeading()
'''
pass
def getMultipliedLeading():
'''public float getMultipliedLeading()
'''
pass
def setYLine():
'''public void setYLine(final float yLine)
'''
pass
def getYLine():
'''public float getYLine()
'''
pass
def setAlignment():
'''public void setAlignment(final int alignment)
'''
pass
def getAlignment():
'''public int getAlignment()
'''
pass
def setIndent():
'''public void setIndent(final float indent)
'''
pass
def getIndent():
'''public float getIndent()
'''
pass
def setFollowingIndent():
'''public void setFollowingIndent(final float indent)
'''
pass
def getFollowingIndent():
'''public float getFollowingIndent()
'''
pass
def setRightIndent():
'''public void setRightIndent(final float indent)
'''
pass
def getRightIndent():
'''public float getRightIndent()
'''
pass
def go():
'''public int go()
public int go(final boolean simulate)
'''
pass
def getExtraParagraphSpace():
'''public float getExtraParagraphSpace()
'''
pass
def setExtraParagraphSpace():
'''public void setExtraParagraphSpace(final float extraParagraphSpace)
'''
pass
def clearChunks():
'''public void clearChunks()
'''
pass
def getSpaceCharRatio():
'''public float getSpaceCharRatio()
'''
pass
def setSpaceCharRatio():
'''public void setSpaceCharRatio(final float spaceCharRatio)
'''
pass
def setRunDirection():
'''public void setRunDirection(final int runDirection)
'''
pass
def getRunDirection():
'''public int getRunDirection()
'''
pass
def getLinesWritten():
'''public int getLinesWritten()
'''
pass
def getArabicOptions():
'''public int getArabicOptions()
'''
pass
def setArabicOptions():
'''public void setArabicOptions(final int arabicOptions)
'''
pass
def getDescender():
'''public float getDescender()
'''
pass
def getWidth():
'''public static float getWidth(final Phrase phrase, final int runDirection, final int arabicOptions)
public static float getWidth(final Phrase phrase)
'''
pass
def showTextAligned():
'''public static void showTextAligned(final PdfContentByte canvas, int alignment, final Phrase phrase, final float x, final float y, final float rotation, final int runDirection, final int arabicOptions)
public static void showTextAligned(final PdfContentByte canvas, final int alignment, final Phrase phrase, final float x, final float y, final float rotation)
'''
pass
def getCanvas():
'''public PdfContentByte getCanvas()
'''
pass
def setCanvas():
'''public void setCanvas(final PdfContentByte canvas)
'''
pass
def zeroHeightElement():
'''public boolean zeroHeightElement()
'''
pass
def isUseAscender():
'''public boolean isUseAscender()
'''
pass
def setUseAscender():
'''public void setUseAscender(final boolean use)
'''
pass
