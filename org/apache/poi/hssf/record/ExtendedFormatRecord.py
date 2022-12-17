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
def ():
    '''returns ExtendedFormatRecord\n\n
    ()\n
    (final RecordInputStream in)\n
    '''
def setFontIndex():
    '''returns None\n\n
    setFontIndex(final short index)\n
    '''
def setFormatIndex():
    '''returns None\n\n
    setFormatIndex(final short index)\n
    '''
def setCellOptions():
    '''returns None\n\n
    setCellOptions(final short options)\n
    '''
def setLocked():
    '''returns None\n\n
    setLocked(final boolean locked)\n
    '''
def setHidden():
    '''returns None\n\n
    setHidden(final boolean hidden)\n
    '''
def setXFType():
    '''returns None\n\n
    setXFType(final short type)\n
    '''
def set123Prefix():
    '''returns None\n\n
    set123Prefix(final boolean prefix)\n
    '''
def setParentIndex():
    '''returns None\n\n
    setParentIndex(final short parent)\n
    '''
def setAlignmentOptions():
    '''returns None\n\n
    setAlignmentOptions(final short options)\n
    '''
def setAlignment():
    '''returns None\n\n
    setAlignment(final short align)\n
    '''
def setWrapText():
    '''returns None\n\n
    setWrapText(final boolean wrapped)\n
    '''
def setVerticalAlignment():
    '''returns None\n\n
    setVerticalAlignment(final short align)\n
    '''
def setJustifyLast():
    '''returns None\n\n
    setJustifyLast(final short justify)\n
    '''
def setRotation():
    '''returns None\n\n
    setRotation(final short rotation)\n
    '''
def setIndentionOptions():
    '''returns None\n\n
    setIndentionOptions(final short options)\n
    '''
def setIndent():
    '''returns None\n\n
    setIndent(final short indent)\n
    '''
def setShrinkToFit():
    '''returns None\n\n
    setShrinkToFit(final boolean shrink)\n
    '''
def setMergeCells():
    '''returns None\n\n
    setMergeCells(final boolean merge)\n
    '''
def setReadingOrder():
    '''returns None\n\n
    setReadingOrder(final short order)\n
    '''
def setIndentNotParentFormat():
    '''returns None\n\n
    setIndentNotParentFormat(final boolean parent)\n
    '''
def setIndentNotParentFont():
    '''returns None\n\n
    setIndentNotParentFont(final boolean font)\n
    '''
def setIndentNotParentAlignment():
    '''returns None\n\n
    setIndentNotParentAlignment(final boolean alignment)\n
    '''
def setIndentNotParentBorder():
    '''returns None\n\n
    setIndentNotParentBorder(final boolean border)\n
    '''
def setIndentNotParentPattern():
    '''returns None\n\n
    setIndentNotParentPattern(final boolean pattern)\n
    '''
def setIndentNotParentCellOptions():
    '''returns None\n\n
    setIndentNotParentCellOptions(final boolean options)\n
    '''
def setBorderOptions():
    '''returns None\n\n
    setBorderOptions(final short options)\n
    '''
def setBorderLeft():
    '''returns None\n\n
    setBorderLeft(final short border)\n
    '''
def setBorderRight():
    '''returns None\n\n
    setBorderRight(final short border)\n
    '''
def setBorderTop():
    '''returns None\n\n
    setBorderTop(final short border)\n
    '''
def setBorderBottom():
    '''returns None\n\n
    setBorderBottom(final short border)\n
    '''
def setPaletteOptions():
    '''returns None\n\n
    setPaletteOptions(final short options)\n
    '''
def setLeftBorderPaletteIdx():
    '''returns None\n\n
    setLeftBorderPaletteIdx(final short border)\n
    '''
def setRightBorderPaletteIdx():
    '''returns None\n\n
    setRightBorderPaletteIdx(final short border)\n
    '''
def setDiag():
    '''returns None\n\n
    setDiag(final short diag)\n
    '''
def setAdtlPaletteOptions():
    '''returns None\n\n
    setAdtlPaletteOptions(final short options)\n
    '''
def setTopBorderPaletteIdx():
    '''returns None\n\n
    setTopBorderPaletteIdx(final short border)\n
    '''
def setBottomBorderPaletteIdx():
    '''returns None\n\n
    setBottomBorderPaletteIdx(final short border)\n
    '''
def setAdtlDiag():
    '''returns None\n\n
    setAdtlDiag(final short diag)\n
    '''
def setAdtlDiagLineStyle():
    '''returns None\n\n
    setAdtlDiagLineStyle(final short diag)\n
    '''
def setAdtlFillPattern():
    '''returns None\n\n
    setAdtlFillPattern(final short fill)\n
    '''
def setFillPaletteOptions():
    '''returns None\n\n
    setFillPaletteOptions(final short options)\n
    '''
