sid = "short  224"
NULL = "short  -16"
XF_STYLE = "short  1"
XF_CELL = "short  0"
NONE = "short  0"
THIN = "short  1"
MEDIUM = "short  2"
DASHED = "short  3"
DOTTED = "short  4"
THICK = "short  5"
DOUBLE = "short  6"
HAIR = "short  7"
MEDIUM_DASHED = "short  8"
DASH_DOT = "short  9"
MEDIUM_DASH_DOT = "short  10"
DASH_DOT_DOT = "short  11"
MEDIUM_DASH_DOT_DOT = "short  12"
SLANTED_DASH_DOT = "short  13"
GENERAL = "short  0"
LEFT = "short  1"
CENTER = "short  2"
RIGHT = "short  3"
FILL = "short  4"
JUSTIFY = "short  5"
CENTER_SELECTION = "short  6"
VERTICAL_TOP = "short  0"
VERTICAL_CENTER = "short  1"
VERTICAL_BOTTOM = "short  2"
VERTICAL_JUSTIFY = "short  3"
NO_FILL = "short  0"
SOLID_FILL = "short  1"
FINE_DOTS = "short  2"
ALT_BARS = "short  3"
SPARSE_DOTS = "short  4"
THICK_HORZ_BANDS = "short  5"
THICK_VERT_BANDS = "short  6"
THICK_BACKWARD_DIAG = "short  7"
THICK_FORWARD_DIAG = "short  8"
BIG_SPOTS = "short  9"
BRICKS = "short  10"
THIN_HORZ_BANDS = "short  11"
THIN_VERT_BANDS = "short  12"
THIN_BACKWARD_DIAG = "short  13"
THIN_FORWARD_DIAG = "short  14"
SQUARES = "short  15"
DIAMONDS = "short  16"
def ExtendedFormatRecord():
    '''    public ExtendedFormatRecord()
    public ExtendedFormatRecord(final RecordInputStream in)
    '''
def setFontIndex():
    '''    public void setFontIndex(final short index)
    '''
def setFormatIndex():
    '''    public void setFormatIndex(final short index)
    '''
def setCellOptions():
    '''    public void setCellOptions(final short options)
    '''
def setLocked():
    '''    public void setLocked(final boolean locked)
    '''
def setHidden():
    '''    public void setHidden(final boolean hidden)
    '''
def setXFType():
    '''    public void setXFType(final short type)
    '''
def set123Prefix():
    '''    public void set123Prefix(final boolean prefix)
    '''
def setParentIndex():
    '''    public void setParentIndex(final short parent)
    '''
def setAlignmentOptions():
    '''    public void setAlignmentOptions(final short options)
    '''
def setAlignment():
    '''    public void setAlignment(final short align)
    '''
def setWrapText():
    '''    public void setWrapText(final boolean wrapped)
    '''
def setVerticalAlignment():
    '''    public void setVerticalAlignment(final short align)
    '''
def setJustifyLast():
    '''    public void setJustifyLast(final short justify)
    '''
def setRotation():
    '''    public void setRotation(final short rotation)
    '''
def setIndentionOptions():
    '''    public void setIndentionOptions(final short options)
    '''
def setIndent():
    '''    public void setIndent(final short indent)
    '''
def setShrinkToFit():
    '''    public void setShrinkToFit(final boolean shrink)
    '''
def setMergeCells():
    '''    public void setMergeCells(final boolean merge)
    '''
def setReadingOrder():
    '''    public void setReadingOrder(final short order)
    '''
def setIndentNotParentFormat():
    '''    public void setIndentNotParentFormat(final boolean parent)
    '''
def setIndentNotParentFont():
    '''    public void setIndentNotParentFont(final boolean font)
    '''
def setIndentNotParentAlignment():
    '''    public void setIndentNotParentAlignment(final boolean alignment)
    '''
def setIndentNotParentBorder():
    '''    public void setIndentNotParentBorder(final boolean border)
    '''
def setIndentNotParentPattern():
    '''    public void setIndentNotParentPattern(final boolean pattern)
    '''
def setIndentNotParentCellOptions():
    '''    public void setIndentNotParentCellOptions(final boolean options)
    '''
def setBorderOptions():
    '''    public void setBorderOptions(final short options)
    '''
def setBorderLeft():
    '''    public void setBorderLeft(final short border)
    '''
def setBorderRight():
    '''    public void setBorderRight(final short border)
    '''
def setBorderTop():
    '''    public void setBorderTop(final short border)
    '''
def setBorderBottom():
    '''    public void setBorderBottom(final short border)
    '''
def setPaletteOptions():
    '''    public void setPaletteOptions(final short options)
    '''
def setLeftBorderPaletteIdx():
    '''    public void setLeftBorderPaletteIdx(final short border)
    '''
def setRightBorderPaletteIdx():
    '''    public void setRightBorderPaletteIdx(final short border)
    '''
def setDiag():
    '''    public void setDiag(final short diag)
    '''
def setAdtlPaletteOptions():
    '''    public void setAdtlPaletteOptions(final short options)
    '''
def setTopBorderPaletteIdx():
    '''    public void setTopBorderPaletteIdx(final short border)
    '''
def setBottomBorderPaletteIdx():
    '''    public void setBottomBorderPaletteIdx(final short border)
    '''
def setAdtlDiag():
    '''    public void setAdtlDiag(final short diag)
    '''
def setAdtlDiagLineStyle():
    '''    public void setAdtlDiagLineStyle(final short diag)
    '''
def setAdtlFillPattern():
    '''    public void setAdtlFillPattern(final short fill)
    '''
def setFillPaletteOptions():
    '''    public void setFillPaletteOptions(final short options)
    '''
def setFillForeground():
    '''    public void setFillForeground(final short color)
    '''
def setFillBackground():
    '''    public void setFillBackground(final short color)
    '''
def getFontIndex():
    '''    public short getFontIndex()
    '''
def getFormatIndex():
    '''    public short getFormatIndex()
    '''
def getCellOptions():
    '''    public short getCellOptions()
    '''
def isLocked():
    '''    public boolean isLocked()
    '''
def isHidden():
    '''    public boolean isHidden()
    '''
def getXFType():
    '''    public short getXFType()
    '''
def get123Prefix():
    '''    public boolean get123Prefix()
    '''
def getParentIndex():
    '''    public short getParentIndex()
    '''
def getAlignmentOptions():
    '''    public short getAlignmentOptions()
    '''
def getAlignment():
    '''    public short getAlignment()
    '''
def getWrapText():
    '''    public boolean getWrapText()
    '''
def getVerticalAlignment():
    '''    public short getVerticalAlignment()
    '''
def getJustifyLast():
    '''    public short getJustifyLast()
    '''
def getRotation():
    '''    public short getRotation()
    '''
def getIndentionOptions():
    '''    public short getIndentionOptions()
    '''
def getIndent():
    '''    public short getIndent()
    '''
def getShrinkToFit():
    '''    public boolean getShrinkToFit()
    '''
def getMergeCells():
    '''    public boolean getMergeCells()
    '''
def getReadingOrder():
    '''    public short getReadingOrder()
    '''
def isIndentNotParentFormat():
    '''    public boolean isIndentNotParentFormat()
    '''
def isIndentNotParentFont():
    '''    public boolean isIndentNotParentFont()
    '''
def isIndentNotParentAlignment():
    '''    public boolean isIndentNotParentAlignment()
    '''
def isIndentNotParentBorder():
    '''    public boolean isIndentNotParentBorder()
    '''
def isIndentNotParentPattern():
    '''    public boolean isIndentNotParentPattern()
    '''
def isIndentNotParentCellOptions():
    '''    public boolean isIndentNotParentCellOptions()
    '''
def getBorderOptions():
    '''    public short getBorderOptions()
    '''
def getBorderLeft():
    '''    public short getBorderLeft()
    '''
def getBorderRight():
    '''    public short getBorderRight()
    '''
def getBorderTop():
    '''    public short getBorderTop()
    '''
def getBorderBottom():
    '''    public short getBorderBottom()
    '''
def getPaletteOptions():
    '''    public short getPaletteOptions()
    '''
def getLeftBorderPaletteIdx():
    '''    public short getLeftBorderPaletteIdx()
    '''
def getRightBorderPaletteIdx():
    '''    public short getRightBorderPaletteIdx()
    '''
def getDiag():
    '''    public short getDiag()
    '''
def getAdtlPaletteOptions():
    '''    public int getAdtlPaletteOptions()
    '''
def getTopBorderPaletteIdx():
    '''    public short getTopBorderPaletteIdx()
    '''
def getBottomBorderPaletteIdx():
    '''    public short getBottomBorderPaletteIdx()
    '''
def getAdtlDiag():
    '''    public short getAdtlDiag()
    '''
def getAdtlDiagLineStyle():
    '''    public short getAdtlDiagLineStyle()
    '''
def getAdtlFillPattern():
    '''    public short getAdtlFillPattern()
    '''
def getFillPaletteOptions():
    '''    public short getFillPaletteOptions()
    '''
def getFillForeground():
    '''    public short getFillForeground()
    '''
def getFillBackground():
    '''    public short getFillBackground()
    '''
def toString():
    '''    public String toString()
    '''
def serialize():
    '''    public void serialize(final LittleEndianOutput out)
    '''
def getSid():
    '''    public short getSid()
    '''
def cloneStyleFrom():
    '''    public void cloneStyleFrom(final ExtendedFormatRecord source)
    '''
def hashCode():
    '''    public int hashCode()
    '''
def equals():
    '''    public boolean equals(final Object obj)
    '''
def stateSummary():
    '''    public int[] stateSummary()
    '''