def setFillForeground():
    '''returns None\n\n
    setFillForeground(final short color)\n
    '''
def setFillBackground():
    '''returns None\n\n
    setFillBackground(final short color)\n
    '''
def getFontIndex():
    '''returns short\n\n
    getFontIndex()\n
    '''
def getFormatIndex():
    '''returns short\n\n
    getFormatIndex()\n
    '''
def getCellOptions():
    '''returns short\n\n
    getCellOptions()\n
    '''
def isLocked():
    '''returns boolean\n\n
    isLocked()\n
    '''
def isHidden():
    '''returns boolean\n\n
    isHidden()\n
    '''
def getXFType():
    '''returns short\n\n
    getXFType()\n
    '''
def get123Prefix():
    '''returns boolean\n\n
    get123Prefix()\n
    '''
def getParentIndex():
    '''returns short\n\n
    getParentIndex()\n
    '''
def getAlignmentOptions():
    '''returns short\n\n
    getAlignmentOptions()\n
    '''
def getAlignment():
    '''returns short\n\n
    getAlignment()\n
    '''
def getWrapText():
    '''returns boolean\n\n
    getWrapText()\n
    '''
def getVerticalAlignment():
    '''returns short\n\n
    getVerticalAlignment()\n
    '''
def getJustifyLast():
    '''returns short\n\n
    getJustifyLast()\n
    '''
def getRotation():
    '''returns short\n\n
    getRotation()\n
    '''
def getIndentionOptions():
    '''returns short\n\n
    getIndentionOptions()\n
    '''
def getIndent():
    '''returns short\n\n
    getIndent()\n
    '''
def getShrinkToFit():
    '''returns boolean\n\n
    getShrinkToFit()\n
    '''
def getMergeCells():
    '''returns boolean\n\n
    getMergeCells()\n
    '''
def getReadingOrder():
    '''returns short\n\n
    getReadingOrder()\n
    '''
def isIndentNotParentFormat():
    '''returns boolean\n\n
    isIndentNotParentFormat()\n
    '''
def isIndentNotParentFont():
    '''returns boolean\n\n
    isIndentNotParentFont()\n
    '''
def isIndentNotParentAlignment():
    '''returns boolean\n\n
    isIndentNotParentAlignment()\n
    '''
def isIndentNotParentBorder():
    '''returns boolean\n\n
    isIndentNotParentBorder()\n
    '''
def isIndentNotParentPattern():
    '''returns boolean\n\n
    isIndentNotParentPattern()\n
    '''
def isIndentNotParentCellOptions():
    '''returns boolean\n\n
    isIndentNotParentCellOptions()\n
    '''
def getBorderOptions():
    '''returns short\n\n
    getBorderOptions()\n
    '''
def getBorderLeft():
    '''returns short\n\n
    getBorderLeft()\n
    '''
def getBorderRight():
    '''returns short\n\n
    getBorderRight()\n
    '''
def getBorderTop():
    '''returns short\n\n
    getBorderTop()\n
    '''
def getBorderBottom():
    '''returns short\n\n
    getBorderBottom()\n
    '''
def getPaletteOptions():
    '''returns short\n\n
    getPaletteOptions()\n
    '''
def getLeftBorderPaletteIdx():
    '''returns short\n\n
    getLeftBorderPaletteIdx()\n
    '''
def getRightBorderPaletteIdx():
    '''returns short\n\n
    getRightBorderPaletteIdx()\n
    '''
def getDiag():
    '''returns short\n\n
    getDiag()\n
    '''
def getAdtlPaletteOptions():
    '''returns int\n\n
    getAdtlPaletteOptions()\n
    '''
def getTopBorderPaletteIdx():
    '''returns short\n\n
    getTopBorderPaletteIdx()\n
    '''
def getBottomBorderPaletteIdx():
    '''returns short\n\n
    getBottomBorderPaletteIdx()\n
    '''
def getAdtlDiag():
    '''returns short\n\n
    getAdtlDiag()\n
    '''
def getAdtlDiagLineStyle():
    '''returns short\n\n
    getAdtlDiagLineStyle()\n
    '''
def getAdtlFillPattern():
    '''returns short\n\n
    getAdtlFillPattern()\n
    '''
def getFillPaletteOptions():
    '''returns short\n\n
    getFillPaletteOptions()\n
    '''
def getFillForeground():
    '''returns short\n\n
    getFillForeground()\n
    '''
def getFillBackground():
    '''returns short\n\n
    getFillBackground()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final LittleEndianOutput out)\n
    '''
def getSid():
    '''returns short\n\n
    getSid()\n
    '''
def cloneStyleFrom():
    '''returns None\n\n
    cloneStyleFrom(final ExtendedFormatRecord source)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def stateSummary():
    '''returns int[]\n\n
    stateSummary()\n
    '''
